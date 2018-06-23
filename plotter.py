import numpy as np
import matplotlib.pyplot as plt
import sys
import os

def a(mes):
  if len(mes) == 2:
    return mes
  else:
    return '0'+mes

'''
day = int(input('Digite o dia desejado: '))
month = input('Digite o mes: ')
year = int(input('Digite o ano: '))
inst = input("de qual instrumento voce deseja obter os dados? [STA/STB] ")
dt = str(inst)+'_'+str(day)+a(month)+str(year)+'.txt'
print('a data escolhida eh ', dt)'''

#dt = input("digite o nome/diretório do arquivo: ")
dt = ""
try:
  dt = sys.argv[1]
  print(dt)
except:
  if len(dt) < 1:
    dt = input("digite o nome do arquivo: ")

def lined(vars, ax, time=0):
  for var in vars:
    f = sorted(var)
    ax.plot([time, time], [0, int(f[-1])], color = 'red', linewidth=0.5)

t = []
BTOTAL = []
NP = []
SPEED = []
TEMPERATURE = []
VP_RTN = []
BETA = []
TOTAL_PRESSURE = []
BX = []
BY = []
BZ = []
THERMAL_SPEED = []

today = []

with open(dt, 'r') as dataset:
    for line in dataset:
        line = line.strip()
        if line[0] != '#':
          
          #if int(line[:2]) == day and int(line[3:5]) == month and int(line[6:10]) == year:
          today.append(line)
          
del today[2]
del today[1]
del today[0]
for line in today:
    line = line.replace('-1.00000E+30',"      nan   " )
    t.append(((float(line[11:13])*60 + float(line[14:16]))/1440)+float(line[:2]))
    BTOTAL.append(float(line[23:37]))
    #print(BTOTAL[-1])
    NP.append(float(line[37:52]))
    #print(NP[-1])
    SPEED.append(float(line[51:65]))
    #print(SPEED[-1])
    TEMPERATURE.append(float(line[65:79]))
    #print(TEMPERATURE[-1])
    THERMAL_SPEED.append(float(line[79:93]))
    #print(THERMAL_SPEED[-1])
    VP_RTN.append(float(line[93:107]))
    #print(VP_RTN[-1])
    BETA.append(float(line[107:122]))
    #print(BETA[-1])
    TOTAL_PRESSURE.append(float(line[122:137]))
    #print(TOTAL_PRESSURE[-1])
    BX.append(float(line[137:152]))
    #print(BX[-1])
    BY.append(float(line[152:166]))
    #print(BY[-1])
    BZ.append(float(line[166:]))
    #print(BZ[-1])
    print(str(t[-1])+': ')



fig = plt.figure()
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                wspace=0.2, hspace=0.0)

ax1 = fig.add_subplot(6, 1, 1)
ax2 = fig.add_subplot(6, 1, 2)
ax3 = fig.add_subplot(6, 1, 3)
ax4 = fig.add_subplot(6, 1, 4)
ax5 = fig.add_subplot(6, 1, 5)
ax6 = fig.add_subplot(6, 1, 6)

ax1.plot(t, BTOTAL, color='blue', linewidth=1, label='BTOTAL')
ax1.plot(t, BX, color='red', linewidth=0.4, label='BX')
ax1.plot(t, BY, color='orange', linewidth=0.4, label='BY')
ax1.plot(t, BZ, color='green', linewidth=0.4, label='BZ')
ax1.legend(loc='upper left', fontsize=8)
ax1.set_title(dt)#('BTOTAL - BX - BY - BZ', fontsize=7, x=1, y=0)
#ax1.set_xlabel('dia')
ax1.set_ylabel('nT')
ax1.set_xticklabels('')
ax1.grid(True)

ax2.plot(t, SPEED, color='blue', linewidth=1, label='SPEED')
ax2.plot(t, VP_RTN, color='red', linewidth=0.4, label='VP_RTN')
ax2.legend(loc='upper left')
ax2.set_title("")#('SPEED - VP_RTN', fontsize=7)
#ax2.set_xlabel('dia')
ax2.set_ylabel('km/s')
ax2.set_xticklabels("")
ax2.grid(True)


ax3.plot(t, TEMPERATURE, color='blue', linewidth=0.4, label='TEMPERATURE')
ax3.legend(loc='upper left')
ax3.set_title("")#('TEMPERATURE', fontsize=7)
#ax3.set_xlabel('dia')
ax3.set_ylabel('deg_K')
ax3.set_xticklabels("")
ax3.grid(True)


ax4.plot(t, NP, color='blue', linewidth=0.4, label='NP')
ax4.legend(loc='upper left')
ax4.set_title("")#('NP', fontsize=7)
#ax4.set_xlabel('dia')
ax4.set_ylabel('1/cm^3')
ax4.set_xticklabels("")
ax4.grid(True)


ax5.plot(t, BETA, color='blue', linewidth=0.4, label='BETA')
ax5.legend(loc='upper left')
ax5.set_title("")#('BETA', fontsize=7)
#ax5.set_xlabel('dia')
ax5.set_ylabel('pPa')
ax5.set_xticklabels("")
ax5.grid(True)


ax6.plot(t, TOTAL_PRESSURE, color='blue', linewidth=0.4, label='TOTAL_PRESSURE')
ax6.legend(loc='upper left')
ax6.set_title("")#('TOTAL_PRESSURE', fontsize=7)
ax6.set_xlabel('dia')
ax6.set_ylabel('nT')
e = t[-1]
xticklabels  = [t[0], e*0.1, e*0.2, e*0.3, e*0.4, e*0.5, e*0.6, e*0.7,  e*0.8, e*0.9, e]
ax6.grid(True)



try:
  figManager = plt.get_current_fig_manager()
  figManager.window.showMaximized()
except:
  pass

plt.grid(True)
plt.savefig(dt+'_graph.png')
print("saved!")


plt.show()
