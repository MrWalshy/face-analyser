import cv2 as cv
import sys

# Get path of image
# img_path = input("Please enter the relative path:\n")
img_path = sys.argv[1]
original_img = cv.imread(img_path)

# Create grayscale version of original image for Viola-Jones Obj Detection
grayscale_img = cv.cvtColor(original_img, cv.COLOR_BGR2GRAY)

# Create the cascade obj for face-detection
face_cascade = cv.CascadeClassifier('./haarcascade_frontalface_alt.xml')

# Detect and store detected faces
detected_faces = face_cascade.detectMultiScale(grayscale_img)

# Iterate over the detected faces, applying a rectangle on the original img for each
# rectangle
for (column, row, width, height) in detected_faces:
    cv.rectangle(
        original_img,
        (column, row),
        (column + width, row + height),
        (0, 255, 0),
        2
    )

# Display the modified original_image
cv.imshow('Image', original_img) # Displays the img
cv.waitKey(0) # Waits for a keystroke, arg '0' waits indefinitely
cv.destroyAllWindows() # Closes the window