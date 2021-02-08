import matplotlib.pyplot as plt
f, ax = plt.subplots()
f.set_figheight(10)
f.set_figwidth(10)
x = [i for i in range(10)]
y = [i**2 for i in x]
ax.plot(x, y);
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.savefig("week5Python.png", dpi = 72)

f, ax = plt.subplots()
ax.plot(x, y);
ax.set_xlabel('$\\sigma$')
ax.set_ylabel('$\\tau$')
plt.show()

f, ax = plt.subplots()
ax.plot(x, y);
ax.set_xlabel('$\\sigma{_s}{^2}$')
ax.set_ylabel('y')
plt.show()


f, ax = plt.subplots()
ax.plot(x, y, 'r-.',linewidth=3)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

gamma = 7;
f, ax = plt.subplots()
ax.plot(x, y);
plt.title('$\\Gamma$ = ' + str(gamma))
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()


gamma = 7;
f, ax = plt.subplots()
ax.plot(x, y)
plt.annotate("$\\Gamma$ = " + str(gamma), xy=(2,30))
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()


f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, y, 'r-.', linewidth=3)
ax2.plot(x, y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.show()

import matplotlib.gridspec as gridspec
fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)
f_ax1 = fig.add_subplot(spec[0, 0])
f_ax2 = fig.add_subplot(spec[0, 1])
f_ax3 = fig.add_subplot(spec[1, 0])
f_ax4 = fig.add_subplot(spec[1, 1])
f_ax1.plot(x, y)
f_ax1.set_xlabel('$\\sigma$')
f_ax1.set_ylabel('$\\tau$')
f_ax2.plot(x, y)
f_ax2.set_xlabel('$\\sigma{_s}{^2}$')
f_ax2.set_ylabel('y')
f_ax3.plot(x, y, 'r-.', linewidth=3)
f_ax3.set_xlabel('x')
f_ax3.set_ylabel('y')
f_ax4.plot(x, y)
plt.title('$\\Gamma$ = ' + str(gamma))
f_ax4.set_xlabel('x')
f_ax4.set_ylabel('y')
plt.show()