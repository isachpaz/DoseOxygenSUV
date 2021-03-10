class PO2:
    def __init__(self, A, B, C) -> None:
        super().__init__()
        self.C = C
        self.B = B
        self.A = A

    def calculate_from_uptake(self, uptake):
        return self.C * (self.A - uptake) / (self.B - self.A + uptake)

    def calculate_uptake_from_po2(self, po2):
        return self.A - (self.B*po2 / (self.C + po2))

    def __repr__(self) -> str:
        return f"A={self.A}, B={self.B}, C={self.C}"

