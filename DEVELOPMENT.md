# Development Guide

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/umitkacar/Awesome-ComfyUI-Beyond.git
cd Awesome-ComfyUI-Beyond

# Initialize development environment
make init-dev

# Run tests
make test-cov

# Run all checks
make check-all
```

## 📦 Tools Overview

### Hatch

Hatch is our build system and environment manager.

**Common commands:**

```bash
# Run tests
hatch run test

# Run with coverage
hatch run test-cov

# Lint code
hatch run lint

# Format code
hatch run format

# Type check
hatch run type-check

# Run all checks
hatch run check-all
```

### Pre-commit

Automated code quality checks before commits.

**Setup:**

```bash
# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```

**Included hooks:**

- ✅ Black (formatting)
- ✅ Ruff (linting)
- ✅ MyPy (type checking)
- ✅ Bandit (security)
- ✅ isort (import sorting)
- ✅ Various file checks

### Ruff

Ultra-fast Python linter and formatter.

**Configuration:** `pyproject.toml` → `[tool.ruff]`

```bash
# Check code
ruff check src tests

# Fix issues automatically
ruff check --fix src tests

# Format code (alternative to black)
ruff format src tests
```

### Black

Opinionated code formatter.

**Configuration:** `pyproject.toml` → `[tool.black]`

```bash
# Format code
black src tests

# Check without modifying
black --check src tests
```

### MyPy

Static type checker.

**Configuration:** `pyproject.toml` → `[tool.mypy]`

```bash
# Type check
mypy src

# Generate report
mypy src --html-report mypy-report
```

### Pytest

Testing framework.

**Configuration:** `pyproject.toml` → `[tool.pytest.ini_options]`

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run parallel
pytest -n auto

# Run specific test
pytest tests/test_utils.py::test_validate_url

# Run marked tests only
pytest -m "not slow"
```

## 🏗️ Project Structure

```
awesome-comfyui-beyond/
│
├── src/awesome_comfyui/          # Source code
│   ├── __init__.py               # Package initialization
│   └── utils.py                  # Utility functions
│
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures
│   ├── test_example.py          # Example tests
│   └── test_utils.py            # Utils tests
│
├── .github/workflows/            # CI/CD
│   ├── ci.yml                   # Main CI pipeline
│   ├── release.yml              # Release automation
│   └── dependabot-auto-merge.yml
│
├── pyproject.toml               # Project configuration
├── .pre-commit-config.yaml      # Pre-commit hooks
├── .gitignore                   # Git ignore rules
├── .editorconfig                # Editor configuration
├── Makefile                     # Build automation
├── CONTRIBUTING.md              # Contribution guide
├── DEVELOPMENT.md               # This file
└── README.md                    # Project readme
```

## 🧪 Testing Best Practices

### Test Organization

```python
# tests/test_feature.py

import pytest
from awesome_comfyui.feature import my_function


class TestMyFunction:
    """Tests for my_function."""

    def test_valid_input(self):
        """Test with valid input."""
        result = my_function("valid")
        assert result is True

    def test_invalid_input(self):
        """Test with invalid input."""
        with pytest.raises(ValueError):
            my_function("invalid")

    @pytest.mark.parametrize(
        "input,expected",
        [
            ("a", 1),
            ("b", 2),
            ("c", 3),
        ],
    )
    def test_parametrized(self, input, expected):
        """Test multiple scenarios."""
        assert my_function(input) == expected
```

### Using Fixtures

```python
# tests/conftest.py


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {"key": "value"}


# tests/test_feature.py


def test_with_fixture(sample_data):
    """Test using fixture."""
    assert sample_data["key"] == "value"
```

### Coverage Goals

- Aim for >90% code coverage
- Focus on critical paths
- Test edge cases and error handling

## 🔧 Configuration Files

### pyproject.toml

Central configuration for:

- Package metadata
- Build system (Hatch)
- Dependencies
- Tool configurations (Ruff, Black, MyPy, Pytest, Coverage)

### .pre-commit-config.yaml

Pre-commit hook configurations:

- Which tools to run
- When to run them
- Tool-specific arguments

### .editorconfig

Editor configuration for:

- Indentation
- Line endings
- Character encoding
- Max line length

## 🚀 CI/CD Pipeline

### On Push/PR

1. **Lint & Format Check**

   - Black formatting
   - Ruff linting
   - MyPy type checking

1. **Security Scan**

   - Bandit security analysis
   - Dependency vulnerability check

1. **Test Suite**

   - Python 3.10, 3.11, 3.12
   - Ubuntu, Windows, macOS
   - Coverage reporting

1. **Build Package**

   - Package building
   - Metadata validation

1. **Documentation**

   - Docs building
   - Link checking

### On Release (Tag)

1. Build package
1. Publish to PyPI
1. Create GitHub Release
1. Deploy documentation

## 💡 Tips & Tricks

### Fast iteration

```bash
# Watch mode for tests
pytest-watch

# Only run failed tests
pytest --lf

# Run tests in random order
pytest --random-order
```

### Debugging

```python
# Add breakpoint
import pdb

pdb.set_trace()

# Or use pytest's built-in
breakpoint()

# Run pytest with pdb
pytest - -pdb
```

### Performance

```python
# Profile slow tests
pytest --durations=10

# Parallel execution
pytest -n auto
```

## 🔍 Useful Commands

```bash
# Check what pre-commit will do
pre-commit run --all-files --verbose

# Clean everything
make clean

# Update all tools
make update

# Run CI checks locally
make ci

# Security audit
make security

# Build package
make build

# View coverage report
make test-cov
# Then open htmlcov/index.html
```

## 📚 Resources

- [Hatch Documentation](https://hatch.pypa.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pre-commit Documentation](https://pre-commit.com/)

## ❓ FAQ

**Q: Why Hatch instead of Poetry/Pipenv?**
A: Hatch is faster, more modern, and follows PEP standards closely.

**Q: Why Ruff instead of Flake8/Pylint?**
A: Ruff is 10-100x faster and combines multiple tools.

**Q: Do I need to run all checks manually?**
A: No! Pre-commit hooks and CI will run them automatically.

**Q: How do I skip a pre-commit hook?**
A: Use `git commit --no-verify` (not recommended)

**Q: Tests are slow, what can I do?**
A: Use `pytest -n auto` for parallel execution or mark slow tests with `@pytest.mark.slow`
