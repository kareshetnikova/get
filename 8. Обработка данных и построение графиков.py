import numpy as np
import matplotlib.pyplot as plt
import textwrap
with open("settings.txt", "r") as set:
    tmp = [float(i) for i in set.read().split("\n")]

data_arr = np.loadtxt("data.txt", dtype=int)
arr_num = np.array([i for i in range(data_arr.size)])  #массив номеров

data_arr_vol = data_arr * tmp[0]  #перевод отсчетов АЦП в вольты
data_arr_time = arr_num * tmp[1]  #перевод в секунды

fig, ax = plt.subplots(figsize=(16, 10), dpi=400)
ax.plot(data_arr_time, data_arr_vol, color='r', linewidth=1.5)
ax.scatter(data_arr_time[0:data_arr.size:20],   #маркеры
          data_arr_vol[0:data_arr.size:20],
          marker='s',
          c='red',
          s=25)

ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")

ax.axis([data_arr_vol.min(),data_arr_time.max(),data_arr_vol.min(),data_arr_vol.max()+0.2]) #максмальные минимальные значения для осей 


plt.grid()  #сетка
ax.minorticks_on() #второстепенные деления осей 
ax.grid(
    which='major',
    color='black',  #  цвет линий
    linewidth=0.3) #  толщина
  

ax.grid(
    which='minor',
    color='grey',  #  цвет линий
    linewidth=0.3,  #  толщина
    linestyle=':')  #  начертание

ax.text(7.5, 1.7, "Время зарядки: 4.21 с", fontsize=15)
ax.text(7.5, 1.9, "Время зарядки: 5.65 с", fontsize=15)

ax.legend('V',loc='upper left') #легенда 

ax.set_title("\n".join(textwrap.wrap("Зарядка и разрядка конденсатора в RC-цепи",60)),loc='center')
fig.savefig("test_vol_ispr.png")
fig.savefig("test_vol_ispr.svg")
plt.show()
