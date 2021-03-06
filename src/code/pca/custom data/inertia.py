"""
    compute the inertia
    of a dataset related to a given axis
"""
import numpy as np
import matplotlib.pyplot as plt


def orthogonal_projection(vector, axis):
    inner_product = np.dot(vector, axis)
    projected_vector = inner_product*axis
    return projected_vector


# load and center the data
pca_data = np.load("pca_data.npy")
x_data = pca_data[:, 0]
y_data = pca_data[:, 1]
x_mean = np.mean(x_data)
y_mean = np.mean(y_data)
# center the data
x_data = x_data-np.mean(x_data)
y_data = y_data-np.mean(y_data)
pca_data = np.column_stack((x_data, y_data))
# plot the data
plt.plot(x_data, y_data, "o", color="olivedrab", markersize="3")
plt.savefig("centered data.pdf")

def test_axis(axis, x_data, y_data):
    """
        function used to evaluate the inertia
        of the data related to an axis.
        we assume the data are centered.
    """
    # normalize the axis
    axis = 1/np.linalg.norm(axis)*axis
    # check if vector is normed
    # print(np.linalg.norm(axis))

    # plot the data
    plt.plot(x_data, y_data, "o", color="olivedrab", markersize="3")

    # plot the axis we want to project on
    coefficient_directeur = axis[1]/axis[0]
    x_axis = np.linspace(-8, 8, 100)
    plt.plot(x_axis, coefficient_directeur*x_axis,
             alpha="0.5",
             color="darkblue",
             label="axis")

    # project each datapoint to the chosen axis
    # and compute the inertia due to this point.
    nb_datapoints = x_data.shape[0]
    inertia = 0
    """
        EDIT THIS LOOP
    """
    for datapoint_index in range(nb_datapoints):
        vector = pca_data[datapoint_index, :]
        projected_vector = orthogonal_projection(vector, axis)
        # check orthogonality
        # print(np.dot(axis, vector-projected_vector))
        #
        # add lines here
        #


    plt.title(f"axis=({axis[0]:.2f}, {axis[1]:.1f}) \ninertia = {inertia:.2f}")
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.savefig(f"images/projection axis=({axis[0]:.2f}, {axis[1]:.2f}).pdf")
    plt.close()


# choose axes and compute the inertia
axis = np.array([3, 1])
test_axis(axis, x_data, y_data,)
