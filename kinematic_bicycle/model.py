import numpy as np


class Bicycle():
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0

        self.L = 2  # wheelbase length
        self.lr = 1.2  # Distance from rear axle to the center of mass
        self.w_max = 1.22  # Maximum steering angle rate (rad/s)

        self.sample_time = 0.01

    def step(self, v, w):
        w = min(w, self.w_max)

        # kinematic model equations
        xc_dot = v * np.cos(self.theta + self.beta)
        yc_dot = v * np.sin(self.theta + self.beta)
        theta_dot = v * np.cos(self.beta) * np.tan(self.delta) / self.L

        # Integrate motion
        self.xc += xc_dot * self.sample_time
        self.yc += yc_dot * self.sample_time
        self.theta += theta_dot * self.sample_time

        # Update slip angle and steering angle
        self.beta = np.arctan(self.lr * np.tan(self.delta) / self.L)
        self.delta += w * self.sample_time
