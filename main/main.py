import argparse
from finder_path import PathHandler


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
        try:
            file = open(self.get_args().path, "r").readlines()
        except FileNotFoundError:
            print(f'{str(FileNotFoundError)}')
        finally:
            first_line = file.pop(0)
            i, j = first_line.strip().split(" ")
            first = [line.strip().split(" ") for line in file]            
            flatten_matrix = [int(val) for sublist in first for val in sublist]
            data = {'x': i, 'y': j, 'matrix': flatten_matrix}
            PathHandler.Handler(data=data)


if __name__ == "__main__":
    Main().main()
