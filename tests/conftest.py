"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def sample_data() -> dict[str, str]:
    """Sample data fixture for testing."""
    return {
        "name": "ComfyUI",
        "category": "Image Generation",
        "status": "active",
    }


@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("test content")
    return test_file
