import numpy as np
from numpy import poly1d
from scipy import special
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy import optimize

from scipy.fftpack import fft
from scipy.signal import blackman

import scopes_namespaces as scoNam
import Complex
import C, DerivedClassName, Mapping

from pandas import DataFrame
from pandas.util.print_versions import show_versions
import pandas as pd



def example_one():
    ## call manual about submodule
    print(np.info(optimize.fmin))

    ## index tricks
    a = np.concatenate(([3], [0]*5, np.arange(-1, 1.002, 2/9.0)))
    print(a)
    a = np.r_[3, [0]*5, -1:1:10j]
    print(a)    # same output, easier syntax

    b = np.mgrid[0:5,0:5]
    print(b)
    b = np.mgrid[0:5:4j]
    print(b)


# working with polynom
def example_two():
    # 1-d polynomials
    # create polynomial 3x^2 + 4x + 5
    p = poly1d([3,4,5])
    print(p)

    # multiple two polynomial equation
    x = p * p
    print(x)

    # integrate
    z = p.integ(k=6)
    print(z)

    # derivative
    y = p.deriv()
    print(y)

    # x^5 - x^3 + 1 and result
    x = poly1d([1,0,-1,0,0,1])
    print(x)
    print(x.deriv())

    print(p([4,5]))

def example_three():
    # create array of items in interval
    x = np.r_[-15:30]
    print(x)

    # select special items from interval
    y = np.select([x > 3, x >= 0], [0, x+2])
    print(y)

def drumhead_height(n, k, distance, angle, t):
    kth_zero = special.jn_zeros(n,k)[-1]
    return np.cos(t) * np.cos(n*angle) * special.jn(n, distance * kth_zero)

# special example for figure
def example_four():
    theta = np.r_[0:2*np.pi:50j]
    radius = np.r_[0:1:50j]
    x = np.array([r * np.cos(theta) for r in radius])
    y = np.array([r * np.sin(theta) for r in radius])
    z = np.array([drumhead_height(1,1,r,theta,0.5) for r in radius])

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(x,y,z,rstride=1,cstride=1, cmap=cm.jet)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def example_five():
    N = 600 #  number of sample points
    T = 1.0 / 800.0 # sample spacing
    x = np.linspace(0.0, N*T, N)
    y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5*np.sin(80.0*np.pi*x)
    yf = fft(y)
    w = blackman(N)
    ywf = fft(y*w)
    xf = np.linspace(0.0, 1.0/(2.0*T),N/2)

    plt.semilogy(xf[1:N/2], 2.0/N * np.abs(yf[1:N/2]), '-b')
    plt.semilogy(xf[1:N/2], 2.0/N * np.abs(ywf[1:N/2]), '-r')
    plt.legend(['FFT', 'FFT w. window'])
    plt.grid()
    plt.show()

def example_six():
    t = scoNam.scopeTestClass()
    t.scope_test()

    x = Complex.Complex(3.0, -4.5)
    print(x.r, x.i)

    # this usually only server to confuse the reader of program
    print(C.C.g(self=C.C))

    # example of inheritance [dedenie]
    c = DerivedClassName.DerivedClassName()
    print(c.i, c.r)

    """private variables"""
    t = Mapping.Mapping(iterable=[15, 16, 17])
    t.update(iterable=[14])
    print(t.item_list)

    # instance of empty class
    emplo = Mapping
    emplo.Employee()

    emplo.name = "Fero"
    emplo.vorname = "Mrkvicka"
    emplo.age = 23
    emplo.salary = 1000

def example_seven():
    # df = DataFrame()
    # show_versions()
    dtypes = ['int64', 'float64', 'datetime64[ns]', 'timedelta64[ns]',
              'complex128', 'object', 'bool']
    n = 5000

    data = dict([ (t, np.random.randint(100, size=n).astype(t))
                   for t in dtypes])

    df = pd.DataFrame(data)
    df['categorical'] = df['object'].astype('category')
    # df.info()
    df.memory_usage()

def example_eight():
    s = pd.Series([1,3,5,np.nan,6,8])
    print(s)
    dates = pd.date_range('20130101', periods=6)
    print(dates)
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
    print(df)



def main():
    print("Hello main")

    #example_one()
    #example_two()
    #example_three()
    #example_four()
    #example_five()
    #example_six()
    # example_seven()
    #example_eight()


if __name__ == '__main__':
    main()


