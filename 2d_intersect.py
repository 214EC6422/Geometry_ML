# -*- coding: utf-8 -*-
"""2D_intersect.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xeRzlFu98lzEXtPv7rMVQFOd_7DyRfm2
"""

#Calculate the intersection point for two lines.
import numpy as np
#Parameters for the first line a1x+b1y=c1
#Parameters for the second line a2x+b2y=c2
def intersect_point(a1,b1,c1,a2,b2,c2):
  # Matrix
  a = np.array([[a1] , [a2]])
  a = np.asmatrix(a)
  b = np.array([[b1],[b2]])
  b = np.asmatrix(b)
  c = np.array([[c1],[c2]]) 
  c = np.asmatrix(c)
  mat_a_b = np.concatenate((a,b), axis=1)
  mat_b_c = np.concatenate((c,b),axis = 1)
  mat_a_c = np.concatenate((a,c),axis=1)
  # Determinants
  det_mat_a_b = np.linalg.det(mat_a_b)
  det_mat_b_c = np.linalg.det(mat_b_c)
  det_mat_a_c = np.linalg.det(mat_a_c)
  #Check for the parallel line.
  check_value = det_mat_a_b
  if check_value == 0.0:
    print("This is a parallel line so no intersection point exists.")
    return None
  else:
    # Cramer's rule
    x_val , y_val = np.divide(det_mat_b_c,det_mat_a_b), np.divide(det_mat_a_c, det_mat_a_b)
    return x_val,y_val
#return check_value
a1 = float(input("a1: "))
b1 = float(input("b1: "))
c1 = float(input("c1: "))
a2 = float(input("a2: "))
b2 = float(input("b2: "))
c2 = float(input("c2: "))
val = intersect_point(a1,b1,c1,a2,b2,c2)
print(val)

