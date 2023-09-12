import numpy as np
import cv2
import random
from console import draw_control
from mario import draw_mario
from droids import draw_droid
from amongs import draw_amongs
from colors_constant import MJX_COLORS


def draw_mojix(scale):
    board = np.zeros((512, 512), dtype=np.uint8)
    board[0:512, 0:512] = 255
    board = cv2.cvtColor(board, cv2.COLOR_GRAY2RGB)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    mjx_base = random.choice(MJX_COLORS)
    cv2.circle(board, (50*scale, 40*scale), 3*scale, mjx_base[0], -1)
    cv2.circle(board, (40*scale, 30*scale), 3*scale, mjx_base[0], -1)
    cv2.circle(board, (40*scale, 50*scale), 3*scale, mjx_base[0], -1)
    cv2.circle(board, (60*scale, 30*scale), 3*scale, mjx_base[0], -1)
    cv2.circle(board, (60*scale, 50*scale), 3*scale, mjx_base[0], -1)

    cv2.circle(board, (40*scale, 40*scale), 3*scale, mjx_base[1], -1)
    cv2.circle(board, (50*scale, 30*scale), 3*scale, mjx_base[1], -1)
    cv2.circle(board, (60*scale, 40*scale), 3*scale, mjx_base[1], -1)
    cv2.circle(board, (50*scale, 50*scale), 3*scale, mjx_base[1], -1)

    cv2.putText(board, 'mojix', (20*scale, 80*scale),
                font, 0.9*scale, mjx_base[0], 2, cv2.LINE_AA)

    cv2.circle(board, (59*scale, 69*scale),
               round(int(1.4*scale)), mjx_base[0], -1)
    cv2.circle(board, (66*scale, 69*scale),
               round(int(1.4*scale)), mjx_base[0], -1)

    DRAW_COORDINATES = [
        [5, 5], [400, 10], [405, 320], [5, 200], [5, 415]
    ]

    draw_control(board, 200, 10)

    for coordinate in DRAW_COORDINATES:
        draw_choice = random.randint(1, 3)
        if draw_choice == 1:
            draw_amongs(board, coordinate[0], coordinate[1])
        elif draw_choice == 2:
            draw_mario(board, coordinate[0], coordinate[1])
        elif draw_choice == 3:
            draw_droid(board, coordinate[0], coordinate[1])
    output_filename = "examples/ppm_image.ppm"
    save_ppm_image(board, output_filename)

    cv2.imshow("mojix", board)
    cv2.waitKey()
    cv2.destroyAllWindows()


def save_ppm_image(image, filename):
    with open(filename, 'w') as ppm_file:
        ppm_file.write(f'P3\n{len(image[0])}\n{len(image)}\n255\n')
        for row in image:
            for pixel in row:
                ppm_file.write(f'{pixel[2]} {pixel[1]} {pixel[1]} ')
                ppm_file.write('\n')
            # ppm_file.write('\n')


draw_mojix(5)
