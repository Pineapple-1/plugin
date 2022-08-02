import argparse
import os
from typing import Sequence



def main(argv: Sequence[str] | None = None):
    # parser = argparse.ArgumentParser()
    # parser.add_argument("path")
    # args = parser.parse_args()
    # MIGRATION_DIR = args.path
    # filenames = os.listdir(MIGRATION_DIR)
    # filenames.remove('__init__.py')
    # checklist = []
    # for filename in filenames:
    #     arr = filename.split("_")
    #     checklist.append(arr[0])
    

    # if len(set(checklist)) == len(checklist):
    #     pass
    # else:
    #     raise ValueError("Duplicates In Migrations .")
    
    print(argv)

        





if __name__ == "__main__":
    raise SystemExit(main())
