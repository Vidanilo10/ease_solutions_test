 
class FinderPathHandler:
    def __init__(self) -> None:
        pass

    def Handler(i, j, matrix) -> None:
        print(i)
        print(j)
        new_matrix = [[int(c) for c in line.split(" ")] for line in matrix]
        print(new_matrix)