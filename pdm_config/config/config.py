from dataclasses import dataclass


@dataclass
class MetricsConfig:
    scoring: list[str]
    refit: str


@dataclass
class DataConfig:
    num_samples: int
    num_features: int
    num_classes: int
    target_col: str
    test_size: float


@dataclass
class ModelConfig:
    metrics: MetricsConfig
    data: DataConfig
    n_folds: int
    n_iter: int
    random_state: int
    verbose_level: int


@dataclass
class EnvironmentConfig:
    SSH_KEY: str
    DB_CONNECTION: str


@dataclass
class Config:
    model: ModelConfig
    environment: EnvironmentConfig
