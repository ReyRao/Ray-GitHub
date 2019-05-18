import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0, 50, 0.1)
# x = np.linspace(0, 49, 490)
# print(x[:10])
FCT = 23
HCT = 11
upper1 = 23000 * 1.05
upper2 = 23000 * 1.043
y1 = upper1 * x / (1.3 + abs(x))
y2 = upper2 * x / (0.75 + abs(x))

plt.plot(x, y1, color='b')
plt.plot(x, y2, color='g')

plt.text(22, upper1-2700, 'FULL(CT=%i, Cm=%i)' %(FCT, y1[FCT*10]), color='r')
plt.plot(x[FCT*10], y1[FCT*10], 'r*', markersize=12)
plt.text(8, upper1-4500, 'Half(CT=%i, Cm=%i)' %(HCT, y1[HCT*10]), color='b')
plt.plot(x[HCT*10], y1[HCT*10], 'r*',color='b', markersize=12)

plt.text(22, upper2-200, 'FULL(CT=%i, Cm=%i)' %(FCT, y2[FCT*10]), color='r')
plt.plot(x[FCT*10], y2[FCT*10], 'r*', markersize=12)
plt.text(2, upper2-800, 'Half(CT=%i, Cm=%i)' %(HCT, y2[HCT*10]), color='b')
plt.plot(x[HCT*10], y2[HCT*10], 'r*',color='b', markersize=12)


plt.title('Charging-rate Scheme', size=15)
plt.ylabel('Mutual Capacity (Cm)')
plt.xlabel('Cycle Time (CT)')
plt.tight_layout()
plt.show()

