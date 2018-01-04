from matplotlib import pyplot as plt

class plotdata(object):
    def __init__(self, data, theoretical_limit, kwargs):
        self.data = data
        self.theoretical_limit = theoretical_limit
        self.kwargs = kwargs

class Plotter(object):
    def __init__(self, xmin, xmax, xlabel=None, ylabel=None):
        self.data = []
        self.xmin = xmin
        self.xmax = xmax

        self.yticks = []
        self.xticks = []

        self.xlabel = xlabel
        self.ylabel = ylabel

    def add_plot(self, ydata, theoretical_limit=None, **kwargs):
        ydata_len = len(ydata)
        x_range = self.xmax-self.xmin+1
        if ydata_len != x_range:
            raise Exception("y-data length (%d) must match given x-data range (%d)" \
                            % (len(ydata), x_range))
        self.data.append(plotdata(ydata, theoretical_limit, kwargs))

    def add_yticks(self, yticks):
        self.yticks += yticks

    def add_xticks(self, xticks):
        self.xticks = xticks

    def plot(self, show_plot=True, export_file=None):
        # Create a new figure of size 16x9 points, using 80 dots per inch
        plt.figure(figsize=(16,9), dpi=80)

        # Create a new subplot from a grid of 1x1
        plt.subplot(111)

        x = range(self.xmin, self.xmax+1)
        for pdata in self.data:
            plt.plot(x, pdata.data, **pdata.kwargs)
            if pdata.theoretical_limit is not None:
                if "color" in pdata.kwargs:
                    plt.plot(x, [pdata.theoretical_limit]*len(x), color=pdata.kwargs["color"],
                             linestyle=":")
                else:
                    plt.plot(x, [pdata.theoretical_limit]*len(x), linestyle=":")

        #plot ticks
        if self.xticks:
            plt.xticks(self.xticks)
        if self.yticks:
            plt.yticks(self.yticks)

        #set axes
        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data',0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data',0))

        # set axes labels
        if self.xlabel:
            plt.xlabel(self.xlabel)
        if self.ylabel:
            plt.ylabel(self.ylabel)

        plt.legend(loc='upper right', frameon=False)

        if export_file is not None:
            plt.savefig(export_file)
        if show_plot:
            plt.show()

def float_range(start, stop, step):
    r = []

    start = float(start)
    stop = float(stop)
    step = float(step)

    curr = start
    while curr <= stop:
        r.append(curr)
        curr += step
    return r
