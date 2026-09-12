# River Video PyORC Analysis

This repository documents my actual development journey using **pyOpenRiverCam (pyorc)** for river-video analysis.

## Objectives

The project aims to process my own river video and, after proper camera/georeferencing and cross-section information are available, estimate:

1. River surface velocity
2. Velocity direction and magnitude
3. Cross-section/transect information
4. Bulk/depth-averaged velocity
5. River discharge in m³/s
6. Graphs and visualizations

The official **Ngwerere** example was used only for learning/testing pyorc. It is **not part of this project's dataset or final results**.

## Current status

- Setup and JupyterLab: completed
- Own river video loading: completed
- Frame extraction: completed
- Uncalibrated optical-flow testing: completed
- Camera calibration/georeferencing for own video: **To be completed**
- PyORC projection/PIV on own video: **To be completed**
- Surface velocity: **To be completed**
- Bulk velocity: **To be completed**
- Discharge: **To be completed**

### Version note

The supplied project specification identifies **pyorc 0.9.9** as the target version. The earlier learning environment used during development was **pyorc 0.5.3**. Because pyorc APIs can change, this repository requires API inspection before version-sensitive operations and does not claim an operation was completed on 0.9.9 unless verified in that environment.

## Technologies

Windows, Miniforge/Mamba, Python, JupyterLab, pyorc, OpenCV, NumPy, Pandas, Matplotlib, Xarray, and Git/GitHub.

Environment:

```text
pyorc_env
```

## Installation

Initialize Mamba for Windows Command Prompt:

```cmd
mamba shell init --shell cmd.exe --root-prefix=%USERPROFILE%.local\share\mamba
```

Create and activate:

```cmd
mamba create -n pyorc_env python pip
mamba activate pyorc_env
```

Cartopy can be installed through Mamba when needed:

```cmd
mamba install -c conda-forge cartopy
```

Install pyOpenRiverCam:

```cmd
python -m pip install pyopenrivercam
```

Install notebook/analysis packages:

```cmd
python -m pip install jupyterlab ipykernel opencv-python numpy pandas matplotlib xarray
```

Register and launch JupyterLab:

```cmd
python -m ipykernel install --user --name pyorc_env --display-name "Python (pyorc_env)"
mamba activate pyorc_env
jupyter lab
```

Verify:

```python
import sys
import pyorc
import cv2

print(sys.executable)
print(pyorc.__version__)
print(cv2.__version__)
```

The Python executable should point to `pyorc_env`.

## Folder structure

```text
river-video-pyorc/
├── README.md
├── requirements.txt
├── environment.yml
├── .gitignore
├── data/
│   ├── raw/
│   ├── config/
│   ├── cross_section/
│   └── processed/
├── notebooks/
│   └── river_analysis.ipynb
├── scripts/
│   ├── setup_check.py
│   ├── video_info.py
│   ├── piv_analysis.py
│   ├── velocity_analysis.py
│   └── discharge_analysis.py
├── results/
│   ├── figures/
│   ├── velocity/
│   └── discharge/
└── docs/
    ├── setup.md
    ├── workflow.md
    ├── methodology.md
    └── troubleshooting.md
```

Large video files are ignored by Git. Put the own video in `data/raw/` locally.

## Own river video

Use a configurable path:

```python
video_path = r"data\raw\my_river_video.mp4"
```

Known conditions:

- Phone was handheld.
- Phone was approximately 8–10 m from the water.
- Some small camera movement was present.
- Exact river width was initially unknown.

These conditions are limitations for calibration and final accuracy.

## Initial own-video test

The own video was successfully loaded and individual frames were read. Initial OpenCV optical-flow testing was used before calibration.

Five frame intervals were tested:

- 0–30
- 30–60
- 60–90
- 90–120
- 120–150

Overall average image movement:

```text
6.8960485 pixels
```

Overall average image-space components:

```text
X = +2.7479858 pixels
Y = -0.7804416 pixels
```

This indicates dominant movement toward the right side of the image with a smaller upward component.

**These are image-space optical-flow measurements only, not calibrated river velocity in m/s.**

## Camera configuration

PyORC needs camera/georeferencing information to convert image coordinates into real-world coordinates.

Relevant information includes:

- Image width and height
- CRS
- Ground Control Points (GCPs)
- Reference elevation
- Camera parameters
- Resolution
- Camera orientation

No camera configuration values are invented for the own video.

## PyORC workflow

```text
SETUP
→ JUPYTERLAB
→ PYORC INSTALLATION
→ VIDEO LOADING
→ CAMERA CONFIGURATION
→ FRAME EXTRACTION
→ PROJECTION
→ PIV
→ VELOCITY
→ QUALITY FILTERING
→ CROSS-SECTION
→ TRANSECT
→ SURFACE VELOCITY
→ BULK VELOCITY
→ DISCHARGE
→ GRAPHS
→ FINAL RESULTS
```

## API troubleshooting

Check the installed API before using version-sensitive methods:

```python
import inspect
print(inspect.signature(...))
```

During development:

