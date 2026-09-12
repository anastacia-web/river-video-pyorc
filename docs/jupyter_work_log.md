# Jupyter Work Log – Own River Video

This document explains what is included in `notebooks/river_analysis.ipynb`. The notebook was updated to preserve the actual analysis sequence used with `IMG_9373 (1).MOV`.

## Included actual workflow
1. Environment/version check
2. Project-relative video path check
3. PyORC video loading
4. Frame 30 display
5. Frame 0→30 pixel-difference test
6. Difference-map display
7. Short PyORC video test (frames 0–60)
8. `get_frames()` calibration error documented
9. Individual frame loading
10. Farneback optical flow for frame 0→30
11. Optical-flow quiver plot
12. Water-region movement test
13. Focused water ROI test
14. Strong-movement threshold (>2 pixels)
15. Focused water ROI quiver plot
16. Five frame-pair consistency test
17. Overall average movement
18. Average X/Y image movement
19. Calibrated PyORC stage marked TO BE COMPLETED
20. Velocity/quality filtering marked TO BE COMPLETED
21. Transect/surface/bulk/discharge marked IN PROGRESS

## Recorded own-video optical-flow results
- Overall average movement: 6.8960485 pixels
- Average X movement: +2.7479858 pixels
- Average Y movement: -0.7804416 pixels

These are image-space optical-flow results. They are not calibrated m/s measurements and should not be reported as river velocity or discharge.

## Important exclusion
The Ngwerere sample video was used only for PyORC learning/testing. It is not included as the user's project dataset or final results.
