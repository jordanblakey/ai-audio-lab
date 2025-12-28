from typing import Optional
import numpy as np
from audio_modules.easings import EASINGS, EasingType

def amplitude_envelope(
    samples: np.ndarray,
    fade_in_ms: Optional[int] = 15,
    fade_out_ms: Optional[int] = 15,
    ease_in: EasingType = "linear",
    ease_out: EasingType = "linear"
):
    """Applies an envelope to the samples."""
    envelope = np.ones(len(samples))
    
    ease_in_func = EASINGS.get(ease_in, EASINGS["linear"])
    ease_out_func = EASINGS.get(ease_out, EASINGS["linear"])    

    if fade_in_ms:
        fade_in_samples = int(48000 * (fade_in_ms / 1000))
        if len(samples) >= fade_in_samples:
            t = np.linspace(0, 1, fade_in_samples)
            envelope[:fade_in_samples] = ease_in_func(t)

    if fade_out_ms:
        fade_out_samples = int(48000 * (fade_out_ms / 1000))
        if len(samples) >= fade_out_samples:
            t = np.linspace(1, 0, fade_out_samples)
            envelope[-fade_out_samples:] = ease_out_func(t)
    
    return samples * envelope
