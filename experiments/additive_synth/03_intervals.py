import time

import numpy as np
import scipy.signal

from audio_modules import narrate, Wave, Audio

with Audio() as a:
    narrate("This is a 440 hertz sine wave.")
    w1 = Wave(hz=440, amp=1.0, duration=1).sine()
    a.buffer.append(w1)
    a.play_buffer()
    time.sleep(1)
    
    narrate("Now, let's resample it to a higher pitch. This basically squashes the waveform horizontally, making it shorter.")
    interval_ratio = 2**(4/12)  # Major third ratio
    a.buffer.append(scipy.signal.resample(w1, int(len(w1) / interval_ratio)))
    a.play_buffer()
    time.sleep(1)

    narrate("This particular musical interval, or ratio between 2 frequencies, is called a major third.")
    narrate("Let's hear them together.")
    a.buffer.append(Wave(hz=440, amp=1.0, duration=1).sine())
    a.buffer.append(Wave(hz=440 * 2 ** (4/12), amp=1.0, duration=1).sine())
    a.play_buffer()
    time.sleep(1)

    interval_names = [
        "unison",
        "minor 2nd",
        "major 2nd",
        "minor 3rd",
        "major 3rd",
        "perfect 4th",
        "tritone",
        "perfect 5th",
        "minor 6th",
        "major 6th",
        "minor 7th",
        "major 7th",
        "octave"
    ]
    narrate(f"There are 12 of these intervals in an octave.")
    narrate("Let's hear them.")
    for i, interval_name in enumerate(interval_names):
        narrate(f"{interval_name}")
        a.buffer.append(Wave(hz=440, duration=.5).sine())
        a.buffer.append(np.zeros(int(100)))
        a.buffer.append(Wave(hz=int(440 * 2 ** (i/12)), duration=.5).sine())
        a.play_buffer()
        time.sleep(.1)

    narrate("Combining intervals in a sequence creates a melody.")
    narrate("Perhaps you will recognize this one.")

    a.buffer.append(Wave(hz=int(440* 2 ** (0/12)), amp=1.0, duration=0.30).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440* 2 ** (0/12)), amp=1.0, duration=0.15).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (5/12)), amp=1.0, duration=1.0).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (12/12)), amp=1.0, duration=1.0).triangle())

    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (10/12)), amp=1.0, duration=0.15).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (9/12)), amp=1.0, duration=0.15).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (7/12)), amp=1.0, duration=0.15).triangle())

    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (17/12)), amp=1.0, duration=1.0).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (12/12)), amp=1.0, duration=0.5).triangle())

    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (10/12)), amp=1.0, duration=0.15).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (9/12)), amp=1.0, duration=0.15).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (7/12)), amp=1.0, duration=0.15).triangle())

    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (17/12)), amp=1.0, duration=1.0).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (12/12)), amp=1.0, duration=0.5).triangle())

    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (10/12)), amp=1.0, duration=0.15).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (9/12)), amp=1.0, duration=0.15).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (10/12)), amp=1.0, duration=0.15).triangle())
    a.buffer.append(np.zeros(int(500)))
    a.buffer.append(Wave(hz=int(440 * 2 ** (7/12)), amp=1.0, duration=1.00).triangle())

    a.play_buffer()