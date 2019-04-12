"""
=======================
Plot phase distribution
=======================

Test whether it is uniformly distributed.
"""
# Authors: Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
#          Tadeusz W. Kononowicz <t.w.kononowicz@icloud.com>
#
# License: BSD (3-clause)

import numpy as np
import matplotlib.pyplot as plt

import mne
from mne.time_frequency import tfr_morlet
from mne.stats import permutation_cluster_1samp_test
from mne.datasets import sample

from mne_phase.utils import rayleigh_test

print(__doc__)

###############################################################################
#
# As starting point we will borrow some code from XXXXXXXXXXXXX
#
# Set parameters
# --------------
data_path = sample.data_path()
raw_fname = data_path + '/MEG/sample/sample_audvis_raw.fif'
tmin, tmax, event_id = -0.3, 0.6, 1

# Setup for reading the raw data
raw = mne.io.read_raw_fif(raw_fname)
events = mne.find_events(raw, stim_channel='STI 014')

include = []
raw.info['bads'] += ['MEG 2443', 'EEG 053']  # bads + 2 more

# picks MEG gradiometers
picks = mne.pick_types(raw.info, meg='grad', eeg=False, eog=True,
                       stim=False, include=include, exclude='bads')

# Load condition 1
event_id = 1
epochs = mne.Epochs(raw, events, event_id, tmin, tmax, picks=picks,
                    baseline=(None, 0), preload=True,
                    reject=dict(grad=4000e-13, eog=150e-6))

# Take only one channel
ch_name = 'MEG 1332'
epochs.pick_channels([ch_name])

evoked = epochs.average()

# Factor to down-sample the temporal dimension of the TFR computed by
# tfr_morlet. Decimation occurs after frequency decomposition and can
# be used to reduce memory usage (and possibly computational time of downstream
# operations such as nonparametric statistics) if you don't need high
# spectrotemporal resolution.
decim = 5
freqs = [10]  # define frequencies of interest
sfreq = raw.info['sfreq']  # sampling in Hz
tfr_epochs = tfr_morlet(epochs, freqs, n_cycles=4., decim=decim,
                        average=False, return_itc=False, n_jobs=1,
                        output='complex')

###############################################################################
#
# Now that we have `tfr` we chan show bla bla in terms of bla bla XXXXXXXXXXXXX

# bla bla bla bla bla
my_data = np.angle(tfr_epochs._data.squeeze())
t0_sample_idx = np.where(tfr_epochs.times==0)[0][0]

p_val = rayleigh_test(my_data[t0_sample_idx, :])

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
plt.title('Phase')
plt.hist(my_data[t0_sample_idx, :], bins=20, color = 'grey', alpha=0.5)
plt.show()
