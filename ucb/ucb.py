import math
from typing import List

from numpy.random import randint

from arms import Arm


def calc_success_rate(arm: Arm) -> float:
    trial = arm.succeed + arm.failed
    if trial == 0:
        return 0
    return arm.succeed / trial


def calc_score(arm: Arm, k: int) -> float:
    bonus = math.sqrt(2 * math.log(k) / (arm.succeed + arm.failed))
    return calc_success_rate(arm) + bonus


def ucb(arms: List[Arm]) -> int:
    reward = 0
    for i in range(1, 501):
        if i == 1:
            index = randint(0, 4)
        else:
            history = [calc_score(arm=arm, k=i) for arm in arms]
            index = history.index(max(history))
        reward += arms[index].selected()
    return reward


def main():
    arms = [Arm(p=0.2), Arm(p=0.2), Arm(p=0.1), Arm(p=0.3), Arm(p=0.5)]
    reward = ucb(arms=arms)
    print(reward)


if __name__ == "__main__":
    main()
