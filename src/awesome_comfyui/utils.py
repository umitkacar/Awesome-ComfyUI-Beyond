"""Utility functions for Awesome ComfyUI Beyond."""

from typing import Any


def validate_url(url: str) -> bool:
    """
    Validate if a string is a valid URL.

    Args:
        url: The URL string to validate

    Returns:
        True if valid URL, False otherwise

    Examples:
        >>> validate_url("https://github.com/user/repo")
        True
        >>> validate_url("not a url")
        False
    """
    return url.startswith(("http://", "https://"))


def parse_resource(resource: dict[str, Any]) -> dict[str, str]:
    """
    Parse and validate a resource dictionary.

    Args:
        resource: Dictionary containing resource information

    Returns:
        Validated resource dictionary

    Raises:
        ValueError: If required fields are missing

    Examples:
        >>> resource = {"name": "ComfyUI", "url": "https://github.com/comfyanonymous/ComfyUI"}
        >>> parsed = parse_resource(resource)
        >>> parsed["name"]
        'ComfyUI'
    """
    required_fields = ["name", "url"]

    for field in required_fields:
        if field not in resource:
            raise ValueError(f"Missing required field: {field}")

    if not validate_url(resource["url"]):
        raise ValueError(f"Invalid URL: {resource['url']}")

    return {
        "name": resource["name"],
        "url": resource["url"],
        "description": resource.get("description", ""),
        "category": resource.get("category", "general"),
    }
