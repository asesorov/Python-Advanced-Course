import sys
import argparse

def cli_argument_parser():
    parser = argparse.ArgumentParser(description='Display word, line, and byte counts for each file.')

    parser.add_argument('files',
                        nargs='*',
                        help='Path(s) to input file(s)',
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    return parser.parse_args()

def wc(file_obj):
    num_lines = 0
    num_words = 0
    num_bytes = 0

    for line in file_obj:
        num_lines += 1
        num_words += len(line.split())
        num_bytes += len(line.encode('utf-8'))

    return num_lines, num_words, num_bytes

def main():
    args = cli_argument_parser()
    total_lines = 0
    total_words = 0
    total_bytes = 0

    if not args.files or args.files == [sys.stdin]:
        lines, words, bytes_ = wc(sys.stdin)
        print(f"{lines} {words} {bytes_}")
    else:
        for file_obj in args.files:
            lines, words, bytes_ = wc(file_obj)
            total_lines += lines
            total_words += words
            total_bytes += bytes_
            print(f"{lines} {words} {bytes_} {file_obj.name}")

    if len(args.files) > 1:
        print(f"{total_lines} {total_words} {total_bytes} total")

if __name__ == '__main__':
    sys.exit(main() or 0)
