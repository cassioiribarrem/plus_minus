class plusMinus():
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

    def positive_numbers(self):
        i = positives = 0
        for i in range(0, self.n):
            if self.arr[i] > 0:
                positives += 1
        return positives

    def negative_numbers(self):
        i = negatives = 0
        for i in range(0, self.n):
            if self.arr[i] < 0:
                negatives += 1
        return negatives

    def nule_numbers(self):
        i = nules = 0
        for i in range(0, self.n):
            if self.arr[i] == 0:
                nules += 1
        return nules

    def ratios(self):
        positive_ratio = self.positive_numbers() / self.n
        negative_ratio = self.negative_numbers() / self.n
        nule_ratio = self.nule_numbers() / self.n

        print(f'{positive_ratio:.6f}')
        print(f'{negative_ratio:.6f}')
        print(f'{nule_ratio:.6f}')
        return positive_ratio, negative_ratio, nule_ratio