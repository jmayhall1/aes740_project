# coding=utf-8
"""
@author: John Mark Mayhall
"""
import glob
import os

import matplotlib.pyplot as plt
import netCDF4
import numpy as np
import pandas as pd
from mayavi import mlab

path = 'C:/Users/jmayhall/Downloads/aes740_project/cm1out_liqhurr.nc'

data_qv = np.array(netCDF4.Dataset(path).variables.get('qv'))
data_ql = np.array(netCDF4.Dataset(path).variables.get('ql'))
data_th = np.array(netCDF4.Dataset(path).variables.get('th'))
data_rho = np.array(netCDF4.Dataset(path).variables.get('rho'))
data_tke = np.array(netCDF4.Dataset(path).variables.get('tke'))

for i in range(data_qv.shape[0]):
    if i < 12: continue
    qv_data = data_qv[i, :, :, :]
    qv_data = qv_data.swapaxes(0, 2)
    # s = mlab.volume_slice(qv_data)
    # mlab.show()
    #
    # s = mlab.contour3d(qv_data, contours=10)
    # mlab.show()
    #
    ql_data = data_ql[i, :, :, :]
    ql_data = ql_data.swapaxes(0, 2)
    # s = mlab.volume_slice(ql_data)
    # mlab.show()
    #
    # s = mlab.contour3d(ql_data, contours=10)
    # mlab.show()
    #
    th_data = data_th[i, :, :, :]
    th_data = th_data.swapaxes(0, 2)
    # s = mlab.volume_slice(th_data)
    # mlab.show()
    #
    # s = mlab.contour3d(th_data, contours=10)
    # mlab.show()
    #
    rho_data = data_rho[i, :, :, :]
    rho_data = rho_data.swapaxes(0, 2)
    # s = mlab.volume_slice(rho_data)
    # mlab.show()
    #
    # s = mlab.contour3d(rho_data, contours=10)
    # mlab.show()
    #
    tke_data = data_tke[i, :, :, :]
    tke_data = tke_data.swapaxes(0, 2)
    # s = mlab.volume_slice(tke_data)
    # mlab.show()

    s = mlab.contour3d(tke_data, contours=10, colormap='Greys')
    v = mlab.contour3d(qv_data, contours=25, colormap='jet', opacity=0.5)
    mlab.show()

exit()



# data = np.array(netCDF4.Dataset('C:/Users/jmayhall/Downloads/aes740_hw3/cm1out.nc').variables.get('dbz'))[:, :, 0, :]
# z = np.array(netCDF4.Dataset('C:/Users/jmayhall/Downloads/aes740_hw3/cm1out.nc').variables.get('zh'))
# x = np.array(netCDF4.Dataset('C:/Users/jmayhall/Downloads/aes740_hw3/cm1out.nc').variables.get('xh'))
# for i in range(data.shape[0]):
#     current_data = data[i, :, :]
#     plt.imshow(current_data, vmin=-50, vmax=50, aspect='auto', cmap='gist_ncar',
#                extent=(np.min(x), np.max(x), np.max(z), np.min(z)))
#     plt.gca().invert_yaxis()
#     plt.ylabel('Height (km)')
#     plt.xlabel('Distance (km)')
#     plt.title(f'Simulated Reflectivity (dBZ) at {2 * i} Minutes')
#     plt.colorbar(label='dBZ')
#     plt.savefig(f'C:/Users/jmayhall/Downloads/aes740_hw3/reflectivity/dbz_time{i}.png')
#     plt.close('all')
#
# data = np.array(netCDF4.Dataset('C:/Users/jmayhall/Downloads/aes740_hw3/cm1out.nc').variables.get('tke'))[:, :, 0, :]
# for i in range(data.shape[0]):
#     current_data = data[i, :, :]
#     plt.imshow(current_data, vmin=0, vmax=0.5, aspect='auto', cmap='terrain_r',
#                extent=(np.min(x), np.max(x), np.max(z), np.min(z)))
#     plt.gca().invert_yaxis()
#     plt.ylabel('Height (km)')
#     plt.xlabel('Distance (km)')
#     plt.title(f'TKE at {2 * i} Minutes')
#     plt.colorbar(label=r'TKE ($\frac{m^2}{s^2}$)')
#     plt.savefig(f'C:/Users/jmayhall/Downloads/aes740_hw3/tke/tke_time{i}.png')
#     plt.close('all')
#
# data = np.array(netCDF4.Dataset('C:/Users/jmayhall/Downloads/aes740_hw3/cm1out.nc').variables.get('w'))[:, :, 0, :]
# for i in range(data.shape[0]):
#     current_data = data[i, :, :]
#     plt.imshow(current_data, vmin=-1, vmax=1, aspect='auto', cmap='rainbow',
#                extent=(np.min(x), np.max(x), np.max(z), np.min(z)))
#     plt.gca().invert_yaxis()
#     plt.ylabel('Height (km)')
#     plt.xlabel('Distance (km)')
#     plt.title(f'Vertical Velocity (w) at {2 * i} Minutes')
#     plt.colorbar(label=r'w ($\frac{m}{s}$)')
#     plt.savefig(f'C:/Users/jmayhall/Downloads/aes740_hw3/w/w_time{i}.png')
#     plt.close('all')
