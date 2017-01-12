#from Pipeline import Pipeline
from steamworks_rail import steamworks_rail
from PIL import Image
import cv2


camera_port = 1

#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)

# Captures a single image from the camera and returns it in PIL format
def get_image():
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im

# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
     temp = get_image()
     print("Taking image...")

# Take the actual image we want to keep
camera_capture = get_image()

file = "test_image.png"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)

# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)


mypip = steamworks_rail()
mypip.set_source0(camera_capture)
mypip.process()

#img = Image.fromarray(mypip.hsv_threshold_output())
cv2.imwrite("resize.png", mypip.cv_resize_output)

print mypip.hsl_threshold_output
cv2.imwrite("hsltest.png", mypip.hsl_threshold_output)

#print mypip.find_contours_output
#cv2.imwrite("contourstest.png", mypip.find_contours_output)


contours= sorted(mypip.find_contours_output, key=cv2.contourArea, reverse=True)[:10]
print ""
print " **** Sorted Contours ******"
print contours

screenContour = None

# loop over our contours
resize_img = mypip.cv_resize_output
for c in contours:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # if our approximated contour has four points, then
    # we can assume that we have found our screen
    if len(approx) == 4:
        screenContour = approx
        cv2.drawContours(resize_img, [screenContour], -1, (0, 255, 0), 3)
        print "rectangle:", screenContour




cv2.imwrite("steamworks.png", resize_img)

