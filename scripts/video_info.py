from pathlib import Path
import cv2

video_path = Path("data/raw/my_river_video.mp4")

if not video_path.exists():
    raise FileNotFoundError(
        f"{video_path} not found. Put the own video in data/raw/ and update the path."
    )

cap = cv2.VideoCapture(str(video_path))
if not cap.isOpened():
    raise RuntimeError("OpenCV could not open the video.")

fps = cap.get(cv2.CAP_PROP_FPS)
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Width:", width)
print("Height:", height)
print("FPS:", fps)
print("Frames:", frames)
print("Duration:", frames / fps if fps else None, "seconds")

cap.release()
