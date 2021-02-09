class DoseModificationFactor:
    def __init__(self, max_oer, k_mmHg) -> None:
        super().__init__()
        self.k_mmHg = k_mmHg
        self.max_oer = max_oer

    def calculate(self, po2):
        return self.max_oer * (self.k_mmHg + po2) / (self.k_mmHg + self.max_oer * po2)
