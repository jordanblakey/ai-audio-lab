import wave
import numpy as np
import pyaudio

# import numpy
# numpy.show_config()


class Audio:
    def __init__(self, rate=48000, chunk_size=2048):
        self.p = pyaudio.PyAudio()
        self.rate = rate
        self.chunk_size = chunk_size
        self.buffer = []
        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.rate,
            output=True,
            frames_per_buffer=self.chunk_size,
        )

    def save_buffer(self, filename="recordings/output.wav"):
        # Convert to 16-bit integer PCM for standard WAV compatibility
        data = np.concatenate(self.buffer)
        data = np.clip(data, -1.0, 1.0)
        samples = (data * 32767).astype(np.int16)

        with wave.open(filename, "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(self.rate)
            f.writeframes(samples.tobytes())

    def play_buffer(self, clear=True):
        if not self.buffer:
            return

        # 1. Prepare data (Robust: One allocation)
        data = np.concatenate(self.buffer).astype(np.float32)
        data = np.clip(data, -1.0, 1.0)

        try:
            # 2. Chunked loop (Interruptible)
            for i in range(0, len(data), self.chunk_size):
                chunk = data[i : i + self.chunk_size]
                self.stream.write(chunk.tobytes(), exception_on_underflow=False)

        except KeyboardInterrupt:
            # 3. Clean Stop: We play a tiny bit of silence to clear the hardware buffer
            print("\n[Playback Interrupted]")
            silence = np.zeros(self.chunk_size, dtype=np.float32)
            self.stream.write(silence.tobytes())

        if clear:
            self.buffer.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Clean Stop: We play a tiny bit of silence to clear the hardware buffer
        silence = np.zeros(self.chunk_size * 2, dtype=np.float32)
        self.stream.write(silence.tobytes())

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
