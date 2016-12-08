from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import pylab


def input_files(filename):
    x, y, z = [], [], []
    with open(filename, 'r') as f:
        for line in f:
            line.split()

            x.append(line.split()[0])
            y.append(line.split()[1])
            z.append(float(line.split()[2]) * -1)

    print 'x : ', x
    print 'y: ', y
    print 'z: ', z

    fig = pylab.figure()
    ax = Axes3D(fig)
    ax.scatter(x, y, z)
    pyplot.show()


def main():
    input = raw_input("Enter name of file")
    input_files(input)


if __name__ == '__main__': main()

