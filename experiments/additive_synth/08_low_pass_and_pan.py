from audio_modules import Audio, Noise, effects, narrate
import time

with Audio() as a:

    narrate('Let\'s test some effects.')

    # high and low pass filters

    narrate('For reference, here is some white noise')
    w = Noise(amp=1.0, duration=2.0).white()
    a.buffer.append(w)
    a.play_buffer()
    
    narrate('Now, let\'s try adding a highpass filter at 2000 hertz. Notice how the lower frequencies are attenuated.')
    w = Noise(amp=1.0, duration=2.0).white()
    a.buffer.append(effects.highpass_filter(w, cutoff_hz=2000))
    a.play_buffer()

    narrate('Now, let\'s try adding a lowpass filter at 500 hertz. Notice how the higher frequencies are attenuated.')
    w = Noise(amp=1.0, duration=2.0).white()
    a.buffer.append(effects.lowpass_filter(w, cutoff_hz=500))
    a.play_buffer()


    # panning
    
    narrate('Now, let\'s try panning the noise to the left.')
    w = Noise(amp=1.0, duration=2.0).white()
    a.buffer.append(effects.pan(w, pan=-1.0))
    a.play_buffer()

    narrate('And to the right.')
    w = Noise(amp=1.0, duration=2.0).white()
    a.buffer.append(effects.pan(w, pan=1.0))
    a.play_buffer()

    time.sleep(1)

    narrate('When you test your speakers, you might hear something like this.')

    samples, sample_rate = narrate('Front', play=False)
    na = Audio(sample_rate=sample_rate)
    na.buffer.append(effects.pan(samples, pan=-1.0))
    na.play_buffer() 

    samples, _ = narrate('Left', play=False)
    na.buffer.append(effects.pan(samples, pan=-1.0))
    na.play_buffer()

    time.sleep(1)

    samples, _ = narrate('Front', play=False)
    na.buffer.append(effects.pan(samples, pan=1.0))
    na.play_buffer()

    samples, _ = narrate('Right', play=False)
    na.buffer.append(effects.pan(samples, pan=1.0))
    na.play_buffer()

