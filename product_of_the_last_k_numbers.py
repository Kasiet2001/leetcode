class ProductOfNumbers:

    def __init__(self):
        self.preff_prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.preff_prod = [1]
        else:
            prod = self.preff_prod[-1] * num
            self.preff_prod.append(prod)

    def getProduct(self, k: int) -> int:
        if k >= len(self.preff_prod):
            return 0
        return self.preff_prod[-1] // self.preff_prod[-k - 1]