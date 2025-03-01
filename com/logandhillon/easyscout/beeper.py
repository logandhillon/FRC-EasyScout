from time import sleep
import numpy as np
import sounddevice as sd

samplerate = 44100


def tone(hz, s):
    """Play a tone on the devices speakers

    Args:
        hz (number): freqyency
        s (number): amount of seconds
    """
    t = np.linspace(0, s, int(samplerate * s), endpoint=False)
    w = 0.5 * np.sin(2 * np.pi * hz * t)
    sd.play(w, samplerate)
