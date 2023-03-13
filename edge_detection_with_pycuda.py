import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
from pycuda.compiler import SourceModule

img = np.load("../images/1.jpeg")

sobel_kernel = """
__global__ void sobel_filter(float *img, float *out, int width, int height) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < 1 || x >= width - 1 || y < 1 || y >= height - 1) {
        out[y * width + x] = 0.0f;
        return;
    }

    float gx = img[(y-1) * width + (x-1)] - img[(y+1) * width + (x-1)] + 2 * img[(y-1) * width + x] - 2 * img[(y+1) * width + x] + img[(y-1) * width + (x+1)] - img[(y+1) * width + (x+1)];

    float gy = img[(y-1) * width + (x-1)] + 2 * img[y * width + (x-1)] + img[(y+1) * width + (x-1)] - img[(y-1) * width + (x+1)] - 2 * img[y * width + (x+1)] - img[(y+1) * width + (x+1)];

    out[y * width + x] = sqrt(gx * gx + gy * gy);
}
"""

mod = SourceModule(sobel_kernel)
sobel_filter = mod.get_function("sobel_filter")

out = np.zeros_like(img)

block_size = (16, 16, 1)
grid_size = ((img.shape[0] + block_size[0] - 1) // block_size[0], (img.shape[1] + block_size[1] - 1) // block_size[1], 1)
sobel_filter(cuda.In(img), cuda.Out(out), np.int32(img.shape[1]), np.int32(img.shape[0]), block=block_size, grid=grid_size)

np.save("image_with_pycuda.npy", out)

