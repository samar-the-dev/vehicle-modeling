# vehicle-modeling

This project implements a simple representation of the **Kinematic Bicycle Model**, a fundamental vehicle motion model used in robotics and autonomous driving systems.

The project demonstrates how a vehicle can follow different trajectories such as:
- Circular paths
- Figure-eight paths

The model is implemented in Python using a discrete-time kinematic update step.

The bicycle kinematics equations are:

![Kinematic Model Equations](images/kinematic_equations.png)

Where:
- $\theta$: heading angle
- $\delta$: steering angle
- $\beta$: slip angle
- $v$: linear velocity
- $\omega$: steering rate
- $L$: wheelbase
- $l_r$: distance from rear axle to center

velocity $v$ can be computed as:

![velocity Equation](images/velocity.png)

and the desired steering angle $\delta$ as 

![Steering Angle Equation](images/steering_angle_equation.png)

##  Model Overview

The **Bicycle model** is a simplified representation of a vehicle with two wheels:
- It updates the vehicle’s position and orientation based on steering and velocity commands.
- The model includes parameters such as:
  - Wheelbase (`L`)
  - Rear axle distance (`lr`)
  - Steering constraints (`delta`, `w_max`)
  - Sample time


## 🛠 Requirements

- Python 3.10+
- numpy

You can install dependencies manually or using [Pipenv](https://pipenv.pypa.io/):

```bash
pipenv install
pipenv run python main.py

