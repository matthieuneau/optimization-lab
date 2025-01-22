import numpy as np


def exp_strategy(N: float, Tmin: float = 1, Tmax: float = 1000) -> np.ndarray:
    n = np.arange(1, N + 1)
    T = Tmin * np.exp((-(n - 1) * np.log(Tmin / Tmax)) / (N - 1))
    return T


if __name__ == "__main__":
    T_min = 1
    T_max = 1000
    N = 100
    T = exp_strategy(N, T_min, T_max)
    print(T)
