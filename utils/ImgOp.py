import numpy as np
import cv2
import matplotlib.pyplot as plt

def imshow(image, cmap=None, title=None):
    fig, ax = plt.subplots(1, 1)
    img = image.copy()

    if cmap == 'gray':
        ax.imshow(img, cmap=cmap)
    else:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        ax.imshow(img)
    ax.axis('off')

    if title:
        ax.set_title(title)
    plt.show()