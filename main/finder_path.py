class PathHandler:
    def __init__(self) -> None:
        pass

    def Handler(i, j, matrix) -> None:
        new_matrix = [[int(c) for c in line.split(" ")] for line in matrix]
        print(new_matrix)