#matplotlib.pyplot for the graph
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
#numpy for the arrays and math-on-array stuff
import numpy as np


#defining the domain
x = np.arange(-1.5,1.51,0.01)             # µm
z = np.arange(-1.5,1.51,0.01)             # µm
X1, Z1 = np.meshgrid(x, z[z<=0.1])
X2, Z2 = np.meshgrid(x, z[z>=0])

# params
e1 = 2
e2 = 1
n1 = np.sqrt(e1) + 0j
n2 = np.sqrt(e2) + 0j
l = 633*10**(-3)                     # µm
k0 = 2*np.pi/l

# variable part
def calc_field(n1, n2, X1, X2, Z1, Z2, th1 = 40):
    t1 = np.pi/180 * th1
    kx = n1*k0*np.sin(t1)
    kz1 = n1*k0*np.cos(t1)
    kz2 = np.sqrt((n2*k0)**2 - kx**2) # implement sqrt
    r = (kz1 - kz2)/(kz1 + kz2)
    t = (2*kz1)/(kz1 + kz2)

    #f, the function
    F1 = np.exp(1j*(kx*X1 + kz1*Z1)) + r*np.exp(1j*(kx*X1 - kz1*Z1))
    F2 = t*np.exp(1j*(kx*X2 + kz2*Z2))

    return F1, F2

F1, F2 = calc_field(n1, n2, X1, X2, Z1, Z2, 40)
F3, F4 = calc_field(n1, n2, X1, X2, Z1, Z2, 46)
#plot the actual graph with the label
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
#plt.plot(x, np.cos(2*np.pi/l*x))
#ax = plt.axes(projection='3d')
#ax.plot_surface(X1, Z1, F1, rstride=1, cstride=1, cmap='jet', edgecolor='none')
# plt.imshow(np.real(F1), extent=[-1.5, 1.5, -1.5, 0])
ax1.contourf(X1,Z1,np.real(F1))
ax1.contourf(X2,Z2,np.real(F2))
ax2.contourf(X1,Z1,np.real(F3))
ax1.set_title(r"$\Re(\vec{E})$ with angle 40°")
ax2.set_title(r"$\Re(\vec{E})$ with angle 46°")
im2 = ax2.contourf(X2,Z2,np.real(F4))
#show the label
divider = make_axes_locatable(ax2)
cax = divider.append_axes('right', size='5%', pad=0.15)
fig.colorbar(im2, cax=cax, orientation='vertical')
#show the graph
plt.show()
# ---------

x = np.arange(-1.5,1.51,0.01)             # µm
# params
e1 = 2
e2 = 1
n1 = np.sqrt(e1) + 0j
n2 = np.sqrt(e2) + 0j
l = 633*10**(-3)                     # µm
k0 = 2*np.pi/l

# variable part
def calc_field(n1, n2, X1, X2, Z1, Z2, th1 = 40):
    t1 = np.pi/180 * th1
    kx = n1*k0*np.sin(t1)
    kz1 = n1*k0*np.cos(t1)
    kz2 = np.sqrt((n2*k0)**2 - kx**2) # implement sqrt
    r = (kz1 - kz2)/(kz1 + kz2)
    t = (2*kz1)/(kz1 + kz2)

    #f, the function
    F1 = np.exp(1j*(kx*X1 + kz1*Z1)) + r*np.exp(1j*(kx*X1 - kz1*Z1))
    F2 = t*np.exp(1j*(kx*X2 + kz2*Z2))

    return F1, F2
F1i, F2i = calc_field(n1, n2, x, x, 0, 0, 40)
F1gi, F2gi = np.gradient(F1i), np.gradient(F2i)
((F1gi[1] - F2gi[1]) <= 1.1*sys.float_info.epsilon).all()       # check gradient continuity along z
# ---------

F1, F2 = calc_field(n1, n2, X1, X2, Z1, Z2, 40)

F1g, F2g = np.gradient(F1), np.gradient(F2)

#plot the actual graph with the label
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

ax1.contourf(X1,Z1,np.real(F1g[0]))
ax1.contourf(X2,Z2,np.real(F2g[0]))
ax2.contourf(X1,Z1,np.real(F1g[1]))
im2 = ax2.contourf(X2,Z2,np.real(F2g[1]))

ax1.set_title(r"$\Re(\nabla{E}_x)$ with angle 40°")
ax2.set_title(r"$\Re(\nabla{E}_z)$ with angle 40°")

#show the label
divider = make_axes_locatable(ax2)
cax = divider.append_axes('right', size='5%', pad=0.15)
fig.colorbar(im2, cax=cax, orientation='vertical')
#show the graph
plt.show()