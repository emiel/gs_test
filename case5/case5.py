"""
Write a function that examines the barcode pairs of each sample in a given json
of the above structure and returns false if any of the barcode pairs in one
sample are the same as any of the barcode pairs in another sample. Barcode
pairs are considered the same if both parts of the barcodes are the same or if
one part or both parts of the barcode pair differ by only one base (character)
from the same part of the barcode pair in another sample. (max 30 lines)
"""
import json


def _ndiff(a, b):
    diff = 0
    for i in range(8):
        if a[i] != b[i]:
            diff += 1
    return diff


class Pair:
    def __init__(self, fst, snd):
        self.fst = fst
        self.snd = snd
        assert len(fst) == 8 and len(snd) == 8

    def __str__(self):
        return "{},{}".format(self.fst, self.snd)

    def __eq__(self, other):
        if self.fst == other.fst and self.snd == other.snd:
            return True

        if _ndiff(self.fst, other.fst) <= 1 or _ndiff(self.snd, other.snd) <= 1:
            return True

        return False


class Sample:
    def __init__(self, name, sequences):
        self.name = name
        self.sequences = sequences


class Runner:
    def __init__(self, filename="case5.json"):
        with open(filename) as file:
            self.data = json.load(file)

    def valid(self):
        sample_0 = self.data["0"]
        sample_1 = self.data["1"]

        for seq0 in sample_0["index_sequences"]:
            pair0 = Pair(seq0[0], seq0[1])

            for seq1 in sample_1["index_sequences"]:
                pair1 = Pair(seq1[0], seq1[1])
                print("- pair0: {}".format(pair0))
                print("- pair1: {}".format(pair1))

                if pair0 == pair1:
                    print("  => Pair is equal!")
                    return False

        return True


if __name__ == "__main__":
    runner = Runner()
    if not runner.valid():
        print("Samples include an equal barcode pair")
    else:
        print("Samples are ok")
