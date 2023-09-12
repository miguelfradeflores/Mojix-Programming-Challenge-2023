import random
from common import draw_box2
from colors_constant import BLACK, AMONG_COLORS, VISOR_BASE, VISOR_FILL, WHITE


AMONG_CONTOUR = [
    (1, 8, 2, 14),  # bag
    (2, 7, 3, 8),
    (2, 14, 3, 15),
    (3, 6, 4, 7),
    (3, 15, 4, 16),
    (4, 3, 5, 17),  # back
    (5, 2, 6, 3),
    (5, 17, 7, 18),  # left foot
    (6, 1, 11, 2),  # head
    (11, 2, 13, 3),  # forehead
    (9, 3, 14, 10),  # top eye,
    (8, 4, 15, 9),
    (7, 5, 16, 8),
    (13, 8, 14, 17),  # body
    (11, 17, 13, 18),  # right foot
    (10, 14, 11, 17),  # leg right
    (7, 14, 8, 17),   # leg left
    (8, 13, 10, 14),  # crunch
]

AMONG_BASE = [
    (2, 7, 4, 15),  # bag
    (6, 2, 13, 12)  # body
]

AMONG_DETAIL = [
    (3, 9, 4, 15),  # bag
    (5, 3, 6, 17),  # back
    (6, 11, 7, 17),
    (7, 12, 11, 14),
    (11, 11, 13, 17)
]

AMONG_VISOR_BASE = [
    (8, 5, 13, 8),  # EYE
    (9, 8, 14, 9)  # EYE 2
]

AMONG_VISOR_FILL = [
    (9, 4, 14, 7),  # EYE
    (10, 7, 14, 8),  # eye 2
    (14, 5, 15, 8)  # eye 3
]

AMONG_VISOR_DETAIL = [
    (11, 4, 14, 6),  # EYE
]


def draw_amongs(img, x_offset=0, y_offset=0):
    cell_size_w = int(512 / 68)
    cell_size_h = int(512 / 68)   # 17, 17 for total size
    csw = cell_size_w
    csh = cell_size_h
    among_brush = random.choice(AMONG_COLORS)
    for g in AMONG_BASE:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw),
                  among_brush[0])

    for g in AMONG_DETAIL:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw),
                  among_brush[1])

    for g in AMONG_CONTOUR:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BLACK)

    for g in AMONG_VISOR_BASE:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), VISOR_BASE)

    for g in AMONG_VISOR_FILL:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), VISOR_FILL)

    for g in AMONG_VISOR_DETAIL:
        x1, y1, x2, y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                  x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), WHITE)
