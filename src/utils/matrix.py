from numba import njit
from src.shared.typings import GrayImage


@njit(cache=True, fastmath=True)
def hasMatrixInsideOther(matrix: GrayImage, other: GrayImage) -> bool:
    totalTextPixels = 0
    matchedPixels = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if other[i][j] == 0:
                totalTextPixels += 1
                val = matrix[i][j]
                if val == 0 or val == 113 or val == 29 or val == 57 or val == 91 or val == 152 or val == 170 or val == 192:
                    matchedPixels += 1
    if totalTextPixels == 0:
        return True
    return (matchedPixels / totalTextPixels) >= 0.88

