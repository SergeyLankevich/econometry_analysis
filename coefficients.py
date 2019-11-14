import pandas as pd
import math
import numpy as np


list1 = []
centered_list = []
list_alpha = []
list_beta = []
k = 0
T_average = 0
list_I = []

with open('econ.txt') as file_1:
    for line in file_1:
        list1.append(float(line))
T = len(list1)

for k in list1:
    T_average += k
T_average /= T


for k in list1:
    k -= T_average
    centered_list.append(k)

if T % 2 == 1:
    for k in range(int((T - 1) / 2 + 1)):
        alpha_k = 0
        for n in range(1, len(centered_list + 1)):
            alpha_k += centered_list[n - 1] * (math.cos(2 * math.pi * n * k / T))
        alpha_k *= 2 / T
        list_alpha.append(alpha_k)
    list_alpha[0] = 0

    for k in range(int((T - 1) / 2 + 1)):
        beta_k = 0
        for n in range(1, len(centered_list) + 1):
            beta_k += centered_list[n - 1] * (math.sin(2 * math.pi * n * k / T))
        beta_k *= 2 / T
        list_beta.append(beta_k)
    list_beta[0] = 0

    for m in range(int((T - 1) / 2 + 1)):
        coef = T / 2 * (list_alpha[m] ** 2 + list_beta[m] ** 2)
        list_I.append(coef)
else:
    for k in range(int(T / 2 + 1)):
        alpha_k = 0
        for n in range(1, len(centered_list) + 1):
            alpha_k += centered_list[n - 1] * (math.cos(2 * math.pi * n * k / T))
        alpha_k *= 2 / T
        list_alpha.append(alpha_k)
    list_alpha[0] = 0
    list_alpha[-1] /= 2



    for k in range(int(T / 2 + 1)):
        beta_k = 0
        for n in range(1, len(centered_list) + 1):
            beta_k += centered_list[n - 1] * (math.sin(2 * math.pi * n * k / T))
        beta_k *= 2 / T
        list_beta.append(beta_k)
    list_beta[0] = 0
    list_beta[-1] = 0

    for m in range(int(T / 2 + 1)):
        coef = T / 2 * (list_alpha[m] ** 2 + list_beta[m] ** 2)
        list_I.append(coef)

J = list_I.index(max(list_I))
#print(list_I)
#print(list_alpha, list_beta)
#for y in range(len(list_I)):
    #R = math.sqrt(list_alpha[y] ** 2 + list_beta[y] ** 2)
    #L = 2 * math.pi * y / T
    #if list_alpha[y] == 0:
        #print(0)
    #else:
        #O = math.atan(list_beta[y] / list_alpha[y])
        #print(y, R, L, O)


R = math.sqrt(list_alpha[J] ** 2 + list_beta[J] ** 2)
L = 2 * math.pi * J / T
if list_alpha[J] == 0:
    print(0)
else:
    O = math.atan(list_beta[J] / list_alpha[J])
    print(R, L, O)

accounting_list = []
for q in range(len(centered_list)):
    p = R * math.cos(L * (q + 1) - O)
    accounting_list.append(p)
print(accounting_list)
