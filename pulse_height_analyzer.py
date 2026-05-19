import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Hardware driver
# ---------------------------------------------------------------------------
try:
    from waveforms_ads import WaveFormsADS, DWFError
    HW_AVAILABLE = True
except ImportError:
    print("Waveforms packages not installed. Close and try again")