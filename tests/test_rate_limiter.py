import pytest
from middleware.rate_limiter import (
    Request,
    is_rate_limited,
    reset_rate_limits,
    get_client_identifier,
)


@pytest.fixture(autouse=True)
def clean_state():
    reset_rate_limits()


def test_proxied_request_extraction():
    """Validates IP extraction when running behind a proxy."""
    req = Request(headers={"X-Forwarded-For": "203.0.113.195, 70.41.3.18"})
    assert get_client_identifier(req) == "203.0.113.195"


def test_missing_forwarded_header_fallback():
    """
    Fails on unpatched code with:
    AttributeError: 'NoneType' object has no attribute 'split'
    """
    req = Request(headers={}, client_ip="192.168.1.50")
    # Must fallback cleanly to request.client_ip instead of crashing
    assert get_client_identifier(req) == "192.168.1.50"


def test_empty_header_string_fallback():
    """Handles edge case where header is present but empty or whitespace."""
    req = Request(headers={"X-Forwarded-For": "  "}, client_ip="10.0.0.1")
    assert get_client_identifier(req) == "10.0.0.1"


def test_rate_limiting_enforcement():
    """Verifies standard rate limit thresholding."""
    req = Request(client_ip="192.168.1.100")
    for _ in range(5):
        assert is_rate_limited(req) is False
    assert is_rate_limited(req) is True