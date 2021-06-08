"""
Test module to be imported in the Notebook
"""
import numpy as np
from obspy import Trace  # for smoothed_ampspec annotation
from obspy.core.inventory.response import Response  # for smoothed_ampspec annotation
from obspy.signal.konnoohmachismoothing import konno_ohmachi_smoothing as ko_smooth


def smoothed_ampspec(trace: Trace, inventory: Response = None):
    """
    Amplitude spectrum, smoothed
    
    :param trace: (obspy Trace) the trace
    :param inventory: (obspy Response) the optional inventory. When provided
        and not None, the response will be removed from the trace as first
        operation
    
    :return: a tuple of two numpy arrays: `(freqs, ampspec)`
    """
    
    if inventory is not None:
        trace = trace.remove_response(inventory)
    
    # Removing the mean from the trace
    trace = trace.detrend(type='constant')
    
    # Taper (after trim endpoints are !=0)
    trace = trace.taper(max_percentage=0.05, type='cosine')
    
    # Get the amplitude values (numpy array) from the resulting traces
    array = trace.data
    
    # Apply the fourier transformation to the arrays
    fft = np.fft.rfft(array)
    
    # Amplitude spectrum
    ampspec = np.abs(fft)
    
    # Compute the frequency bins
    # (one is sufficient for all traces: same length, same dt):
    freqs = np.fft.rfftfreq(array.size, d=trace.stats.delta)

    # Smoothing:
    ampspec_smooth = ko_smooth(ampspec, freqs)

    return freqs, ampspec_smooth


def hv_spectrum(h_ampspec1, h_ampspec2, v_ampspec):
    """
    Hv spectrum i.e. the ration between the mean of the two horizontal spectra
    and the vertical spectrum
    
    :param h_ampspec1: the amplitude spectrum from the first horizontal
        component (see :func:`smoothed_amspec`)
    :param h_ampspec2: the amplitude spectrum from the second horizontal
        component (see :func:`smoothed_amspec`)
    :param v_ampspec: the amplitude spectrum from the vertical component
        (see :func:`smoothed_amspec`)
    
    :return: a numpy array (same size of the passed amplitude spectra)
        representing the hv spectrum
    """
    # Horizontal components mean:
    h_ampspec_mean = np.sqrt(h_ampspec1**2 + h_ampspec2**2)
    # divide the two components:
    return np.divide(h_ampspec_mean, v_ampspec)