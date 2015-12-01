# -*- coding: utf-8 -*-
"""
This example demonstrates the use of ImageView, which is a high-level widget for 
displaying and analyzing 2D and 3D data. ImageView provides:

  1. A zoomable region (ViewBox) for displaying the image
  2. A combination histogram and gradient editor (HistogramLUTItem) for
     controlling the visual appearance of the image
  3. A timeline for selecting the currently displayed frame (for 3D data only).
  4. Tools for very basic analysis of image data (see ROI and Norm buttons)

"""

import numpy as np
import scipy
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import cv2 

app = QtGui.QApplication([])

## Create window with ImageView widget
win = QtGui.QMainWindow()
win.resize(800,800)
imv = pg.ImageView()
win.setCentralWidget(imv)
win.show()
win.setWindowTitle('pyqtgraph example: ImageView')

## Create random 3D data set with noisy signals
img = scipy.ndimage.gaussian_filter(np.random.normal(size=(200, 200)), (5, 5)) * 20 + 100
img = img[np.newaxis,:,:]
decay = np.exp(-np.linspace(0,0.3,100))[:,np.newaxis,np.newaxis]
data = np.random.normal(size=(100, 200, 200))
data += img * decay
data += 2

## Add time-varying signal
"""
sig = np.zeros(data.shape[0])
sig[30:] += np.exp(-np.linspace(1,10, 70))
sig[40:] += np.exp(-np.linspace(1,10, 60))
sig[70:] += np.exp(-np.linspace(1,10, 30))

sig = sig[:,np.newaxis,np.newaxis] * 3
data[:,50:60,50:60] += sig
"""
data = cv2.imread("C:\\Users\\analyst\\Documents\\Data_science\\pyside_blog\\lena.jpg")
data2 = cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
cols,rows,n= data2.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(data2,M,(cols,rows))
## Display the data and assign each frame a time value from 1.0 to 3.0
"""
imv.setImage(data, xvals=np.linspace(1., 3., data.shape[0]))
"""
imv.setImage(dst)
## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
