#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   plot_linearity_fbg_transimpedance.py
@Time    :   2023/09/26 11:22:35
@Author  :   Roney D. Silva
@Contact :   roneyddasilva@gmail.com
'''

import h5py
import numpy as np
import sympy as sp
import locale
import pandas as pd
import matplotlib.pyplot as plt
import lvm_read
from modeling.mathModelAccel import AccelModel
seismic_mass = AccelModel().seismic_mass


locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
# plt.style.use("default")
plt.style.use("common_functions/roney3.mplstyle")
my_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
FIG_L = 6.29
FIG_A = (90.0) / 25.4

f1 = pd.read_csv("labview_files/daq_dyn/data_collected/histerese.lvm",
                 sep='\t', names=['time', 'fbg', 'tap', 'dyn'])

f2 = pd.read_csv("labview_files/daq_dyn/data_collected/first_data_collected.lvm",
                 sep='\t', names=['time', 'fbg', 'tap', 'dyn'])

f3 = pd.read_csv("labview_files/daq_dyn/data_collected/saturation_test.lvm",
                 sep='\t', names=['time', 'fbg', 'tap', 'dyn'])

f4 = pd.read_csv("labview_files/daq_dyn/data_collected/linear_test.lvm",
                 sep='\t', names=['time', 'fbg', 'tap', 'dyn'])
fig.clear()


fig, ax = plt.subplots(1, 1, num=1, sharex=True, figsize=(FIG_L, FIG_A))
ax.plot(4.0*(-f['dyn']-0.5)/(seismic_mass*9.8), f['fbg'], ':')
ax.set_ylabel(r'$v^\text{tr}[\si{\volt}]$')
ax.set_xlabel('Aceleração[g]')
plt.show()


# f = h5py.File('test.hdf5', 'r')
# ff = f.require_group('transimpedance_analysis')
# ff.attrs['info'] = 'Test of relation between transimpendance tension and mechanical traction. '
# ff.attrs['size of fiber on test [m]'] = 0.036
# names = ['time', 'fbg', 'tap', 'dyn']
# for i in ['linear_test', 'histerese', 'first_data_collected', 'saturation_test']:
#     fff = ff.require_group(i)
#     f_pd = pd.read_csv("labview_files/daq_dyn/data_collected/"+i+".lvm",
#                     sep='\t', names=names)
#     for j in names:
#         fff[j] = f_pd[j]
# f.close()


f_test = h5py.File('test.hdf5', 'r')
f = h5py.File('./../data/phd_data.hdf5')
f.copy
