# Contributing to Awesome ComfyUI Beyond

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Development Setup

### Prerequisites

- Python 3.10 or higher
- Git
- Make (optional, for convenience)

### Initial Setup

1. **Fork and clone the repository:**

```bash
git clone https://github.com/umitkacar/Awesome-ComfyUI-Beyond.git
cd Awesome-ComfyUI-Beyond
```

2. **Install development dependencies:**

```bash
# Using Make
make install

# Or manually
pip install -e ".[dev]"
pre-commit install
```

## Development Workflow

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run in parallel
make test-parallel

# Run specific test
hatch run pytest tests/test_specific.py
```

### Code Quality

```bash
# Format code
make format

# Check formatting
make format-check

# Lint code
make lint

# Fix linting issues automatically
make lint-fix

# Type check
make type-check

# Run all checks
make check-all
```

### Pre-commit Hooks

Pre-commit hooks will run automatically on commit. To run manually:

```bash
make pre-commit

# Or update hooks
pre-commit autoupdate
```

## Code Standards

### Code Style

- We use **Black** for code formatting (line length: 100)
- We use **Ruff** for linting
- We use **MyPy** for type checking
- Follow **PEP 8** guidelines

### Type Hints

All functions should have type hints:

```python
def my_function(param: str) -> bool:
    """Function description.

    Args:
        param: Parameter description

    Returns:
        Return value description
    """
    return True
```

### Documentation

- Use Google-style docstrings
- Include examples in docstrings when helpful
- Update README.md if adding new features

### Testing

- Write tests for all new code
- Aim for >90% code coverage
- Use pytest fixtures for common test data
- Mark slow/integration tests appropriately:

```python
@pytest.mark.slow
def test_slow_operation():
    pass


@pytest.mark.integration
def test_integration():
    pass
```

## Pull Request Process

1. **Create a feature branch:**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes and commit:**

```bash
git add .
git commit -m "feat: add awesome feature"
```

Commit message format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Maintenance tasks

3. **Push and create PR:**

```bash
git push origin feature/your-feature-name
```

4. **Ensure CI passes:**
   - All tests pass
   - Code coverage maintained
   - Linting passes
   - Type checking passes

## Project Structure

```
awesome-comfyui-beyond/
├── src/
│   └── awesome_comfyui/
│       ├── __init__.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_*.py
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── release.yml
├── pyproject.toml
├── .pre-commit-config.yaml
├── Makefile
└── README.md
```

## Questions?

Feel free to open an issue for:

- Bug reports
- Feature requests
- Questions about contributing
- Suggestions for improvements

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on what is best for the community
- Show empathy towards other community members

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
