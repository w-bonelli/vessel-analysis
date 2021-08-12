# Vessel Detector

![CI](https://github.com/w-bonelli/vessel-detector/workflows/CI/badge.svg) [![Coverage Status](https://coveralls.io/repos/github/w-bonelli/vessel-detector/badge.svg?branch=master)](https://coveralls.io/github/w-bonelli/vessel-detector?branch=master)

Detect injection-filled and empty vessels in stem tissues.

## Acknowledgements


General approach inspired by Suxing Liu, in particular [Smart Plant Growth Top-Down Traits](https://github.com/Computational-Plant-Science/spg).

[PlantCV](https://github.com/danforthcenter/plantcv) also used to analyze each vessel's shape.

## Requirements

[Docker](https://www.docker.com/) is required to run this project in a Unix environment.

## Installation

To install from source, clone the project with `git clone https://github.com/w-bonelli/vessel-detecetor.git`, then build the image from the root directory with `docker build -t <your tag> -f Dockerfile .`.

Alternatively, you can just pull the pre-built image with `docker pull wbonelli/vessel-detector`, or allow it to be pulled automatically from another Docker CLI command (as below).

## Usage

To analyze an image:

```shell
docker run wbonelli/vessel-detector python3.8 /opt/code/vd.py detect <input file>
```

## Development

To set up a development environment and explore or modify the source, just mount the project root as your container's working directory, for instance:

```bash
docker run -it -v $(pwd):/opt/dev -w /opt/dev wbonelli/vessel-detector bash
```

A good way to get started is to run the tests:

```shell
docker run -it -v $(pwd):/opt/dev -w /opt/dev wbonelli/vessel-detector python3 -m pytest -s
```

### Supported filetypes

By default, JPG, PNG, and CZI files are supported. To limit the analysis to certain filetypes, use the `-ft` flag (a comma-separated for multiple), for instance: `-ft png,czi`.
