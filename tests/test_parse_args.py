import sys

from homework.src.wordcount import parse_args


def test_parse_args():
    # Llamada en el prompt:
    #
    #   $ python3 -m homework data/input/ data/output/
    #
    test_args = ["homework", "data/input/", "data/output/"]
    sys.argv = test_args

    input_folder, output_folder = parse_args()
    assert input_folder == test_args[1]
    assert output_folder == test_args[2]
