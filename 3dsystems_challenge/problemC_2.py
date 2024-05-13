import matplotlib.pyplot as plt

def plot_intervals(intervals):
    for i, interval in enumerate(intervals):
        plt.plot([interval[0], interval[1]], [i, i], linewidth=5)
    
    plt.xlabel('Value')
    plt.ylabel('Interval')
    plt.title('Visualization of Intervals')
    plt.yticks(range(len(intervals)), [f'Interval {i+1}' for i in range(len(intervals))])
    plt.ylim(-1, len(intervals))
    plt.grid(True)
    plt.show()

# Example usage:
#intervals = [(57, 94), (82, 91), (67, 90), (3, 64), (18, 34), (58, 81), (59, 100), (22, 74), (20, 90), (87, 97)]
intervals = [[55, 83], [29, 44], [60, 71], [45, 81], [19, 95], [20, 66]]
intervals.sort(key=lambda x: x[1])
plot_intervals(intervals)
