import random
import numpy as np
import matplotlib.pyplot as plt


def gaussian(mean, coord, std_dev):
    return np.e ** (-((mean - coord) ** 2) / (2 * std_dev ** 2))


def calculate_coord_with_gauss(mean, std_dev):
    while True:
        gaussian_threshold = int(random.uniform(0, 1) * 1000) / 1000.0
        coord = random.uniform(-300, 300)
        gaus_result = gaussian(mean, coord, std_dev)
        if gaus_result >= gaussian_threshold:
            return coord


class Zone:
    def __init__(self, mean_x, mean_y, std_dev_x, std_dev_y, no_of_points, noise_ratio=0.1):
        self.mean_x = mean_x
        self.mean_y = mean_y
        self.std_dev_x = std_dev_x
        self.std_dev_y = std_dev_y
        self.no_of_points = no_of_points

    def scattered_points(self):
        points = []
        for _ in range(self.no_of_points):
            point_x = calculate_coord_with_gauss(self.mean_x, self.std_dev_x)
            point_y = calculate_coord_with_gauss(self.mean_y, self.std_dev_y)
            points.append((point_x, point_y))
        return points

class Centroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


blue_zone = Zone(180, 220, 10, 10, 3333)
red_zone = Zone(-100, 110, 20, 10, 3333)
yellow_zone = Zone(210, -150, 20, 10, 3333)

for zone, color in zip([blue_zone, red_zone, yellow_zone], ['b', 'r', 'y']):
    points = zone.scattered_points()
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, c=color, marker='.', s=1)

# Set the limits for the x and y axes
plt.xlim(-300, 300)
plt.ylim(-300, 300)

# Label the axes and add a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Plane Scatter Plot with Noise')

# Show the plot on the screen
plt.show()
