#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   plot_linearity_fbg_transimpedance.py
@Time    :   2023/09/26 11:22:35
@Author  :   Roney D. Silva
@Contact :   roneyddasilva@gmail.com
'''

import numpy as np
import sympy as sp
import locale
import pandas as pd
import matplotlib.pyplot as plt
import lvm_read
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
# plt.style.use("default")
plt.style.use("common_functions/roney3.mplstyle")
my_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
FIG_L = 6.29
FIG_A = (90.0) / 25.4

f = pd.read_csv("labview_files/daq_dyn/data_collected/histerese.lvm", sep='\t', names=['time', 'fbg','tap','dyn'])

plt.plot(f['time'],f['dyn'])
plt.plot(f['time'], f['fbg'])
plt.figure(2)
plt.plot(f['dyn'],f['fbg'])
plt.xlabel('Dyn')
plt.ylabel('FBG')
