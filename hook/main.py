import argparse
import os
import logging
from typing import Optional, Sequence


logger = logging.getLogger()

def main(argv: Optional(Sequence[str])):
    logger.info(argv)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--path",dest='migration_dir',action="store")
    args = parser.parse_args()
    
    MIGRATION_DIR = args.migration_dir
    filenames = os.listdir(MIGRATION_DIR)
    filenames.remove('__init__.py')
    checklist = []
    for filename in filenames:
        arr = filename.split("_")
        checklist.append(arr[0])
    

    if len(set(checklist)) == len(checklist):
        print(checklist)
    else:
        raise ValueError("Duplicates In Migrations .")
    


if __name__ == "__main__":
    raise SystemExit(main())
