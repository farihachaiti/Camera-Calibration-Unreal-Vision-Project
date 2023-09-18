import numpy as np
import sys


def calculate_World_Points(x, y, scaling_factor, camera_matrix, translation_matrix, rotation_matrix):
    translation_matrix = np.array([translation_matrix], dtype=np.float64).T
    homogeneous_image_points = np.array([[x,y,1]], dtype=np.float64).T
    s_xy = np.float64(scaling_factor)*homogeneous_image_points
    xyz = np.matmul(np.linalg.inv(np.float64(camera_matrix)),s_xy)
    xyz = xyz-np.float64(translation_matrix)
    XYZ = np.matmul(np.linalg.inv(rotation_matrix),xyz)
 
    return XYZ

def get_rotation_matrix(angle_x, angle_y, angle_z):
    Rx = np.zeros(shape=(3, 3))
    Rx[0, 0] = 1
    Rx[1, 1] = np.cos(angle_x)
    Rx[1, 2] = -np.sin(angle_x)
    Rx[2, 1] = np.sin(angle_x)
    Rx[2, 2] = np.cos(angle_x)
    
    Ry = np.zeros(shape=(3, 3))
    Ry[1, 1] = 1
    Ry[0, 0] = np.cos(angle_y)
    Ry[2, 0] = -np.sin(angle_y)
    Ry[0, 2] = np.sin(angle_y)
    Ry[2, 2] = np.cos(angle_y)

    Rz = np.zeros(shape=(3, 3))
    Rz[2, 2] = 1
    Rz[0, 0] = np.cos(angle_z)
    Rz[1, 0] = -np.sin(angle_z)
    Rz[0, 1] = np.sin(angle_z)
    Rz[1, 1] = np.cos(angle_z)

   
    R = np.matmul(Rx,Ry)
    R = np.matmul(R,Rz)
  
    return R


x = sys.argv[1]
y = sys.argv[2]
scaling_factor = sys.argv[3]
fx = sys.argv[4]
fy = sys.argv[5]
cx = sys.argv[6]
cy = sys.argv[7]

camera_matrix = [[fx, 0, cx],
                [0, fy, cy], 
                [0, 0, 1]]
translation_matrix = sys.argv[8].split(',')
translation_matrix = np.array([float(i) for i in translation_matrix]) 

rotation_angles = sys.argv[9].split(',')
rotation_angles = np.array([float(i) for i in rotation_angles])


rotation_matrix = get_rotation_matrix(rotation_angles[0], rotation_angles[1], rotation_angles[2])

print(calculate_World_Points(x, y, scaling_factor, camera_matrix, translation_matrix, rotation_matrix))