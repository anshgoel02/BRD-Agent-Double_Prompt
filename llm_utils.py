from __future__ import annotations

import base64
import json
import mimetypes
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

import requests

_CACHED_TOKEN: str | None = None


def _get_token() -> str:
    global _CACHED_TOKEN
    if _CACHED_TOKEN:
        return _CACHED_TOKEN

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    if not client_id or not client_secret:
        raise EnvironmentError("CLIENT_ID and CLIENT_SECRET are required to generate the access token.")

    url = "https://daia.privatelink.azurewebsites.net/authentication-service/api/v1/auth/generate-token"
    response = requests.post(url, json={"client_id": client_id, "client_secret": client_secret}, verify=False, timeout=30)
    response.raise_for_status()
    token = response.json().get("token")
    if not token:
        raise RuntimeError("Token not found in authentication response.")
    _CACHED_TOKEN = token
    return token


def _build_content(prompt: str, image_paths: List[str] | None = None) -> Any:
    if not image_paths:
        return prompt
    content: List[Dict[str, Any]] = [{"type": "text", "text": prompt}]
    for raw in image_paths:
        path = Path(raw)
        if not path.exists():
            continue
        mime_type, _ = mimetypes.guess_type(str(path))
        mime_type = mime_type or "image/png"
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        content.append({"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{encoded}"}})
    return content


def generate_text(prompt: str, max_tokens: int = 100000, image_paths: List[str] | None = None) -> str:
    model = os.getenv("MODEL_AS_A_SERVICE_MODEL", "gpt-5")
    headers = {"Authorization": f"Bearer {_get_token()}"}
    payload: Dict[str, Any] = {
        "model": model,
        "messages": [{"role": "user", "content": _build_content(prompt, image_paths)}],
        "max_tokens": max_tokens,
    }
    response = requests.post(
        "https://daia.privatelink.azurewebsites.net/model-as-a-service/chat/completions",
        json=payload,
        headers=headers,
        verify=False,
        timeout=(30, 300),
    )
    response.raise_for_status()
    data = response.json()
    try:
        return data["choices"][0]["message"]["content"]
    except Exception as exc:
        raise RuntimeError(f"Unexpected response format: {data}") from exc


def estimate_tokens(text: str) -> int:
    if not text:
        return 0
    return max(1, len(text) // 4)


def generate_text_with_usage(prompt: str, max_tokens: int = 100000, image_paths: List[str] | None = None) -> Tuple[str, dict]:
    output = generate_text(prompt, max_tokens=max_tokens, image_paths=image_paths)
    usage = {"prompt_tokens": estimate_tokens(prompt), "completion_tokens": estimate_tokens(output)}
    usage["total_tokens"] = usage["prompt_tokens"] + usage["completion_tokens"]
    return output, usage


def parse_json_obj(text: str) -> dict:
    raw = text.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-zA-Z]*\n|\n```$", "", raw, flags=re.MULTILINE).strip()
    if not raw:
        return {}
    try:
        obj = json.loads(raw)
        return obj if isinstance(obj, dict) else {}
    except json.JSONDecodeError:
        start = raw.find("{")
        end = raw.rfind("}")
        if start == -1 or end == -1 or end <= start:
            return {}
        try:
            obj = json.loads(raw[start : end + 1])
            return obj if isinstance(obj, dict) else {}
        except json.JSONDecodeError:
            return {}
