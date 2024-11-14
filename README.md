# HighUd_mutationaccumulation
Code for mutation accumulation under high Ud

To start using please create a new enviornment using the yml file in this repo.
You can do this by typing 

```
conda env create --file HighUd_env.yml
conda activate HidhUd_mutationaccumulation
```

This should let you use the environment on the VSCode kernell

If using Jupyter notbooks you can aditionally type the next command on a terminal

```
python -m ipykernel install --user --name=HidhUd_mutationaccumulation
```

This will abilitate the environment into your jupyter notebook kernell selection

After this you can start working on the Jupyter notbooks available:

| File      | Description | 
| :--- | :---- | 
| PfixDFE.ipynb | This file allows to calculate the rate of mutation accumulation and genetic load for Moran population genetic models. Then it compares the theoretical prediction to simulated data. |
| findfixedmut.ipynb | This file allows to compute the table of fix mutations during a simulation. Then it calculate their CDF and compares it with theoretical expectation. |


To start use 

conda env create --file HighUd_env.yml

to create the environment to work on this file

PfixDFE.ipynb has functions to calculate the rate of mutation accumulation for population genetic models.
Then it compares the theoretical prediction to simulated data

findfixedmut.ipynb calculates the CDF of mutations that fix during simulations and compares it with theoretical expectation. It also calculates the load for a simulated population.