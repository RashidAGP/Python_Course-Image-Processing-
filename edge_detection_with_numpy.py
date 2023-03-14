import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d


img = Image.open('./images/2.jpg').convert('L')
#img_array = np.array(img)

#img_array = img.size
kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

img_x = np.abs(convolve2d(img, kernel_x, mode='same'))
img_y = np.abs(convolve2d(img, kernel_y, mode='same'))
edge = img_x + img_y


plt.imshow(edge, cmap='gray')
plt.show()


