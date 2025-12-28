from audio_modules import Wave, Audio

with Audio() as a:
    a.buffer.append(Wave(hz=110, amp=1.0, duration=0.1).sine())
    a.buffer.append(Wave(hz=220, amp=1.0, duration=0.1).sine())
    a.buffer.append(Wave(hz=440, amp=1.0, duration=0.1).sine())

    a.buffer.append(Wave(hz=110, amp=1.0, duration=0.2).square())
    a.buffer.append(Wave(hz=220, amp=1.0, duration=0.2).square())
    a.buffer.append(Wave(hz=440, amp=1.0, duration=0.2).square())

    a.buffer.append(Wave(hz=110, amp=1.0, duration=0.3).triangle())
    a.buffer.append(Wave(hz=220, amp=1.0, duration=0.3).triangle())
    a.buffer.append(Wave(hz=440, amp=1.0, duration=0.3).triangle())

    a.buffer.append(Wave(hz=110, amp=1.0, duration=0.4).sawtooth())
    a.buffer.append(Wave(hz=220, amp=1.0, duration=0.4).sawtooth())
    a.buffer.append(Wave(hz=440, amp=1.0, duration=0.4).sawtooth())

    # play audio immediately
    a.play_buffer(clear=False)

    # save audio to .wav file
    a.save_buffer("recordings/track1.wav")