import random
import cv2
import numpy as np
from colors_constant import COLORS


def pixel():
    return np.array([random.randint(0, 255),
                     random.randint(0, 255),
                     random.randint(0, 255)])


def draw_box2(img, y1, y2, x1, x2, brush_color):
    box_color = brush_color
    img[y1:y2, x1:x2] = box_color


def draw_box(img, y1, y2, x1, x2):
    box_color = random.choice(COLORS)
    img[x1:x2, y1:y2] = box_color


def display_image():
    img = np.zeros((512, 512), dtype=np.uint8)
    img[50:450, 50:450] = 255
    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    white_board = np.zeros((512, 512), dtype=np.uint8)
    white_board[0:512, 0:512] = 255
    white_board = cv2.cvtColor(white_board, cv2.COLOR_GRAY2RGB)

    brush_color = random.choice(COLORS)
    for i in range(1, 512):
        img_color.itemset(i, i, 0, brush_color[0])
        img_color.itemset(i, i, 1, brush_color[1])
        img_color.itemset(i, i, 2, brush_color[2])

    brush_color2 = random.choice(COLORS)
    for j in range(1, 512, 5):
        brush_color2 = random.choice(COLORS)
        for i in range(1, 512):
            img_color.itemset(i, j, 0, brush_color2[0]
                              if i != 5 and i % 2 == 0 else 0)
            img_color.itemset(i, j, 1, brush_color2[1]
                              if i != 5 and i % 2 == 0 else 0)
            img_color.itemset(i, j, 2, brush_color2[2]
                              if i != 5 and i % 2 == 0 else 0)

    for j in range(1, 512, 8):
        brush_color2 = random.choice(COLORS)
        for i in range(1, 512):
            img_color.itemset(j, i, 0, brush_color2[0]
                              if i != 5 and i % 2 == 0 else 0)
            img_color.itemset(j, i, 1, brush_color2[1]
                              if i != 5 and i % 2 == 0 else 0)
            img_color.itemset(j, i, 2, brush_color2[2]
                              if i != 5 and i % 2 == 0 else 0)

    draw_box(img_color, 90, 120, 90, 150)
    ret, thresh = cv2.threshold(img, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    color = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    img = cv2.drawContours(color, contours, -1,
                           COLORS[random.randint(0, len(COLORS)-1)], 2)
    cv2.imshow("contours", color)
    cv2.imshow("diagonal", img_color)
    cv2.imshow("droid", white_board)
    cv2.waitKey()
    cv2.destroyAllWindows()
