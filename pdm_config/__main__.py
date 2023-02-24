"""
Run main module with `python -m pdm_config` from package root (pdm-config/pdm_config),
not project root!
"""
from pathlib import Path

from pdm_config.config import read_config

config_path = Path("./config/config.toml")
config = read_config(config_path)

# model config
print(f"{config.model.data.num_classes = }")
print(f"{config.model.data.num_features = }")
print(f"{config.model.data.num_samples = }")
print(f"{config.model.data.target_col = }")
print(f"{config.model.data.test_size = }")

print(f"{config.model.metrics.refit = }")
print(f"{config.model.metrics.scoring = }")

print(f"{config.model.n_folds = }")
print(f"{config.model.n_iter = }")
print(f"{config.model.random_state = }")
print(f"{config.model.verbose_level = }")

# environment config
print(f"{config.environment.SSH_KEY = }")
print(f"{config.environment.DB_CONNECTION = }")
