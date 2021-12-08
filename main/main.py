import argparse
from finder_path import FinderPathHandler


class HandleArgs:
    def __init__(self) -> None:
        pass
    
    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--path", help="Input path file", nargs="?", default="4x4.txt"
        )
        args = parser.parse_args()
        return args


class Main(HandleArgs):
    
    def __init__(self) -> None:
        pass


    def main(self) -> None:
        with open(self.get_args().path, "r") as f:
            i, j = f.readline().strip().split(" ")
            matrix = [line.strip() for line in f.readlines()]
            FinderPathHandler.Handler(i, j, matrix)

if __name__ == "__main__":
    Main().main()
