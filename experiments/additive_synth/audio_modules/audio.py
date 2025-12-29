import wave
import numpy as np
import pyaudio

# import numpy
# numpy.show_config()

class Audio:
    def __init__(self, sample_rate=192000, chunk_size=2048, channels=2):
        self.p = pyaudio.PyAudio()
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.channels = channels
        self.buffer = []
        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            channels=self.channels,
            rate=self.sample_rate,
            output=True,
            frames_per_buffer=self.chunk_size,
        )

    def prepare_buffer(self):
        if not self.buffer:
            return np.empty((0, self.channels), dtype=np.float32)

        data = np.concatenate(self.buffer, axis=0).astype(np.float32)

        # handle mono to stereo and stereo to mono mismatch
        if data.ndim == 1 and self.channels > 1:
            data = np.column_stack((data, data))
        elif data.ndim == 2 and self.channels == 1:
            data = np.mean(data, axis=1)

        # 1. Prepare data (Robust: One allocation)
        data = np.clip(data, -1.0, 1.0)
        return data

    def save_buffer(self, filename="recordings/output.wav"):
        # Convert to 16-bit integer PCM for standard WAV compatibility
        data = self.prepare_buffer()
        samples = (data * 32767).astype(np.int16)

        with wave.open(filename, "wb") as f:
            f.setnchannels(self.channels)
            f.setsampwidth(2)
            f.setframerate(self.sample_rate)
            f.writeframes(samples.tobytes())

    def play_buffer(self, clear=True):
        data = self.prepare_buffer()

        try:
            # 2. Chunked loop (Interruptible)
            for i in range(0, len(data), self.chunk_size):
                chunk = data[i : i + self.chunk_size]
                self.stream.write(chunk.tobytes(), exception_on_underflow=False)

        except KeyboardInterrupt:
            # 3. Clean Stop: We play a tiny bit of silence to clear the hardware buffer
            print("\n[Playback Interrupted]")
            silence = np.zeros((self.chunk_size * 2, self.channels), dtype=np.float32)
            self.stream.write(silence.tobytes())

        if clear:
            self.buffer.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Clean Stop: We play a tiny bit of silence to clear the hardware buffer
        silence = np.zeros((self.chunk_size * 2, self.channels), dtype=np.float32)
        self.stream.write(silence.tobytes())

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
