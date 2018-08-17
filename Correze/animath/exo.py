# %%
from pandas import read_csv
import matplotlib.pyplot as plt
import math

# %%
palmares = read_csv('./animath/palmares.csv')

# %%
scores = [0] * 5
student_cnt = 0

for student_data in palmares.iterrows():
    student_cnt += 1
    student_info = student_data[1]
    for i in range(5):
        if student_info["classe"] != "première":
            continue
        exo_score = student_info[f"exo {i + 4}"]
        if not math.isnan(exo_score):
            scores[i] += exo_score

# %%
plt.figure()
plt.bar(range(4, 9), list(map(lambda s: s / student_cnt, scores)))
plt.xlabel("Exo nº")
plt.ylabel("Average score / 7")
plt.ylim([0, 7])
plt.title("Coupe Animath Printemps 2018\nClasse de Première")
plt.show()
