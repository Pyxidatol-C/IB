# %% Imports
import glob
import cv2
import numpy as np

# %%
path_name = "./D4_group4_project/lilia_cv/Scrnshts"
for i in range(1, 13):
    for whatever in ('f', 'b'):
        img = cv2.imread(f"{path_name}/{i}{whatever}.png")
        print(f"{i}{whatever}")
        mean = np.mean(img, axis=(0, 1))
        b, g, r = mean
        print("blue:", round(b, 3), "\ngreen:", round(g, 3), "\nred:", round(r, 3), end="\n\n")
# %% Crop image (if needed)
# cropped_img = img[64:128, 256:320, :]  # ':' to get all of BGR
# success = cv2.imwrite(f"{path_name}/cropped.png", cropped_img)
# assert success, "Failed to save."

# %% Read pixel
# TODO get exact position of desired pixel (using Preview?)
# TODO or use opencv's recognition modelsb, g, r = cropped_img[32, 32, :]
# print("b:", b)
# print("g:", g)
# print("r:", r)

# %% Mean of image
mu = np.mean(cropped_img, axis=(0, 1))
b_mu, g_mu, r_mu = mu
# btw hold down alt and left click for multi-cursor
print("b_avg:", b_mu)
print("g_avg:", g_mu)
print("r_avg:", r_mu)
