from typing import List

from numpy.random import beta

from arms import Arm


def tompson_sampling(arms: List[Arm]) -> int:
    reward = 0
    for _ in range(1, 501):
        history = [beta(a=arm.succeed, b=arm.failed) for arm in arms]
        index = history.index(max(history))
        reward += arms[index].selected()
    return reward


def main():
    arms = [Arm(p=0.2), Arm(p=0.2), Arm(p=0.1), Arm(p=0.3), Arm(p=0.5)]
    reward = tompson_sampling(arms=arms)
    print(reward)


if __name__ == "__main__":
    main()
