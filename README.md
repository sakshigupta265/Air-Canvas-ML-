# Air-Canvas-ML-

  ### Algorithm:

- Start reading the frames and convert the captured frames to HSV color space (Easy for color detection).
- Prepare the canvas frame
- Adjust the track bar values for finding the mask of the colored marker (here, I used yellow color).
- Preprocess the mask with morphological operations (Eroding and dilation).
- Detect the contours, find the center coordinates of largest contour and keep storing them in the array for successive frames (Arrays for drawing points on canvas).
- Finally draw the points stored in an array on the frames and canvas.
