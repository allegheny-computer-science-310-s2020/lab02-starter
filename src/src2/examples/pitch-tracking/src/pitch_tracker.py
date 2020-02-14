import cv2
import imutils as im

# Load in the video
# video's original resolution is (1080, 1920)
video_capture = cv2.VideoCapture('New_Videos/pitch01.m4v')

# Defining video codec and creating a VideoWriter object for outputted video
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
writer = cv2.VideoWriter("output01.avi", fourcc, 60, (480, 853), True)

# creating a background subtractor to separate the foreground from background
fgbg = cv2.createBackgroundSubtractorMOG2()

# Arrays to be used for blobs within our region of interest
x_vals = []
y_vals = []
new_keypoints = []

# Begin looping
while(True):
    grabbed, frame = video_capture.read()

    if not grabbed:
        break

    # Resizing the viewing window to 480x853
    my_window = 'Pitch'
    cv2.namedWindow(my_window, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(my_window, (480, 853))

    # Resize the video but keep the same aspect ratio
    resized_vid = im.resize(frame, width=480)

    # Rotate the video to be played at the correct viewing angle
    angle = 0
    normal_vid = im.rotate(resized_vid, angle)

    # creating a copy of the normal video
    tracking_vid = normal_vid
    blob_vid = normal_vid

    # Convert the video to grayscale
    gray_vid = cv2.cvtColor(normal_vid, cv2.COLOR_BGR2GRAY)

    # Blurring the grayscale video. This part is optional
    blur_vid = cv2.medianBlur(gray_vid, 7)

    # Applying the background subtraction to the gray_vid
    fgmask = fgbg.apply(gray_vid)

    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 4
    params.maxArea = 100

    # Filter by Color
    params.filterByColor = True
    params.blobColor = 255

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.8

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.9

    # Detect blobs
    blob_detector = cv2.SimpleBlobDetector_create(params)
    # detect the blobs in the fgmask2 video
    keypoints = blob_detector.detect(fgmask)

    # Setting the region of interest to ensure that we are detecting blobs
    # in the area of the baseball
    x1 = 220
    x2 = 315
    y1 = 290
    y2 = 400

    # draws the region of interest, only used for testing
    # cv2.rectangle(tracking_vid, (x1, y1), (x2, y2), (200,0,0), 2)
    # drawing the strikezone as a rectangle
    sx1 = 277
    sx2 = 295
    sy1 = 357
    sy2 = 385
    cv2.rectangle(tracking_vid, (sx1, sy1), (sx2, sy2), (255, 255, 255), 1)

    # Outline blobs with a green circle if in the ROI
    for coordinates in keypoints:
        x = coordinates.pt[0]
        y = coordinates.pt[1]
        if x > x1 and x < x2 and y > y1 and y < y2:
            x_vals.append(x)
            y_vals.append(y)

    # This new_keypoints is an array of tuples where each tuple is
    # an x,y coordinate of a blob detected inside the ROI
    new_keypoints = zip(x_vals, y_vals)

    new_keypoints_list = list(new_keypoints)

    for pts in new_keypoints_list:
        x_pt = pts[0]
        y_pt = pts[1]
        # outline the points with a green circle.
        # This circle will appear around the baseball
        cv2.circle(tracking_vid, (int(x_pt), int(y_pt)), 3, (0, 255, 0), -1)

    writer.write(tracking_vid)

    # These are the all of the videos that should be viewed
    # cv2.imshow(my_window, blob_vid)
    cv2.imshow(my_window, tracking_vid)
    # cv2.imshow(my_window, gray_vid)
    # cv2.imshow(my_window, fgmask)

    if cv2.waitKey(64) & 0xFF == ord('q'):
        break

end = len(new_keypoints_list) - 1
v1 = new_keypoints_list[end][0]
v2 = new_keypoints_list[end][1]

if v1 > sx1 and v1 < sx2 and v2 > sy1 and v2 < sy2:
    print("STRIKE")
else:
    print("BALL")

# Release everything when finished
video_capture.release()
# output.release()
cv2.destroyAllWindows()
