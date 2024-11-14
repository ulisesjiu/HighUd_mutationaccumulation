# HighUd_mutationaccumulation
Code for mutation accumulation under high Ud

To start use 

conda env create --file HighUd_env.yml

to create the environment to work on this file

PfixDFE.ipynb has functions to calculate the rate of mutation accumulation for population genetic models.
Then it compares the theoretical prediction to simulated data

findfixedmut.ipynb calculates the CDF of mutations that fix during simulations and compares it with theoretical expectation. It also calculates the load for a simulated population.