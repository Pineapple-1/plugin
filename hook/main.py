import argparse
import os 


def print_arguments(arguments):
    for argument in arguments:
        print(argument)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    MIGRATION_DIR = args.path
    filenames = os.listdir(MIGRATION_DIR)
    filenames.remove('__init__.py')
    checklist = []

    for filename in filenames:
        arr = filename.split("_")
        checklist.append(arr[0])
    

    if len(set(checklist)) == len(checklist):
        pass
    else:
        raise ValueError("Duplicates In Migrations .")
        





if __name__ == "__main__":
    main()