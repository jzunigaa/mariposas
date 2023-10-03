class libraries:
  def __init__(self):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import pywt
    import pywt.data
    import os
    import cv2
    from cvxopt import matrix, solvers
    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
    from sklearn.metrics import classification_report
    from scipy import stats
    from PIL import Image
    from skimage import exposure
    from skimage.feature import hog
    print('clase ejecutada')

if __name__ == '__main__':
    lib = libraries()
