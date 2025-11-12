# Multi-level Synthetic Control Estimator

[![PyPI](https://img.shields.io/pypi/v/multi-level-sc-estimator.svg)](https://pypi.org/project/multi-level-sc-estimator/)
[![Tests](https://github.com/leabottmer/multi-level-sc-estimator/actions/workflows/test.yml/badge.svg)](https://github.com/leabottmer/multi-level-sc-estimator/actions/workflows/test.yml)
[![Changelog](https://img.shields.io/github/v/release/leabottmer/multi-level-sc-estimator?include_prereleases&label=changelog)](https://github.com/leabottmer/multi-level-sc-estimator/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/leabottmer/multi-level-sc-estimator/blob/main/LICENSE)

This package implements the multi-level SC estimator (mlSC) for the treatment effect for a single, treated, aggregated unit in panel data with multiple levels of aggregation, as proposed in Bottmer (2025). 

## Installation

Install this library using `pip`:
```bash
pip install multi-level-sc-estimator
```
## Usage

Usage instructions go here.

## References
Lea Bottmer. **Synthetic Control with Disaggregated Data**, 2025. [[link]](https://leabottmer.github.io/job_market/jmp_bottmer.pdf)

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:
```bash
cd multi-level-sc-estimator
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
python -m pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
