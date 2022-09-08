import matplotlib.pyplot as plt
import math

fig = plt.figure()
plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)

sine0 = [[0.968, 0.996, 0.996, 0.996, 0.997],
         [1.16, 1.17, 1.19, 1.19, 1.19],
         [1.35, 1.37, 1.40, 1.40, 1.37],
         [1.57, 1.58, 1.59, 1.59, 1.58],
         [1.77, 1.78, 1.81, 1.78, 1.79],
         [1.97, 1.99, 1.98, 1.98, 1.98]]
sine1 = [[0.969, 0.992, 0.994, 0.992, 0.995],
         [1.16, 1.17, 1.19, 1.19, 1.19],
         [1.36, 1.36, 1.39, 1.39, 1.37],
         [1.58, 1.57, 1.60, 1.60, 1.57],
         [1.78, 1.78, 1.79, 1.78, 1.78],
         [1.97, 1.97, 1.97, 1.98, 1.97]]
sine2 =[[0.980, 1.00, 1.00, 1.00, 1.00, 1.00],
        [1.19, 1.19, 1.20, 1.20, 1.20],
        [1.38, 1.38, 1.41, 1.41, 1.38],
        [1.58, 1.59, 1.61, 1.61, 1.59],
        [1.79, 1.80, 1.82, 1.80, 1.80],
        [2.00, 2.00, 2.00, 2.00, 2.00]]

x = [536.9, 812.1, 1113.6, 1771.0, 2512.6]
source0 = [[3.92, 3.91, 3.88, 3.87, 3.71],
           [4.75, 4.74, 4.72, 4.64, 4.48],
           [5.55, 5.53, 5.50, 5.44, 5.24],
           [6.40, 6.36, 6.30, 6.23, 6.00],
           [7.26, 7.23, 7.18, 6.95, 6.73],
           [8.06, 8.03, 7.99, 7.73, 7.53]]

serr0 = [[0.0325, 0.0471, 0.0642, 0.0284, 0.03],
         [0.0222, 0.0343, 0.0289, 0.0333, 0.0232],
         [0.021, 0.0362, 0.041, 0.0408, 0.0247],
         [0.0234, 0.0446, 0.0481, 0.0211, 0.0389],
         [0.0275, 0.043, 0.033, 0.0256, 0.0415],
         [0.0423, 0.0371, 0.0482, 0.0517, 0.029]]


'''for j in range(len(source0)):
    plt1.errorbar(x, source0[j], serr0[j], label='Amplitude0.' + str(j+5), marker='.')
'''
gain = []
yerr = []
for j in range(6):
    one = []
    two = []
    y = source0[j]
    s = sine0[j]
    err = serr0[j]
    for i in range(5):
        a = y[i]/(s[i])
        errone = err[i]/(s[i])
        #b = math.log(a, 10)
        one.append(a)
        two.append(errone)
    gain.append(one)
    yerr.append(two)


for j in range(len(gain)):
    plt1.errorbar(x, gain[j], yerr=yerr[j], label='Amplitude 0.' + str(j+5), marker='.')

plt1.set_title('Frequency Response Source 0')
plt1.legend()
plt1.set_xlabel('Frequency (Hz)')
plt1.set_ylabel('Voltage ratio (Vout/Vin)')

source2 = [[33.8, 14.4, 7.54, 2.91, 1.41],
           [40.6, 17.0, 9.14, 3.29, 1.70],
           [43.4, 19.9, 10.5, 4.08, 1.97],
           [44.0, 22.9, 12.1, 4.71, 2.27],
           [44.0, 25.6, 13.6, 5.18, 2.53],
           [44.0, 28.4, 15.2, 5.77, 2.82]]
# 0.307
serr2 = [[0.307, 0.0641, 0.0528, 0.0177, 0.00515],
         [0.115, 0.154, 0.0318, 0.021, 0.0771],
         [0.253, 0.118, 0.0548, 0.0303, 0.0169],
         [0.112, 0.155, 0.0581, 0.0365, 0.0154],
         [0.181, 0.188, 0.0528, 0.0505, 0.0146],
         [0.195, 0.169, 0.0672, 0.0605, 0.0151]]

gain2 = []
yerr2 = []
for j in range(6):
    one = []
    two = []
    y = source2[j]
    s = sine2[j]
    err = serr2[j]
    for i in range(5):
        a = y[i]/(s[i])
        one.append(a)
        errone = err[i] / (s[i])
        two.append(errone)
    gain2.append(one)
    yerr2.append(two)

