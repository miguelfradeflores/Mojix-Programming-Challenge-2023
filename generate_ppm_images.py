import numpy as np
import cv2
import random
from console import draw_control

RED = (0,0,255); DARK_RED = (0,0,75); SHADOW_RED = (0,0,139)
BLUE = (255,0,0); DARK_BLUE = (75,0,0); SHADOW_BLUE = (139,0,0)
GREEN = (0,255,0); DARK_GREEN = (0,75,0); SHADOW_GREEN = (0,139,0)
BLACK = (0,0,0); WHITE = (255,255,255); SHADOW_WHITE = (211,211,211)
PURPLE = (255,0,255); PINK = (203,192,255); SHADOW_PINK = (100,69,139)
ORANGE= (0,140,255); SHADOW_ORANGE= (0,69,255)
YELLOW= (0,255,255); SHADOW_YELLOW= (11,134,184) 
CYAN = (255,255,0); SHADOW_CYAN = (139,139,0)
GRAY =(170,170,170)
MIX = (132,43,55)
MIX4 = (122,143,55)
SKIN = (185, 216, 250)
VISOR_BASE= (100,50,20)
VISOR_FILL= (230,160,120)
COLORS = [RED, CYAN, BLUE, GREEN, PURPLE, ORANGE, MIX, MIX4]
MJX_COLORS = [[RED,DARK_RED], [BLUE, DARK_BLUE], [GREEN, DARK_GREEN] ]
AMONG_COLORS = [[RED,SHADOW_RED], [BLUE,SHADOW_BLUE], [GREEN,SHADOW_GREEN],
                [PINK, SHADOW_PINK], [WHITE,SHADOW_WHITE], [ORANGE,SHADOW_ORANGE],
                [YELLOW, SHADOW_YELLOW], [CYAN, SHADOW_CYAN]]

DROID_CONTORS = [
    (5, 6, 6, 26), # main left body
    (18, 6, 19, 26), # main body rigth
    (5, 6, 18, 10), # neck
    (5, 22, 18, 23),  #bottom
    (3, 10, 6, 11),  # top sholder left
    (19, 10, 21, 11), # top sholder rigth
    (2, 13, 6, 14), # bottom sholder left
    (19, 13, 22, 14), # bottom sholder rigth
    (2, 11, 3, 14),  # margin sholder left
    (21, 11, 22, 14), # madring sholder rigth
    (3, 14, 4, 21),  # left arm
    (20, 14, 21, 21),  # rigth arm
    (3, 20, 5, 21),  # end left arm
    (19, 20, 21, 21),  # end rigth arm
    (2, 21, 3, 23),  # left ankle
    (21, 21, 22, 23),  # rigth ankle   
    (1, 23, 2, 26),  # left foot
    (22, 23, 23, 26),  # rigth foot
    (1, 25, 5, 26),  # base left foot
    (19, 25, 23, 26),  # base rigth foot
    (8, 25, 16, 26), # mid base
    (8, 24, 9, 25), # mid base l1
    (9, 23, 10, 24), # mid base l2
    (15, 24, 16, 25), # mid base r1
    (14, 23, 15, 24), # mid base r2
    (10, 1, 14, 2), # mid top head
    (8, 2, 16, 3), # mid head
    (7, 3, 8, 4), # left head side
    (16, 3, 17, 4), # rigth head side
    (12, 3, 13, 4), # eye
    (6, 4, 18, 6), # mid head 2
    (11, 20, 12, 21), # belly 1
    (12, 19, 13, 20) # belly 2
]

DROID_CONTRAST = [
    (6, 6, 18, 9), # bottom neck,
    (7, 4, 10, 6), # left face
    (14, 4, 17, 6), # left face
    (10, 2, 11, 3),
    (13, 2, 14, 3),
    (9, 3, 10, 4),
    (14, 3, 15, 4),
    (6, 11, 7, 19), # left-body detail 1
    (7, 11, 8, 12),   (7, 18, 8, 19),
    (8, 11, 9, 22), # left-body detail 2
    (15, 11, 16, 19), # rigth-body detail 1
    (16, 11, 17, 12),   (16, 18, 17, 19),
    (17, 11, 18, 22), # rigth-body detail 2
    (11, 19, 12, 20), # belly 1
    (12, 20, 13, 21), # belly 2
    (11,15,13,17), # stomach
    (11, 23, 13, 24), # base detail
    (10, 24, 11, 25), # base detail left
    (13, 24, 14, 25), # base detail rigth
    (4, 21, 5, 23), # left ankle,
    (19, 21, 20, 23), # left ankle
]

