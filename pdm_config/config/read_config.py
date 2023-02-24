import os
from dataclasses import dataclass
from pathlib import Path

import dacite
import tomllib
from dotenv import load_dotenv

from pdm_config.config import Config, EnvironmentConfig, ModelConfig


@dataclass
class ConfigReader:
    config_path: Path

    def read_config(self) -> dict:
        with open(self.config_path, "rb") as f:
            config = tomllib.load(f)
        return config


def read_model_config(config_path: Path) -> ModelConfig:
    config_reader = ConfigReader(config_path)
    config_dict = config_reader.read_config()

    return dacite.from_dict(data_class=ModelConfig, data=config_dict["model"])


def read_environment_config() -> EnvironmentConfig:
    """Read environment variables from .env file"""
    load_dotenv()

    ssh_key = os.getenv("SSH_KEY")
    # check for existence such that function always returns strings and mypy is happy
    if ssh_key is None:
        raise ValueError("SSH_KEY not found in .env file")

    db_connection = os.getenv("DB_CONNECTION")
    if db_connection is None:
        raise ValueError("DB_CONNECTION not found in .env file")

    return EnvironmentConfig(SSH_KEY=ssh_key, DB_CONNECTION=db_connection)


def read_config(config_path: Path) -> Config:
    """Merge config from config.toml and environment variables from .env file"""
    model_config = read_model_config(config_path)
    environment_config = read_environment_config()

    return Config(model=model_config, environment=environment_config)
