import scipy as sp
import openpyxl as ox
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# читаем данные

wb = ox.load_workbook(filename = './data.xlsx')
x = list()
y = list()
ws = wb['Sheet1']
for cell in  ws['A']:
	x.append(cell.value)
for cell in  ws['B']:
	y.append(cell.value)
print(x)
print(y)

# настраиваем детали отрисовки графиков
plt.figure(figsize=(8, 6))

plt.xlabel("N")
plt.ylabel("f, Hz")

plt.autoscale(tight=True)

# рисуем исходные точки
plt.errorbar(x, y, yerr=5, fmt='.', ecolor='red', color='red')

legend = []
# аргументы для построения графиков моделей: исходный интервал + 60 дней
fx = sp.linspace(x[0]-0.5, x[len(x) - 1]+0.5, 100)

    # получаем параметры модели для полинома степени 1
fp, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)

    # функция-полином, если её напечатать, то увидите математическое выражение
f = sp.poly1d(fp)
print(f)


avgx = 0
avgy = 0
avgx2 = 0
avgy2 = 0
avgxy = 0
for i in range(len(x)):
	avgx += x[i]
	avgy += y[i]
	avgx2 += x[i] * x[i]
	avgy2 += y[i] * y[i]
	avgxy += x[i] * y[i]

avgx = avgx/len(x)
avgy = avgy/len(x)
avgx2 = avgx2/len(x)
avgy2 = avgy2/len(x)
avgxy = avgxy/len(x)

koef = (avgxy - avgx*avgy)/(avgx2 - avgx*avgx)

sigma = np.sqrt((avgy2 - avgy*avgy)/(avgx2 - avgx*avgx) - koef*koef)/np.sqrt(len(x))

print("Коэффициент = ")
print(koef)

print("Погрешность = ")
print(sigma)
	

    # рисуем график модельной функции
plt.plot(fx, f(fx), linewidth=2)


plt.legend(legend, loc="upper left")
plt.grid()
plt.savefig('data.png', dpi=50)
plt.show()
