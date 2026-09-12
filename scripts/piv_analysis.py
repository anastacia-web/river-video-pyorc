from pathlib import Path
import inspect
import pyorc

video_path = Path("data/raw/my_river_video.mp4")
camera_config_path = Path("data/config/camera_config.json")

if not video_path.exists():
    raise FileNotFoundError("Place the own river video in data/raw/.")

if not camera_config_path.exists():
    raise FileNotFoundError(
        "Camera calibration is not available yet. Prepare a real camera configuration first."
    )

cam_config = pyorc.load_camera_config(str(camera_config_path))
video = pyorc.Video(str(video_path), camera_config=cam_config)
frames = video.get_frames()
frames_obj = pyorc.Frames(frames)

print("pyorc version:", pyorc.__version__)
print("project signature:", inspect.signature(frames_obj.project))
print("get_piv signature:", inspect.signature(frames_obj.get_piv))

# Enable only after verifying the signatures in the installed environment:
#
# projected = frames_obj.project(method="numpy", resolution=0.01)
# piv = frames_obj.get_piv(
#     window_size=(25, 25),
#     overlap=(12, 12),
#     search_area_size=(25, 25),
#     engine="numba",
# )
