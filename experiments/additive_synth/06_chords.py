from audio_modules import Wave, Audio, utils, narrate, effects, theory, theory_ji
import time

with Audio() as a:

    narrate("Let's explore combining notes to create chords and harmonies.")

    narrate("First, let's look at some individual notes, spanning several octaves.")

    # create waves
    waves = [
        Wave(hz=55, amp=1.0, duration=0.5),
        Wave(hz=110, amp=1.0, duration=0.5),
        Wave(hz=220, amp=1.0, duration=0.5),
        Wave(hz=440, amp=1.0, duration=0.5),
        Wave(hz=880, amp=1.0, duration=0.5),
        Wave(hz=1760, amp=1.0, duration=0.5),
    ]    

    # play waves
    for i in range(len(waves)):
        a.buffer.append(waves[i].sine()) 
    a.play_buffer()

    narrate("Now, if we combine the waveforms by summing them, they sound like this.")

    # offset waves and increase duration
    time_shifted_waves = []
    for i in range(len(waves)):
        waves[i].duration = (2.5 + len(waves) * 0.25 - i * 0.25)
        waves[i].delay = i * 0.25
        time_shifted_waves.append(waves[i].sine()) 

    # sum waves
    summed_waveform = utils.sum_waveforms(time_shifted_waves)
    a.buffer.append(summed_waveform)
    a.play_buffer()

    # Chord Types

    narrate("This layering of notes is called a chord.")
    narrate("Let's explore some common chords found in music.")

    narrate("This is a major chord.")
    theory.play_chord(theory.major_chord(440), wave_type='triangle', duration=2.0)

    narrate("This is a minor chord.")
    theory.play_chord(theory.minor_chord(440), wave_type='triangle', duration=2.0)

    narrate("This is a diminished chord.")
    theory.play_chord(theory.diminished_chord(440), wave_type='triangle', duration=2.0)

    narrate("This is an augmented chord.")
    theory.play_chord(theory.augmented_chord(440), wave_type='triangle', duration=2.0)

    narrate("This is a power chord.")
    theory.play_chord(theory.power_chord(440), wave_type='triangle', duration=2.0)


    # Equal Temperament vs Just Intonation

    narrate("Let's explore the difference between Equal Temperament tuning and Just Intonation tuning.") 
    narrate("Almost all modern music is based on Equal Temperament, which equally distributes the octave into 12 semi-tones.")
    narrate("Just Intonation, on the other hand, is based on whole number ratios.")

    narrate("This is a major chord voiced with Equal Temperament tuning.")
    theory.play_chord(theory.major_chord(440), wave_type='triangle', duration=2.0)
    time.sleep(0.5)

    narrate("Now let's hear the same major chord voiced with Just Intonation tuning.")
    theory_ji.play_chord(theory_ji.major_chord(440), wave_type='triangle', duration=2.0)
    time.sleep(0.5)

    narrate("A major chord is made up of the root, major third, and perfect fifth intervals.")
    narrate("With just intonation, the major third is a 5 to 4 ratio, and the perfect fifth is a 3 to 2 ratio.")
    narrate("This creates a more balanced, consonant sound.")

    time.sleep(0.5)
    narrate("Let's hear some more comparisons. Can you detect the difference?")

    narrate("This is a major chord.")
    theory.play_chord(theory.major_chord(440), wave_type='triangle', duration=2.0)
    theory_ji.play_chord(theory_ji.major_chord(440), wave_type='triangle', duration=2.0)
    time.sleep(0.5)

    narrate("This is a minor chord.")
    theory.play_chord(theory.minor_chord(440), wave_type='triangle', duration=2.0)
    theory_ji.play_chord(theory_ji.minor_chord(440), wave_type='triangle', duration=2.0)
    time.sleep(0.5)

    narrate("This is a diminished chord.")
    theory.play_chord(theory.diminished_chord(440), wave_type='triangle', duration=2.0)
    theory_ji.play_chord(theory_ji.diminished_chord(440), wave_type='triangle', duration=2.0)
    time.sleep(0.5)

    narrate("This is an augmented chord.")
    theory.play_chord(theory.augmented_chord(440), wave_type='triangle', duration=2.0)
    theory_ji.play_chord(theory_ji.augmented_chord(440), wave_type='triangle', duration=2.0)
    time.sleep(0.5)

    narrate("This is a power chord.")
    theory.play_chord(theory.power_chord(440), wave_type='triangle', duration=2.0)
    theory_ji.play_chord(theory_ji.power_chord(440), wave_type='triangle', duration=2.0)
    time.sleep(0.5)
    
    narrate("Maybe you noticed that chords using Just Intonation had a more resonant, bell-like quality.")
    narrate("Isn't that interesting?")