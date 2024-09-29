import numpy as np
import cv2

def l0_distance(img1, img2):
    """
    Calculate the L0 distance between two images.

    Parameters:
    img1 (numpy.ndarray): First image.
    img2 (numpy.ndarray): Second image.

    Returns:
    int: L0 distance.
    """
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")

    # Calculate the difference between the two images
    diff = img1 - img2

    # Count the number of non-zero elements in the difference
    l0_dist = np.count_nonzero(diff)

    return l0_dist


def l2_distance(img1, img2):
    """
    Calculate the L2 distance between two images.

    Parameters:
    img1 (numpy.ndarray): First image.
    img2 (numpy.ndarray): Second image.

    Returns:
    float: L2 distance.
    """
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")

    # Calculate the squared difference between the two images
    diff = img1 - img2
    squared_diff = np.square(diff)

    # Sum all the squared differences
    sum_squared_diff = np.sum(squared_diff)

    # Take the square root of the sum to get the L2 distance
    l2_dist = np.sqrt(sum_squared_diff)

    return l2_dist


def l1_distance(img1, img2):
    """
    Calculate the L1 distance between two images.

    Parameters:
    img1 (numpy.ndarray): First image.
    img2 (numpy.ndarray): Second image.

    Returns:
    float: L1 distance.
    """
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")

    # Calculate the absolute difference between the two images
    diff = np.abs(img1 - img2)

    # Sum all the absolute differences
    l1_dist = np.sum(diff)

    return l1_dist


def linf_distance(img1, img2):
    """
    Calculate the L∞ (Chebyshev) distance between two images.

    Parameters:
    img1 (numpy.ndarray): First image.
    img2 (numpy.ndarray): Second image.

    Returns:
    float: L∞ distance.
    """
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")

    # Calculate the absolute difference between the two images
    diff = np.abs(img1 - img2)

    # Find the maximum absolute difference
    linf_dist = np.max(diff)

    return linf_dist


def naive_distance(img1, img2):
    """
    Calculate the naive distance between two images.

    Parameters:
    img1 (numpy.ndarray): First image.
    img2 (numpy.ndarray): Second image.

    Returns:
    float: naive distance.
    """
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")

    # Calculate the absolute difference between the two images
    naive_dist = img1 - img2
    # calculate number of pixels changes
    naive_dist = np.count_nonzero(naive_dist)

    return naive_dist


# Load two images (grayscale)
img1 = cv2.imread("lion.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("lion3.png", cv2.IMREAD_GRAYSCALE)

distance = naive_distance(img1, img2)
print(f"L0 distance: {distance}")
