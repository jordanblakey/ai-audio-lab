import time

import numpy as np
import scipy.signal
import pyaudio

from audio_modules import narrate, Wave, Audio
from audio_modules.effects import amplitude_envelope 

with Audio() as a:
    narrate("This is a 440 hertz sine wave.")
    a.buffer.append(Wave(hz=440, amp=1.0, duration=1).sine())
    a.play_buffer()
    time.sleep(1)
    
    narrate("Now, let's try a square wave.")
    a.buffer.append(Wave(hz=440, amp=1.0, duration=1).square())
    a.play_buffer()
    time.sleep(1)

    narrate("We can also generate the samples for triangle and sawtooth waves with numpy.")
    a.buffer.append(Wave(hz=440, amp=1.0, duration=1).triangle())
    a.buffer.append(np.zeros(int(48000 / 2)))
    a.buffer.append(Wave(hz=440, amp=1.0, duration=1).sawtooth())
    a.play_buffer()
    time.sleep(1)

    narrate("Using simple math functions can create chirp effects, known as aliasing. Here's an example with a square wave.")
    a.buffer.append(Wave(hz=440).aliased_square())    
    a.play_buffer()
    time.sleep(1)
    
    narrate("To prevent aliasing, we can use a process called additive synthesis. Here's a square wave generated with additive synthesis.")
    a.buffer.append(Wave(hz=440, amp=1.0, duration=1).square())
    a.play_buffer()
    time.sleep(1)
    
    narrate("Notice how the square wave sounded much smoother?")