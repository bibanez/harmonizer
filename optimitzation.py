import numpy as np
from itertools import product

class Optimization:

    # Discrete method. Computation time rises exponentially, so it's very slow for
    # more than 5 or 6 chords.
    @staticmethod
    def brute_force(chords):
        possibilities = []

        for a in product(*chords):
            possibilities.append(a)

        best_option = []
        best_sum = 1000

        for x in range(len(possibilities)):
            temp_sum = 0
            for y in range(len(possibilities[x]) - 1):
                difference = abs(np.sum(possibilities[x][y] - possibilities[x][y+1]))
                temp_sum += difference
            if temp_sum < best_sum:
                best_option = possibilities[x]
                best_sum = temp_sum

        return best_option

    # Loosely based on the Dijsktra algorithm, always takes the shortest path. It's
    # very fast but not the most accurate.
    @staticmethod
    def shortest_path(chords):
        path = []
        if len(chords) >= 2:
            path.append(Optimization.brute_force(chords[:1])[0].tolist())
            while len(path) < len(chords):
                sum = 1000
                temp_chord = []
                for chord in chords[len(path)]:
                    difference = abs(np.sum(chord - path[-1]))
                    if difference < sum:
                        sum = difference
                        temp_chord = chord
                path.append(temp_chord)
            for x in range(len(path)):
                if type(path[x]) == np.ndarray:
                    path[x] = path[x].tolist()
            return path
        else:
            return chords
