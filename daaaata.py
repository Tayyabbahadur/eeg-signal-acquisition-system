import mne
import numpy as np
from scipy.signal import welch

raw = mne.io.read_raw_edf("SC4001E0-PSG.edf", preload=True)
raw.pick(['EEG Fpz-Cz'])

data, times = raw[:]
signal = data[0]
sf = raw.info['sfreq']

freqs, psd = welch(signal, sf, nperseg=sf*4)

bands = {
    "delta": (0.5,4),
    "theta": (4,8),
    "alpha": (8,13),
    "beta": (13,30),
    "gamma": (30,45)
}

total_power = np.sum(psd)

print("\nRelative Band Power (%)\n")

for band,(low,high) in bands.items():

    idx = (freqs>=low) & (freqs<=high)
    band_power = np.sum(psd[idx])
    percent = (band_power/total_power)*100

    print(f"{band}: {percent:.2f}%")


import mne

raw = mne.io.read_raw_edf("SC4001E0-PSG.edf", preload=True)

duration_seconds = raw.times[-1]
duration_minutes = duration_seconds / 60
duration_hours = duration_seconds / 3600

print(f"Duration: {duration_seconds:.2f} seconds")
print(f"Duration: {duration_minutes:.2f} minutes")
print(f"Duration: {duration_hours:.2f} hours")