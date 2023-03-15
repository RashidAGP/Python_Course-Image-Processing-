# Python_Course-Image-Processing
## Edge Detection of Pictures (Abstract)
In this project, several libraries are used to implement edge detection of images. Furthermore, The performance of different implmentation will be compared. And Finally it will be optimized the bottleneck of the programs.
## Problem Definition
Because of nature of python programming language, which is script based, it is relatively bad in terms of performance and execution time in comparison to compiler based programming language such as c/c++. For this reason, in HPC, c/c++ is more favourable. On the otherhand, Time to production of c/c++ in bad. That is why sometime python is more ecceptable, in spite of bad runtime delay. In this project I will discussed about the pros and cons of pyhton prgoramming language in high performance computing.
# Implementation
This project was implmented in three ways. Maybe I will extend it to another ways as well.

# RAW Implmentation.

In this implementation, edge detection was implmented without any package.

# NUMPY Implementation

In this method, numpy was used for edge detection.

# Implmenting with CUDA

CUDA was used for edge detection. This technique must have better performance than previous. This approach is highly dependent on the dimension and size of grid and block of the kernel. But for simplicity, I coinsider the block size (16,16,1). But according to dimension and size, the performance can be changed dramatically. Furthermore, it depends on speed of  PCI-e and datamovement between CPU and GPU, which I ingonred it for now. 

# Results

The results of this project were illustrated here.

## Performance (a.k.a Execution Time)
The exection Time of each technique has been illustratd in the following table. It should be noted that the time units is second.
|      RAW      |     NUMPY     |     CUDA    |
| ------------- | ------------- | ------------
|     77.08     |      0.81     |      ?      |


## Quality of images
Original images are inside images directory. One of the example is shown in the below.

![]()<img src="/images/1.jpg"  width="240">

The results are shown in following pictures.

![]()<img src="/out/1_RAW.png"  width="240">

![]()<img src="/out/1_np.png"  width="240">
