import numpy as np
# 3D Robo frame (mm)
Robo1 = [271.56,0.05,189.75]
Robo2 = [145.73,-125.99,437.63] #210.1615
Robo3 = [397.66,282.08,187.52]
Robo4 = [524.74,153.28,-33.01]
Robo5 = [537.16,-127.98,264.69]
Robo6 = [240.20,128.40,470.06]
Robo7 = [320.84,-160.40,423.57]
Robo8 = [542.04,-95.88,183.95]
Robo9 = [410.86,72.29,-42.20]


# 3D Camera frame (px: (x,y,z))
Cam1 = [332,271,1968] # green block
Cam2 = [259,137,2599] # red block
Cam3 = [471,283,1498] # blue block
Cam4 = [407,393,1716]
Cam5 = [270,276,1291]
Cam6 = [405,126,2577]
Cam7 = [252,166,2609]
Cam8 = [296,312,1421]
Cam9 = [373,366,1720]


A_list = []
bx_list = []
by_list = []
bz_list = []


for i in np.arange(1,10):
    robo_point = eval('Robo' + str(i))
    A_list.append(robo_point)

    cam_point = eval('Cam' + str(i))
    bx_list.append(cam_point[0])
    by_list.append(cam_point[1])
    bz_list.append(cam_point[2])

# Transform list to numpy array for further processing
A = np.asarray(A_list)
bx = np.asarray(bx_list)
by = np.asarray(by_list)
bz = np.asarray(bz_list)

# A = np.array([[X1, Y1, Z1], [X2, Y2, Z2], [X3, Y3, Z3]])
#A = np.array([Robo1,Robo2,Robo3,Robo4,Robo5, Robo6, Robo7,Robo8, Robo9])
#A = np.array([Robo1,Robo2,Robo3])

#bx = np.array([x1, x2, x3])
#bx = np.array([Cam1[0], Cam2[0], Cam3[0],Cam4[0],Cam5[0], Cam6[0], Cam7[0], Cam8[0],Cam9[0]])
#bx = np.array([Cam1[0], Cam2[0], Cam3[0]])
#xi = np.linalg.solve(A, bx)
xi = np.linalg.lstsq(A, bx, rcond=None)[0]
#print(xi)

# check if solution is correct
#print("Result: " + str(np.allclose(np.dot(A, xi), bx)))

#for d e f does not work for variables, we have to use it with our measured values as in the example above
# by = np.array([y1, y2, y3])
#by = np.array([Cam1[1], Cam2[1], Cam3[1]])
#by = np.array([Cam1[1], Cam2[1], Cam3[1],Cam4[1],Cam5[1], Cam6[1], Cam7[1], Cam8[1],Cam9[1]])
#xii = np.linalg.solve(A, by)
xii = np.linalg.lstsq(A, by, rcond=None)[0]
#print(xii)

# check if solution is correct
#print("Result: " + str(np.allclose(np.dot(A, xii), by)))

#for g h i does not work for variables, we have to use it with our measured values as in the example above
# bz = np.array([z1, z2, z3])
#bz = np.array([Cam1[2], Cam2[2], Cam3[2]])
#bz = np.array([Cam1[2], Cam2[2], Cam3[2],Cam4[2],Cam5[2], Cam6[2], Cam7[2], Cam8[2],Cam9[2]])
#xiii = np.linalg.solve(A, bz)
xiii = np.linalg.lstsq(A, bz, rcond=None)[0]
#print(xiii)

# check if solution is correct
#print("Result: " + str(np.allclose(np.dot(A, xiii), bz)))

TrafoMatrix = np.array([xi, xii, xiii])
print("Camera Matrix:")
print(TrafoMatrix)
print()
print("Inverse Camera Matrix:")
invTrafoMatrix = np.linalg.inv(TrafoMatrix)
print(invTrafoMatrix)