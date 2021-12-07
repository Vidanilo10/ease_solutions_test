import argparse
from finder_path import FinderPath


class EaseTest:
    def __init__(self) -> None:
        pass

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--path", help="Input path file", nargs="?", default="4x4.txt"
        )
        args = parser.parse_args()
        return args

    def main(self) -> None:
        with open(self.get_args().path, "r") as f:
            i, j = f.readline().strip().split(" ")
            matrix = f.readlines()
            FinderPath.find_longest_path(i, j, matrix)


if __name__ == "__main__":
    EaseTest().main()
