import numpy as np
from audio_modules.effects import fade
from audio_modules.easings import EasingType

SAMPLE_RATE = 48000


class Noise:
    def __init__(self, amp: float = 1.0, duration: float = 1.0):
        self.amp = amp
        self.duration = duration
        self.t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)

    def __str__(self):
        return f"Noise(amp={self.amp}, duration={self.duration})"

    @property
    def duration(self):
        return self.t.shape[0] / SAMPLE_RATE

    @duration.setter
    def duration(self, value):
        self.t = np.linspace(0, value, int(SAMPLE_RATE * value), endpoint=False)

    def white(self):
        """Generates white noise."""
        return np.random.uniform(-1, 1, self.t.shape[0]) * self.amp

    def _colored_noise(self, alpha):
        """
        Generates colored noise with 1/f^alpha power spectral density.
        alpha=1: Pink
        alpha=2: Brown
        alpha=-1: Blue
        alpha=-2: Violet
        """
        # Generate white noise in frequency domain
        white = np.fft.rfft(np.random.normal(0, 1, self.t.shape[0]))

        # Calculate frequency bins
        freqs = np.fft.rfftfreq(self.t.shape[0], d=1 / SAMPLE_RATE)

        # Avoid division by zero at DC (0 Hz)
        # We can set the first component to 0 or leave it as is (white noise DC)
        # Usually colored noise is zero-mean, so let's zero out DC or scaling factor 1.
        # Standard approach: scale amplitudes by 1 / f^(alpha/2)

        scaling = np.ones_like(freqs)
        # Only scale positive frequencies
        scaling[1:] = 1 / (freqs[1:] ** (alpha / 2))

        # Apply scaling
        colored_spectrum = white * scaling

        # Transform back to time domain
        colored_noise = np.fft.irfft(colored_spectrum, n=self.t.shape[0])

        # Normalize to -1 to 1 range approx, then apply amp
        # Normalization can be tricky as random range varies.
        # We'll normalize by max absolute value to ensure it stays within bounds.
        max_val = np.max(np.abs(colored_noise))
        if max_val > 0:
            colored_noise /= max_val

        samples = colored_noise * self.amp

        return fade(
            samples,
            fade_in_ms=15,
            fade_out_ms=15,
            ease_in="easeOutQuad",
            ease_out="easeOutQuad",
        )

    def pink(self):
        """Generates pink noise (1/f)."""
        return self._colored_noise(1)

    def brown(self):
        """Generates brown noise (1/f^2)."""
        return self._colored_noise(2)

    def blue(self):
        """Generates blue noise (f^1)."""
        return self._colored_noise(-1)

    def violet(self):
        """Generates violet noise (f^2)."""
        return self._colored_noise(-2)
