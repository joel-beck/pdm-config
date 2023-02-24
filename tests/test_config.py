from dataclasses import fields
from typing import ClassVar, Protocol

from pdm_config.config import Config, EnvironmentConfig, ModelConfig


class IsDataclass(Protocol):
    """
    Check if class is a dataclass, see
    https://stackoverflow.com/questions/54668000/type-hint-for-an-instance-of-a-non-specific-dataclass
    """

    __dataclass_fields__: ClassVar[dict]


def _test_dataclass_keys(dataclass: IsDataclass, keys: list[str]) -> None:
    assert [field.name for field in fields(dataclass)] == keys


def test_config_keys_parsing(config: Config) -> None:
    _test_dataclass_keys(config, ["model", "environment"])


def test_model_config_keys_parsing(model_config: ModelConfig) -> None:
    _test_dataclass_keys(
        model_config,
        [
            "metrics",
            "data",
            "n_folds",
            "n_iter",
            "random_state",
            "verbose_level",
        ],
    )


def test_environment_config_keys_parsing(environment_config: EnvironmentConfig) -> None:
    _test_dataclass_keys(environment_config, ["SSH_KEY", "DB_CONNECTION"])


def test_recursive_dataclasses_parsing(model_config: ModelConfig) -> None:
    assert model_config.data.__class__.__name__ == "DataConfig"
    assert model_config.metrics.__class__.__name__ == "MetricsConfig"


def test_dtype_parsing(config: Config) -> None:
    assert isinstance(config.model.data.num_samples, int)
    assert isinstance(config.model.data.num_features, int)
    assert isinstance(config.model.data.num_classes, int)
    assert isinstance(config.model.data.target_col, str)
    assert isinstance(config.model.data.test_size, float)

    assert isinstance(config.model.metrics.scoring, list)
    assert isinstance(config.model.metrics.refit, str)

    assert isinstance(config.model.n_folds, int)
    assert isinstance(config.model.n_iter, int)
    assert isinstance(config.model.random_state, int)
    assert isinstance(config.model.verbose_level, int)

    assert isinstance(config.environment.SSH_KEY, str)
    assert isinstance(config.environment.DB_CONNECTION, str)
