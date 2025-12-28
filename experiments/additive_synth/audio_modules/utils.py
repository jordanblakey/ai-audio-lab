import numpy as np

def sum_waveforms(wl: list[np.ndarray[np.float64]]) -> np.ndarray[np.float64]:
    max_length = max(map(len, wl))
    for i in range(len(wl)):
        wl[i] = np.pad(wl[i], (0, max_length - len(wl[i])))
    s = sum(wl)
    if np.max(s) > 1.0:
        s = s / np.max(s)
    return s