import glob
import os
import time

import matplotlib.pyplot as plt
from numpy import linspace, max


def remove_png_files():
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)


def generate_plt():
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not cached

    plotfile = os.path.join('./static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile


def bmi(weight, height):
    return weight / (height * height) * 703.0


def compute_bmi(weight, height):
    w = linspace(weight - 30, weight + 30, 61)
    y = bmi(w, height)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(w, y)
    plt.title('BMI as a function of weight.')
    remove_png_files()
    return generate_plt()


def cholesterol_risk(hdl, ldl, gender):
    if gender == 'female':
        multiplier = 0.95
    else:
        multiplier = 1.05
    excess_ldl = (ldl - 100) / 100.0
    excess_hdl = (hdl - 50) / 100.0
    return (0.03 + excess_ldl**3 - excess_hdl**3) * multiplier**3


def stroke_risk(sys_bp):
    excess = (sys_bp - 120) / 100.0
    return 0.03 + excess**3


def compute_cholesterol_risk(hdl, ldl, gender):

    ldl_base = linspace(ldl - 30, ldl + 30, 61)
    hdl_base = linspace(hdl - 30, hdl + 30, 61)
    y_ldl = cholesterol_risk(hdl, ldl_base, gender)
    y_hdl = cholesterol_risk(hdl_base, ldl, gender)

    fig, axs = plt.subplots(2, constrained_layout=True)
    axs[0].plot(ldl_base, y_ldl, 'tab:red')
    axs[0].set_title('[FAKE DATA] Heart Attack Risk before age 70 as a function of LDL')
    axs[0].set(xlabel='LDL (mg/dL)', ylabel='Heart Attack Probability')

    multiplier = 1
    if gender == 'female':
        multiplier = 1.1

    ylim_ldl = max(y_ldl)*multiplier
    ylim_hdl = max(y_hdl) * multiplier

    axs[0].set_ylim(0.0, ylim_ldl)
    axs[1].set_ylim(0.0, ylim_hdl)

    axs[1].plot(hdl_base, y_hdl, 'tab:green')
    axs[1].set_title('[FAKE DATA] Heart Attack Risk before age 70 as a function of HDL')
    axs[1].set(xlabel='HDL (mg/dL)', ylabel='Heart Attack Probability')

    #fig.tight_layout()

    remove_png_files()

    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile
    # plt.figure()  # needed to avoid adding curves in plot
    # plt.plot(ldl_base, y_ldl)
    # # plt.plot(hdl_base, y_hdl)
    # plt.title('[FAKE DATA] Heart Attack Risk before age 70 as a function of hdl and ldl.')
    # remove_png_files()
    # ldl_plt = generate_plt(plt)
    #
    # plt.figure()  # needed to avoid adding curves in plot
    # plt.plot(hdl_base, y_hdl)
    # plt.title('[FAKE DATA] Heart Attack Risk before age 70 as a function of hdl and ldl.')
    # hdl_plt = generate_plt(plt)
    # return ldl_plt, hdl_plt


def compute_stroke_risk(sys_bp):
    base_line = linspace(sys_bp - 30, sys_bp + 30, 61)
    y = stroke_risk(base_line)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(base_line, y)
    plt.title('[FAKE DATA] Stroke Risk before age 70 as a function of sys bp.')
    remove_png_files()
    return generate_plt()


def compute_heart_attack_risk(sys_bp):
    base_line = linspace(sys_bp - 30, sys_bp + 30, 61)
    y = stroke_risk(base_line)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(base_line, y)
    plt.title('[FAKE DATA] Heart Attack Risk before age 70 as a function of sys bp.')
    remove_png_files()
    return generate_plt()

