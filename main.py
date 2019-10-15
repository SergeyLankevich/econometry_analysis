import math
import numpy as np
import matplotlib.pyplot as plt
import quantecon as qt

alpha_k = 0
beta_k = 0
list1 = []
centered_list = []
list_alpha = []
list_beta = []
k = 0
T_average = 0
list_I = []


def input_function():
    T = int(input())
    for _ in range(T):
        t = float(input())
        list1.append(t)

def centered_list():
    for k in list1:
        T_average += k
    T_average /= T

    for k in list1:
        k -= T_average
        centered_list.append(k)

if T % 2 == 1:
    for k in range(int((T - 1) / 2 + 1)):
        for n in range(len(centered_list)):
            alpha_k += centered_list[n] * math.cos(2 * math.pi * n / T)
        alpha_k *= 2 / T
        list_alpha.append(alpha_k)
    list_alpha[0] = 0

    for k in range(int((T - 1) / 2 + 1)):
        beta_k = 0
        for n in range(len(centered_list)):
            beta_k += centered_list[n] * math.sin(2 * math.pi * n / T)
        beta_k *= 2 / T
        list_beta.append(beta_k)
    list_beta[0] = 0

    for m in range(int((T - 1) / 2 + 1)):
        coef = T / 2 * (list_alpha[m] ** 2 + list_beta[m] ** 2)
        list_I.append(coef)
else:
    for k in range(int(T / 2 + 1)):
        alpha_k = 0
        for n in range(len(centered_list)):
            alpha_k += centered_list[n] * math.cos(2 * math.pi * n / T)
        alpha_k *= 2 / T
        list_alpha.append(alpha_k)
    list_alpha[0] = 0
    list_alpha[-1] /= 2



    for k in range(int(T / 2 + 1)):
        beta_k = 0
        for n in range(len(centered_list)):
            beta_k += centered_list[n] * math.sin(2 * math.pi * n / T)
        beta_k *= 2 / T
        list_beta.append(beta_k)
    list_beta[0] = 0
    list_alpha[-1] = 0

    for m in range(int(T / 2 + 1)):
        coef = T / 2 * (list_alpha[m] ** 2 + list_beta[m] ** 2)
        list_I.append(coef)

J = list_I.index(max(list_I))
print(list_I)
print(list_alpha, list_beta)
for y in range(len(list_I)):
    R = math.sqrt(list_alpha[y] ** 2 + list_beta[y] ** 2)
    L = 2 * math.pi * y / T
    if list_alpha[y] == 0:
        print(0)
    else:
        O = math.atan(list_beta[y] / list_alpha[y])
        print(y, R, L, O)


window_length = len(list_I) # Кол-во наблюдений
y1 = [ϕ**k / (1 - O**2) for window_length in list_I]
y2 = [np.cos(np.pi * window_length) for window_length in list_I]
y3 = [a * b for a, b in pair(y1, y2)]

num_rows, num_cols = 3, 1
fig, axes = plt.subplots(num_rows, num_cols, figsize=(10, 8))
plt.subplots_adjust(hspace=0.25)

# Автоковариация после подсчёта гамма (О)
ax = axes[0]
ax.plot(times, y1, 'bo-', alpha=O, label='$\gamma(k)$')
ax.set(xlim=(0, 15), yticks=(-2, 0, 2))
ax.hlines(0, 0, 15, linestyle='--', alpha=0.5)

# Гармоническое разложение
ax = axes[2]
ax.stem(times, y3, label='Ряд Фурье после разложения')
ax.legend(loc='upper right')
ax.set(xlim=(0, 15), ylim=(-3, 3), yticks=(-1, 0, 1, 2, 3))
ax.hlines(0, 0, 15, linestyle='--', alpha=0.5)
ax.set_xlabel("k")

# TODO: Сглаживание по инндикаторам дисперсии k-ой степени


fig, ax = plt.subplots(3, 1, figsize=(10, 12))

for i, wl in range(20):  # Window lengths

    x, y = periodogram(X)
    ax[i].plot(x, y, 'b-', lw=2, alpha=0.5, label='Периодограмма')

    x_sd, y_sd = lp.spectral_density(two_pi=False, res=120)
    ax[i].plot(x_sd, y_sd, 'r-', lw=2, alpha=0.8, label='Спектральная частота')

    x, y_smoothed = periodogram(X, window='hamming', window_len=wl)
    ax[i].plot(x, y_smoothed, 'k-', lw=2, label='Сглаженная преиодограмма')

    ax[i].legend()

for i, wl in range(175):  # Window lengths

    x, y = periodogram(X)
    ax[i].plot(x, y, 'b-', lw=2, alpha=0.5, label='Периодограмма')

    x_sd, y_sd = lp.spectral_density(two_pi=False, res=120)
    ax[i].plot(x_sd, y_sd, 'r-', lw=2, alpha=0.8, label='Спектральная частота')

    x, y_smoothed = periodogram(X, window='hamming', window_len=wl)
    ax[i].plot(x, y_smoothed, 'k-', lw=2, label='Сглаженная преиодограмма')

plt.show()
