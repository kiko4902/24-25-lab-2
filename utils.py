def remove_noise(img):
    """
    Remove noise from the image

    Args:
    img: image to remove noise from (numpy array, RGB/BGR)

    Returns:
    img_: image with noise removed (numpy array, grayscale)
    """
    img_ = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    return cv.morphologyEx(img_, cv.MORPH_OPEN, kernel)

def bounding_rect(img):
    """
    Get the bounding rectangle of the largest contour in the image

    Args:
    img: image to get bounding rectangle from (numpy array, grayscale)

    Returns:
    rect: bounding rectangle of the largest contour (tuple, (x, y, w, h))
    """
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    rect = cv.boundingRect(contours[0])
    return rect