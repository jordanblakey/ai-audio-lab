from typing import Callable, Literal
import numpy as np

# https://easings.net/

# Type for easing function: takes a float or numpy array (0-1) and returns same
EasingFunc = Callable[[float | np.ndarray], float | np.ndarray]

def linear(x):
    return x

def easeInSine(x):
    return 1 - np.cos((x * np.pi) / 2)

def easeOutSine(x):
    return np.sin((x * np.pi) / 2)

def easeInOutSine(x):
    return -(np.cos(np.pi * x) - 1) / 2

def easeInQuad(x):
    return x * x

def easeOutQuad(x):
    return 1 - (1 - x) * (1 - x)

def easeInOutQuad(x):
    return np.where(x < 0.5, 2 * x * x, 1 - np.power(-2 * x + 2, 2) / 2)

def easeInCubic(x):
    return x * x * x

def easeOutCubic(x):
    return 1 - np.power(1 - x, 3)

def easeInOutCubic(x):
    return np.where(x < 0.5, 4 * x * x * x, 1 - np.power(-2 * x + 2, 3) / 2)

def easeInQuart(x):
    return x * x * x * x

def easeOutQuart(x):
    return 1 - np.power(1 - x, 4)

def easeInOutQuart(x):
    return np.where(x < 0.5, 8 * x * x * x * x, 1 - np.power(-2 * x + 2, 4) / 2)

def easeInQuint(x):
    return x * x * x * x * x

def easeOutQuint(x):
    return 1 - np.power(1 - x, 5)

def easeInOutQuint(x):
    return np.where(x < 0.5, 16 * x * x * x * x * x, 1 - np.power(-2 * x + 2, 5) / 2)

def easeInExpo(x):
    return np.where(x == 0, 0, np.power(2, 10 * x - 10))

def easeOutExpo(x):
    return np.where(x == 1, 1, 1 - np.power(2, -10 * x))

def easeInOutExpo(x):
    cond1 = x == 0
    cond2 = x == 1
    cond3 = x < 0.5
    
    # We need to be careful with handling array vs scalar here if we use pure where logic deeply nested
    # But since these are element-wise operations on numpy arrays, np.where works fine.
    
    res = np.where(cond3, np.power(2, 20 * x - 10) / 2, (2 - np.power(2, -20 * x + 10)) / 2)
    res = np.where(cond2, 1, res)
    res = np.where(cond1, 0, res)
    
    return res

EASINGS = {
    "linear": linear,
    "easeInSine": easeInSine,
    "easeOutSine": easeOutSine,
    "easeInOutSine": easeInOutSine,
    "easeInQuad": easeInQuad,
    "easeOutQuad": easeOutQuad,
    "easeInOutQuad": easeInOutQuad,
    "easeInCubic": easeInCubic,
    "easeOutCubic": easeOutCubic,
    "easeInOutCubic": easeInOutCubic,
    "easeInQuart": easeInQuart,
    "easeOutQuart": easeOutQuart,
    "easeInOutQuart": easeInOutQuart,
    "easeInQuint": easeInQuint,
    "easeOutQuint": easeOutQuint,
    "easeInOutQuint": easeInOutQuint,
    "easeInExpo": easeInExpo,
    "easeOutExpo": easeOutExpo,
    "easeInOutExpo": easeInOutExpo,
}

EasingType = Literal[
    "linear",
    "easeInSine", "easeOutSine", "easeInOutSine",
    "easeInQuad", "easeOutQuad", "easeInOutQuad",
    "easeInCubic", "easeOutCubic", "easeInOutCubic",
    "easeInQuart", "easeOutQuart", "easeInOutQuart",
    "easeInQuint", "easeOutQuint", "easeInOutQuint",
    "easeInExpo", "easeOutExpo", "easeInOutExpo",
]
