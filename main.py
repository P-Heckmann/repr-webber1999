import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.special

YEAR_IN_SECONDS = 365.25 * 24 * 60 * 60  # s, seconds in a year
DYKE_THICKNESS = 25  # m, thickness
T_MAGMA = 850  # C, initial magma temperature
T_COUNTRY_ROCK = 450  # C, country rock temperature
KAPPA = 1.66e-7  # m2/s, thermal diffusivity
# x = range(1, 100)  # m, distance
t1 = 15 * YEAR_IN_SECONDS  # s, seconds in 15 years
t2 = 30 * YEAR_IN_SECONDS  # s, seconds in 30 years
t_list = [
    0.5 * YEAR_IN_SECONDS,
    2 * YEAR_IN_SECONDS,
    7 * YEAR_IN_SECONDS,
    15 * YEAR_IN_SECONDS,
    30 * YEAR_IN_SECONDS,
]


def erf(y: float) -> float:
    a1 = 0.34802
    a2 = -0.09587
    a3 = 0.74785
    return 1 - (a1 * gamma(y) + a2 * gamma(y) ** 2 + a3 * gamma(y) ** 3) * math.exp(
        -(y ** 2)
    )


def gamma(y: float) -> float:
    return 1 / (1 + 0.47047 * y)


def temperature_value(distance: float, time: float) -> float:
    part1 = erf(
        (distance / DYKE_THICKNESS + 1)
        / (2 * math.sqrt(KAPPA * time / DYKE_THICKNESS ** 2))
    )
    part2 = erf(
        (distance / DYKE_THICKNESS - 1)
        / (2 * (math.sqrt(KAPPA * time / DYKE_THICKNESS ** 2)))
    )
    return 0.5 * (part1 - part2)


def temperature_curve(distances: list[float], time: float) -> list[float]:
    return [temperature_value(distance, time) for distance in distances]


if __name__ == "__main__":
    distances = np.arange(-200, 200, 0.1)
    temperatures = np.array(temperature_curve(distances, 2 * YEAR_IN_SECONDS))

    plt.plot(distances, temperatures - T_MAGMA)
    plt.show()
