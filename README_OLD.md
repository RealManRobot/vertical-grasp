# Example

```python
import cv2
from vertical_grab.interface import vertical_catch


depth_frame = cv2.imread("real_depth_frame.png", cv2.IMREAD_GRAYSCALE) # 测试数据在tests文件夹内
mask = cv2.imread("manual_catch_mask.png", cv2.IMREAD_GRAYSCALE) # 测试数据在tests文件夹内

center = [368, 302]
color_intr = {"ppx": 326.721, "ppy": 252.721, "fx": 606.721, "fy": 607.55}
current_pose = [-0.06532000005245209, 0.004813000094145536, 0.3710620105266571, -3.058000087738037, 0.24199999868869781,
                0.041999999433755875]

arm_gripper_length = 0.02
vertical_rx_ry_rz = [3.14, 0, -0.020999999716877937]

rotation_matrix = [[0.01990299, 0.98175955, -0.18908215], [-0.9996762, 0.02254041, 0.01180814],
                   [0.01585474, 0.18878591, 0.98189027]]
translation_vector = [-0.06860006, 0.04255893, 0.01080163]


ret = vertical_catch(
    center, mask, depth_frame, color_intr, current_pose, arm_gripper_length, vertical_rx_ry_rz, rotation_matrix,
    translation_vector, True
)
```


# Distribute
1. Execute the following commands in the same directory as setup.py: `python setup.py bdist_wheel`.
2. find the `.wheel` in folder `dist`, example: `dist/vertical_grab-0.1.0-py3-none-any.whl`

# Install

`pip install vertical_grab-0.1.0-py3-none-any.whl`


# Unit Test
1. cd into `tests`
2. execute: `pytest`