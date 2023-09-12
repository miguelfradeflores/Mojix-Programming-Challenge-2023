
from colors_constant import BLACK, BASE_COLORS
from common import draw_box2


CONTROL_INSIDE = []

CONTROL_COUNTOUR = [
    (1, 4, 2, 12),  # left side
    (2, 3, 3, 4),
    (3, 2, 4, 3),
    (4, 1, 9, 2),  # left top
    (2, 12, 3, 13),
    (3, 13, 7, 14),  # left bottom
    (7, 12, 8, 13),
    (8, 11, 18, 12),  # bottom
    (9, 2, 17, 3),  # top
    (17, 1, 23, 2),  # right top
    (24, 3, 25, 4),
    (23, 2, 24, 3),
    (25, 4, 26, 12),  # right side
    (19, 13, 24, 14),  # right bottom
    (18, 12, 19, 13),
    (24, 12, 25, 13),
    (3, 6, 9, 8),  # pad H
    (5, 4, 7, 10),  # pad V
    (10, 8, 11, 9),
    (11, 7, 12, 8),
    (13, 8, 14, 9),
    (14, 7, 15, 8)
]

CONTROL_BUTTOMS = [
    (17, 6, 19, 8),  # LEFT BUTTOM
    (19, 4, 21, 6),  # TOP BUTTOM
    (21, 6, 23, 8),  # RIGHT BUTTOM
    (19, 8, 22, 10)  # BOTTOM BUTTOM

]


def draw_control(img, x_offset=0, y_offset=0):
    cell_size_w = int(512 / 92)
    cell_size_h = int(512 / 78)  # 15, 17 for total size
    csw = cell_size_w
    csh = cell_size_h
    for g in CONTROL_COUNTOUR:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BLACK)
    for i, g in enumerate(CONTROL_BUTTOMS):
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw),
                  BASE_COLORS[i])
