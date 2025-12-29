from audio_modules import Wave, Audio, utils, narrate
from audio_modules.theory_ji import chord, interval, play_chord

with Audio() as a:

    # wave = Wave(220, amp=0).sine()
    # wave += Wave(220, amp=1).sine()
    # wave += Wave(440, amp=0.5).sine()
    # wave += Wave(660, amp=0.25).sine()
    # wave += Wave(880, amp=0.125).sine()
    # wave += Wave(1100, amp=0.0625).sine()
    # wave += Wave(1320, amp=0.03125).sine()
    # wave += Wave(1540, amp=0.015625).sine()
    # wave += Wave(1760, amp=0.0078125).sine()
    # wave += Wave(1980, amp=0.00390625).sine()
    # wave += Wave(2200, amp=0.001953125).sine()
    # wave += Wave(2420, amp=0.0009765625).sine()
    # wave += Wave(2640, amp=0.00048828125).sine()
    # wave += Wave(2860, amp=0.000244140625).sine()
    # wave += Wave(3080, amp=0.0001220703125).sine()
    # wave += Wave(3300, amp=0.00006103515625).sine()
    # wave += Wave(3520, amp=0.000030517578125).sine()
    # wave += Wave(3740, amp=0.0000152587890625).sine()
    # wave += Wave(3960, amp=0.00000762939453125).sine()
    # wave += Wave(4180, amp=0.000003814697265625).sine()
    # wave += Wave(4400, amp=0.0000019073486328125).sine()
    # wave += Wave(4620, amp=0.00000095367431640625).sine()
    # wave += Wave(4840, amp=0.000000476837158203125).sine()
    # wave += Wave(5060, amp=0.0000002384185791015625).sine()
    # wave += Wave(5280, amp=0.00000011920928955078125).sine()
    # wave += Wave(5500, amp=0.000000059604644775390625).sine()
    # wave += Wave(5720, amp=0.0000000298023223876953125).sine()
    # wave += Wave(5940, amp=0.00000001490116119384765625).sine()
    # wave += Wave(6160, amp=0.000000007450580596923828125).sine()
    # wave += Wave(6380, amp=0.0000000037252902984619140625).sine()
    # wave += Wave(6600, amp=0.00000000186264514923095703125).sine()
    # wave += Wave(6820, amp=0.000000000931322574615478515625).sine()
    # wave += Wave(7040, amp=0.0000000004656612873077392578125).sine()
    # wave += Wave(7260, amp=0.00000000023283064365386962890625).sine()
    # wave += Wave(7480, amp=0.000000000116415321826934814453125).sine()
    # wave += Wave(7700, amp=0.0000000000582076609134674072265625).sine()
    # wave += Wave(7920, amp=0.00000000002910383045673370361328125).sine()




    # try to make a triangle wave with additive synthesis
    amp, hz, dur = .125, 220, 1
    wave = Wave(hz, amp=0, duration=dur).sine()

    j = 0
    for i in range(1, 200, 2):
        harmonic_amp = amp / (i**2)
        if j == 1:
            wave += Wave(hz * i, amp=harmonic_amp, duration=dur).sine()
        else:
            wave += Wave(hz * i, amp=harmonic_amp, duration=dur).sine() * -1
        j = 0 if j == 1 else 1

    # wave = Wave(hz, amp=1, duration=dur).triangle()
    a.buffer.append(wave)
    a.save_buffer('additive_synth_10_harmonics_triangle.wav')
    a.play_buffer()



    # Trying to make a square wave with additive synthesis
    amp, hz, dur = .125, 220, 1
    wave = Wave(hz, amp=0, duration=dur).sine()

    for i in range(1, 200, 2):
        harmonic_amp = amp / i
        wave += Wave(hz * i, amp=harmonic_amp, duration=dur).sine()

    # wave = Wave(hz, amp=1, duration=dur).square()
    a.buffer.append(wave)
    a.save_buffer('additive_synth_10_harmonics_square.wav')
    a.play_buffer()