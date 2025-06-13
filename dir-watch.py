#!/bin/python3
import argparse
import os
import datetime
import sys

SNAPSHOTS = 'snapshots/'

def directory(dir):
    counter = 0 # does not need to test all of the files for now, only a small dataset 
    filename=os.path.join(SNAPSHOTS, str(datetime.datetime.now()))
    out=[]
    with open(filename, 'w') as snapshot:
        for dirpath, subfolders, files in os.walk(dir):
            for f in files:
                counter=counter+1
                if counter >= 10:
                    sys.exit(0)
                snapshot.write(f'{os.path.join(dirpath,f)}\n')

    # return filename

def compare(dir):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='dir-watch',
        description='Monitor and detect directory changes',
        epilog='Made with love by Zorzella Davide')

    parser.add_argument('-d', '--directory', type=str, required=True)
    parser.add_argument('-c', '--compare', action="store_true")
    args = parser.parse_args()

    if args.compare:
        compare(directory(args.directory))
    elif args.directory:
        directory(args.directory)