DROID_DETAILS = [
    (11, 2, 13, 3), # TOP EYE
    (11, 5, 13, 6), # BOTTOM EYE
    (10, 3, 11, 6), # LEFT EYE
    (13, 3, 14, 6), # RIGTH EYE
    (8,3,9,4), (7,4,8,5), (15,3,16,4), (16,4,17,5), # head details
    (7,6,9,7),
    (7,8,9,9),
    (10,7,11,9),
    (12,7,15,9),
    (16,7,17,9),
    (10,11,14,12),  # body lines 1
    (10,13,14,14),  # body lines 2
    (10,15,11,17), # stomach left
    (13,15,14,17), # stomach rigth
    (10,18,14,19),  # bottom lines 1
    (10,21,14,22),  # bottom lines 2
    (10,19,11,21), 
    (13,19,14,21), 
]

DROID_LIGHT = [
    (13,8,14,9)
]

MARIO_SKIN = [
    (2, 12, 14, 15), # HANDS
    (4,  4, 12, 8), # face
    (5,  8, 13, 9), # neck
    (11, 5, 14, 7), # nose 1
    (13, 6, 15, 7), # nose 2
]   

MARIO_CLOTH = [
    (5,2,11,3), # hat 1
    (4,3,15,4), # hat 2
    (4,9,11,10),
    (3,10,13,11),
    (2,11,14,12),
    (4,12,12,13),

]

MARIO_FACE_DETAILS = [
    (10, 4, 11, 6), # EYE
    (11, 6, 12, 7), # mustache 1
    (10, 7, 14, 8), # mustache 2
    (4,  4,  7, 5), # patilla 1
    (5,  5,  6, 6), # patilla 2
    (5,  6,  7, 7), # patilla 3
    (3,  5,  4, 8), # cabello 1
    (4,  7,  5, 8), # cabello 2
    (3, 16,  6,17),
    (2, 17,  6,18),
    (10,16,  13,17),
    (10,17,  14,18),

]

MARIO_OVER_ALL = [
    (6,  9, 7,16),
    (9, 10,10,16),
    (7, 11, 9,15),
    (5, 12, 6,16),
    (10,12,11,16),
    (4, 14, 5,16),
    (11,14,12,16),
]

MARIO_BUTTOMS = [
    (6, 12, 7,13),
    (9, 12,10,13), 
]

AMONG_CONTOUR = [
    (1, 8, 2,14), # bag
    (2, 7, 3, 8),
    (2,14, 3,15),
    (3, 6, 4, 7),
    (3,15, 4,16),
    (4, 3, 5,17), # back
    (5, 2, 6, 3),
    (5,17, 7,18), # left foot
    (6, 1,11, 2), # head
    (11, 2,13,3), # forehead
    (9, 3,14, 10), # top eye,
    (8, 4,15, 9),
    (7, 5,16, 8),
    (13,8,14,17), # body
    (11,17,13,18), # right foot
    (10,14,11,17), # leg right
    (7,14, 8,17),  # leg left
    (8,13,10,14), # crunch
]

AMONG_BASE = [
    (2, 7, 4,15), # bag
    (6 ,2,13,12)  # body
]

AMONG_DETAIL = [
    (3, 9, 4,15), # bag
    (5 ,3, 6,17), # back
    (6,11, 7,17),
    (7,12,11,14),
    (11,11,13,17)
]

AMONG_VISOR_BASE = [
    (8, 5, 13,8), # EYE
    (9, 8, 14,9) # EYE 2
]

AMONG_VISOR_FILL = [
    (9, 4,14,7), # EYE
    (10,7,14,8),  # eye 2
    (14,5,15,8)  # eye 3
]

AMONG_VISOR_DETAIL = [
    (11, 4,14,6), # EYE
]

def pixel():
    return np.array([random.randint(0,255), random.randint(0,255),random.randint(0,255) ])

