import matplotlib.pyplot as plt
import numpy as np
import random as random

"""Random walk """

class Walk:
    def __init__(self):
        self.x0 = 0
        self.y0 = 0
        print("The initial values are x = " + str(self.x0) + "and y = " + str(self.y0))

class Random(Walk):
    def __init__(self):
        super().__init__()
        self.x0 = 0
        self.y0 = 0

    def randomwalkloop(self):

        """Initialise a seed, and deltas"""
        #random.seed(123)
        del_x = random.randint(-1,1)
        del_y = random.randint(-1,1)
        L_norm = ((del_x ** 2) + (del_y ** 2)) ** 0.5
        if L_norm == 0:
            return self.x0, self.y0

        del_x_norm = (1/ L_norm) * del_x
        del_y_norm = (1 / L_norm) * del_y

        self.x0 += del_x_norm
        self.y0 += del_y_norm

        return self.x0,self.y0

    def walker(self):
        x_coor = [self.x0]
        y_coor = [self.y0]

        for i in range(num_steps):
            x, y = self.randomwalkloop()
            x_coor.append(x)
            y_coor.append(y)

        return x_coor,y_coor

        # Plot the random walk
        # plt.figure(figsize=(10, 6))
        # plt.plot(x_coor, y_coor, linestyle='-', marker='', color='blue', label="Random Walk Path")
        # plt.scatter(x_coor[0], y_coor[0], color='green', label="Start Point")  # Start point
        # plt.scatter(x_coor[-1], y_coor[-1], color='red', label="End Point")  # End point
        # plt.title("2D Random Walk")
        # plt.xlabel("X-coordinate")
        # plt.ylabel("Y-coordinate")
        # plt.legend()
        # plt.grid(True)
        # plt.show()

seedling, num_steps = 123, 1000

plt.figure(figsize=(10, 6))
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

for seeding in range(seedling, seedling+10, 1):
    random.seed(seeding)
    WalkerInstance = Random()
    x_coords, y_coords = WalkerInstance.walker()
    plt.plot(x_coords, y_coords, linestyle='-', marker='', color=colors[seeding % len(colors)], label=f"Walk {seeding + 1}")

    # Mark start and end points for each walk
    plt.scatter(x_coords[0], y_coords[0], color='black', s=20)  # Start point
    plt.scatter(x_coords[-1], y_coords[-1], color=colors[seeding % len(colors)], s=20)  # End point

# Customize plot
plt.title("Multiple 2D Random Walks")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.legend()
plt.grid(True)
plt.show()