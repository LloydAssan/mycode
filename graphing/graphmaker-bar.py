#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import matplotlib.pyplot as plt
import numpy as np

def main():

    labels = ['LeBron James', 'Stephen Curry', 'Giannas The Greek Freak']
    points = [20, 34, 30]
    assists_rebounds = [8.0, 6.4, 13.3]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, points, width, label='Points')
    rects2 = ax.bar(x + width/2, assists_rebounds, width, label='Assists')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Points')
    ax.set_title('Top 3 NBA player stats')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()
    # display the graph
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/mycode/graphing/nbastats.png")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/nbastats.png")




if __name__ == "__main__":
    main()
