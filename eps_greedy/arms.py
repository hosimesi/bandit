
from numpy.random import binomial

class Arm:
    def __init__(self, p: float) -> None:
        self.succeed = 0
        self.failed = 0
        self.p = p

    def selected(self) -> int:
        reward = binomial(n=1, p=self.p)
        if reward == 1:
            self.succeed += 1
        else:
            self.failed += 1

        return reward
