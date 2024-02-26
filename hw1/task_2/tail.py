import sys
import argparse

def cli_argument_parser():
    parser = argparse.ArgumentParser(description='Display the last part of each file to stdout.')

    parser.add_argument('files',
                        nargs='*',
                        help='Path(s) to input file(s)',
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    return parser.parse_args()

def tail(file_obj, lines=10):
    all_lines = file_obj.readlines()
    for line in all_lines[-lines:]:
        sys.stdout.write(line)

def main():
    args = cli_argument_parser()

    if not args.files or args.files == [sys.stdin]:
        tail(sys.stdin, 17)
    else:
        for i, file_obj in enumerate(args.files):
            if i > 0:
                sys.stdout.write('\n')
            if len(args.files) > 1:
                sys.stdout.write(f"==> {file_obj.name} <==\n")
            tail(file_obj)
            file_obj.close()
    print()

if __name__ == '__main__':
    sys.exit(main() or 0)
