from unittest import mock

import numpy as np

from part1 import image_combiner


def test_get_a_and_b_calls_odd():
    """
    # TODO: write a test using mock to check that is_odd is called
    """
    assert True


@mock.patch.object(image_combiner.os.path, 'join', side_effect=lambda y, x: x)
@mock.patch.object(image_combiner.cv2, 'imread', side_effect=lambda x: x)
@mock.patch.object(image_combiner.cv2, 'imwrite')
def test_combine_images(mock_imwrite, mock_imread, mock_join):
    bg = np.ones((5, 5))
    fg = np.zeros((3, 3))
    fg[1, 1] = 2
    final_image_should_be = np.ones((5, 5))
    final_image_should_be[2, 2] = 2
    final_image = image_combiner.combine_images(bg, fg, None)
    np.testing.assert_array_equal(final_image, final_image_should_be)
