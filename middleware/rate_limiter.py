from typing import Dict, Optional


class Request:
    def __init__(self, headers: Optional[Dict[str, str]] = None, client_ip: str = "127.0.0.1"):
        self.headers = headers if headers is not None else {}
        self.client_ip = client_ip


# In-memory hit counter for demo purposes: {ip: request_count}
REQUEST_COUNTS: Dict[str, int] = {}
RATE_LIMIT = 5


def get_client_identifier(request: Request) -> str:
    """
    Extract the effective client IP.
    DEFECT: Assumes 'X-Forwarded-For' always exists as a valid string.
    Raises AttributeError when headers are empty or 'X-Forwarded-For' is None.
    """
    # BUGGY LINE: Calling .split() directly on None when header is missing
    forwarded_for = request.headers.get("X-Forwarded-For")
    client_ip = forwarded_for.split(",")[0].strip()
    return client_ip


def is_rate_limited(request: Request) -> bool:
    """
    Checks if a given request exceeds the allowed request threshold.
    """
    client_id = get_client_identifier(request)
    current_count = REQUEST_COUNTS.get(client_id, 0)

    if current_count >= RATE_LIMIT:
        return True

    REQUEST_COUNTS[client_id] = current_count + 1
    return False


def reset_rate_limits() -> None:
    REQUEST_COUNTS.clear()