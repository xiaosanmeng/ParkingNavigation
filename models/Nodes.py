import numpy as np
import json

class Node:
    def __init__(self, x, y, is_entrance=False, is_empty=False,id = None, is_parking=False):
        self.x = x  # 横坐标
        self.y = y  # 纵坐标
        self.id = id
        self.is_entrance = is_entrance  # 是否为入口，默认为False
        self.is_empty = is_empty  # 是否为空车位，默认为False
        self.is_parking = is_parking

    def __str__(self):
        return f"Node at ({self.x}, {self.y}), Entrance: {self.is_entrance}, Empty: {self.is_empty}"
    
    def distance(self, w):
        dx = self.x - w.x
        dy = self.y - w.y
        return np.sqrt(dx * dx + dy * dy)

    def read(file):
        total = []
        with open(file, 'r') as f:
            data = json.load(f)
        return [Node(item['x'], item['y'], item['is_entrance'], 
                     item['is_empty'], item['id'], item['is_parking']) for item in data]
            

if __name__ == '__main__':
    node1 = Node(3, 4, True, False)
    node2 = Node(5, 6, False, True)
    print(node1.distance(node2))
