import numpy as np


def getPoly(real, degree):
    x = range(real.size)
    y = real
    '''
    print "*********Math Util**************"
    print x
    print y
    print "********************************"
    '''
    pc, residuals, rank, sv, r = np.polyfit(x, y, degree, full=True)
    '''
    fStraight = np.poly1d(pc)
    fx = np.linspace(0, x[-1], 1000)

    print pc
    print residuals
    print rank
    print sv
    print rcond
    plt.scatter(x, y)
    plt.xlabel("Days")
    plt.ylabel("Values")
    plt.plot(fx, fStraight(fx), linewidth=2)
    plt.autoscale(tight=True)
    plt.grid()
    plt.show()
    '''
    return pc
