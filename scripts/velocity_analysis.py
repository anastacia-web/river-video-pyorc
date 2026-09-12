import numpy as np

def velocity_magnitude(vx, vy):
    return np.sqrt(vx**2 + vy**2)

def quality_filter(velocity, s2n, corr, s2n_min=3, corr_min=0.2):
    mask = (s2n >= s2n_min) & (corr >= corr_min)
    return velocity.where(mask) if hasattr(velocity, "where") else np.where(mask, velocity, np.nan)

# After loading the own calibrated PIV:
# velocity = velocity_magnitude(piv.v_x, piv.v_y)
# print("Mean:", float(velocity.mean()))
# print("Maximum:", float(velocity.max()))
# print("Minimum:", float(velocity.min()))
# velocity_filtered = quality_filter(velocity, piv.s2n, piv.corr)
