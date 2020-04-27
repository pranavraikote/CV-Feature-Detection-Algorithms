# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:11:41 2020

@author: Pranav
"""
#Import OpenCV Module - Version - 3.4.1
import cv2

#Read/Open the Image
img = cv2.imread('Harry.jpg', 0)
img = cv2.resize(img, (220, 290), cv2.INTER_NEAREST)

#FAST Feature Detector
fast = cv2.FastFeatureDetector_create()
keypoints_fast = fast.detect(img)
fast_img = cv2.drawKeypoints(img, keypoints_fast, None)

#SIFT Feature Detector
sift = cv2.xfeatures2d.SIFT_create()
keypoints_sift = sift.detect(img)
sift_img = cv2.drawKeypoints(img, keypoints_sift, None)

#SUFT Feature Detector
surf = cv2.xfeatures2d.SURF_create()
keypoints_surf = surf.detect(img)
surf_img = cv2.drawKeypoints(img, keypoints_surf, None)

#ORB Feature Detector
orb = cv2.ORB_create(nfeatures = 1000)
keypoints_orb = orb.detect(img)
orb_img = cv2.drawKeypoints(img, keypoints_orb, None)

#Display Windows 
cv2.imshow('Image', img)
cv2.imshow('FAST', fast_img)
cv2.imshow('SIFT', sift_img)
cv2.imshow('SURF', surf_img)
cv2.imshow('ORB', orb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()