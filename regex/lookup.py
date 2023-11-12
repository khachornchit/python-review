import re
import argparse


def search_word_in_file():
    """Search for a word in a file."""
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help="specify word to search for")
    parser.add_argument('fname', help='specify file to search')
    args = parser.parse_args()

    try:
        with open(args.fname, 'r') as search_file:
            for line_num, line in enumerate(search_file, start=1):
                line = line.strip('\n\r')
                search_result = re.search(args.word, line, re.M | re.I)
                if search_result:
                    print(f"{line_num} : {line}")

        if not search_result:
            print(f"Not found [{args.word}] in the file!")

    except FileNotFoundError:
        print(f"Error: File '{args.fname}' not found.")


if __name__ == '__main__':
    search_word_in_file()
