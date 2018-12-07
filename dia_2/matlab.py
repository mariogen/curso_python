import numpy as np
from scipy import optimize,integrate,interpolate
import matplotlib.pyplot as plt
 
A = np.array([[1.,2.],[4.,5.]])
print('A =\n',A,'\n')
print('norm(A) =',np.linalg.norm(A),'\n')

B = np.ones((2,2))
C = np.zeros(B.shape)
D = np.eye(4)
E = np.diag(range(3))
b = B[:,1]

#solve A*x=b
x0 = np.linalg.inv(A)@b
x1 = np.linalg.pinv(A)@b
x2 = np.linalg.solve(A,b)
x3,residuals,rank,s = np.linalg.lstsq(A,b)

for i,x in enumerate([x0,x1,x2,x3]):
    print('x{} = {}'.format(i,x))

u,s,vh = np.linalg.svd(A)
L = np.linalg.cholesky(D)
w,v = np.linalg.eig(A)
q,r = np.linalg.qr(A)

signal = np.sin(np.linspace(0,3*np.pi,100))
out = np.fft.fft(signal)

plt.subplot(1,2,1)
plt.plot(abs(out))
plt.title('modulo')
plt.subplot(1,2,2)
plt.plot(np.angle(out))
plt.title('fase')

y,abserr = integrate.quad(lambda x: np.sqrt(1-x**2), -1, 1)

res = optimize.minimize(lambda x: np.exp(x)+x**2,
                  x0=1,
                  method='BFGS',
                  tol = 0.6)

x = np.linspace(-np.pi,np.pi,4)
y = np.sin(x)
x_new = np.linspace(-np.pi,np.pi,100)
y_new = interpolate.interp1d(x, y,'cubic')(x_new)
plt.figure()
plt.plot(x, y, 'o',
         x_new, y_new, '-',
         x_new, np.sin(x_new), '--')

sol = integrate.solve_ivp(fun = lambda t,y: -0.5*y,
                          t_span = [0, 10],
                          y0 = [5,4,2,1,3],
                          method = 'RK45',
                          max_step = 0.1)
plt.figure()
plt.plot(sol.t,sol.y.T)

plt.figure()
plt.bar(['um','dois','tres'],[4,5,6])

x = np.arange(0,4,0.1)
y = 2*x+np.random.randn(*x.shape)
plt.figure()
plt.scatter(x,y,marker='*')


N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-2.0, 2.0, N)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
plt.figure()
plt.contourf(X,Y,Z)
plt.figure()
plt.contour(X,Y,Z)
plt.figure()
plt.imshow(Z)

plt.figure()
plt.pie([3,4,2,5])

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z,cmap=cm.rainbow)


"""
Muitas outras referencias de gráficos em
matplotlib.org/gallery/index.html
"""





