import os
import argparse

import numpy as np
import cv2

IMG_DIR = 'images'


def add_images(bg, fg):
    """
    Add the foreground image to the background image by replacing all bg pixels
    with the fg values unless the fg is 0
    :param bg: array of background pixels
    :param fg: array of foreground pixels, same dims as bg
    :return: array of combined image, same dims as bg
    """
    return np.where(fg > 0, fg, bg)


def is_odd(x):
    """
    Checks if an number is odd
    :param x: (int) number to check
    :return: (bool) True if number is odd
    """
    return x % 2 != 0


def get_central_pixel(array_length):
    """
    Given an array length, give the central pixel value, taking floor
    if the array length is odd
    :param array_length: (int) the length of an array along one dimension
    :return: the central pixel
    """
    return int(np.floor(array_length / 2))


def get_a_and_b(bg_shape, fg_shape):
    """
    Get the indices needed to centre the foreground image
    :param bg_shape: (int) shape of background image in one dimension
    :param fg_shape: (int) shape of foreground image in one dimension
    :return: (int, int) indices to centre the foreground image
    """
    bg_centre = get_central_pixel(bg_shape)
    fg_shape_half = get_central_pixel(fg_shape)
    a, b = bg_centre - fg_shape_half, bg_centre + fg_shape_half
    if is_odd(fg_shape):
        b += 1
    return a, b


def create_padded_fg(fg, bg_shape):
    """
    Pad the foreground image with 0s to make it the same size as the background image
    :param fg: (array) foreground image
    :param bg_shape: (tuple) shape if the background image
    :return: (array) 0-padded foreground image
    """
    # Make a 0-padded version of the foreground image that is
    # the same size as the background image
    fg_padded = np.zeros(bg_shape)
    a0, b0 = get_a_and_b(bg_shape[0], fg.shape[0])
    a1, b1 = get_a_and_b(bg_shape[1], fg.shape[1])
    fg_padded[a0:b0, a1:b1] = fg
    return fg_padded


def combine_images(bg_file, fg_file, output_file):
    """
    Combine two images by overlaying the foreground image on the background image
    :param bg_file: (string) background image filename
    :param fg_file: (string) foreground image filename
    :param output_file: (string) output image filename
    """
    print(f'Reading in images:\n - {IMG_DIR}/{bg_file}\n - {IMG_DIR}/{fg_file}')
    bg = cv2.imread(os.path.join(IMG_DIR, bg_file))
    fg = cv2.imread(os.path.join(IMG_DIR, fg_file))
    fg_padded = create_padded_fg(fg, bg.shape)
    final_image = add_images(bg, fg_padded)
    cv2.imwrite(os.path.join(IMG_DIR, output_file), final_image)
    print(f'Combined image written to:\n - {IMG_DIR}/{output_file}')
    return final_image


def image_combiner():
    parser = argparse.ArgumentParser(description='Combine a foreground and background image')
    parser.add_argument('-b', '--bg-file', type=str, default='bg.jpg',
                        help='Name of background image file')
    parser.add_argument('-f', '--fg-file', type=str, default='fg.png',
                        help='Name of foreground image file')
    parser.add_argument('-o', '--output-file', type=str, default='output.png',
                        help='Name of output image file')
    args = parser.parse_args()

    combine_images(args.bg_file, args.fg_file, args.output_file)


if __name__ == '__main__':
    image_combiner()
