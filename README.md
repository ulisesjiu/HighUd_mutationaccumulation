## About
Code to analysis output data from the simulation package https://github.com/MaselLab/MutationLoad. Analysis include estimating the rate of mutation accumulation, genetic load in the population and CDF of fixed mutations.

## How to build
To start please create a new enviornment using the yml file in this repo.
You can do this by typing in a terminal:

```
conda env create --file HighUd_env.yml
conda activate HidhUd_mutationaccumulation
```

This should let you use the environment on the VSCode kernell

If you are using Jupyter notebooks, additionally type the next command on a terminal

```
python -m ipykernel install --user --name=HidhUd_mutationaccumulation
```

This will enable the environment into your jupyter notebook's kernell 

The analysis is performed using jupyter notebooks in python.
| File      | Description | 
| :--- | :---- | 
| PfixDFE.ipynb | This file allows to calculate the rate of mutation accumulation and genetic load for Moran population genetic models. Then it compares the theoretical prediction to simulated data. |
| findfixedmut.ipynb | This file allows to compute the table of fix mutations during a simulation. Then it calculate their CDF and compares it with theoretical expectation. |

## Folders

| Folder      | Description | 
| :--- | :---- | 
| graphs | Stores the graphs that results from the jupyter notebooks scripts |
| data | Contains example data to perform analysis |