def draw_box(img, y1, y2, x1, x2):
    box_color = random.choice(COLORS)
    img[x1:x2, y1:y2] = box_color

def draw_box2(img, y1, y2, x1, x2, brush_color):
    box_color = brush_color
    img[y1:y2, x1:x2] = box_color

def draw_droids(val):
    white_board = np.zeros((512,512), dtype=np.uint8)
    white_board[0:512, 0:512] = 255
    white_board = cv2.cvtColor(white_board, cv2.COLOR_GRAY2RGB)
    # for i in range(val):
    #     white_board = np.zeros((512,512), dtype=np.uint8)
    #     white_board[0:512, 0:512] = 255
    #     white_board = cv2.cvtColor(white_board, cv2.COLOR_GRAY2RGB)
    #     draw_droid(white_board)
    #     cv2.imshow(f"droid_{i}", white_board)
    #     cv2.waitKey(500)
    draw_droid(white_board)
    draw_droid(white_board, 255, 0 )
    draw_droid(white_board, 0, 255 )
    draw_droid(white_board, 255, 255 )
    cv2.imshow(f"droids", white_board)
    cv2.waitKey()
    cv2.destroyAllWindows()

def draw_droid(img, x_offset=0, y_offset=0):
    # Define heigth width
    cell_size_w = int(512/92); cell_size_h = int(512/100)   # 23, 25 for total size
    csw=cell_size_w; csh=cell_size_h
    for g in DROID_CONTORS:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BLACK)
    for g in DROID_CONTRAST:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), GRAY)
    detail_brush = random.choice(COLORS)
    for g in DROID_DETAILS:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), detail_brush)
    light_brush = RED if detail_brush!=RED else BLUE
    for g in DROID_LIGHT:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), light_brush)

def display_image():
    img = np.zeros((512, 512), dtype=np.uint8)
    img[50:450, 50:450] = 255
    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    white_board = np.zeros((512,512), dtype=np.uint8)
    white_board[0:512, 0:512] = 255
    white_board = cv2.cvtColor(white_board, cv2.COLOR_GRAY2RGB)

    brush_color = random.choice(COLORS) 
    for i in range(1,512):
        img_color.itemset(i, i, 0, brush_color[0])
        img_color.itemset(i, i, 1, brush_color[1])
        img_color.itemset(i, i, 2, brush_color[2])

    brush_color2 = random.choice(COLORS)
    for j in range(1,512,5):
        brush_color2 = random.choice(COLORS)
        for i in range(1,512):
            img_color.itemset(i, j, 0, brush_color2[0] if i!=5 and i%2==0 else 0 )
            img_color.itemset(i, j, 1, brush_color2[1] if i!=5 and i%2==0 else 0 )
            img_color.itemset(i, j, 2, brush_color2[2] if i!=5 and i%2==0 else 0 )

    for j in range(1,512,8):
        brush_color2 = random.choice(COLORS)
        for i in range(1,512):
            img_color.itemset(j, i, 0, brush_color2[0] if i!=5 and i%2==0 else 0 )
            img_color.itemset(j, i, 1, brush_color2[1] if i!=5 and i%2==0 else 0 )
            img_color.itemset(j, i, 2, brush_color2[2] if i!=5 and i%2==0 else 0 )

    draw_box(img_color, 90, 120, 90, 150)
    draw_droid(white_board)
    ret, thresh = cv2.threshold(img, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE)
    color = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    img = cv2.drawContours(color, contours, -1, COLORS[random.randint(0,len(COLORS)-1)], 2)
    cv2.imshow("contours", color)
    cv2.imshow("diagonal", img_color)
    cv2.imshow("droid", white_board)
    cv2.waitKey()
    cv2.destroyAllWindows()
    # Define heigth width
    cell_size_w = int(512/46); cell_size_h = int(512/50)   # 23, 25 for total size
    csw=cell_size_w; csh=cell_size_h

def draw_mario(img, x_offset=0, y_offset=0):
    cell_size_w = int(512/60); cell_size_h = int(512/68)   # 15, 17 for total size
    csw=cell_size_w; csh=cell_size_h
    for g in MARIO_SKIN:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), SKIN)
    BROS_COLOR = random.choice([RED,DARK_GREEN,ORANGE]) 
    for g in MARIO_CLOTH:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BROS_COLOR)
    for g in MARIO_FACE_DETAILS:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BLACK)
    for g in MARIO_OVER_ALL:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BLUE)
    for g in MARIO_BUTTOMS:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), ORANGE)

