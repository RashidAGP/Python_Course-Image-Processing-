import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('../images/1.jpeg').convert('L')

kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

img_x = np.abs(np.convolve(img, kernel_x, mode='same'))
img_y = np.abs(np.convolve(img, kernel_y, mode='same'))
edge = img_x + img_y


plt.imshow(edge, cmap='gray')
plt.show()


