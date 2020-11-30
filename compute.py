import glob
import os
import time

import matplotlib.pyplot as plt
from numpy import exp, cos, linspace


def bmi(weight, height):
    return weight / (height * height) * 703.0


def compute_bmi(weight, height):
    w = linspace(weight - 30, weight + 30, 61)
    y = bmi(w, height)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(w, y)
    plt.title('BMI as a function of weight.')
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not cached
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile


if __name__ == '__main__':
    print(compute(1, 0.1, 1, 20))
