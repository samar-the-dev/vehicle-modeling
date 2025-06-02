import numpy as np
from kinematic_bicycle.model import Bicycle


def generate_circular_trajectory(time_end=20, radius=10):
    model = Bicycle()
    t_data = np.arange(0, time_end, model.sample_time)
    x_data = np.zeros_like(t_data)
    y_data = np.zeros_like(t_data)

    for i in range(t_data.shape[0]):
        x_data[i] = model.xc
        y_data[i] = model.yc

        if model.delta < np.arctan(model.L/radius):
            model.step(np.pi, model.w_max)
        else:
            model.step(np.pi, 0)

    return x_data, y_data


def generate_eight_figure_trajectory(time_end=30, radius=8):
    model = Bicycle()
    t_data = np.arange(0, time_end, model.sample_time)
    x_data = np.zeros_like(t_data)
    y_data = np.zeros_like(t_data)
    v_data = np.zeros_like(t_data)
    w_data = np.zeros_like(t_data)

    v_data[:] = 2 * 2 * np.pi * radius / time_end
    delta = np.arctan(model.L / radius)
    w_data[0:350] = model.w_max
    w_data[350:1800] = -model.w_max

    w_data[1800:3000] = model.w_max

    for i in range(t_data.shape[0]):
        x_data[i] = model.xc
        y_data[i] = model.yc
        if w_data[i] > 0:
            if model.delta < delta:
                model.step(v_data[i], w_data[i])
            else:
                model.step(v_data[i], 0)
        else:
            if model.delta > -delta:
                model.step(v_data[i], w_data[i])
            else:
                model.step(v_data[i], 0)
    return x_data, y_data
