# Workflow

The project sequence is:

Setup → JupyterLab → pyorc installation → own video loading → camera configuration → frame extraction → projection → PIV → velocity → quality filtering → cross-section → transect → surface velocity → bulk velocity → discharge → graphs → final results.

The own video was tested first using OpenCV optical flow. Five intervals were tested: 0–30, 30–60, 60–90, 90–120, and 120–150.

Overall average image movement: **6.8960485 pixels**.

Average image-space components: **X = +2.7479858 pixels**, **Y = -0.7804416 pixels**.

These are not calibrated river velocities.
