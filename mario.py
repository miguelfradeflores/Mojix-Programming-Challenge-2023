import cv2
import random
import numpy as np
from common import draw_box2
from colors_constant import SKIN, RED, DARK_GREEN, ORANGE, YELLOW, BLACK, BLUE

MARIO_SKIN = [
    (2, 12, 14, 15),  # HANDS
    (4,  4, 12, 8),  # face
    (5,  8, 13, 9),  # neck
    (11, 5, 14, 7),  # nose 1
    (13, 6, 15, 7),  # nose 2
]

MARIO_CLOTH = [
    (5, 2, 11, 3),  # hat 1
    (4, 3, 15, 4),  # hat 2
    (4, 9, 11, 10),
    (3, 10, 13, 11),
    (2, 11, 14, 12),
    (4, 12, 12, 13),

]

MARIO_FACE_DETAILS = [
    (10, 4, 11, 6),  # EYE
    (11, 6, 12, 7),  # mustache 1
    (10, 7, 14, 8),  # mustache 2
    (4, 4, 7, 5),  # patilla 1
    (5, 5, 6, 6),  # patilla 2
    (5, 6, 7, 7),  # patilla 3
    (3, 5, 4, 8),  # cabello 1
    (4, 7, 5, 8),  # cabello 2
    (3, 16, 6, 17),
    (2, 17, 6, 18),
    (10, 16, 13, 17),
    (10, 17, 14, 18)
]

MARIO_OVER_ALL = [
    (6,  9, 7, 16),
    (9, 10, 10, 16),
    (7, 11, 9, 15),
    (5, 12, 6, 16),
    (10, 12, 11, 16),
    (4, 14, 5, 16),
    (11, 14, 12, 16),
]

MARIO_BUTTOMS = [
    (6, 12, 7, 13),
    (9, 12, 10, 13),
]


def draw_mario(img, x_offset=0, y_offset=0):
    cell_size_w = int(512 / 60)
    cell_size_h = int(512 / 68)   # 15, 17 for total size
    csw = cell_size_w
    csh = cell_size_h
    for g in MARIO_SKIN:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), SKIN)
    BROS_COLOR = random.choice([RED, DARK_GREEN, ORANGE, YELLOW])
    for g in MARIO_CLOTH:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BROS_COLOR)
    for g in MARIO_FACE_DETAILS:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BLACK)
    for g in MARIO_OVER_ALL:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BLUE)
    for g in MARIO_BUTTOMS:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), ORANGE)


def draw_marios():
    white_board = np.zeros((512, 512), dtype=np.uint8)
    white_board[0:512, 0:512] = 255
    white_board = cv2.cvtColor(white_board, cv2.COLOR_GRAY2RGB)
    draw_mario(white_board, 0, 0)
    cv2.imshow("marios", white_board)
    cv2.waitKey()
    cv2.destroyAllWindows()
