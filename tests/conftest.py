from pathlib import Path

import pytest

from pdm_config.config import Config, EnvironmentConfig, ModelConfig, read_config


@pytest.fixture
def root_path() -> Path:
    return Path(__file__).parent.parent


@pytest.fixture
def config_path(root_path: Path) -> Path:
    return root_path / "pdm_config" / "config" / "config.toml"


@pytest.fixture
def config(config_path: Path) -> Config:
    # Mock environment variables for testing
    return read_config(config_path, mock=True)


@pytest.fixture
def model_config(config: Config) -> ModelConfig:
    return config.model


@pytest.fixture
def environment_config(config: Config) -> EnvironmentConfig:
    return config.environment
