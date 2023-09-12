import cv2
import random
import numpy as np
from common import draw_box2
from colors_constant import BLACK, GRAY, RED, BLUE, COLORS

DROID_CONTORS = [
    (5, 6, 6, 26),     # main left body
    (18, 6, 19, 26),   # main body rigth
    (5, 6, 18, 10),    # neck
    (5, 22, 18, 23),   # bottom
    (3, 10, 6, 11),    # top sholder left
    (19, 10, 21, 11),  # top sholder rigth
    (2, 13, 6, 14),    # bottom sholder left
    (19, 13, 22, 14),  # bottom sholder rigth
    (2, 11, 3, 14),    # margin sholder left
    (21, 11, 22, 14),  # madring sholder rigth
    (3, 14, 4, 21),    # left arm
    (20, 14, 21, 21),  # rigth arm
    (3, 20, 5, 21),    # end left arm
    (19, 20, 21, 21),  # end rigth arm
    (2, 21, 3, 23),    # left ankle
    (21, 21, 22, 23),  # rigth ankle
    (1, 23, 2, 26),    # left foot
    (22, 23, 23, 26),  # rigth foot
    (1, 25, 5, 26),    # base left foot
    (19, 25, 23, 26),  # base rigth foot
    (8, 25, 16, 26),   # mid base
    (8, 24, 9, 25),    # mid base l1
    (9, 23, 10, 24),   # mid base l2
    (15, 24, 16, 25),  # mid base r1
    (14, 23, 15, 24),  # mid base r2
    (10, 1, 14, 2),    # mid top head
    (8, 2, 16, 3),     # mid head
    (7, 3, 8, 4),      # left head side
    (16, 3, 17, 4),    # rigth head side
    (12, 3, 13, 4),    # eye
    (6, 4, 18, 6),     # mid head 2
    (11, 20, 12, 21),  # belly 1
    (12, 19, 13, 20)   # belly 2
]

DROID_CONTRAST = [
    (6, 6, 18, 9),   # bottom neck,
    (7, 4, 10, 6),   # left face
    (14, 4, 17, 6),  # left face
    (10, 2, 11, 3),
    (13, 2, 14, 3),
    (9, 3, 10, 4),
    (14, 3, 15, 4),
    (6, 11, 7, 19),    # left-body detail 1
    (7, 11, 8, 12), (7, 18, 8, 19),
    (8, 11, 9, 22),    # left-body detail 2
    (15, 11, 16, 19),  # rigth-body detail 1
    (16, 11, 17, 12), (16, 18, 17, 19),
    (17, 11, 18, 22),  # rigth-body detail 2
    (11, 19, 12, 20),  # belly 1
    (12, 20, 13, 21),  # belly 2
    (11, 15, 13, 17),  # stomach
    (11, 23, 13, 24),  # base detail
    (10, 24, 11, 25),  # base detail left
    (13, 24, 14, 25),  # base detail rigth
    (4, 21, 5, 23),  # left ankle,
    (19, 21, 20, 23),  # left ankle
]

DROID_DETAILS = [
    (11, 2, 13, 3),  # TOP EYE
    (11, 5, 13, 6),  # BOTTOM EYE
    (10, 3, 11, 6),  # LEFT EYE
    (13, 3, 14, 6),  # RIGTH EYE
    (8, 3, 9, 4), (7, 4, 8, 5),
    (15, 3, 16, 4), (16, 4, 17, 5),  # head details
    (7, 6, 9, 7),
    (7, 8, 9, 9),
    (10, 7, 11, 9),
    (12, 7, 15, 9),
    (16, 7, 17, 9),
    (10, 11, 14, 12),  # body lines 1
    (10, 13, 14, 14),  # body lines 2
    (10, 15, 11, 17),  # stomach left
    (13, 15, 14, 17),  # stomach rigth
    (10, 18, 14, 19),  # bottom lines 1
    (10, 21, 14, 22),  # bottom lines 2
    (10, 19, 11, 21),
    (13, 19, 14, 21)
]

DROID_LIGHT = [
    (13, 8, 14, 9)
]


def draw_droids():
    white_board = np.zeros((512, 512), dtype=np.uint8)
    white_board[0:512, 0:512] = 255
    white_board = cv2.cvtColor(white_board, cv2.COLOR_GRAY2RGB)
    draw_droid(white_board)
    draw_droid(white_board, 255, 0)
    draw_droid(white_board, 0, 255)
    draw_droid(white_board, 255, 255)
    cv2.imshow("droids", white_board)
    cv2.waitKey()
    cv2.destroyAllWindows()


def draw_droid(img, x_offset=0, y_offset=0):
    # Define heigth width
    cell_size_w = int(512/92)
    cell_size_h = int(512/100)   # 23, 25 for total size
    csw = cell_size_w
    csh = cell_size_h
    for g in DROID_CONTORS:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BLACK)
    for g in DROID_CONTRAST:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), GRAY)

    detail_brush = random.choice(COLORS)
    for g in DROID_DETAILS:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw),
                  detail_brush)

    light_brush = RED if detail_brush != RED else BLUE
    for g in DROID_LIGHT:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw),
                  light_brush)
