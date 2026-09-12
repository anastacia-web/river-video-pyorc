# Methodology

## Video
The own river video is the actual dataset. It was recorded with a handheld phone approximately 8–10 m from the water, with some camera movement.

## Calibration
PyORC needs camera/georeferencing information including GCPs, CRS, reference elevation, camera parameters, resolution, and orientation. No values are invented.

## Projection

```python
projected = frames_obj.project(method="numpy", resolution=0.01)
```

Verify the installed signature first.

## PIV

```python
piv = frames_obj.get_piv(
    window_size=(25, 25),
    overlap=(12, 12),
    search_area_size=(25, 25),
    engine="numba"
)
```

Verify the installed signature first.

## Velocity

```python
velocity = np.sqrt(piv.v_x**2 + piv.v_y**2)
```

## Quality filter

```python
quality_mask = (piv.s2n >= 3) & (piv.corr >= 0.2)
velocity_filtered = velocity.where(quality_mask)
```

## Discharge

Transect geometry, depth/elevation, calibrated velocity, and a justified surface-to-depth correction are required before discharge can be calculated.
