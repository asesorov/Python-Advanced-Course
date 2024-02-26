import sys
import argparse


def process_lines(input_stream, line_number=1):
    for line in input_stream:
        yield f"{line_number}\t{line}"
        line_number += 1


def cli_argument_parser():
    parser = argparse.ArgumentParser(description='Numerate strings')

    parser.add_argument('file',
                        help='Path to input file',
                        nargs='?',
                        type=argparse.FileType('r'),
                        default=sys.stdin)
    args = parser.parse_args()

    return args


def main():
    args = cli_argument_parser()
    try:
        for numbered_line in process_lines(args.file):
            sys.stdout.write(numbered_line)
        print()
    except KeyboardInterrupt:
        return 0
    except Exception as e:
        print(f"An error occurred: {e}\n")
        return 1
    finally:
        if args.file is not sys.stdin:
            args.file.close()


if __name__ == '__main__':
    sys.exit(main() or 0)
