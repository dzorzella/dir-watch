import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='dir-watch',
        description='Monitor and detect directory changes',
        epilog='Made with love by Zorzella Davide')
    
    parser.add_argument('-d', '--directory')
    args = parser.parse_args()
    print(args.directory)

    # command to start from: tree -J -o $(date '+%Y-%m-%d_%H:%M:%S')