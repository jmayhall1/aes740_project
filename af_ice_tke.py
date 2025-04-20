# coding=utf-8
"""
Last Edited: 04/09/2025
@author: John Mark Mayhall
"""
import os
from pathlib import Path

import matplotlib.pyplot as plt
import metpy.calc as mpcalc
import netCDF4
import numpy as np
import pandas as pd
from mayavi import mlab
from metpy.units import units

# Define paths
data_path = Path("input_sounding_ice")
nc_file = Path("C:/Users/jmayhall/Downloads/aes740_project/tke/cm1out_icehurr.nc")
output_dir = Path("C:/Users/jmayhall/Downloads/aes740_project/tke/ice_photos/af")
output_dir.mkdir(parents=True, exist_ok=True)  # Ensure output directory exists

# Read sounding data
data = pd.read_csv(data_path, skiprows=[0], header=None, sep=r"\s+")
surface = pd.read_csv(data_path, skiprows=np.arange(1, len(data) + 1, 1), header=None, sep=r"\s+")

# Set column names
data.columns = ["Height", "Potential Temp", "qv", "u", "v"]
surface.columns = ["Pressure", "Potential Temp", "qv"]

# Surface pressure and temperature calculations
p_surface = surface.Pressure.values[0] * units.hectopascals
t_surface = mpcalc.temperature_from_potential_temperature(p_surface, surface["Potential Temp"].values[0] *
                                                          units.kelvin).to(units.celsius)
td_surface = mpcalc.dewpoint_from_specific_humidity(p_surface, surface.qv.values[0] * units("g/kg"))

# Open NetCDF dataset
with netCDF4.Dataset(nc_file) as nc:
    qc, qr, qi = (np.asarray(nc.variables[var]) for var in ["qc", "qr", "qi"])
    x, y, z = (np.asarray(nc.variables[var]) for var in ["xh", "yh", "zh"])
    ql = qc + qr + qi
    model_z = np.asarray(nc.variables["zh"])
    tke = np.asarray(nc.variables["tke"])  # TKE is used in all plots

# Compute pressure levels and parcel profile
model_p = mpcalc.height_to_pressure_std(model_z * units.kilometers)
prof = mpcalc.parcel_profile(model_p, t_surface, td_surface).to("degC")

# Compute the mixing ratio and adiabatic fraction
parcel_mixing_ratio = mpcalc.saturation_mixing_ratio(model_p, (prof.magnitude + 273.15) * units.kelvin)
qla = surface.qv.values[0] / 1000 - parcel_mixing_ratio.magnitude
qla[qla < 0] = 0

# Loop through time steps and generate plots
for i in range(ql.shape[0]):
    current_data = np.divide(ql[i, :, :, :].swapaxes(0, 2), qla, where=qla != 0)  # Avoid division by zero

    fig = mlab.figure(size=(1500, 1000))
    tke_data = tke[i, :, :, :].swapaxes(0, 2)

    s = mlab.contour3d(tke_data, contours=10, colormap="Greys",
                       extent=[np.min(x), np.max(x), np.min(y), np.max(y), 0, 25])
    v = mlab.contour3d(current_data, contours=100, colormap="jet", opacity=0.5, vmax=100,
                       extent=[np.min(x), np.max(x), np.min(y), np.max(y), 0, 25])

    ax = mlab.axes()
    ax.axes.font_factor = 1
    mlab.axes(xlabel="x (km)", ylabel="y (km)", zlabel="z (km)")
    mlab.outline(v)
    mlab.colorbar(object=v, label_fmt='%.4f', nb_labels=3)
    mlab.title(f'Adiabatic Fraction (%)', size=0.5)

    mlab.savefig(f"C:/Users/jmayhall/Downloads/aes740_project/tke/ice_photos/af/af_{i}.png")

    # Cleanup
    mlab.close(all=True)
    mlab.clf()
