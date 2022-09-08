from pyMilk.interfacing.shm import SHM
import numpy as np
import matplotlib.pyplot as plt; plt.ion()
import time

alicia = SHM('alicia')

rdata = []
for i in range(1000):
    a = alicia.get_data()
    rdata.append(a)
    time.sleep(0.01)
newdata = np.zeros((768, 1024))

ave = 0.0 * rdata[0]
for x in range(1000):
    ave += rdata[x]
ave = ave/1000
newdata = ave
z = newdata


plt.matshow(newdata)

from astropy.modeling import models, fitting
from astropy.utils.exceptions import AstropyUserWarning

y, x = np.mgrid[:256, :256]
p_init = models.AiryDisk2D(amplitude=13000, x_0=127, y_0=127, radius=)
fit_p = fitting.LevMarLSQFitter()
p = fit_p(p_init, x, y, z)
y, x = np.mgrid[:256, :256]
