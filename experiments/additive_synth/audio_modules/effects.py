from typing import Optional
import numpy as np
from audio_modules.easings import EASINGS, EasingType
from scipy.signal import butter, lfilter

SAMPLE_RATE = 48000

def remove_dc_offset(samples: np.ndarray[np.float64]):
    return samples - np.mean(samples)

def normalize(samples: np.ndarray[np.float64]):
    return samples / np.max(np.abs(samples))

def rms_normalize(samples: np.ndarray[np.float64], target_rms: float = 0.1):
    # Calculate the current average power
    current_rms = np.sqrt(np.mean(samples**2))
    # Scale to the target
    return samples * (target_rms / current_rms)

def gain(samples: np.ndarray[np.float64], gain: float):
    return samples * gain
    
def hard_clip(samples: np.ndarray[np.float64], gain: float):
    processed = samples * gain
    return np.clip(processed, -1.0, 1.0)
    
def soft_clip(samples: np.ndarray[np.float64], gain: float):
    # tanh naturally curves off as it approaches 1.0 and -1.0
    return np.tanh(samples * gain)

def pan(samples: np.ndarray[np.float64], pan: float = 0.0):
    """
    pan: -1.0 (full left) to 1.0 (full right)
    Uses 'Constant Power' panning so the center isn't quieter than the sides.
    """
    # Convert pan to 0.0 -> 1.0 range
    p = (pan + 1) / 2
    left_gain = np.cos(p * (np.pi / 2))
    right_gain = np.sin(p * (np.pi / 2))
    
    # If input is mono, make it stereo
    if samples.ndim == 1:
        return np.column_stack((samples * left_gain, samples * right_gain))
    
    # If input is already stereo, adjust channels
    samples[:, 0] *= left_gain
    samples[:, 1] *= right_gain
    return samples

def highpass_filter(
    samples: np.ndarray[np.float64], 
    sample_rate: int = SAMPLE_RATE, 
    cutoff_hz: float = 40
):
    nyq = 0.5 * sample_rate
    normal_cutoff = cutoff_hz / nyq
    b, a = butter(1, normal_cutoff, btype='high', analog=False)
    return lfilter(b, a, samples)

def lowpass_filter(
    samples: np.ndarray[np.float64], 
    sample_rate: int = SAMPLE_RATE, 
    cutoff_hz: float = 1000
):
    nyq = 0.5 * sample_rate
    normal_cutoff = cutoff_hz / nyq
    b, a = butter(1, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, samples)

def fade(
    samples: np.ndarray[np.float64],
    sample_rate: int = SAMPLE_RATE,
    fade_in_ms: Optional[int] = 15,
    fade_out_ms: Optional[int] = 15,
    ease_in: EasingType = "linear",
    ease_out: EasingType = "linear",
):
    """Applies an envelope to the samples."""
    envelope = np.ones(len(samples))
    
    ease_in_func = EASINGS.get(ease_in, EASINGS["linear"])
    ease_out_func = EASINGS.get(ease_out, EASINGS["linear"])    

    if fade_in_ms:
        fade_in_samples = int(sample_rate * (fade_in_ms / 1000))
        if len(samples) >= fade_in_samples:
            t = np.linspace(0, 1, fade_in_samples)
            envelope[:fade_in_samples] = ease_in_func(t)

    if fade_out_ms:
        fade_out_samples = int(sample_rate * (fade_out_ms / 1000))
        if len(samples) >= fade_out_samples:
            t = np.linspace(1, 0, fade_out_samples)
            envelope[-fade_out_samples:] = ease_out_func(t)
    
    return samples * envelope