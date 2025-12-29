from audio_modules import Wave, Audio, utils, narrate
from audio_modules.theory_ji import chord, interval, play_chord
# from audio_modules.theory import chord, interval, play_chord

import time

with Audio() as a:

    narrate("Let's mess around with some chords in Just Intonation.")
    time.sleep(1)

    narrate("Here's a super turbo major chord.")
    c = chord(256, ['uni', 'ma3', 'p5', 'oct', 'ma10', 'p12', 'oct2'])
    print(f'frequencies: {c}')
    play_chord(c, wave_type='sine', roll_on=0.1, duration=2.5)
    time.sleep(1)

    narrate("Here's an interesting lydian chord progression with a minor triad stacked on top of a major triad.")
    root_hz = 256
    notes = ['uni', 'ma3', 'p5', 'ma7', 'ma9', 'tri2']
    positions = [0, -5, -4, -3, 0]
    for pos in positions:
        c = chord(interval(root_hz, pos), notes)
        print(f'frequencies: {c}')
        play_chord(c, wave_type='sine', roll_on=0.1, duration=2.5)
    
    narrate("Here's the same chord, but moving down one semitone at a time.")
    root_hz = 256
    notes = ['uni', 'ma3', 'p5', 'ma7', 'ma9', 'tri2']
    positions = [0, -1, -2, -3, -4]
    for pos in positions:
        c = chord(interval(root_hz, pos), notes)
        print(f'frequencies: {c}')
        duration = 1 if pos != -4 else 2
        play_chord(c, wave_type='sine', roll_on=0.01, duration=duration)    
    narrate("Side note: our Just Intonation library has been updated to use SymPy.")
    narrate("SymPy lets us represent intervals as rational numbers as long as possible.")   
    narrate("Here we use 256 as our root frequency.")
    narrate("Since it's a power of 2, most of the frequencies actually end up being not just rational numbers, but integers themselves.")
    time.sleep(1)

    # #####################################################################
    # Harmonic series
    # #####################################################################

    narrate("Now, let's look at the harmonics or multiples of a fundamental frequency.")

    narrate("Here's a dense harmonic series chord using the 8th, 10th, 12th, 14th, and 15th harmonics of a 32 hertz fundamental.")
    narrate("This combines a harmonic seventh with a major seventh for a very rich resonance.")
    fundamental = 32 
    harmonics = [8, 10, 12, 14, 15] 
    c = [fundamental * h for h in harmonics]
    print(f'frequencies: {c}')
    # Result: [256, 320, 384, 448, 480]
    play_chord(c, wave_type='sine', roll_on=0.1, duration=5)
    time.sleep(1)

    narrate("Here's the full physical harmonic series spanning four octaves, starting from a 256 hertz fundamental.")
    fundamental = 256
    harmonics = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] 
    c = [fundamental * h for h in harmonics]
    # frequencies: [256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 2816, 3072, 3328, 3584, 3840, 4096]
    print(f'frequencies: {c}')
    play_chord(c, wave_type='sine', roll_on=0.5, duration=8.0)

    narrate("Now, we'll take the eighth through sixteenth harmonics and compress them into a single octave.")
    narrate("This creates a scale derived entirely from the physics of a single string.")
    fundamental = 256
    scale_frequencies = []
    for h in range(8, 16): # Using the 8th through 15th harmonics as our 'neighborhood'
        freq = fundamental * h
        # Reduce by octaves until it's between 256 and 511
        while freq >= 512:
            freq /= 2
        scale_frequencies.append(freq)
    # Sort them so they play low to high
    scale_frequencies.sort()
    
    print(f'Just Scale frequencies: {scale_frequencies}')
    for f in scale_frequencies:
        play_chord([f], wave_type='sine', duration=0.5)
    play_chord(scale_frequencies, wave_type='sine', roll_on=0.2, duration=3.0)
    time.sleep(1)

    # #####################################################################
    # Interference patterns
    # #####################################################################

    narrate("Next, let's compare Just Intonation to Standard Tuning using the C-Major Ionian mode.")
    fundamental = 256
    ratios = [1, 9/8, 5/4, 4/3, 3/2, 5/3, 15/8, 2]
    semitones = [0, 2, 4, 5, 7, 9, 11, 12]
    for i, ratio in enumerate(ratios):
        ji_freq = fundamental * ratio
        std_freq = fundamental * (2 ** (semitones[i] / 12))       
        print(f"Note {i}: Just={ji_freq:.2f}Hz | Std={std_freq:.2f}Hz")
    narrate("First, the Just Intonation scale. Listen for the 'glassy' stability. Because the frequencies are pure ratios, the interference patterns lock into a steady, singular pulse.")
    ji_freqs = [fundamental * ratio for ratio in ratios]
    play_chord(ji_freqs, wave_type='sine', roll_on=1, duration=10.0)
    time.sleep(1)
    narrate("Now, Equal Temperament. Notice the shimmering or 'wobbling' texture. Since these frequencies are slightly out of alignment with the harmonic series, they create an irregular beating pattern.")
    std_freqs = [fundamental * (2 ** (semitones[i] / 12)) for i in range(len(semitones))]
    play_chord(std_freqs, wave_type='sine', roll_on=1, duration=10.0)
    narrate("Can you hear the difference?")
    time.sleep(1)

    narrate("Next, let's explore interference patterns some more.")
    narrate("We'll play the 4th, 5th, and 6th harmonics of 32 hertz.")
    narrate("These are high enough for your speakers to play at 128 hertz and up.")
    narrate("But their interference pattern creates a 32 hertz heartbeat.")
    fundamental = 32
    harmonics = [4, 5, 6] 
    c = [fundamental * h for h in harmonics]
    narrate("I'm not playing the low note. Can you feel the 32 hertz 'ghost' pulse created by these three higher notes?")
    print(f'Frequencies: {c}') # [128, 160, 192]
    play_chord(c, wave_type='sine', duration=4.0)
    time.sleep(1)