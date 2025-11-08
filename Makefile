.PHONY: help install test lint format clean pre-commit build docs

# Default target
.DEFAULT_GOAL := help

# Color output
BLUE := \033[0;34m
GREEN := \033[0;32m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Show this help message
	@echo '$(BLUE)Available commands:$(NC)'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

install: ## Install dependencies
	@echo '$(BLUE)Installing dependencies...$(NC)'
	pip install -e ".[all]"
	pre-commit install

test: ## Run tests
	@echo '$(BLUE)Running tests...$(NC)'
	hatch run test

test-cov: ## Run tests with coverage
	@echo '$(BLUE)Running tests with coverage...$(NC)'
	hatch run test-cov

test-parallel: ## Run tests in parallel
	@echo '$(BLUE)Running tests in parallel...$(NC)'
	hatch run test-parallel

lint: ## Run linters
	@echo '$(BLUE)Running linters...$(NC)'
	hatch run lint

lint-fix: ## Fix linting issues
	@echo '$(BLUE)Fixing linting issues...$(NC)'
	hatch run lint-fix

format: ## Format code
	@echo '$(BLUE)Formatting code...$(NC)'
	hatch run format

format-check: ## Check code formatting
	@echo '$(BLUE)Checking code formatting...$(NC)'
	hatch run format-check

type-check: ## Run type checker
	@echo '$(BLUE)Running type checker...$(NC)'
	hatch run type-check

check-all: ## Run all checks (format, lint, type, test)
	@echo '$(BLUE)Running all checks...$(NC)'
	hatch run check-all

pre-commit: ## Run pre-commit hooks
	@echo '$(BLUE)Running pre-commit hooks...$(NC)'
	pre-commit run --all-files

build: ## Build package
	@echo '$(BLUE)Building package...$(NC)'
	hatch build

clean: ## Clean build artifacts
	@echo '$(BLUE)Cleaning build artifacts...$(NC)'
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .eggs/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf site/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete

docs: ## Build documentation
	@echo '$(BLUE)Building documentation...$(NC)'
	hatch run docs:build

docs-serve: ## Serve documentation locally
	@echo '$(BLUE)Serving documentation...$(NC)'
	hatch run docs:serve

update: ## Update dependencies
	@echo '$(BLUE)Updating dependencies...$(NC)'
	pre-commit autoupdate
	pip install --upgrade hatch

security: ## Run security checks
	@echo '$(BLUE)Running security checks...$(NC)'
	bandit -r src -c pyproject.toml
	safety check

init-dev: install pre-commit ## Initialize development environment
	@echo '$(GREEN)Development environment initialized!$(NC)'

ci: check-all build ## Run CI checks locally
	@echo '$(GREEN)All CI checks passed!$(NC)'
