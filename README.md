# Pytest examples

This repository contains example unit tests with some blank ones to be 
filled in (and solutions on another branch). 

All commands should be run from the top level directory.

## Installation

Should work with Python >= 3.6. Install the packages from 
`requirements.txt` into your environment. 

## Main scripts

### Part 1

In part 1, the script `image_combiner.py` is for overlaying a foreground
image over a background image, using files in the `images` directory.

Run `python part1/image_combiner.py -h` to see the input parameters.

Source for background images:
[Pexels](https://www.pexels.com/creative-commons-images/)

Source for foreground images:
[PNG ALL](http://www.pngall.com/)

### Part 2

A very simple script to tell you whether it is the weekend or not. 

To run it try `python part2/is_it_the_weekend.py`

## Tests

The tests are located in the `tests` directory. To run them you just need to execute
the command `pytest`.

`test_part1.py` and `test_part2.py` correspond to the respective directories.

`test_part3.py` is intended for more complex tests for the `part1` directory script.
