# This file is, of course, just a copy of the tutorial given in the Discord
# channel. Because I have been doing something for the past week, while very
# little, I do want to at least get something pushed to the GitHub and this
# is it. I will be working on the actual assignment that, for some reason,
# I missed over the past week of discussion in the Discord. I apoligize in
# advance for my insolence but unfortunately, right now, this is all I have to
# show.

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

points = {"blue": [[2,4,3], [1,3,5], [2,3,1], [3,2,3], [2,1,6]],
          "red": [[5,6,5], [4,5,2], [4,6,1], [6,6,1], [5,4,6], [10,10,4]]}

new_point = [10,3,2]

def euclidean_distance(p, q):
    return np.sqrt(np.sum((np.array(p) - np.array(q)) ** 2))

class KNearestNeighbors:
    def __init__(self, k=3):
        self.k = k
        self.point = None

    def fit(self, points):
        self.points = points

    def predict(self, new_point):
        distances = []

        for category in self.points:
            for point in self.points[category]:
                distance = euclidean_distance(point, new_point)
                distances.append([distance, category])

        categories = [category[1] for category in sorted(distances)[:self.k]]
        result = Counter(categories).most_common(1)[0][0]
        return result

clf = KNearestNeighbors()
clf.fit(points)
print(clf.predict(new_point))

# Visualize

fig = plt.figure(figsize=(15,12))
ax = fig.add_subplot(projection="3d")
ax.grid(True, color = "#323232")
ax.set_facecolor("black")
ax.figure.set_facecolor("#121212")
ax.tick_params(axis="x", color="white")
ax.tick_params(axis="y", color="white")

for point in points['blue']:
    ax.scatter(point[0], point[1], point[2], color="#104DCA", s=60)

for point in points['red']:
    ax.scatter(point[0], point[1], point[2], color="#FF0000", s=60)

new_class = clf.predict(new_point)
color = "#FF0000" if new_class == "red" else "#104DCA"

ax.scatter(new_point[0], new_point[1], new_point[2], color=color, marker="*", s=200, zorder = 100)

for point in points['blue']:
    ax.plot([new_point[0], point[0]], [new_point[1], point[1]], [new_point[2], point[2]], color="#104DCA", linestyle="--", linewidth=1)

for point in points['red']:
    ax.plot([new_point[0], point[0]], [new_point[1], point[1]], [new_point[2], point[2]], color="#FF0000", linestyle="--", linewidth=1)

plt.show()