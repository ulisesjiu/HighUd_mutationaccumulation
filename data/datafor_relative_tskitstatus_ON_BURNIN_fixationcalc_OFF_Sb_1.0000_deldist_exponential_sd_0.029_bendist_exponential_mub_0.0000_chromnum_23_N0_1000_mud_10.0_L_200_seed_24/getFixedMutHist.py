# Implements functionality for generating a histogram of the probability of 
# fixation for deleterious mutations of different effect sizes

import os
import io
import numpy as np
import pandas as pd
import sys
import concurrent.futures
import msprime
import tskit
import math
import matplotlib.pyplot as plt

# Added code for obtaining a histogram with the probability of fixation for deleterious mutations 
# with varying effect sizes

allFixedData = np.loadtxt("fixed_mut.txt", skiprows=1)
# allFixedData = np.multiply(allFixedData, -1)
hist, binEdges = np.histogram(allFixedData, bins=100)

N = int(input("Enter population size: "))
burnin = int(input("Enter burn-in generation: "))
Ud = float(input("Enter Ud: "))
totalGen = int(input("Enter the total number of generations: "))
gensSinceBurnin = totalGen - burnin
divValue = N * Ud * gensSinceBurnin
probHist = np.divide(hist, divValue)

# Attempt at creating a CDF (without binning)
numVals = len(allFixedData)
sorted = np.sort(allFixedData)
CDF = np.arange(numVals) / float(numVals)
plt.xlabel("Effect size")
plt.ylabel("Cumulative Probability")
plt.title("CDF of Fixed Mutation Counts")
plt.plot(sorted, CDF)
plt.savefig("nonbinnedCDFAttempt.png")



'''
plt.stairs(probHist, binEdges, fill=True)
# plt.vlines(binEdges, probHist.min(), probHist.max(), colors="w")
plt.xlabel("Negated effect size", fontweight = "bold")
plt.ylabel("Probability of fixation * DFE", fontweight = "bold")
plt.tight_layout()
plt.ylim(0, 0.000003)

plt.savefig("fixedMutHistogram.png")
'''