"""Tests for utility functions."""

import pytest

from awesome_comfyui.utils import parse_resource, validate_url


class TestValidateUrl:
    """Tests for validate_url function."""

    @pytest.mark.parametrize(
        "url,expected",
        [
            ("https://github.com/user/repo", True),
            ("http://example.com", True),
            ("https://comfyui.org", True),
            ("not a url", False),
            ("github.com", False),
            ("", False),
        ],
    )
    def test_validate_url(self, url: str, expected: bool) -> None:
        """Test URL validation."""
        assert validate_url(url) == expected


class TestParseResource:
    """Tests for parse_resource function."""

    def test_parse_valid_resource(self) -> None:
        """Test parsing a valid resource."""
        resource = {
            "name": "ComfyUI",
            "url": "https://github.com/comfyanonymous/ComfyUI",
            "description": "The best UI",
            "category": "core",
        }

        result = parse_resource(resource)

        assert result["name"] == "ComfyUI"
        assert result["url"] == "https://github.com/comfyanonymous/ComfyUI"
        assert result["description"] == "The best UI"
        assert result["category"] == "core"

    def test_parse_minimal_resource(self) -> None:
        """Test parsing a resource with only required fields."""
        resource = {
            "name": "Test",
            "url": "https://example.com",
        }

        result = parse_resource(resource)

        assert result["name"] == "Test"
        assert result["url"] == "https://example.com"
        assert result["description"] == ""
        assert result["category"] == "general"

    def test_parse_missing_name(self) -> None:
        """Test parsing fails with missing name."""
        resource = {"url": "https://example.com"}

        with pytest.raises(ValueError, match="Missing required field: name"):
            parse_resource(resource)

    def test_parse_missing_url(self) -> None:
        """Test parsing fails with missing URL."""
        resource = {"name": "Test"}

        with pytest.raises(ValueError, match="Missing required field: url"):
            parse_resource(resource)

    def test_parse_invalid_url(self) -> None:
        """Test parsing fails with invalid URL."""
        resource = {
            "name": "Test",
            "url": "not a url",
        }

        with pytest.raises(ValueError, match="Invalid URL"):
            parse_resource(resource)
