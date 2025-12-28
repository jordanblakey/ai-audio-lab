import time
from audio_modules import narrate, Audio, Noise

with Audio() as a:
    narrate("Let's talk about noise.")

    narrate("White noise has a flat frequency spectrum, meaning it contains all audible frequencies with equal sound power. It sounds like constant TV static or a fan's hum.")
    time.sleep(.1)
    a.buffer.append(Noise(amp=0.20, duration=5.0).white())
    a.play_buffer()
    time.sleep(1)

    narrate("Pink noise, or one-over-f noise, has a -3db decrease in sound power per octave, making it sound like steady rain or rustling leaves.")
    time.sleep(.1)
    a.buffer.append(Noise(amp=0.5, duration=5.0).pink())
    a.play_buffer()
    time.sleep(1)

    narrate("Brown noise, also known as Brownian or red noise, has a -6db decrease in sound power per octave, emphasizing low frequencies, creating a deep rumble like a distant thunderstorm or a growling engine.")
    time.sleep(.1)
    a.buffer.append(Noise(amp=1.0, duration=5.0).brown())
    a.play_buffer()
    time.sleep(1)

    narrate("Blue noise is the opposite of pink noise; It has a +3db increase in sound power per octave. This creates a sharp hiss, similar to the sound of a high-pressure water spray.")
    time.sleep(.1)
    a.buffer.append(Noise(amp=1.0, duration=5.0).blue())
    a.play_buffer()
    time.sleep(1)

    narrate("Violet noise is the opposite of brown noise, with a +6db increase in sound power per octave. It is the highest-pitched color, sounding like intense, shrill static.")
    time.sleep(.1)
    a.buffer.append(Noise(amp=1.0, duration=5.0).violet())
    a.play_buffer()
    time.sleep(1)