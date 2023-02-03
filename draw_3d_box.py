import numpy as np


# Access the data as a numpy array
#vertex_array = np.array(mesh.vertices)


def ply_vtx(pth):
    f = open(pth)
    assert f.readline().strip() == "ply"
    f.readline()
    f.readline()
    N = int(f.readline().split()[-1])
    while f.readline().strip() != "end_header":
        continue
    pts = []
    for _ in range(N):
        pts.append(np.float32(f.readline().split()[:3]))
    return np.array(pts)

import random
pointxyz = ply_vtx('obj_04.ply') / 1000.0
dellist = [j for j in range(0, len(pointxyz))]
dellist = random.sample(dellist, len(pointxyz) - 2000)
pointxyz = np.delete(pointxyz, dellist, axis=0)

R = np.array(
    [
         [0.9611407391977216, 0.02764368482776658, -0.27467126923578206],
         [0.19390287739569104, -0.7758104690879676, 0.600433002250191],
         [-0.19649466555640432, -0.6303601690642027, -0.7510232377664643]
    ]
)
# Define the translation vector
#t = np.array([[-105.35775150], [-117.52119142], [1014.87701320]])
t = np.array([[0.05040458794907015], [0.0016392607731894882], [0.4787009536928209]])
# Form the 4x4 transformation matrix
transformation = np.hstack((R, t))
transformation = np.vstack((transformation, np.array([0, 0, 0, 1])))

import numpy as np


# Remove the last row
transformation = transformation[0:3, :]

K = np.array(
    [
        [411.9532675638686, 0.0, 323.57535317408457],
        [0.0, 396.0686482174296, 243.6098441558203],
        [0.0, 0.0, 1.0]
    ]
)
def project_p3d(p3d, cam_scale, K):
    p3d = p3d * cam_scale
    p2d = np.dot(p3d, K.T)
    p2d_3 = p2d[:, 2]
    p2d_3[np.where(p2d_3 < 1e-8)] = 1.0
    p2d[:, 2] = p2d_3
    p2d = np.around((p2d[:, :2] / p2d[:, 2:])).astype(np.int32)
    return p2d

mesh_p2ds = project_p3d(mesh_pts, 1.0, K)

img = cv2.imread("1_000000.png", cv2.IMREAD_ANYDEPTH)
h, w = img.shape[0], img.shape[1]

color=[(255, 0, 255)]
for pt_2d, c in zip(mesh_p2ds, color):
    pt_2d[0] = np.clip(pt_2d[0], 0, w)
    pt_2d[1] = np.clip(pt_2d[1], 0, h)
    img = cv2.circle(
        img, (pt_2d[0], pt_2d[1]), 1, c, -1
    )

cv2_imshow(img)

