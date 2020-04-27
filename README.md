# CV-Feature-Detection-Algorithms
Python implementation of popular Feature Detection Algorithms

# About
Feature Detection and Feature Descriptions are two main things involved when we talk about features in a digital image. Its very important to understand and find features to describe and match them later. Feature Detection is looking for the regions in images which have maximum variation when moved in all regions around it. Whereas, Feature Description is  describing the region around the feature so that it can find it in other images. <br>

The Following Algorithms are covered: <br>
1. FAST (Features from Accelerated Segment Test) Algorithm <br>
A pixel is selected whose intensity alongwith 16 neighbours of the selected pixel, the feature vectors are defined in three brackets - Lighter, Darker, Same Intensity. A boolean value is defined for storing if edge found or not. It is iteratively processed using ID3 to process the complete image. It is several times faster than other existing corner detectors. But it is not robust to high levels of noise. It is dependent on a threshold. . Find the complete explanation [here](https://docs.opencv.org/4.2.0/df/d0c/tutorial_py_fast.html).<br>

2. SIFT (Scale-Invariant Feature Transform) Algorithm <br>
What if the image is scaled up? For this, scale-space filtering is used. In it, Laplacian of Gaussian is found for the image with various σ values. LoG acts as a blob detector which detects blobs in various sizes. But this LoG is a little costly, so SIFT algorithm uses Difference of Gaussians which is an approximation of LoG. DoG has higher response for edges, so edges also need to be removed. For this, a concept similar to Harris corner detector is used. They used a 2x2 Hessian matrix (H) to compute the principal curvature. Now an orientation is assigned to each keypoint to achieve invariance to image rotation. A Keypoint descriptor is created. A 16x16 neighbourhood around the keypoint is taken. Find the complete explanation [here](https://docs.opencv.org/4.2.0/da/df5/tutorial_py_sift_intro.html).<br>

3. SURF (Speeded-Up Robust Features) Algorithm <br>
SURF goes a little further and approximates LoG with Box Filter. Below image shows a demonstration of such an approximation. One big advantage of this approximation is that, convolution with box filter can be easily calculated with the help of integral images. And it can be done in parallel for different scales. Also the SURF rely on determinant of Hessian matrix for both scale and location. For orientation assignment, SURF uses wavelet responses in horizontal and vertical direction for a neighbourhood of size 6s. For feature description, SURF uses Wavelet responses in horizontal and vertical direction (again, use of integral images makes things easier). A neighbourhood of size 20sX20s is taken around the keypoint where s is the size. In short, SURF adds a lot of features to improve the speed in every step. Analysis shows it is 3 times faster than SIFT while performance is comparable to SIFT. SURF is good at handling images with blurring and rotation, but not good at handling viewpoint change and illumination change. Find the complete explanation [here](https://docs.opencv.org/4.2.0/df/dd2/tutorial_py_surf_intro.html).<br>

4. ORB (Oriented FAST and Rotated BRIEF) Algorithm <br>
ORB is basically a fusion of FAST keypoint detector and BRIEF descriptor with many modifications to enhance the performance. First it use FAST to find keypoints, then apply Harris corner measure to find top N points among them. It also use pyramid to produce multiscale-features. But one problem is that, FAST doesn't compute the orientation. So what about rotation invariance? Authors came up with following modification. ORB is much faster than SURF and SIFT and ORB descriptor works better than SURF. ORB is a good choice in low-power devices for panorama stitching. Find the complete explanation [here](https://docs.opencv.org/4.2.0/d1/d89/tutorial_py_orb.html).<br>

<br>

# Pre-requisites
Download and install the following module: <br> 
1) opencv - pip install cv2 <br>
2) opencv-contrib - pip install opencv-contrib-python <br>

Note:
1. SIFT and SURF are Patented, not to be used commercially without permission.

# Author
Pranav Raikote
