import numpy as np

from part1.image_combiner import add_images, is_odd, get_central_pixel,\
    get_a_and_b, create_padded_fg


def test_is_odd():
    """
    Test that the is_odd method returns True for odd numbers,
    and False for even numbers
    """
    assert is_odd(1)
    assert not is_odd(2)


def test_get_central_pixel():
    """
    Test that the get_central_pixel method returns the central pixel
    """
    assert get_central_pixel(10) == 5
    # For odd numbers it should take the floor
    assert get_central_pixel(11) == 5
    # Edge case: should return 0 for 0
    assert get_central_pixel(0) == 0


def test_add_images():
    """
    Test that the image overlaying function works as expected
    """
    bg = np.ones((5, 5))
    fg = np.zeros((5, 5))
    fg[2, 3] = 10
    # The expected image should be the same as the background
    # with the pixel at (2, 3) set to 10
    expected_image = np.ones((5, 5))
    expected_image[2, 3] = 10
    np.testing.assert_array_equal(expected_image, add_images(bg, fg))


def test_get_a_and_b():
    """
    # TODO: write a test that checks if get_a_and_b returns reasonable values
    # hint: the should difference to fg_shape
    """
    assert True


def test_create_padded():
    """
    # TODO: write a test that checks if create_padded_fg works as expected
    """
    assert True
