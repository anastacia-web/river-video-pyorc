# Troubleshooting

## Mamba not recognized
Use a Miniforge/Mamba prompt or initialize Mamba:

```cmd
mamba shell init --shell cmd.exe --root-prefix=%USERPROFILE%.local\share\mamba
```

## Cartopy issue
Install Cartopy through conda-forge:

```cmd
mamba install -c conda-forge cartopy
```

## Wrong Jupyter Python
Run:

```python
import sys
print(sys.executable)
```

It should point to `pyorc_env`.

## API differences
Inspect methods:

```python
print(dir(video))
print(dir(frames_obj))
```

Inspect signatures:

```python
import inspect
print(inspect.signature(frames_obj.project))
print(inspect.signature(frames_obj.get_piv))
```

## Frames object
If `get_frames()` returns an xarray DataArray:

```python
frames_obj = pyorc.Frames(frames)
```

## Transect
The transect stage is **IN PROGRESS** because the dataset required `xcoords`, `ycoords`, and `zcoords`. Do not report transect results until these are correctly associated with real cross-section information.

## No calibration
Optical flow can show image-space movement, but it cannot by itself provide calibrated river velocity in m/s.
