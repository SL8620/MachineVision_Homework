import cv2
import numpy as np
from math import *

# 读取图像
img_raw = cv2.imread("meme2.jpg")
cv2.imshow("img_raw", img_raw)

# 缩小
img_resize = cv2.resize(img_raw, dsize=None, fy=0.5, fx=0.5)
cv2.imshow("img_resize", img_resize)  # 显示灰度图

# 旋转
M_rotate = cv2.getRotationMatrix2D((0, 0), 45, 1)   # 旋转矩阵
print(M_rotate)
img_rotate = cv2.warpAffine(img_raw, M_rotate, dsize=[img_raw.shape[0], img_raw.shape[1]])
cv2.imshow("img_roate", img_rotate)  # 显示平移结果

# 平移
M_shift = np.float32([[1, 0, 150], [0, 1, 250]])    # 平移矩阵
print(M_shift)
img_shift = cv2.warpAffine(img_raw, M_shift, dsize=[img_raw.shape[0], img_raw.shape[1]])
cv2.imshow("img_shift", img_shift)  # 显示平移结果

cv2.waitKey(0)
