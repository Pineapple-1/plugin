import argparse

def print_arguments(arguments):
    for argument in arguments:
        print(argument)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filenames", type=str, nargs="*")
    args = parser.parse_args()

    print_arguments(args.filenames)


if __name__ == "__main__":
    main()