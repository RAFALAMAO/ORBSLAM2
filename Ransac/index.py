import pyransac3d as pyrsc
import numpy as np

# points = load_points(.) # Load your point cloud as a numpy array (N, 3)
points = np.loadtxt('CuboRubik.xyz')
# print(points.shape)

pnt = pyrsc.Point()
center, inliers = pnt.fit(points, thresh=0.2, maxIteration=10000)
print(center, inliers)