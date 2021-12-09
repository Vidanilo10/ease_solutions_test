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

        """
        for b in range(int(data['y'])):
            for a in range(int(data['x'])):
                print(self.G[self.tuple(a, b)])
        """
        return self.G
        
class PathHandler:
    def __init__(self) -> None:
        pass

    def Handler(data: Dict):
        # Instance section
        graph_instance = Graph()
        peak_instance = Peaks()
        bottom_instance = Bottom()
        path_instance = Path()

        # Logic section
        graph = graph_instance.build_graph(data=data)
        peak = peak_instance.find_peak(G=graph)
        bottom = bottom_instance.find_bottom(G=graph)
        
        N = {}
        for area in graph:
            N[area] = Neighbors().find_neighbors(graph, area)
            #print(area, N[area])
        
        for area in graph:
            print(area, graph[area], peak_instance.find_next_peak(N, graph, area))
        

        print(" ")
        print("------------------------------------------")
        print("Path")
        P = {}
        P[peak] = graph[peak]
        path = [peak]
        path_instance.find_path(N, graph, path, bottom, peak, peak_instance)
        print(path)
        return path
        print(" ")
        print("------------------------------------------")

class Peaks:
    def __init__(self) -> None:
        self.maxpt = 0

    def find_peak(self, G):
        for coord in G:
            if G[coord] > self.maxpt:
                self.maxpt = G[coord]
                maxcoord = coord
        return maxcoord        

    def find_next_peak(self, N, G, peak):
        next_peak = None
        next_peak_val = None
        for n in N[peak]:
            if N[peak][n] < G[peak]:
                if N[peak][n]:
                    next_peak = n
                    next_peak_val = N[peak][n]
        return next_peak, next_peak_val


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

class Neighbors:
    def __init__(self) -> None:
        pass
    
    def get_tuple(self, tuple_xy):
        x, y = tuple_xy
        return x, y

    def find_neighbors(self, G, peak):
        neighbors = {}
        x, y = self.get_tuple(peak)
        N = x, y-1
        S = x, y+1
        E = x+1, y
        W = x-1, y
        directions = [N, E, S, W]
        for d in directions:
            if d in G:
                if d != peak:
                    neighbors[d] = G[d]
        
        return neighbors


class Path:
    def __init__(self) -> None:
        pass

    def find_path(self, N, G, path, bottom, peak, peak_instance):
        if peak == bottom:
            return path
        next_peak, val = peak_instance.find_next_peak(N, G, peak)
        print(next_peak, val)
        if not next_peak == None:
            path.append(next_peak)
        else:
            return path
        return self.find_path(N, G, path, bottom, next_peak, peak_instance)


if __name__ == "__main__":
    PathHandler().Handler()
