class Fractie:

    def __init__(self, numarator, numitor):
        self.numitor = numitor
        self.numarator = numarator

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, frac1):
        numitor = self.numitor * frac1.numitor
        numarator = self.numarator * frac1.numitor + self.numitor * frac1.numarator
        return Fractie(numarator, numitor)

    def __sub__(self, frac1):
        numitor = self.numitor * frac1.numitor
        numarator = self.numarator * frac1.numitor - self.numitor * frac1.numarator
        return Fractie(numarator, numitor)

    def inverse(self):
        return Fractie(numarator=self.numitor, numitor= self.numarator)


frac2 = Fractie(1, 2)

print(frac2)