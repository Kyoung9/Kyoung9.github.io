from typing import Optional, Dict

import requests


DEFAULT_TIMEOUT = 10
DEFAULT_HEADERS = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15"
}


def get_html(url: str, *, timeout: int = DEFAULT_TIMEOUT, headers: Optional[Dict[str, str]] = None) -> str:
    merged_headers = DEFAULT_HEADERS.copy()
    if headers:
        merged_headers.update(headers)
    response = requests.get(url, headers=merged_headers, timeout=timeout)
    response.raise_for_status()
    return response.text
