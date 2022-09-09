import numpy as np
import matplotlib.pyplot as plt; plt.ion()
from scipy.ndimage.interpolation import rotate
from astropy.modeling import models, fitting
import math as m
import os, sys, time
from astropy.io import fits as pf
import array
import matplotlib.pyplot as plt
from scipy.special import jv
import scipy.signal as signal
from astropy.modeling import models, fitting
from astropy.modeling.models import custom_model
from scipy.interpolate import interp1d

# the psf for modulator 1 set at 0.5 256
m = np.load('/Users/aliciachun/Desktop/mod/mod0_at1.npy')

# find columns of interest:
startcol = 0
for i in range(len(m)):
    if np.max(m[:, i] >= 6000):
        startcol = i
        break

endcol = 0
for i in reversed(range(len(m))):
    if np.max(m[:, i] >= 6000):
        endcol = i
        break
# take columns of interest of m (81, 169) and append the index of their maximum value to y = []. This is y value.

y = []
for i in range(startcol, endcol):
    mcol = m[:, i]
    x = list(range(len(m)))
    centroid = np.sum(mcol*x)/np.sum(mcol)
    y.append(centroid)

x = list(range(startcol, endcol))

plt.figure()
plt.plot(x, y)
fit = fitting.LinearLSQFitter()
line_init = models.Linear1D()
fitted_line = fit(line_init, x, y)

plt.plot(x, fitted_line(x), 'k-', label='Fitted Model')

slope = fitted_line.slope.value
angle = (np.arctan(slope)*180.0/math.pi)

# rotate figure
rotated = rotate(m, angle=angle)

# find row w/ max value for small values
rcol = rotated[:, startcol]
rrcol = rotated[:, endcol]
index = (rcol.argmax()+rrcol.argmax())/2
rrow130 = rotated[int(index)]
plt.figure()
plt.plot(rrow130)
plt.matshow(rotated)
plt.show()


# best fit
@custom_model
def modulated_line(x, amplitude=1.0, x_0=0, span=1.):
    radius = 10.15
    r0 = 1.2196698912665045
    x1 = np.arange(x.min(), x.max()+1,1e-2)
    x2 = np.arange(-5*radius, 5*radius, 1e-2)
    psf = (jv(1,np.pi*x2/radius*r0)/(np.pi*x2/radius*r0))**2
    sig = 1/np.sqrt(1-(2*(x1-x_0)/span)**2)
    sig = np.nan_to_num(sig)
    sig = sig*(sig<1000)
    filtered = signal.convolve(sig, psf, mode='same')/np.sum(psf)
    filtered *= amplitude
    final_func = interp1d(x1,filtered, kind='linear')
    final_eval = final_func(x)
    return(final_eval)

xx = np.arange(0,352)

fitter1 = fitting.LevMarLSQFitter()
model_init = modulated_line(amplitude=2000, x_0 = 175, span = 188)
fitted_line = fitter1(model_init,xx,rrow130, maxiter=1000)
print(fitted_line)
plt.plot(xx, fitted_line(xx))

#BE WARNED: THIS CODE HAS SOME ISSUES
