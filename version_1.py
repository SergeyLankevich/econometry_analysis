import math
import sympy
import numpy
alpha_k = 0
beta_k = 0
T_average = 0
k = 0
list1 = []
centered_list = []
a_coefficients = []
b_coefficients = []
list_I = []

T = int(input())
for _ in range(T):
    t = float(input())
    list1.append(t)

for k in list1:
    T_average += k
T_average /= T

for k in list1:
    k -= T_average
    centered_list.append(k)

print(centered_list)
if T % 2 == 1:
    for _ in range(int((T - 1) / 2 + 1)):
        for n in range(len(centered_list)):
            alpha_k += centered_list[n] + (math.cos(2 * math.pi) * n / T)
        alpha_k *= 2 / T
        print(alpha_k)
        a_coefficients.append(alpha_k)
        alpha_k = 0
    a_coefficients[0] = 0

    for _ in range(int((T - 1) / 2 + 1)):
        for n in range(len(centered_list)):
            beta_k += centered_list[n] + (math.sin(2 * math.pi) * n / T)
        beta_k *= 2 / T
        b_coefficients.append(beta_k)
        print(beta_k)
        beta_k = 0
    b_coefficients[0] = 0

    for m in range(int((T - 1) / 2 + 1)):
        coef = T / 2 * (a_coefficients[m] ** 2 + b_coefficients[m] ** 2)
        list_I.append(coef)
else:
    for _ in range(int(T / 2 + 1)):
        alpha_k = 0
        for n in range(len(centered_list)):
            alpha_k += centered_list[n] + (math.cos(2 * math.pi) * n / T)
        alpha_k *= 2 / T
        a_coefficients.append(alpha_k)
        alpha_k = 0
    a_coefficients[0] = 0
    a_coefficients[-1] /= 2

    for _ in range(int(T / 2 + 1)):
        beta_k = 0
        for n in range(len(centered_list)):
            beta_k += centered_list[n] + (math.sin(2 * math.pi) * n / T)
        beta_k *= 2 / T
        b_coefficients.append(beta_k)
    b_coefficients[0] = 0
    b_coefficients[-1] = 0

    for m in range(int(T / 2 + 1)):
        coef = T / 2 * (a_coefficients[m] ** 2 + b_coefficients[m] ** 2)
        list_I.append(coef)

J = list_I.index(max(list_I))
for y in range(len(list_I)):
    R = math.sqrt(a_coefficients[y] ** 2 + b_coefficients[y] ** 2)
    L = 2 * math.pi * y / T
    if a_coefficients[y] == 0:
        print(0)
    else:
        O = math.atan(a_coefficients[y] / b_coefficients[y])
        print(y, R, L, O)
print(a_coefficients, b_coefficients)
