# %% Import data
from itertools import combinations
import numpy as np
from pandas import read_csv

data = read_csv("./D1_jun_26_monday/quadrats2018.csv")
species = {
    "clover": 1,
    "dandelion": 2,
    "plantain": 3,
    "yarrow": 4
}


# %% chi-squared test


def chi_squared_test(x, y):
    # X & Y, X & !Y, !X & Y, !X & !Y
    obs = [0] * 4
    grand_total = 0
    for row in data.iterrows():
        row_data = row[1]
        if row_data[x] and row_data[y]:
            obs[0] += 1
        if row_data[x] and not row_data[y]:
            obs[1] += 1
        if not row_data[x] and row_data[y]:
            obs[2] += 1
        if not row_data[x] and not row_data[y]:
            obs[3] += 1
        grand_total += 1

    obs = np.array(obs)
    print(obs)
    exp = np.array([(obs[0] + obs[1]) * (obs[0] + obs[2]),
                    (obs[0] + obs[1]) * (obs[1] + obs[3]),
                    (obs[2] + obs[3]) * (obs[0] + obs[2]),
                    (obs[2] + obs[3]) * (obs[1] + obs[3])
                    ]) / grand_total
    chi_squared = np.sum((obs - exp) ** 2 / exp)
    return chi_squared


# %% dandelion and yarrow
max_name_len = max(map(len, species.keys()))
for species1, species2 in combinations(species.keys(), 2):
    chi_2 = chi_squared_test(species[species1], species[species2])
    critical_val = 3.84  # chi^2 corresponding to p=0.05
    print(f"\n==={species1} & {species2}")
    print("There is " + ("a " if chi_2 >= 3.84 else "no ") + "correlation")
    print(f"chi^2 = {chi_2}")
# chi_squared_test(species["plantain"], species["yarrow"])
