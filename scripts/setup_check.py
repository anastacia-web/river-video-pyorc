import inspect
import sys
import cv2
import pyorc

print("Python:", sys.executable)
print("pyorc:", pyorc.__version__)
print("OpenCV:", cv2.__version__)
print("pyorc module:", pyorc.__file__)

print("Frames/Video names:", [x for x in dir(pyorc) if "Frame" in x or "Video" in x])

if hasattr(pyorc, "Frames"):
    print("pyorc.Frames signature:", inspect.signature(pyorc.Frames))
