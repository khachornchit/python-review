import numpy as np


def create_random_3d(thickness, width, length):
    return np.random.randint(0, 1000, size=(thickness, width, length))


def create_step_array(start, stop, step):
    return np.arange(start=10, stop=1000, step=50)


if __name__ == '__main__':
    matrix3d = create_random_3d(2, 5, 1000000)
    # print(matrix3d)
    print('matrix3d shape = ', matrix3d.shape)

    arrange = create_step_array(start=10, stop=1000, step=50)
    print('arrange matrix = ', arrange)