for j in range(len(gain2)):
    plt2.errorbar(x, gain2[j], yerr2[j], label='Amplitude 0.' + str(j+5), marker='.')
plt2.set_title('Frequency Response Source 2')
plt2.legend()
plt2.set_xlabel('Frequency (Hz)')
plt2.set_ylabel('Voltage Ratio (Vout/Vin)')

source1 = [[3.46, 3.44, 3.39, 3.30, 3.16],
           [4.15, 4.01, 3.95, 3.97, 3.77],
           [4.87, 4.72, 4.70, 4.64, 4.50],
           [5.50, 5.34, 5.28, 5.26, 5.14],
           [6.20, 6.10, 6.00, 5.85, 5.73],
           [6.91, 6.87, 6.72, 6.55, 6.36]]

serr1 = [[0.0118, 0.0193, 0.0158, 0.0257, 0.0155],
         [0.0119, 0.0625, 0.0631, 0.0157, 0.0369],
         [0.0178, 0.0244, 0.0382, 0.0327, 0.026],
         [0.0282, 0.0735, 0.0586, 0.0206, 0.0373],
         [0.0235, 0.0567, 0.0601, 0.0511, 0.0141],
         [0.0257, 0.0295, 0.0556, 0.0425, 0.0405]]

gain3 = []
yerr3 = []
for j in range(6):
    one = []
    two = []
    y = source1[j]
    s = sine1[j]
    err = serr1[j]
    for i in range(5):
        a = y[i]/(s[i])
        one.append(a)
        errone = err[i]/(s[i])
        two.append(errone)
    gain3.append(one)
    yerr3.append(two)
for j in range(len(gain3)):
    plt3.errorbar(x, gain3[j], yerr3[j], label='Amplitude 0.' + str(j+5), marker='.')
plt3.set_title('Frequency Response Source 1')
plt3.legend()
plt3.set_xlabel('Frequency (Hz)')
plt3.set_ylabel('Voltage Ratio (Vout/Vin)')

fig2 = plt.figure()
plt4 = fig2.add_subplot(221)
plt5 = fig2.add_subplot(222)
plt6 = fig2.add_subplot(223)
plt7 = fig2.add_subplot(224)



phase0 = [5.117, 7.898, 11.56, 18.10, 25.05]
perr0 = [1.153, 0.8411, 0.8456, 1.196, 0.9878]
plt4.errorbar(x, phase0, perr0, label='Phase 0', marker='.')

phase1 = [4.842, 8.039, 11.53, 19.21, 26.84]
perr1 = [1.356, 0.9513, 1.111, 1.299, 1.448]
plt5.errorbar(x, phase1, perr1, label='Phase 1', marker='.')


phase2 = [149.9, 164.6, 175.5, 187.9, 197.6]
perr2 = [0.7022, 0.9552, 0.6624, 0.6297, 0.9201]
plt6.errorbar(x, phase2, perr2, label='Phase 2', marker='.')

plt4.set_title('Phase Differences, Source 0')
plt4.legend()
plt4.set_xlabel('Frequency (Hz)')
plt4.set_ylabel('Phase (°)')

plt5.set_title('Phase Differences, Source 1')
plt5.legend()
plt5.set_xlabel('Frequency (Hz)')
plt5.set_ylabel('Phase (°)')

plt6.set_title('Phase Differences, Source 2')
plt6.legend()
plt6.set_xlabel('Frequency (Hz)')
plt6.set_ylabel('Phase (°)')


plt7.errorbar(x, phase0, perr0, label='Phase=0', marker='.')
phase90 = [5.051, 8.133, 11.54, 18.24, 26.13]
perr90 = [0.9986, 0.9638, 1.008, 0.9772, 1.044]
plt7.errorbar(x, phase90, perr90, label='Phase=90', marker='.')
phase180 = [5.261, 8.380, 11.57, 17.98, 26.06]
perr180 = [1.091, 0.8572, 1.005, 1.204, 1.054]
plt7.errorbar(x, phase180, perr180, label='Phase=180', marker='.')
phase270 = [5.255, 9.104, 11.44, 17.98, 26.06]
perr270 = [1.019, 0.8025, 0.8814, 1.151, 1.106]
plt7.errorbar(x, phase270, perr270, label='Phase=270', marker='.')



plt7.set_title('Source 0 w/ variable phase values')
plt7.legend()
plt7.set_xlabel('Frequency (Hz)')
plt7.set_ylabel('Phase °')

plt.show()
