from note_dict import note_dict
from key_dict import key_dict
import numpy as np

class Chord:

    @staticmethod
    def is_possible(chord):
        # Each interval represents the established vocal range for each voice. Also, the Tenor, Contra Alto
        # and Soprano must be at most an octave apart
        if 17 <= chord[0] <= 37 and chord[0] <= chord[1]:
            if 24 <= chord[1] <= 44 and chord[1] <= chord[2]:
                if 30 <= chord[2] <= 51 and chord[2] <= chord[3] and (chord[2] - chord[1]) <= 12:
                    if 37 <= chord[3] <= 58 and (chord[3] - chord[2]) <= 12:
                        return True
        else:
            return False

    @staticmethod
    def choices(base):
        options = []
        for n in range(0, 5):
            baix = base + 12 * n
            options.append(baix)
        return options

    @staticmethod
    def generate(base):
        chords = []
        positions = [base + 4, base + 7, base + 12]

        tenors = []
        contralts = []
        sopranos = []

        for position in positions:
            tenors += Chord.choices(position)
        for position in positions:
            contralts += Chord.choices(position)
        for position in positions:
            sopranos += Chord.choices(position)

        for tenor in tenors:
            for contralt in contralts:
                for soprano in sopranos:
                    if Chord.is_possible([base, tenor, contralt, soprano]):
                        chord = [base, tenor, contralt, soprano]
                        if len([tenor % 12, contralt % 12, soprano % 12]) == len(set([tenor % 12, contralt % 12, soprano % 12])):
                            chords.append(np.array(chord))

        return chords

    @staticmethod
    def to_musical_notation(chord):
        notated = []
        for voice in chord:
            notated.append(key_dict[voice])
        return notated
