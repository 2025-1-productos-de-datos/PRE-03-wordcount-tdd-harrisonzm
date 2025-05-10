import argparse
import sys

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_count_words


def parse_args():
    parser = argparse.ArgumentParser(description="Count words in files.")
    parser.add_argument(
        "input", type=str, help="Path to the input folder containing files to process"
    )
    parser.add_argument(
        "output", type=str, help="Path to the output folder for results"
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def main():

    if len(sys.argv) != 3:
        print("Usage: python3 -m homework <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)
    words = split_into_words(all_lines)
    counter = count_words(words)
    write_count_words(counter, output_folder)


if __name__ == "__main__":
    main()
