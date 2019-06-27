# Purpose

This repository contains supplemental material to the ESA 2019 paper "PUFFINN: Parameterless and Universally Fast FInding of Nearest Neighbors". This repository 
contains the scripts and Jupyter notebooks used in the evaluation. The code is available at https://github.com/puffinn/puffinn. Please refer to this repository to build the code.

## Replication of Experiments in Paper

1. Get ann-benchmarks from https://github.com/erikbern/ann-benchmarks
2. Copy `algos-puffinn-evaluation.yaml` into the main ann-benchmarks directory.
3. Copy `Dockerfile.puffinn` into `ann_benchmarks/install/`.
4. Install `ann-benchmarks` following the guide on https://github.com/erikbern/ann-benchmarks
5. Run `python run.py --dataset glove-100-angular --definitions algos-puffinn-evaluation.yaml` from the main ann-benchmarks directory to run all experiments on Glove-1M. (Note that this will take several days. Modify the list of parameters used by PUFFINN to shorten the time it takes to carry out the experiment.)

## Looking at the Evaluation

All raw experimental results are found in `evaluation/all.csv`. Data and plots were evaluated using Jupyter notebook. The notebook is available at `evaluation/log.ipynb`. 
