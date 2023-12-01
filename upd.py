import json, cv2
import numpy as np
from utils import *
from detection.inference import dectect

"""更新每个停车位的空车状态"""
def chk(img):
    # 期望传入的是一个二维 ndarray
    assert img is not None
    # imshow(img)
    with open("./config/data.json", 'r') as f:
        data = json.load(f)
    for i in range(len(data)):
        if data[i]['is_parking'] == 0:
            continue
        # (x1, y1) 是左下角 (x2, y2) 是右上角
        x1, y1, x2, y2 = data[i]['x1'], data[i]['y1'], data[i]['x2'], data[i]['y2']
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        target = img[y2:y1, x1:x2, :]
        # imshow(target)
        # 更新状态
        data[i]['is_empty'] = dectect(target) ^ 1
    # 写入 data.json
    with open("./config/data.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    chk(cv2.imread("saveImg/scene1380.jpg"))

