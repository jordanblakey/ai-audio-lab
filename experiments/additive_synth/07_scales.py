from audio_modules import Audio, narrate, theory_ji
import time

with Audio() as a:

    narrate("Let's explore sequences of musical intervals, called scales.")

    narrate("To start, let's hear a chromatic scale. You may notice it contains all 12 intervals.")
    theory_ji.play_scale(theory_ji.chromatic_scale(440), wave_type='sine', duration=0.30)
    time.sleep(0.5)
    theory_ji.play_scale(theory_ji.chromatic_scale(440), wave_type='sine', duration=0.30, ascending=False)
    time.sleep(0.5)

    narrate("This is a pentatonic scale. It's the foundation of blues and rock music.")
    theory_ji.play_scale(theory_ji.pentatonic_scale(440), wave_type='sine', duration=0.30)
    time.sleep(0.5)
    theory_ji.play_scale(theory_ji.pentatonic_scale(440), wave_type='sine', duration=0.30, ascending=False)
    time.sleep(0.5)

    narrate("Now let's explore the diatonic modes—the building blocks of Western music theory.")

    narrate("This is the Ionian mode. You probably recognize it as the standard Major scale.")
    theory_ji.play_scale(theory_ji.ionian_scale(440), wave_type='sine', duration=0.30)
    time.sleep(0.5)
    theory_ji.play_scale(theory_ji.ionian_scale(440), wave_type='sine', duration=0.30, ascending=False)
    time.sleep(0.5)

    narrate("This is the Dorian mode.")
    theory_ji.play_scale(theory_ji.dorian_scale(440), wave_type='sine', duration=0.30)
    time.sleep(0.5)
    theory_ji.play_scale(theory_ji.dorian_scale(440), wave_type='sine', duration=0.30, ascending=False)
    time.sleep(0.5)

    narrate("Now, let's hear the Phrygian mode.")
    theory_ji.play_scale(theory_ji.phrygian_scale(440), wave_type='sine', duration=0.30)
    time.sleep(0.5)
    theory_ji.play_scale(theory_ji.phrygian_scale(440), wave_type='sine', duration=0.30, ascending=False)
    time.sleep(0.5)

    narrate("The Lydian mode.")
    theory_ji.play_scale(theory_ji.lydian_scale(440), wave_type='sine', duration=0.30)
    time.sleep(0.5)
    theory_ji.play_scale(theory_ji.lydian_scale(440), wave_type='sine', duration=0.30, ascending=False)
    time.sleep(0.5)

    narrate("The Mixolydian mode.")
    theory_ji.play_scale(theory_ji.mixolydian_scale(440), wave_type='sine', duration=0.30)
    time.sleep(0.5)
    theory_ji.play_scale(theory_ji.mixolydian_scale(440), wave_type='sine', duration=0.30, ascending=False)
    time.sleep(0.5)

    narrate("Here's the Aeolian mode. It is more commonly known as the Natural Minor scale.")
    theory_ji.play_scale(theory_ji.aeolian_scale(440), wave_type='sine', duration=0.30)
    time.sleep(0.5)
    theory_ji.play_scale(theory_ji.aeolian_scale(440), wave_type='sine', duration=0.30, ascending=False)
    time.sleep(0.5)

    narrate("Finally, we have the Locrian mode.")
    theory_ji.play_scale(theory_ji.locrian_scale(440), wave_type='sine', duration=0.30)
    time.sleep(0.5)
    theory_ji.play_scale(theory_ji.locrian_scale(440), wave_type='sine', duration=0.30, ascending=False)
    time.sleep(0.5)

    narrate("Traditional theory divides the octave into twelve fixed parts, but music isn't limited to these boundaries.")
    narrate("By using microtonality, we can access a continuum of frequencies, unlocking harmonic relationships that exist outside the standard Western system.")