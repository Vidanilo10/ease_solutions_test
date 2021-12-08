from typing import Any, Dict, Tuple


class Graph():
    def __init__(self) -> None:
        self.G: Dict = {}

    def tuple(self, x: int, y: int):
        return x, y

    def build_graph(self, data):
        for b in range(int(data['y'])):
            for a in range(int(data['x'])):
                self.G[self.tuple(a, b)] = data['matrix'].pop(0)

        for b in range(int(data['y'])):
            for a in range(int(data['x'])):
                print(self.G[self.tuple(a, b)])
        return self.G

class PathHandler:
    def __init__(self) -> None:
        pass

    def Handler(data: Dict):
        graph = Graph().build_graph(data=data)
        print(graph)

if __name__ == "__main__":
    PathHandler().Handler()
