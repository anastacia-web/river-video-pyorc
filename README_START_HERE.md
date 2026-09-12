# START HERE

This is the ready-to-use Visual Studio Code folder for the river-video PyORC project.

## Open it

Open the folder **river-video-pyorc** in Visual Studio Code.

Then open:

`notebooks/river_analysis.ipynb`

Select the **Python (pyorc_env)** kernel and run the cells from top to bottom.

## Your video

Your actual river video is already placed in:

`data/raw/IMG_9373 (1).MOV`

The notebook automatically finds the project folder, so you do not need to type a complicated Windows path.

## Important

The Ngwerere example is not included as project data. It was only used for PyORC learning/testing.

Calibrated velocity, PIV, transect, bulk velocity, and discharge remain **To be completed** until real camera/GCP and cross-section information are available.


## Jupyter notebook contents

The main notebook `notebooks/river_analysis.ipynb` now contains the complete recorded workflow used with the own river video, including frame checks, optical-flow tests, ROI tests, quiver plots, consistency tests, and the recorded image-space results. See `docs/jupyter_work_log.md` for the list.
