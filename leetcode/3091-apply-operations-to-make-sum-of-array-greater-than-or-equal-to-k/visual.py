import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Solution:
    def plot_operations(self, k: int):
        x_values = []  # number_of_addition
        y_values = []  # number_of_duplication
        z_values = []  # num_of_addition + num_of_duplication

        for i in range(k):
            num_of_addition = i
            num_of_duplication = math.ceil(k / (i + 1)) - 1
            x_values.append(num_of_addition)
            y_values.append(num_of_duplication)
            z_values.append(num_of_addition + num_of_duplication)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(x_values, y_values, z_values)

        ax.set_xlabel("Number of Addition")
        ax.set_ylabel("Number of Duplication")
        ax.set_zlabel("Total Operations Required")
        ax.set_title("visualize min ops to make sum >= k")

        # Find minimum value and its indices
        min_value = min(z_values)
        min_index = z_values.index(min_value)
        min_x = x_values[min_index]
        min_y = y_values[min_index]

        # Annotate minimum value
        ax.text(
            min_x,
            min_y,
            min_value,
            f"Min: {min_value}\nAddition: {min_x}\nDuplication: {min_y}",
            color="red",
            fontsize=10,
        )

        plt.show()


# Usage:
solution = Solution()
solution.plot_operations(300)  # Change the argument as needed
