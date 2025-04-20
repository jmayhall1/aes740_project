# coding=utf-8
"""
Last Edited: 04/09/2025
@author: John Mark Mayhall
"""
import os

import imageio
from natsort import natsorted

png_dir = 'C:/Users/jmayhall/Downloads/aes740_project/tke/liq_photos/af'
images = []
for file_name in natsorted(os.listdir(png_dir)):
    file_path = os.path.join(png_dir, file_name)
    images.append(imageio.v2.imread(file_path))
    print(file_name)
    print((imageio.v2.imread(file_path)).shape)

# Make it pause at the end so that the viewers can ponder
for _ in range(10):
    images.append(imageio.v2.imread(file_path))

imageio.mimwrite('af_liq.gif', images, duration=1000)

png_dir = 'C:/Users/jmayhall/Downloads/aes740_project/tke/liq_photos/ql'
images = []
for file_name in natsorted(os.listdir(png_dir)):
    file_path = os.path.join(png_dir, file_name)
    images.append(imageio.v2.imread(file_path))
    print(file_name)
    print((imageio.v2.imread(file_path)).shape)

# Make it pause at the end so that the viewers can ponder
for _ in range(10):
    images.append(imageio.v2.imread(file_path))

imageio.mimsave('ql_liq.gif', images, duration=1000)

png_dir = 'C:/Users/jmayhall/Downloads/aes740_project/tke/liq_photos/qv'
images = []
for file_name in natsorted(os.listdir(png_dir)):
    file_path = os.path.join(png_dir, file_name)
    images.append(imageio.v2.imread(file_path))
    print(file_name)
    print((imageio.v2.imread(file_path)).shape)

# Make it pause at the end so that the viewers can ponder
for _ in range(10):
    images.append(imageio.v2.imread(file_path))

imageio.mimsave('qv_liq.gif', images, duration=1000)

png_dir = 'C:/Users/jmayhall/Downloads/aes740_project/tke/liq_photos/rho'
images = []
for file_name in natsorted(os.listdir(png_dir)):
    file_path = os.path.join(png_dir, file_name)
    images.append(imageio.v2.imread(file_path))
    print(file_name)
    print((imageio.v2.imread(file_path)).shape)

# Make it pause at the end so that the viewers can ponder
for _ in range(10):
    images.append(imageio.v2.imread(file_path))

imageio.mimsave('rho_liq.gif', images, duration=1000)

png_dir = 'C:/Users/jmayhall/Downloads/aes740_project/tke/liq_photos/th'
images = []
for file_name in natsorted(os.listdir(png_dir)):
    file_path = os.path.join(png_dir, file_name)
    images.append(imageio.v2.imread(file_path))
    print(file_name)
    print((imageio.v2.imread(file_path)).shape)

# Make it pause at the end so that the viewers can ponder
for _ in range(10):
    images.append(imageio.v2.imread(file_path))

imageio.mimsave('th_liq.gif', images, duration=1000)