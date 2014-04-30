# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 16:48:21 2014

@author: samarth
"""

import numpy as np

def getHistGray(image):
    assert len(image.shape) == 2, "Must be grayscale image"
    hist = np.zeros(255)
    for row in image:
        for col in row:
            hist[int(col)] += 1
    return hist
    
if __name__ == "__main__":
    import grayscale as gs
    from scipy import misc
    image = misc.imread('flower.jpg')
    grey = gs.convertToGreyScale(image)
    hist = getHistGray(grey)
    print hist