- `video.plot()` was attempted but was not available in the installed version.
- `video.get_frames()` returned an xarray `DataArray`.
- The target workflow wraps the DataArray with `pyorc.Frames(frames)`.
- `pyorc.project` was discovered to be a module rather than a callable function.
- The Transect API differed from older examples.
- The transect perspective stage required `xcoords`, `ycoords`, and `zcoords`.

## Projection

Target workflow:

```python
projected = frames_obj.project(
    method="numpy",
    resolution=0.01
)
```

Verify the installed signature before running it.

## PIV

Target configuration:

```python
piv = frames_obj.get_piv(
    window_size=(25, 25),
    overlap=(12, 12),
    search_area_size=(25, 25),
    engine="numba"
)
```

Verify the installed signature first.

Expected outputs include:

- `v_x`
- `v_y`
- `corr`
- `s2n`

## Velocity

```python
velocity = np.sqrt(
    piv.v_x**2 +
    piv.v_y**2
)
```

Final physical velocity values for the own river are **To be completed**.

## Quality filtering

```python
quality_mask = (
    (piv.s2n >= 3) &
    (piv.corr >= 0.2)
)

velocity_filtered = velocity.where(quality_mask)
```

Low-quality vectors should not be treated as reliable velocity measurements.

## Cross-section and transect

Cross-section data can be loaded from:

```python
cs1 = pd.read_csv(r"data\cross_section\cross_section.csv")
```

The actual x, y, and z/elevation values must be supplied from real measurements.

### Transect status

**STATUS: IN PROGRESS**

The PIV dataset contained variables such as:

```text
time, y, x, xp, yp, xs, ys, lon, lat
v_x, v_y, corr, s2n
```

The installed Transect API expected:

```text
xcoords
ycoords
zcoords
```

An attempt to use:

```python
piv.transect.get_transect_perspective()
```

produced:

```text
AttributeError: 'Dataset' object has no attribute 'xcoords'
```

After adding x/y coordinate information, another error showed that `zcoords` was also required.

Required next work:

1. Associate real cross-section coordinates with the PIV dataset.
2. Provide xcoords.
3. Provide ycoords.
4. Provide zcoords.
5. Generate the transect perspective.
6. Verify the physical location across the river.

## Surface velocity

**STATUS: TO BE COMPLETED**

After transect perspective is working, use the exact installed API for the equivalent of:

```python
piv.transect.get_v_surf(...)
```

## Bulk velocity

**STATUS: TO BE COMPLETED**

Surface velocity must be converted to bulk/depth-averaged velocity before discharge.

The target API is:

```python
piv.transect.get_v_bulk(...)
```

The exact signature must be inspected first.

## Discharge

**STATUS: TO BE COMPLETED**

Final target:

```text
m³/s
```

The target API is:

```python
piv.transect.get_q(...)
```

A correction factor of `0.85` appeared in the official learning configuration. It must not automatically be applied to the own data without justification.

Discharge depends on cross-section geometry, depth/elevation, velocity, wetted area, and surface-to-depth correction.

## Visualizations

Planned figures:

- Original river frame
- Projected river frame
- Mean surface velocity
- PIV vector/quiver plot
- Velocity magnitude
- Quality-filtered velocity
- Cross-section
- Transect velocity
- Bulk velocity
- Discharge/river-flow plot

Save figures under `results/figures/`.

```python
plt.savefig(
    "results/figures/velocity_plot.png",
    dpi=300,
    bbox_inches="tight"
)
```

## Final results

| Result | Status |
|---|---|
| Video information | Completed |
| Number of frames | Completed |
| FPS | Completed |
| Resolution | Completed |
| Mean surface velocity | To be completed |
| Maximum surface velocity | To be completed |
| Quality-filtered velocity | To be completed |
| Cross-section information | To be completed |
| Bulk velocity | To be completed |
| Discharge | To be completed |

## Limitations

- Handheld camera movement
- Stabilization requirements
- Unknown river width
- GCP accuracy
- Camera calibration
- Water-surface visibility
- Reflections/glare
- PIV errors
- Need for cross-section measurements
- Need for water-level/elevation information
- Surface velocity is not automatically equal to mean flow velocity
- Discharge accuracy depends strongly on cross-section and depth information

## Reproducibility

1. Install Miniforge/Mamba.
2. Create `pyorc_env`.
3. Install pyorc.
4. Install/run JupyterLab.
5. Clone the repository.
6. Put the own river video in `data/raw/`.
7. Prepare camera configuration.
8. Prepare GCP information.
9. Prepare cross-section data.
10. Load video.
11. Extract frames.
12. Project frames.
13. Calculate PIV.
14. Calculate velocity.
15. Filter velocity.
16. Create transect.
17. Calculate surface velocity.
18. Calculate bulk velocity.
19. Calculate discharge.
20. Generate plots.
21. Save results.

## Reference

Official pyorc repository: https://github.com/localdevices/pyorc

The Ngwerere example is only a learning/reference dataset and is not included as project data.

## License

This repository documents an academic project. PyORC has its own license and should be treated according to the official project license.
