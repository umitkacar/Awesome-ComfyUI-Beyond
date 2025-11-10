"""Example test suite."""

import pytest


def test_basic_assertion() -> None:
    """Test basic assertion."""
    assert 1 + 1 == 2


def test_sample_data(sample_data: dict[str, str]) -> None:
    """Test sample data fixture."""
    assert sample_data["name"] == "ComfyUI"
    assert sample_data["category"] == "Image Generation"


def test_temp_file(temp_file) -> None:
    """Test temporary file fixture."""
    assert temp_file.exists()
    assert temp_file.read_text() == "test content"


@pytest.mark.parametrize(
    "input_value,expected",
    [
        (1, 2),
        (2, 4),
        (3, 6),
        (4, 8),
    ],
)
def test_parametrized(input_value: int, expected: int) -> None:
    """Test parametrized test."""
    assert input_value * 2 == expected


class TestClassExample:
    """Example test class."""

    def test_method_one(self) -> None:
        """Test method one."""
        result = "hello".upper()
        assert result == "HELLO"

    def test_method_two(self) -> None:
        """Test method two."""
        result = [1, 2, 3]
        assert len(result) == 3


@pytest.mark.slow
def test_slow_operation() -> None:
    """Test marked as slow."""
    # Slow operation simulation
    assert True


@pytest.mark.integration
def test_integration_example() -> None:
    """Test marked as integration."""
    # Integration test simulation
    assert True
