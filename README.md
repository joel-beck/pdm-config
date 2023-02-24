# pdm-config

![Pre-Commit](https://github.com/joel-beck/pdm-config/actions/workflows/pre-commit.yaml/badge.svg)
![Tests](https://github.com/joel-beck/pdm-config/actions/workflows/tests.yaml/badge.svg)

This project provides a minimal example for setting up Python packages in 2023 with modern tooling.
Its main purpose is reading information from cofiguration files in a structured, easily extendable and elegant fashion.

## Tools

### Package Manager

As the repository name suggests, this project uses [pdm](https://github.com/pdm-project/pdm) as package manager. `pdm` handles not only the installation of dependencies, but also the creation of virtual environments, execution of custom scripts similar to `npm`, and further serves as a build backend.
Thus, it works as a modern alternative to [poetry](https://github.com/python-poetry/poetry) and replaces the traditional package building process based on [setuptools](https://github.com/python-poetry/poetry).

Further, `pdm` stores all package metadata in `pyproject.toml` according to [PEP 621](https://peps.python.org/pep-0621/). There is no need for `setup.py` or `setup.cfg` files!


### Development Tools

- [black](https://github.com/psf/black) for formatting.
- [ruff](https://github.com/charliermarsh/ruff) for linting as an extremely fast and more complete substitute of [flake8](https://github.com/PyCQA/flake8). ruff can also replace [isort](https://github.com/PyCQA/isort) for sorting imports.
- [pytest](https://github.com/pytest-dev/pytest) for testing. Shared pytest fixtures are collected in `tests/conftest.py`.
- [mypy](https://github.com/python/mypy) for static type checking.


### Libraries

This project uses `toml` as configuration format in combination with the [tomllib](https://docs.python.org/3/library/tomllib.html) library which was added to the standard library in Python 3.11.
Further, it makes heavy use of Python [dataclasses](https://docs.python.org/3/library/dataclasses.html) for convenient and structured storage and access of configuration data.


### Workflow

- [pre-commit](https://github.com/pre-commit/pre-commit) for running all kinds of checks before committing and pushing to the remote repository.
- [pdm scripts](https://pdm.fming.dev/latest/usage/scripts/) for easy and consistent task execution similar to a `Makefile`.
- [GitHub Actions](https://docs.github.com/en/actions) as continuous integration service.


## Installation



## Usage

The entry point for this project is the `__main__.py` file in the `pdm_config` package directory.
It simply prints out the configuration data and can be executed via

```bash
# from `pdm_config` directory
python __main__.py

# from `pdm_config` directory
python -m pdm_config

# from any point of the project
pdm main   # or `pdm run main`
```
