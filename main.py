from note_dict import note_dict
from chord import Chord
import numpy as np
from optimitzation import Optimization
import time

bases = []
bases_chords = []
c = Chord()
o = Optimization()
print("Introduce your inputs: (Write return to delete previous note)")
print("                       (Write exit to finish)")
print("")

# Listen for the inputs
while True:
    base = input("")
    if base == "exit":
        break
    if base == "return":
        if not bases:
            print("No previous inputs found")
        else:
            bases.pop()
            print("Current inputs:", bases)
        continue
    if base in note_dict:
        bases.append(note_dict[base])
    else:
        print("Not recognized")


print(bases)

# Process the chords
for base in bases:
    bases_chords.append(c.generate(base))

time_start = time.perf_counter()
# Optimize and find the best route
#best_option = o.brute_force(bases_chords)
best_option = o.shortest_path(bases_chords)

time_elapsed = (time.perf_counter() - time_start)

# Convert back the chords to musical notation
clean_chords = []
for x in range(len(best_option)):
    clean_chords.append(c.to_musical_notation(best_option[x]))

print(clean_chords)
print(time_elapsed)
