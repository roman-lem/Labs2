import scipy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# читаем данные
data = pd.read_excel('./data.xlsx', header=None, index_col=None)
print(data.items())

x = data[0]
y = data[1]


# plt.figure()
# err = np.random.random_sample(7)
# plt.errorbar(x, y, xerr=2, fmt='+', ecolor='red')
# plt.errorbar(x, y, yerr=50, fmt='+', ecolor='red')
# plt.show()

# настраиваем детали отрисовки графиков
plt.figure(figsize=(8, 6))
plt.title("Installations")

plt.xlabel("Days")
plt.ylabel("Installations")

plt.autoscale(tight=True)

# рисуем исходные точки
#plt.scatter(x, y)
plt.errorbar(x, y, xerr=1, yerr=25, fmt='.', ecolor='red')

legend = []
# аргументы для построения графиков моделей: исходный интервал + 60 дней
fx = sp.linspace(x[0], x[6], 100)

    # получаем параметры модели для полинома степени 1
fp, residuals, rank, sv, rcond = sp.polyfit(x, y, 2, full=True)

    # функция-полином, если её напечатать, то увидите математическое выражение
f = sp.poly1d(fp)
print(f)

    # рисуем график модельной функции
plt.plot(fx, f(fx), linewidth=2)


plt.legend(legend, loc="upper left")
plt.grid()
plt.savefig('data.png', dpi=50)
plt.show()