def draw_marios():
    white_board = np.zeros((512,512), dtype=np.uint8)
    white_board[0:512, 0:512] = 255
    white_board = cv2.cvtColor(white_board, cv2.COLOR_GRAY2RGB)
    draw_mario(white_board, 0, 0)
    cv2.imshow(f"marios", white_board)
    cv2.waitKey()
    cv2.destroyAllWindows()

def draw_amongs(img, x_offset=0, y_offset=0):
    cell_size_w = int(512/68); cell_size_h = int(512/68)   # 17, 17 for total size
    csw=cell_size_w; csh=cell_size_h
    among_brush = random.choice(AMONG_COLORS)
    for g in AMONG_BASE:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), among_brush[0])

    for g in AMONG_DETAIL:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), among_brush[1])

    for g in AMONG_CONTOUR:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), BLACK)

    for g in AMONG_VISOR_BASE:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), VISOR_BASE)

    for g in AMONG_VISOR_FILL:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), VISOR_FILL)
    for g in AMONG_VISOR_DETAIL:
        x1,y1,x2,y2 = g
        draw_box2(img, y_offset + ((y1-1)*csh), y_offset + ((y2-1)*csh),
                   x_offset + ((x1-1)*csw), x_offset + ((x2-1)*csw), WHITE)

def draw_mojix(scale):
    board = np.zeros((512,512), dtype=np.uint8)
    board[0:512, 0:512] = 255
    board = cv2.cvtColor(board, cv2.COLOR_GRAY2RGB)   
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    mjx_base = random.choice(MJX_COLORS)
    cv2.circle(board,(50*scale,40*scale), 3*scale, mjx_base[0], -1)
    cv2.circle(board,(40*scale,30*scale), 3*scale, mjx_base[0], -1)
    cv2.circle(board,(40*scale,50*scale), 3*scale, mjx_base[0], -1)
    cv2.circle(board,(60*scale,30*scale), 3*scale, mjx_base[0], -1)
    cv2.circle(board,(60*scale,50*scale), 3*scale, mjx_base[0], -1)

    cv2.circle(board,(40*scale,40*scale), 3*scale, mjx_base[1], -1)
    cv2.circle(board,(50*scale,30*scale), 3*scale, mjx_base[1], -1)
    cv2.circle(board,(60*scale,40*scale), 3*scale, mjx_base[1], -1)
    cv2.circle(board,(50*scale,50*scale), 3*scale, mjx_base[1], -1)

    cv2.putText(board,'mojix',(20*scale,80*scale), font, 0.9*scale ,mjx_base[0], 2, cv2.LINE_AA)

    cv2.circle(board,(59*scale,69*scale), round(int(1.4*scale)), mjx_base[0], -1)
    cv2.circle(board,(66*scale,69*scale), round(int(1.4*scale)), mjx_base[0], -1)

    DRAW_COORDINATES = [
        [5,5], [400,10], [405,320], [5,200], [5,415]
    ]

    draw_control(board, 200, 10)

    for coordinate in DRAW_COORDINATES:
        draw_choice = random.randint(1,3)
        if draw_choice ==1:
            draw_amongs(board,coordinate[0],coordinate[1])
        elif draw_choice ==2:
            draw_mario(board,coordinate[0],coordinate[1])
        elif draw_choice ==3:
            draw_droid(board,coordinate[0],coordinate[1])
    # output_filename = "ppm_image.ppm"
    # save_ppm_image(board, output_filename)

    cv2.imshow(f"mojix", board)
    cv2.waitKey()
    cv2.destroyAllWindows()

def save_ppm_image(image, filename):
    with open(filename, 'w') as ppm_file:
        ppm_file.write(f'P3\n{len(image[0])} {len(image)}\n255\n')
        for row in image:
            for pixel in row:
                ppm_file.write(f'{pixel[2]} {pixel[1]} {pixel[1]} ')
                ppm_file.write('\n')
            # ppm_file.write('\n')

draw_mojix(5)
