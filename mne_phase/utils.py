import numpy as np

def rayleigh_test(phases):
    """test distrib uniforme."""
    ph = phases.reshape(-1)
    n = len(ph)
    w = np.ones(n)
    r = np.sum(w*np.exp(1j*ph))
    r = abs(r)/np.sum(w)
    R = n*r
    z = R**2 / n
    pval = np.exp(np.sqrt(1+4*n+4*(n**2-R**2))-(1+2*n))
    return pval
