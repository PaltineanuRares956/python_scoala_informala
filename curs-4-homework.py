class Fractie(object):

    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, other):
        if not isinstance(other, Fractie):
            return None

        if other.get_numitor() == self.numitor:
            new_fractie = Fractie(self.numarator + other.get_numarator(), self.numitor)
        else:
            new_numarator = self.numarator * other.get_numitor() + other.get_numarator() * self.numitor
            new_numitor = self.numitor * other.get_numitor()
            new_fractie = Fractie(new_numarator, new_numitor)

        return new_fractie

    def __sub__(self, other):
        if not isinstance(other, Fractie):
            return None

        if other.get_numitor() == self.numitor:
            new_fractie = Fractie(self.numarator - other.get_numarator(), self.numitor)
        else:
            new_numarator = self.numarator * other.get_numitor() - other.get_numarator() * self.numitor
            new_numitor = self.numitor * other.get_numitor()
            new_fractie = Fractie(new_numarator, new_numitor)

        return new_fractie

    def inverse(self):
        return Fractie(self.numitor, self.numarator)

    def set_numarator(self, new_numarator):
        self.numarator = new_numarator

    def get_numarator(self):
        return self.numarator

    def set_numitor(self, new_numitor):
        self.numitor = new_numitor

    def get_numitor(self):
        return self.numitor

fr1 = Fractie(1,2)
fr2 = Fractie(1,3)

fr3 = fr1 - fr2
print(fr3)
print(fr3.inverse())