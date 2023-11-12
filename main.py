import io
import math
import random
from pprint import pprint

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


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
            points.append(Point(point_x, point_y))
        return points


class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


class Centroid:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


def generate_points(zones):
    all_points = []
    for zone in zones:
        points = zone.scattered_points()
        all_points.extend(points)
    return all_points


def draw_plot():
    x_coords, y_coords, colors = zip(*[(point.x, point.y, point.color) for point in all_points])
    points_plot.scatter(x_coords, y_coords, c=colors, marker='.', s=1)
    x_coords, y_coords, colors = zip(*[(centroid.x, centroid.y, centroid.color) for centroid in all_centroids])
    points_plot.scatter(x_coords, y_coords, c=colors, marker='o', s=200)
    points_plot.set_xlim(-300, 300)
    points_plot.set_ylim(-300, 300)
    points_plot.set_xlabel('X-axis')
    points_plot.set_ylabel('Y-axis')
    points_plot.set_title('2D Plane Scatter Plot with Noise')
    plt.draw()


def calculate_point_color_from_nearest_centroid():
    for point in all_points:
        mix_dist = 99999
        closest_centroid = None
        for centroid in all_centroids:
            distance = calc_euclidian_distance(point, centroid)
            if mix_dist > distance:
                mix_dist = distance
                closest_centroid = centroid
        point.color = closest_centroid.color

def calculate_centroid_position_from_wheight_center():
    for centroid in all_centroids:
        average_x = 0,
        average_y = 0
        for point in all_points:
            if centroid.color == point.color:
               #TODO Calculaate average of x, y and centroid (x,y)



def calc_euclidian_distance(point, ce   ntroid):
    return math.sqrt((point.x - centroid.x) ** 2 + (point.y - centroid.y) ** 2)


def k_mean_callback(event):
    points_plot.cla()
    calculate_point_color_from_nearest_centroid()
    calculate_centroid_position_from_wheight_center()
    draw_plot()


blue_zone = Zone(180, 220, 10, 10, 3333)
red_zone = Zone(-100, 110, 20, 10, 3333)
yellow_zone = Zone(210, -150, 20, 10, 3333)

blue_centroid = Centroid(100, 100, 'blue')
red_centroid = Centroid(170, 120, 'red')
yellow_centroid = Centroid(10, 250, 'yellow')

zones = [blue_zone, red_zone, yellow_zone]
all_centroids = [blue_centroid, red_centroid, yellow_centroid]

fig, points_plot = plt.subplots()
all_points = generate_points(zones)
draw_plot()

axes = plt.axes([0.0, 0.0, 0.1, 0.05])
k_mean_button = Button(axes, 'K mean')
k_mean_button.on_clicked(k_mean_callback)

# Show the plot on the screen
plt.show()
