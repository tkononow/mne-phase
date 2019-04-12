import numpy as np
from pytest import approx

from mne_phase.utils import rayleigh_test


def test_basic():
    input = np.array([0.02058449, 0.96990985, 0.83244264, 0.21233911])
    EXPECTED = 0.02172542636470802
    assert rayleigh_test(input) == approx(EXPECTED)
