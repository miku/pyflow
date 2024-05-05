"""
 * Python script to demonstrate Canny edge detection.
 *
 * usage: python canny_edge.py <filename> <sigma> <low_threshold> <high_threshold>
"""
import skimage
import skimage.feature
from skimage.viewer import ImageViewer
import sys

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

filename = sys.argv[1]
sigma = 0.5 if len(sys.argv) < 3 else float(sys.argv[2])
low_threshold = 0.5 if len(sys.argv) < 4 else float(sys.argv[3])
high_threshold = 0.8 if len(sys.argv) < 5 else float(sys.argv[4])

image = skimage.io.imread(fname=filename, as_gray=True)
viewer = ImageViewer(image=image)
viewer.show()

edges = skimage.feature.canny(
    image=image,
    sigma=sigma,
    low_threshold=low_threshold,
    high_threshold=high_threshold,
)

viewer = skimage.viewer.ImageViewer(edges)
viewer.show()
