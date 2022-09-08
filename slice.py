import numpy as np
import matplotlib.pyplot as plt; plt.ion()
from scipy.ndimage.interpolation import rotate
from astropy.modeling import models, fitting
import math

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
angle = (np.arctan2(slope)*180.0/math.pi)

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
