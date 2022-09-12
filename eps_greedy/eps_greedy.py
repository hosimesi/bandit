from typing import List

from numpy.random import binomial, randint

from arms import Arm


def calc_success_rate(arm: Arm) -> float:
    trial = arm.succeed + arm.failed
    if trial == 0:
        return 0
    return arm.succeed / trial


def eps_greedy(arms: List[Arm], eps: float) -> int:
    reward = 0
    for _ in range(500):
        search = binomial(n=1, p=eps)
        if search == 1:
            index = randint(0, 4)
        else:
            history = [calc_success_rate(arm) for arm in arms]
            index = history.index(max(history))
        reward += arms[index].selected()
    return reward


def main():
    arms = [Arm(p=0.2), Arm(p=0.2), Arm(p=0.1), Arm(p=0.3), Arm(p=0.5)]
    eps = 0.2
    reward = eps_greedy(arms=arms, eps=eps)
    print(reward)


if __name__ == "__main__":
    main()
