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
    qv_data = data_qv[i, :, :, :]
    qv_data = qv_data.swapaxes(0, 2)

    # dbz_data = data_dbz[i, :, :, :]
    # dbz_data = dbz_data.swapaxes(0, 2)

    ql_data = data_ql[i, :, :, :]
    ql_data = ql_data.swapaxes(0, 2)

    th_data = data_th[i, :, :, :]
    th_data = th_data.swapaxes(0, 2)

    rho_data = data_rho[i, :, :, :]
    rho_data = rho_data.swapaxes(0, 2)

    tke_data = data_tke[i, :, :, :]
    tke_data = tke_data.swapaxes(0, 2)

    fig = mlab.figure(size=(1024, 1024))
    s = mlab.contour3d(tke_data, contours=10, colormap='Greys')
    v = mlab.contour3d(qv_data, contours=25, colormap='jet', opacity=0.5)
    mlab.axes(xlabel='x', ylabel='y', zlabel='z')
    mlab.outline(s)
    mlab.savefig(f'C:/Users/jmayhall/Downloads/aes740_project/ice_photos/qv/qv_tke_timestep{i}.png')
    mlab.close(all=True)
    mlab.clf()

    # fig = mlab.figure(size=(1024, 1024))
    # s = mlab.contour3d(tke_data, contours=10, colormap='Greys')
    # v = mlab.contour3d(dbz_data, contours=25, colormap='jet', opacity=0.5)
    # mlab.axes(xlabel='x', ylabel='y', zlabel='z')
    # mlab.outline(s)
    # mlab.savefig(f'C:/Users/jmayhall/Downloads/aes740_project/ice_photos/dbz/dbz_tke_timestep{i}.png')
    # mlab.close(all=True)
    # mlab.clf()

    fig = mlab.figure(size=(1024, 1024))
    s = mlab.contour3d(tke_data, contours=10, colormap='Greys')
    v = mlab.contour3d(ql_data, contours=25, colormap='jet', opacity=0.5)
    mlab.axes(xlabel='x', ylabel='y', zlabel='z')
    mlab.outline(s)
    mlab.savefig(f'C:/Users/jmayhall/Downloads/aes740_project/ice_photos/ql/ql_tke_timestep{i}.png')
    mlab.close(all=True)
    mlab.clf()

    fig = mlab.figure(size=(1024, 1024))
    s = mlab.contour3d(tke_data, contours=10, colormap='Greys')
    v = mlab.contour3d(th_data, contours=25, colormap='jet', opacity=0.5)
    mlab.axes(xlabel='x', ylabel='y', zlabel='z')
    mlab.outline(s)
    mlab.savefig(f'C:/Users/jmayhall/Downloads/aes740_project/ice_photos/th/th_tke_timestep{i}.png')
    mlab.close(all=True)
    mlab.clf()

    fig = mlab.figure(size=(1024, 1024))
    s = mlab.contour3d(tke_data, contours=10, colormap='Greys')
    v = mlab.contour3d(rho_data, contours=25, colormap='jet', opacity=0.5)
    mlab.axes(xlabel='x', ylabel='y', zlabel='z')
    mlab.outline(s)
    mlab.savefig(f'C:/Users/jmayhall/Downloads/aes740_project/ice_photos/rho/rho_tke_timestep{i}.png')
    mlab.close(all=True)
    mlab.clf()
