# Setup

```cmd
mamba shell init --shell cmd.exe --root-prefix=%USERPROFILE%.local\share\mamba
mamba create -n pyorc_env python pip
mamba activate pyorc_env
mamba install -c conda-forge cartopy
python -m pip install pyopenrivercam
python -m pip install jupyterlab ipykernel opencv-python numpy pandas matplotlib xarray
python -m ipykernel install --user --name pyorc_env --display-name "Python (pyorc_env)"
jupyter lab
```

Verify in Jupyter:

```python
import sys
import pyorc
print(sys.executable)
print(pyorc.__version__)
```

The executable should point to `pyorc_env`.

**Version note:** the supplied project specification targets pyorc 0.9.9, while the earlier learning environment used 0.5.3. Check the actual environment before using version-sensitive API calls.
