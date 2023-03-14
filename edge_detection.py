import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img = Image.open('./images/1.jpg').convert('L')

print(img)
# This is just a filter. 
kernel_x = ([[-1,0,1], [-2,0,2], [-1,0,1]])
kernel_y = ([[-1,-2,-1],[0,0,0], [1,2,1]])


def convolve(image, kernel):
    i_w, i_h = image.size

    k_w = len(kernel[0])
    k_h = len(kernel)

    p_h = k_h // 2
    p_w = k_w // 2

    padded_image = np.zeros((i_h + 2*p_h, i_w + 2*p_w))
    padded_image[p_h:i_h+p_h, p_w:i_w+p_w] = image

    output_image = np.zeros((i_h, i_w))

    for i in range(p_h, i_h+p_h):
        for j in range(p_w, i_w+p_w):
            patch = padded_image[i-p_h:i+p_h+1, j-p_w:j+p_w+1]
            output_image[i-p_h, j-p_w] = np.sum(patch * kernel)

    return output_image

def absolute(image):
    output_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            output_image[i, j] = abs(image[i, j])

    return output_image

img_x = absolute(convolve(img, kernel_x))
img_y = absolute(convolve(img, kernel_y))
edge = img_x + img_y

plt.imshow(edge, cmap="gray")
plt.show()
