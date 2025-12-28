import time

from audio_modules import narrate, Wave, Audio
from audio_modules.effects import fade


with Audio() as a:
    narrate("An amplitude envelope is a filter that creates smooth transitions over time.")
    narrate("We can use it to shape the attack, sustain, release and decay of a sound.")

    narrate("For reference, here is an unmodified 440 hertz sine wave.")
    wave = Wave(hz=440, amp=1.0, duration=3.0).sine()
    a.buffer.append(wave)
    a.play_buffer()
    time.sleep(0.5)

    narrate("Now, let's add an amplitude envelope, with a 1000 millisecond fade in and fade out.")
    envelope_wave = fade(
        wave, fade_in_ms=1000, fade_out_ms=1000, ease_in="linear", ease_out="linear"
    )
    a.buffer.append(envelope_wave)
    a.play_buffer()
    narrate("As you can hear, the sound now smoothly transitions between silence and full amplitude.")
    time.sleep(0.5)

    narrate("Let's try a 200 millisecond fade in, and a longer, 2000 millisecond fade out.")
    wave = Wave(hz=440, amp=1.0, duration=3.0).sine()
    envelope_wave = fade(
        wave, fade_in_ms=200, fade_out_ms=2000, ease_in="linear", ease_out="linear"
    )
    a.buffer.append(envelope_wave)
    a.play_buffer()
    narrate("Basically, we can use the envelope to shape the attack and release of a sound.")
    time.sleep(0.5)

    narrate("For example, we can create a synthesizer pad with a square wave, a long attack and a very long decay.")
    wave = Wave(hz=440, amp=1.0, duration=5.0).square()
    envelope_wave = fade(
        wave, fade_in_ms=800, fade_out_ms=4000, ease_in="linear", ease_out="linear"
    )
    a.buffer.append(envelope_wave)
    a.play_buffer()
    time.sleep(0.5)

    narrate("Let's try a sharp attack and quick release for a percussive, pluck style.")
    narrate("Using easing functions, we can shape how the sound changes over time.")
    a.buffer.append(
        fade(
            Wave(hz=(440 * 2 ** (0 / 12)), duration=300 / 1000).sine(),
            fade_in_ms=5,
            fade_out_ms=300,
            ease_in="easeOutExpo",
            ease_out="easeInQuad",
        )
    )
    a.buffer.append(
        fade(
            Wave(hz=(440 * 2 ** (4 / 12)), duration=300 / 1000).sine(),
            fade_in_ms=5,
            fade_out_ms=300,
            ease_in="easeOutExpo",
            ease_out="easeInQuad",
        )
    )
    a.buffer.append(
        fade(
            Wave(hz=(440 * 2 ** (7 / 12)), duration=300 / 1000).sine(),
            fade_in_ms=5,
            fade_out_ms=300,
            ease_in="easeOutExpo",
            ease_out="easeInQuad",
        )
    )
    a.buffer.append(
        fade(
            Wave(hz=(440 * 2 ** (12 / 12)), duration=300 / 1000).sine(),
            fade_in_ms=5,
            fade_out_ms=300,
            ease_in="easeOutExpo",
            ease_out="easeInQuad",
        )
    )

    a.play_buffer()
