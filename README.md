# vertical_grab_SDK

## **1. 项目介绍**

在睿眼中很多模块都涉及到了垂直抓取的操作，每次抓取都需重复计算机械臂最终位资。
使用这个sdk只需输入计算需要的数据，例如中心点，mask, 深度图像等数据，便可直接计算出机械臂执行垂直抓取的最终位姿。

- **API链接**：[API链接地址](http://192.168.0.188:8090/ai_lab_rd02/ai_sdks/vertical_grab)

## **2. 代码结构**

```
vertical_grab/
│
├── README.md        <- 项目的核心文档
├── requirements.txt    <- 项目的依赖列表
├── setup.py        <- 项目的安装脚本
├── .gitignore        <- 忽略文件
│
├── vertical_grab/          <- 项目的源代码
│  ├── catch.py       <- 主要是计算抓取出来的位置代码
│  ├── convert.py       <- 计算抓取位置的过程代码，机械臂位姿转化的代码
│  ├── crawl.py       <- 机械臂位姿转化的代码
│  └── interface.py        <- 存放主要接口
└── tests/     <-  功能测试目录
```

## **3.环境与依赖**

* python3.8+
* opencv-python
* numpy
* scipy

## **4. 安装说明**

1. 安装Python 3.8或者更高版本
2. 克隆项目到本地：`git clone http://192.168.0.188:8090/ai_lab_rd02/ai_sdks/vertical_grab.git`
3. 进入项目目录：`cd vertical_grab`
4. 安装依赖：`pip install -r requirements.txt`
5. 编译打包：在与 `setup.py `文件相同的目录下执行以下命令：`python setup.py bdist_wheel`。 在 `dist` 文件夹中找到 `.wheel`
   文件，例如：`dist/vertical_grab-0.1.0-py3-none-any.whl`。
6. 安装：`pip install vertical_grab-0.1.0-py3-none-any.whl`

## **5. 使用指南**

## **6. 接口示例**

```python
import cv2
from vertical_grab.interface import vertical_catch

depth_frame = cv2.imread("real_depth_frame.png", cv2.IMREAD_GRAYSCALE)
mask = cv2.imread("manual_catch_mask.png", cv2.IMREAD_GRAYSCALE)

# 抓取中心点
center = [368, 302]

# 摄像头的内参
color_intr = {"ppx": 326.721, "ppy": 252.721, "fx": 606.721, "fy": 607.55}

# 机械臂当前的位姿
current_pose = [-0.06532000005245209, 0.004813000094145536, 0.3710620105266571, -3.058000087738037, 0.24199999868869781,
                0.041999999433755875]

# 机械臂夹爪的长度，夹爪长度将影响到下爪的距离
arm_gripper_length = 0.02
vertical_rx_ry_rz = [3.14, 0, -0.020999999716877937]

# 手眼标定结果，转换矩阵
rotation_matrix = [[0.01990299, 0.98175955, -0.18908215], [-0.9996762, 0.02254041, 0.01180814],
                   [0.01585474, 0.18878591, 0.98189027]]

# 手眼标定结果，平移矩阵
translation_vector = [-0.06860006, 0.04255893, 0.01080163]

# 根据以上输入能计算出来的结果，做为判断依据
result = ([-0.13396845376699643, -0.03954672752039725, 0.4727158838499269, 3.14, 0, -0.020999999716877937],
          [-0.13396845376699643, -0.03954672752039725, 0.4727158838499269, 3.14, 0, -0.020999999716877937],
          [-0.1339728013898331, -0.03975372674782365, 0.3427160487253468, 3.14, 0, -0.020999999716877937])


def test_vertical_catch():
    # 单元测试内容
    assert vertical_catch(center, mask, depth_frame, color_intr, current_pose, arm_gripper_length, vertical_rx_ry_rz,
                          rotation_matrix,
                          translation_vector, True) == result

```

## 7. **许可证信息**

说明项目的开源许可证类型（如MIT、Apache 2.0等）。

* 本项目遵循MIT许可证。

## **8. 常见问题解答（FAQ）**

列出一些常见问题和解决方案。

- **Q1：机械臂连接失败**

  答案：修改过机械臂IP，请确保电脑和机械臂的网段在同一个网段下

- **Q2：UDP数据推送接口收不到数据**

  答案：检查线程模式、是否使能推送数据、IP以及防火墙