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
        peak = Peaks().find_peak(G=graph)
        bottom = Bottom().find_bottom(G=graph)
        

class Peaks:
    def __init__(self) -> None:
        self.maxpt = 0

    def find_peak(self, G):
        for coord in G:
            if G[coord] > self.maxpt:
                self.maxpt = G[coord]
                maxcoord = coord
        return maxcoord        

class Bottom:
    def __init__(self) -> None:
        self.mincoord = 0, 0

    def find_bottom(self, G):
        minpt = G[0, 0]
        
        for coord in G:
            if G[coord] < minpt:
                minpt = G[coord]
                self.mincoord = coord

        return self.mincoord


if __name__ == "__main__":
    PathHandler().Handler()
