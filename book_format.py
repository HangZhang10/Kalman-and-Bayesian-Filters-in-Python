# -*- coding: utf-8 -*-
from IPython.core.display import HTML
import matplotlib.pylab as pylab

def load_style():
    styles = open("./styles/custom2.css", "r").read()
    return HTML(styles)


pylab.rcParams['figure.figsize'] = 12,6
pylab.rcParams['axes.color_cycle'] = '348ABD, 7A68A6, A60628, 467821, CF4457, 188487, E24A33'
pylab.rcParams['lines.linewidth'] = 1

pylab.rcParams['lines.antialiased'] = True
pylab.rcParams['patch.linewidth'] = 0.5
pylab.rcParams['patch.facecolor'] = '348ABD' #blue
pylab.rcParams['patch.edgecolor'] = 'eeeeee'
pylab.rcParams['patch.antialiased'] = True
pylab.rcParams['font.family'] = 'monospace'
pylab.rcParams['font.size'] = 10.0
pylab.rcParams['font.monospace'] = 'Andale Mono, Nimbus Mono L, Courier New, Courier, Fixed, Terminal, monospace'
pylab.rcParams['axes.facecolor'] = 'eeeeee'
pylab.rcParams['axes.edgecolor'] = 'bcbcbc'
pylab.rcParams['axes.linewidth'] = 1
pylab.rcParams['axes.grid'] = True
pylab.rcParams['axes.titlesize'] = 'x-large'
pylab.rcParams['axes.labelsize'] = 'large'
pylab.rcParams['axes.labelcolor'] = '555555'
pylab.rcParams['axes.axisbelow'] = True
pylab.rcParams['axes.color_cycle'] = '348ABD, 7A68A6, A60628, 467821, CF4457, 188487, E24A33'
pylab.rcParams['xtick.major.pad'] = 6
pylab.rcParams['xtick.minor.size'] = 0
pylab.rcParams['xtick.minor.pad'] = 6
pylab.rcParams['xtick.color'] = '555555'
pylab.rcParams['ytick.direction'] = 'in'
pylab.rcParams['legend.fancybox'] = True
pylab.rcParams['figure.facecolor'] = '0.85'
pylab.rcParams['figure.edgecolor'] = '0.50'
pylab.rcParams['figure.subplot.hspace'] = 0.5
