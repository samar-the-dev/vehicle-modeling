import matplotlib.pyplot as plt
from kinematic_bicycle.trajectories import generate_circular_trajectory, generate_eight_figure_trajectory

def generate_trajectory(trajectory_func, label):
    x_data, y_data = trajectory_func()
    plt.plot(x_data, y_data, label=label)

if __name__ == "__main__":
    # generate_trajectory(generate_circular_trajectory, "Circular")
    generate_trajectory(generate_eight_figure_trajectory, "Eight Figure")
    plt.legend()
    plt.axis("equal")
    plt.title("Kinematic Bicycle Model Trajectory")
    plt.show()