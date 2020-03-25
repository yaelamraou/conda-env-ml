# Anaconda Machine Learning Environment

[![Build Status](https://travis-ci.org/zsxoff/conda_env_ml.svg?branch=master)](https://travis-ci.org/zsxoff/conda_env_ml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Anaconda Machine Learning Environment for development and research.

## Grab this file directly

Via wget:

```bash
wget https://raw.githubusercontent.com/zsxoff/conda_env_ml/master/ml.yml
```

Via curl:

```bash
curl https://raw.githubusercontent.com/zsxoff/conda_env_ml/master/ml.yml -o ml.yml
```

## How to use it

For create this environment run:

```bash
conda env create --file ml.yml
```

For update this environment run:

```bash
conda env update --file ml.yml --prune
```

For remove this environment run:

```bash
conda env remove --name ml
```

## License

See [LICENSE](<https://github.com/zsxoff/conda_env_ml/blob/master/LICENSE>) file.
