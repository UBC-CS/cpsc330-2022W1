import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.neighbors import DistanceMetric
from sklearn.manifold import MDS
from scipy.spatial import distance
from sklearn.datasets import make_blobs
from matplotlib.patches import Circle
from sklearn.linear_model import Lasso


def plot_sup_x_unsup(data, w, h):
    """
        Function to generate a supervised vs unsupervised plot.

        Parameters:
        -----------
        data: pd.DataFrame
            A pandas dataframe with X1 and X2 coordinate, and a target column
            for the classes.
        w: int
            Width of the plot
        h: int
            height of the plot
    """
    # Colors to be used (upt to 5 classes)
    colors = np.array(['black', 'blue', 'red', 'green', 'purple'])

    # Getting the column and classes' names
    col_names = data.columns.to_numpy()
    target_names = data['target'].to_numpy()

    # Getting numerical values for the classes labels
    target = np.unique(data['target'].to_numpy(), return_inverse=True)

    # Getting X1 and X2
    data = data.iloc[:, 0:2].to_numpy()

    # Creates the Figure
    plt.figure(0, figsize=(w, h))

    # Create two subplots
    plt.subplots_adjust(right=2.5)

    # Get the first subplot, which is the Supervised one.
    plt.subplot(1, 2, 1)
    ax = plt.gca()
    for i, label in enumerate(target[0]):
        plt.scatter(data[target_names == label, 0],
                    data[target_names == label, 1],
                    c=colors[i], label=label)

    # Creates the legend
    plt.legend(loc='best', fontsize=22, frameon=True)

    # Name the axes and creates title
    plt.xlabel(col_names[0], fontsize=1.5*(w + h))
    plt.ylabel(col_names[1], fontsize=1.5*(w + h))
    plt.title("Supervised", fontdict={'fontsize': 2 * (w + h)})

    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': w + h})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': w + h})

    # Creates the unsupervised subplot.
    plt.subplot(1, 2, 2)
    ax = plt.gca()
    plt.scatter(data[:, 0], data[:, 1])
    plt.title("Unsupervised", fontdict={'fontsize': 2 * (w + h)})
    plt.xlabel(col_names[0], fontsize=1.5*(w + h))
    plt.ylabel(col_names[1], fontsize=1.5*(w + h))
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': w + h})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': w + h})


def plot_unsup(data, w, h, title=None):
    """
    Function to generate unsupervised plot.

    Parameters:
    -----------
    data: pd.DataFrame
        A pandas dataframe with X1 and X2 coordinate. If more than two
        coordinates, only the first two will be used.
    w: int
        Width of the plot
    h: int
        height of the plot
    title: str
        the tile of the plot
    """

    plt.figure(figsize=(w, h))
    ax = plt.gca()
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
    plt.title(title, fontdict={'fontsize': 1.2*(w + h)})
    plt.xlabel(data.columns[0], fontsize=1.2*w)
    plt.ylabel(data.columns[1], fontsize=1.2*w)
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': w})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': w})


def plot_deck(group_by, w, h):
    """
    Parameters:
    -----------
       group_by: str: ['cards', 'color', 'suits']
         How to group the cards
       w: int
         Width of the plot
       h: int
         height of the plot
    """

    values = np.array(np.arange(1, 14))
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    colors = np.array(["black", "red"])
    cards = np.zeros((52, 3), dtype=int)
    cards[:, 0] = np.array(list(range(1, 14)) * 4)  # Value
    cards[:, 1] = np.repeat([1, 2, 3, 4], 13)       # Suits
    cards[:, 2] = np.repeat([1, 2], 26)             # Color

    fig, ax = plt.subplots(figsize=(w, h))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xticks(values)
    ax.set_xticklabels(["A", "2", "3", "4",
                        "5", "6", "7", "8",
                        "9", "10", "J", "Q", "K"],
                       fontsize=16)
    ax.axis("equal")

    if group_by == 'cards':
        ax.scatter(cards[:, 0], cards[:, 1])
        ax.set_xlabel("Value", fontsize=20)
        ax.set_ylabel("Suits", fontsize=20)
        ax.set_yticks(range(1, 5))
        ax.set_yticklabels(suits, fontsize=16)

    if group_by == 'color':
        e1 = np.zeros((52,))
        e1[0:52:2] = .08
        ax.scatter(cards[:, 0] + e1, cards[:, 2])
        ax.set_xlabel("Value", fontsize=20)
        ax.set_ylabel("Color", fontsize=20)
        ax.set_yticks(range(1, 3))
        ax.set_yticklabels(colors, fontsize=16)

    if group_by == 'suits':
        # just adding some noise to separate the points
        e1 = np.random.normal(scale=.05, size=52)
        e2 = np.random.normal(scale=.05, size=52)
        ax.scatter(cards[:, 1] + e1, cards[:, 2] + e2)
        ax.set_xlabel("Suits", fontsize=20)
        ax.set_ylabel("Color", fontsize=20)
        ax.set_xticks(range(1, 5))
        ax.set_xticklabels(suits, fontsize=16)
        ax.set_yticks(range(1, 3))
        ax.set_yticklabels(colors, fontsize=16)


def plot_intial_center(data, centroids, w, h, title=None):
    """
    Plot the initial centroids.

    Parameters:
    -----------
    data: pd.DataFrame
        A pandas dataframe with X1 and X2 coordinate. If more than two
        coordinates, only the first two will be used.
    centroids: pd.DataFrame
        A pandas dataframe composed by k rows of data, chosen randomly. (where k 
        stands for the number of clusters)
    w: int
        width of the plot
    h: int
        height of the plot
    title: str
        the tile of the plot
    """
    n_clusters = centroids.shape[0]

    colors = np.array(['black', 'blue', 'red', 'green', 'purple'])
    data = data.iloc[:, 0:2]
    centroids = centroids.to_numpy()
    plt.figure(figsize=(w, h))
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], s=350,
                marker='*', color=colors[0:n_clusters])
    plt.xlabel(data.columns[0], fontdict={'fontsize': w})
    plt.ylabel(data.columns[1], fontdict={'fontsize': w})
    plt.title(title, fontdict={'fontsize': (w + h)})
    ax = plt.gca()
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': 0.8*w})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': 0.8*w})


def plot_example_dist(data, centroids, w, h, point=None):
    """
    Plot the distance of a point to the centroids.

    Parameters:
    -----------
    data: pd.DataFrame
        A pandas dataframe with X1 and X2 coordinate. If more than two
        coordinates, only the first two will be used.
    centroids: pd.DataFrame
        A pandas dataframe composed by k rows of data, chosen randomly. (where k 
        stands for the number of clusters)
    w: int
        width of the plot
    h: int
        height of the plot
    point: int
        the index of the point to be used to calculate the distance
    """

    colors = np.array(['black', 'blue', 'red', 'green', 'purple'])
    k = centroids.shape[0]
    if point is None:
        point = np.random.choice(range(0, data.shape[0]), size=1)

    point = data.iloc[point, 0:2].to_numpy()[0]
    centroids = centroids.iloc[:, 0:2].to_numpy()

    plt.figure(figsize=(w, h))
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], s=350,
                marker='*', color=['black', 'blue', 'red'])
    plt.xlabel(data.columns[0], fontdict={'fontsize': w})
    plt.ylabel(data.columns[1], fontdict={'fontsize': w})
    plt.scatter(point[0], point[1], c="orange", s=120)

    dist = np.zeros(k)
    for i in range(0, k):
        l = np.row_stack((point, centroids[i, :]))
        dist[i] = np.sum((point-centroids[i, :])**2)**0.5
        plt.plot(l[:, 0], l[:, 1], c=colors[i], linewidth=1, linestyle='-.')
        if (l[0, 1] <= l[1, 1]):
            plt.text(l[1, 0]-.15, l[1, 1]+.05,
                     f"d = {np.round(dist[i], 2)}", color=colors[i],
                     fontdict={'fontsize': (w+h)/2})
        else:
            plt.text(l[1, 0]-.15, l[1, 1]-.11,
                     f"d = {np.round(dist[i], 2)}", color=colors[i],
                     fontdict={'fontsize': (w+h)/2})

    plt.title(f"This point will be assign to the {colors[np.argmin(dist)]}" +
              " cluster", fontdict={'fontsize': w+h})


def plot_first_assignment(data, centroids, dist, w, h):
    """
    Plot the points after the first assignment.

    Parameters:
    -----------
    data: pd.DataFrame
        A pandas dataframe with X1 and X2 coordinate. If more than two
        coordinates, only the first two will be used.
    centroids: pd.DataFrame
        A pandas dataframe composed by k rows of data, chosen randomly. (where k 
        stands for the number of clusters)
    dist: a matrix of distance of each point to all the centroids. 
          [See scipy.spatial.distance.cdist]
    w: int
        width of the plot
    h: int
        height of the plot
    """

    k = centroids.shape[0]
    colors = np.array(['black', 'blue', 'red', 'green', 'purple'])

    plt.figure(figsize=(w, h))
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1],
                c=colors[np.argmin(dist, 1)], alpha=.5)
    plt.scatter(centroids.iloc[:, 0],
                centroids.iloc[:, 1],
                s=300, marker='*', color=colors[0:k])
    plt.xlabel(data.columns[0], fontdict={'fontsize': w})
    plt.ylabel(data.columns[1], fontdict={'fontsize': w})

    plt.title("First round of assignment - Step #1",
              fontdict={'fontsize': w+h})


def plot_update_centroid(data, w, h, new_centroids, centroids, dist):
    colors = np.array(['black', 'blue', 'red', 'green', 'purple'])
    plt.figure(figsize=(w, h))
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1],
                c=colors[np.argmin(dist, 1)], alpha=.25)
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300,
                marker='*', color=['black', 'blue', 'red'])
    plt.xlabel("$X_1$", fontdict={'fontsize': w})
    plt.ylabel("$X_2$", fontdict={'fontsize': w})
    plt.title("Update the centroids - Step #2", fontdict={'fontsize': w+h})
    plt.scatter(new_centroids[:, 0], new_centroids[:, 1],
                s=300, marker='*', color=['black', 'blue', 'red'])

    aux = new_centroids-(centroids+(new_centroids-centroids)*0.9)
    aux = np.linalg.norm(aux, axis=1)
    for i in range(0, 3):
        plt.arrow(centroids[i, 0], centroids[i, 1],
                  (new_centroids[i, 0]-centroids[i, 0])*0.8,
                  (new_centroids[i, 1]-centroids[i, 1])*0.8,
                  head_width=.1, head_length=aux[i], fc=colors[i], ec=colors[i])


def plot_iterative(data, w, h, starting_centroid):
    k = starting_centroid.shape[0]
    colors = np.array(['black', 'blue', 'red', 'green', 'purple'])
    x = data.iloc[:, 0:2].to_numpy()
    plt.figure(figsize=(w, h))
    centroids = starting_centroid.copy()
    for i in range(0, 5):
        dist = distance.cdist(x, centroids)
        u = np.zeros((k, x.shape[0]))
        u[np.argmin(dist, axis=1), range(0, 150)] = 1
        new_centroids = u @ x / np.sum(u, 1)[:, None]
        plt.scatter(centroids[:, 0], centroids[:, 1], s=300,
                    marker='*', color=['black', 'blue', 'red'])
        plt.scatter(new_centroids[:, 0], new_centroids[:, 1],
                    s=200, marker='*', color=['black', 'blue', 'red'])

        aux = new_centroids-(centroids+(new_centroids-centroids)*0.9)
        aux = np.linalg.norm(aux, axis=1)
        for i in range(0, 3):
            if aux[i] > .005:
                plt.arrow(centroids[i, 0], centroids[i, 1],
                          (new_centroids[i, 0]-centroids[i, 0])*0.8,
                          (new_centroids[i, 1]-centroids[i, 1])*0.8,
                          head_width=.1, head_length=aux[i], fc=colors[i], ec=colors[i])
        centroids = new_centroids

    plt.scatter(x[:, 0], x[:, 1], c=colors[np.argmin(dist, 1)], alpha=.25)
    plt.xlabel(data.columns[0], fontdict={'fontsize': w})
    plt.ylabel(data.columns[1], fontdict={'fontsize': w})
    plt.title("Iterative process", fontdict={'fontsize': w+h})


def plot_silhouette_dist(w, h):

    n = 30
    df, target = make_blobs(n_samples=n,
                            n_features=2,
                            centers=[[0, 0], [1, 1], [2.5, 0]],
                            cluster_std=.15,
                            random_state=1)

    colors = np.array(['black', 'blue', 'red'])

    plt.figure(figsize=(w, h))
    ax = plt.gca()
    ax.set_ylim(-.45, 1.4)
    ax.set_xlim(-.25, 2.8)
    plt.scatter(df[:, 0], df[:, 1], c=colors[target])

    p = 1
    for i in range(0, n):
        plt.plot((df[p, 0], df[i, 0]), (df[p, 1], df[i, 1]),
                 linewidth=.7, c=colors[target[i]])

    plt.scatter(df[p, 0], df[p, 1], c="lightgreen", zorder=10)

    c1 = Circle((.1, -.12), 0.27, fill=False, linewidth=2, color='black')
    c2 = Circle((1.03, 1.04), 0.27, fill=False, linewidth=2, color='blue')
    c3 = Circle((2.48, 0.1), 0.27, fill=False, linewidth=2, color='red')
    ax.add_artist(c1)
    ax.add_artist(c2)
    ax.add_artist(c3)
    plt.xlabel("X1", fontdict={'fontsize': w})
    plt.ylabel("X2", fontdict={'fontsize': w})
    plt.title("Distances for silhouette", fontdict={'fontsize': w+h})


def mds_plot1(w, h, dist=False):
    """
    Plot three points in a three dimensional space with their distances.

    Parameters:
    -----------
    w: int
       the width of the plot.
    h: int
       the height of the plot.
    """
    x = np.array([[0, 0, 0], [0, 1, 0], [1, 0, 0]])
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x[:, 0], x[:, 1], x[:, 2], s=150,
               color=['black', 'red', 'blue'])
    ax.plot3D(x[:, 0], x[:, 1], x[:, 2])
    ax.plot3D(x[[0, 2], 0], x[[0, 2], 1], x[[0, 2], 2])
    ax.text(x[0, 0]-.15, x[0, 1]-.045, x[0, 2] -
            0.015, '$x_1=(0,0,0)$', fontsize=22)
    ax.text(x[1, 0], x[1, 1]-0.05, x[1, 2]+0.01,
            '$x_2=(0,1,0)$', fontsize=22, color="red")
    ax.text(x[2, 0], x[2, 1]-0.01, x[2, 2]-0.01,
            '$x_3=(0,0,1)$', fontsize=22, color="blue")
    ax.set_title("Three dimensional space", fontsize=30)

    if dist:
        ax.text(x[2, 0], x[2, 1]-0.01, x[2, 2]-0.01,
                '$x_3$', fontsize=22, color="blue")
        ax.text(-.15, 0.5, x[2, 2]-0.01, '$d_{12}=1$',
                fontsize=22, color="green", zdir=(0, 1, -.02))
        ax.text(.4, 0.55, x[2, 2]-0.01, '$d_{23}=\sqrt{2}$',
                fontsize=22, color="green", zdir=(1, -.8, 0))
        ax.text(.35, 0, x[2, 2]-0.015,
                '$d_{13}=1$', fontsize=22, color="green")

    return x


def mds_plot2d(x, w, h, plot_dist=True):

    dist = DistanceMetric.get_metric("euclidean")
    if plot_dist:
        random_state = 4
    else:
        random_state = None

    z = MDS(n_components=2, dissimilarity="euclidean",
            random_state=random_state).fit_transform(x)

    plt.figure(figsize=(16, 8))
    plt.scatter(z[:, 0], z[:, 1], color=["black", 'red', 'blue'])
    plt.plot(z[:, 0], z[:, 1])
    plt.plot(z[[0, 2], 0], z[[0, 2], 1])

    plt.annotate('$z_1$', xy=(z[0, 0], z[0, 1]-.05), fontsize=22)
    plt.annotate('$z_2$', xy=(z[1, 0], z[1, 1]+.015), fontsize=22, color='red')
    plt.annotate('$z_3$', xy=(z[2, 0], z[2, 1]+.015),
                 fontsize=22, color='blue')
    if plot_dist:
        plt.annotate('$d_{13}$=' + str(np.round(dist.pairwise(z)
                                                [0, 2], 2)), xy=(-.1, -.4), fontsize=20, rotation=0)
        plt.annotate('$d_{12}$=' + str(np.round(dist.pairwise(z)
                                                [0, 1], 2)), xy=(-.35, .2), fontsize=20, rotation=75)
        plt.annotate('$d_{23}$=' + str(np.round(dist.pairwise(z)
                                                [1, 2], 2)), xy=(0.1, .2), fontsize=20, rotation=-30)


def make_2d_smile(w=22, h=10, happy=True, plot=True):
    """
    Build a 2d smile face

    Parameters:
    -----------
    w: int
      width of the plot
    h: int
      height of the plot
    happy: bool
      is it a happy smile face?
    plot: bool
      false will just generate the data and return it. True will also plot
    """

    x = np.linspace(-1, 1, 200*w//16)
    y = np.sqrt(1 - x**2)
    y = np.concatenate((y, -np.sqrt(1 - x**2))) + \
        np.random.normal(scale=.05, size=400*w//16)
    x = np.concatenate((x, x))
    data = pd.DataFrame({'x': x, 'y': y, 'class': 0})
    if plot:
        plt.figure(figsize=(w, h))
        plt.scatter(x, y, color="black")

    eyes_x = np.random.normal(scale=.07, loc=0.40, size=50*w//16)
    eyes_y = np.random.normal(scale=.07, loc=0.40, size=50*w//16)
    x = np.concatenate((x, eyes_x))
    x = np.concatenate((x, -eyes_x))
    y = np.concatenate((y, eyes_y))
    y = np.concatenate((y, np.random.normal(
        scale=.07, loc=0.40, size=50*w//16)))
    if plot:
        plt.scatter(eyes_x, eyes_y, color="orange")
        plt.scatter(-eyes_x, eyes_y, color="orange")
    mouth_x = np.linspace(-.5, .5, 100*w//16)
    if happy:
        mouth_y = mouth_x**2 + np.random.normal(scale=.05, size=100*w//16) - .4
    else:
        mouth_y = -mouth_x**2 + \
            np.random.normal(scale=.04, size=100*w//16) - .3

    if plot:
        plt.scatter(mouth_x, mouth_y, color="red")

    x = np.concatenate((x, mouth_x))
    y = np.concatenate((y, mouth_y))
    data = data = pd.DataFrame(np.column_stack((x, y)), columns=['x', 'y'])
    color = np.zeros(data.shape[0])
    color[(400*w//16):(400*w//16+100*22//16)] = 1
    color[(400*w//16 + 100*w//16 - 1):] = 2
    data['color'] = color
    return data


def make_3d_smile(w=22, h=10, happy=True):
    """
    Build a smile face in 3d (actually it creates in 2d and then randomly projects it into 3d space)
    """

    data = make_2d_smile(happy=happy, plot=False)
    data_3d = data.iloc[:, 0:2].to_numpy()
    data_3d = data_3d @ np.random.rand(2, 3)
    data_3d[:, 2] += np.random.normal(scale=.05, size=data.shape[0])
    data_3d = pd.DataFrame(data_3d, columns=['Z1', 'Z2', 'Z3'])
    data_3d['color'] = data['color']
    plt.figure(figsize=(w, h))
    ax = plt.axes(projection='3d')
    ax.scatter3D(data_3d.iloc[:, 0], data_3d.iloc[:, 1],
                 data_3d.iloc[:, 2], c=data['color'].to_numpy())
    return data_3d


def rotate(data, theta):
    r = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    return data @ r


def plot_diagram(x, z):
    """
    Will plot the Original Distances vs Projected Distances

    Parameters:
    -----------
    x: original data
    z: projected data
    """
    dist = DistanceMetric.get_metric("euclidean")

    plt.figure(figsize=(22, 10))
    d1 = dist.pairwise(x).ravel()
    d2 = dist.pairwise(z).ravel()
    plt.scatter(d1, d2, alpha=.05)
    linear = Lasso(alpha=.01)
    linear.fit(d1.reshape(-1, 1), d2.reshape(-1, 1))
    plt.plot(np.linspace(0, np.max(d1), 50), linear.predict(
        np.linspace(0, np.max(d1), 50).reshape(-1, 1)), color="red")
    plt.title("Original Distance vs Projected Distance",
              fontdict={'fontsize': 32})
    plt.xlabel("Original Distance", fontdict={'fontsize': 22})
    plt.ylabel("Projected Distance", fontdict={'fontsize': 22})


def plot_mds_europe_map(eur_dist, w=22, h=10):
    eu_mds = MDS(n_components=2, random_state=106, dissimilarity="precomputed")
    z = eu_mds.fit_transform(eur_dist)
    z = rotate(z, np.deg2rad(-22))
    plt.figure(figsize=(w, h))
    plt.scatter(z[:, 0], z[:, 1])
    for i, city in enumerate(eur_dist.index):
        plt.annotate(city, z[i], fontsize=16)
    plt.axis("equal")
    plt.xticks([])
    plt.yticks([])


def plot_digits_mds(z, digits, w=16, h=10):
    plt.figure(figsize=(w, h))
    plt.xlim(np.min(z[:, 0]), np.max(z[:, 0]))
    plt.ylim(np.min(z[:, 1]), np.max(z[:, 1]))
    colors = ["blue", "purple", "orange", "pink", "coral",
              "yellow", "green", "brown", "red", "black"]
    for i in range(digits.data.shape[0]):
        plt.annotate(digits.target[i].__str__(),
                     z[i], color=colors[digits.target[i]])


def plot_digits_tsne(z, digits, w=16, h=10):
    plt.figure(figsize=(15, 10))
    plt.xlim(np.min(z[:, 0]), np.max(z[:, 0]))
    plt.ylim(np.min(z[:, 1]), np.max(z[:, 1]))
    colors = ["blue", "purple", "orange", "pink", "coral",
              "yellow", "green", "brown", "red", "black"]
    for i in range(digits.data.shape[0]):
        plt.annotate(digits.target[i].__str__(),
                     z[i], color=colors[digits.target[i]])


def plot_1d(x, w, h, main_label=None, x_label=None):
    """
    Makes a 1D plot.
    Params:
    -------
    x:  pd.DataFrame
      a numpy array or pandas dataframe. If more than one column, 
      just the first column will be used.
    w:  int
      width of the figure
    h : int
      height of the figure
    main_label : str, optional
      the title of the plot
    x_label : str, optional
      the title of x-axis
    """

    if x_label is None:
        x_label = x.columns[0]

    x = x.to_numpy()

    fig, ax = plt.subplots(1, 1, figsize=(w, h))  # creates the figure object
    ax.scatter(x[:, 0], np.zeros_like(x[:, 0]))  # Plot the points
    ax.spines['left'].set_visible(False)  # Removes frame's left side
    ax.spines['right'].set_visible(False)  # Removes frame's right side
    ax.spines['top'].set_visible(False)  # Removes frame's top side
    ax.set_title(main_label, fontsize=w+h)
    ax.set_yticks([])  # Here it is just removing the ticks from the y-axis

    # Increases the size of the x-axis ticks labels;
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': 16})
    ax.margins(0)
    # Changes the label of x-axis
    ax.set_xlabel(x_label, fontdict={'fontsize': w})


def plot_2d(x, w, h, main_label=None, x_label=None, y_label=None):
    """
    Makes a 2D plot.
    Params:
    -------
    x:  pd.DataFrame
      a numpy array or pandas dataframe. If more than two columns, 
      just the first two will be used.
    w:  int
      width of the figure
    h : int
      height of the figure
    main_label : str, optional
      the title of the plot
    color: pd.Series
      an array of colors for the points
    x_label : str, optional
      the title of x-axis
    y_label : str, optional
      the title of y-axis
    """

    if x_label is None:
        x_label = x.columns[0]
    if y_label is None:
        y_label = x.columns[1]

    x = x.iloc[:, 0:2].to_numpy()

    plt.figure(figsize=(w, h))  # creates the figure object
    plt.scatter(x[:, 0], x[:, 1])  # Plot the points
    ax = plt.gca()  # Retrieve the axis
    ax.spines['top'].set_visible(False)  # Removes frame's top side
    ax.spines['right'].set_visible(False)  # Removes frame's right side

    # Increasing the size of the x-axis ticks labels;
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': 16})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': 16})

    # Changes the label of x-axis
    ax.set_xlabel(x_label, fontdict={'fontsize': w})
    # Changes the label of y-axis
    ax.set_ylabel(y_label, fontdict={'fontsize': w})
    ax.set_title(main_label, fontsize=w+h)  # Define the title of the plot


def plot_3d(x, w, h, main_label=None, x_label=None, y_label=None, z_label=None):
    """
    Makes a 3D plot.
      height of the figure
    main_label : str, optional
      the title of the plot
    color: pd.Series
      an array of colors for the points
    x_label : str, optional
      the title of x-axis
    y_label : str, optional
      the title of y-axis
    z_label : str, optional
      the title of y-axis
    """

    if x_label is None:
        x_label = x.columns[0]
    if y_label is None:
        y_label = x.columns[1]
    if z_label is None:
        z_label = x.columns[2]

    x = x.iloc[:, 0:3].to_numpy()

    # Creates the figure
    fig = plt.figure(figsize=(w, h))

    # Creates a 3D subplot
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x[:, 0], x[:, 1], x[:, 2])  # Plots a 3d scatter
    ax.spines['top'].set_visible(False)  # Removes frame's to side
    ax.spines['right'].set_visible(False)  # Removes frame's right side

    # Increase the size of the ticks labels;
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': w})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': w})
    ax.set_zticklabels(ax.get_zticks(), fontsize=w, horizontalalignment='left')

    # Changes the axes' labels
    ax.set_xlabel('\n' + x_label, fontdict={'fontsize': 1.2*w},
                  linespacing=3.1)
    ax.set_ylabel('\n' + y_label, fontdict={'fontsize': 1.2*w},
                  linespacing=3.2)
    ax.set_zlabel('\n' + z_label, fontdict={'fontsize': 1.2*w},
                  linespacing=6)
    ax.set_title(main_label, fontsize=w+h)


def plot_reduction3d(data, w, h, drop, main_label=None):
    """
    Makes a 3D plot.
      height of the figure
    main_label : str, optional
      the title of the plot
    color: pd.Series
      an array of colors for the points
    drop: list, optional
      a list with the dimensions to drop
    """

    if type(drop) != int:
        raise ValueError

    drop = [drop]

    labels = np.array([data.columns[0], data.columns[1], data.columns[2]])

    x = data.iloc[:, 0:3].to_numpy()

    fig = plt.figure(figsize=(w, h))  # Creates the figure
    fig.subplots_adjust(wspace=.3)
    ax = [None, None]  # Just a list to control the axis
    ax[0] = fig.add_subplot(1, 2, 1, projection='3d')
    ax[0].scatter(x[:, 0], x[:, 1], x[:, 2], s=30)  # Plots a 3d scatter
    ax[0].spines['top'].set_visible(False)  # Removes frame's to side
    ax[0].spines['right'].set_visible(False)  # Removes frame's right side

    # Increase the size of the ticks labels;
    ax[0].locator_params(axis='x', nbins=8)
    ax[0].locator_params(axis='y', nbins=5)
    ax[0].locator_params(axis='z', nbins=5)
    ax[0].set_xticklabels(ax[0].get_xticks(),
                          fontdict={'fontsize': .75*w},
                          rotation=45)
    ax[0].set_yticklabels(ax[0].get_yticks(), fontdict={'fontsize': .75*w})
    ax[0].set_zticklabels(ax[0].get_zticks(), fontsize=.75*w,
                          horizontalalignment='left')

    # Changes the axes' labels
    ax[0].set_xlabel('\n' + labels[0], fontdict={'fontsize': w},
                     linespacing=6)
    ax[0].set_ylabel('\n' + labels[1], fontdict={'fontsize': w},
                     linespacing=3.2)
    ax[0].set_zlabel('\n' + labels[2], fontdict={'fontsize': w},
                     linespacing=7)
    ax[0].set_title(main_label, fontsize=w+h)
    ax[0].set_xlim(-3, 2)
    ax[0].set_ylim(-2, 2.5)
    ax[0].set_zlim(-2.5, 4)

    # Dropping dimension
    dimensions = set([0, 1, 2])
    dimensions = list(dimensions.difference(drop))
    labels = labels[dimensions]

    # This for will draw the red lines in the plot
    for i in range(0, x.shape[0]):
        proj_point = np.array([-2.8 + 2.8*(len(drop) == 2),
                               2 - 2*(len(drop) == 2),
                               -2], dtype=np.float)
        proj_point[dimensions] = x[i, dimensions]

        ax[0].plot([proj_point[0], x[i, 0]],
                   [proj_point[1], x[i, 1]],
                   [proj_point[2], x[i, 2]],
                   color="red",
                   linestyle="-.",
                   alpha=.5)

    if len(dimensions) == 1:
        x[:, 0] = x[:, dimensions[0]]
        dimensions[0] = 0
        dimensions.append(1)
        x[:, dimensions[1]] = 0

    ax[1] = fig.add_subplot(1, 2, 2)  # Creates the second subplot (a 2D one)
    ax[1].scatter(x[:, dimensions[0]], x[:, dimensions[1]])

    ax[1].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)

    # Define the title of the plot
    ax[1].set_title("Projected points", fontsize=w+h)

    ax[1].set_xticklabels(ax[1].get_xticks(), fontdict={'fontsize': .75*w})

    # Changing axes' labels
    ax[1].set_xlabel("$Z_1 = $" + labels[0], fontdict={'fontsize': w})

    if len(labels) > 1:
        ax[1].set_yticklabels(ax[1].get_yticks(), fontdict={'fontsize': .75*w})
        ax[1].set_ylabel("$Z_2 = $" + labels[1], fontdict={'fontsize': w})
    else:
        ax[1].spines['left'].set_visible(False)  # Removes frame's left side
        ax[1].set_yticks([])


def plot_reduction2d(data, w, h, drop):

    dimension = set([0, 1])
    dimension = list(dimension.difference([drop]))[0]

    x_std = data.to_numpy()

    fig, ax = plt.subplots(1, 2, figsize=(w, h))
    ax[0].scatter(x_std[:, 0], x_std[:, 1], zorder=2)  # Plot the points

    # This for will draw the red lines into the plot
    for i in range(0, x_std.shape[0]):
        if dimension == 0:
            ax[0].plot([x_std[i, 0], x_std[i, 0]], [0, x_std[i, 1]],
                       color="red", linestyle="-.", alpha=.4, zorder=1)
        if dimension == 1:
            ax[0].plot([0, x_std[i, 0]],
                       [x_std[i, 1], x_std[i, 1]],
                       color="red", linestyle="-.", alpha=.4, zorder=1)

    # This line plots the black line
    if dimension == 0:
        ax[0].plot([np.min(x_std[:, 0]),
                    np.max(x_std[:, 0])],
                   [0, 0], color="black", zorder=0)
    if dimension == 1:
        ax[0].plot([0, 0], [np.min(x_std[:, 1]), np.max(x_std[:, 1])],
                   color="black", zorder=0)

    # This line plots the red points
    if dimension == 0:
        ax[0].scatter(x_std[:, 0], np.zeros_like(x_std[:, 0]), color="red")
    if dimension == 1:
        ax[0].scatter(np.zeros_like(x_std[:, 1]), x_std[:, 1], color="red")

    # Editing frame
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)

    # Increases the size of the labels' ticks;
    ax[0].set_xticklabels(ax[0].get_xticks(), fontdict={'fontsize': 16})
    ax[0].set_yticklabels(ax[0].get_yticks(), fontdict={'fontsize': 16})

    # Editing labels
    ax[0].set_xlabel(data.columns[0], fontdict={'fontsize': w})
    ax[0].set_ylabel(data.columns[1], fontdict={'fontsize': w})
    ax[0].set_title("Dropping the column $X_" + str(drop+1) +
                    "$ = " + data.columns[drop], fontsize=w+h)

    # The functions called here are the same as above,
    # but this time is for the plot on the right
    ax[1].scatter(x_std[:, dimension], np.zeros_like(x_std[:, 0]), color="red")
    ax[1].spines['left'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    ax[1].set_title("Projected points", fontsize=w+h)
    ax[1].set_yticks([])
    ax[1].set_xticklabels(ax[1].get_xticks(), fontdict={'fontsize': 16})
    ax[1].set_xlabel("$Z_1 = $" + data.columns[dimension],
                     fontdict={'fontsize': w})

def plot_pca2d(data, w, h, errors=False):

    x_std = data.to_numpy()

    pca = PCA(n_components=2)

    # These are the points in the new space
    z = pca.fit_transform(x_std[:, 0:2])

    # These are the projected points
    v = z[:, 0, None]@pca.components_[None, 0, :]

    # The min and max values of the projected points
    minv, maxv = np.min(v, axis=0)[0],  np.max(v, axis=0)[0]

    fig, ax = plt.subplots(1, 2, figsize=(w, h))
    ax[0].scatter(x_std[:, 0], x_std[:, 1])
    ax[0].plot([minv, maxv], [minv*pca.components_[0, 1]/pca.components_[0, 0],
                              maxv*pca.components_[0, 1]/pca.components_[0, 0]],
               color="red", label="Direction of highest variance")

    error = np.round(np.sum((x_std[:, 0:2]-v)**2), 2)

    if errors:
        # This for will draw the red lines into the plot
        for i in range(0, x_std.shape[0]):
            ax[0].plot([x_std[i, 0], v[i, 0]], [x_std[i, 1], v[i, 1]],
                       color="red", linestyle="-.", alpha=.4)
        ax[0].scatter(v[:, 0], v[:, 1], color="red")

    # Removes frame's sides
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)

    # Increase the size of the ticks labels;
    ax[0].set_xticklabels(ax[0].get_xticks(), fontdict={'fontsize': 16})
    ax[0].set_yticklabels(ax[0].get_yticks(), fontdict={'fontsize': 16})

    # Changes the labels
    ax[0].set_xlabel(data.columns[0], fontdict={'fontsize': w})
    ax[0].set_ylabel(data.columns[1], fontdict={'fontsize': w})
    ax[0].set_title(f"PCA - projection error:{error}", fontsize=w+h)
    ax[0].legend(fontsize=w, loc="lower right")

    ax[1].scatter(z, np.zeros_like(z), color="red")
    ax[1].spines['left'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    var = np.round(np.var(z, axis=0)[0], 4)
    ax[1].set_title(f"Projected points (var: {var})", fontsize=w+h)
    ax[1].set_yticks([])  # Here it is just removing the ticks from the y-axis
    ax[1].set_xticklabels(ax[1].get_xticks(), fontdict={'fontsize': 16})
    ax[1].set_xlabel("$Z_1 = $" + str(np.round(pca.components_[0, 0], 4)) +
                     " x " + data.columns[0] + " + " + str(np.round(pca.components_[0, 1], 4)) +
                     " x " + data.columns[1], fontdict={'fontsize': w})

    return ax


def plot_pca_mult_solutions2d(data, w, h):

    x_std = data

    # Create a PCA object
    pca = PCA(n_components=2)

    # Fit and transform the pca object
    pca.fit(x_std[:, 0:2])

    fig, ax = plt.subplots(1, 1, figsize=(w, h))
    ax.axis("equal")

    # Plots the black arrow
    ax.quiver(pca.components_[0, 0], pca.components_[0, 1])

    # Plots the red arrow
    ax.quiver(-1*pca.components_[0, 0], -1*pca.components_[0, 1], color="red")

    ax.scatter(x_std[:, 0], x_std[:, 1])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': 16})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': 16})

    return ax


def plot_pca_rotation2d(data, w, h):

    x_std = data.iloc[:, 0:2].to_numpy()

    pca = PCA(n_components=2)
    z = pca.fit_transform(x_std)

    fig, ax = plt.subplots(1, 2, figsize=(w, h))
    ax[0].scatter(x_std[:, 0], x_std[:, 1], alpha=.4)
    ax[0].axis("equal")
    ax[0].quiver(pca.components_[0, 0], pca.components_[0, 1],
                 color="black", label="Direction 1nd PC")
    ax[0].quiver(pca.components_[1, 0], pca.components_[
                 1, 1], color="red", label="Direction 2nd PC")
    ax[0].spines['top'].set_visible(False)  # Removes the top side of the frame
    # Removes the right side of the frame
    ax[0].spines['right'].set_visible(False)
    # Increase the size of the x-axis ticks labels;
    ax[0].set_xticklabels(ax[0].get_xticks(), fontdict={'fontsize': 16})
    # Increase the size of the y-axis ticks labels;
    ax[0].set_yticklabels(ax[0].get_yticks(), fontdict={'fontsize': 16})
    # Define the title of the plot
    ax[0].set_title(f"Original data", fontsize=w+h)
    ax[0].legend(fontsize=w, loc="lower right")
    ax[0].set_xlabel("$X_1$")
    ax[0].set_ylabel("$X_2$")

    ax[1].scatter(z[:, 0], z[:, 1])
    ax[1].axis("equal")
    ax[1].spines['top'].set_visible(False)  # Removes the top side of the frame
    # Removes the right side of the frame
    ax[1].spines['right'].set_visible(False)
    # Increase the size of the x-axis ticks labels;
    ax[1].set_xticklabels(ax[1].get_xticks(), fontdict={'fontsize': 16})
    # Increase the size of the y-axis ticks labels;
    ax[1].set_yticklabels(np.round(ax[1].get_yticks(), 2),
                          fontdict={'fontsize': 16})
    # Define the title of the plot
    ax[1].set_title(f"Transformed data", fontsize=w+h)
    ax[1].set_xlabel("$Z_1$")
    ax[1].set_ylabel("$Z_2$")


def plot_1d(x, w, h, main_label=None, x_label=None):
    """
    Makes a 1D plot.

    Params:
    -------
    x:  pd.DataFrame
      a numpy array or pandas dataframe. If more than one column, 
      just the first column will be used.
    w:  int
      width of the figure
    h : int
      height of the figure
    main_label : str, optional
      the title of the plot
    x_label : str, optional
      the title of x-axis
    """

    if x_label is None:
        x_label = x.columns[0]

    x = x.to_numpy()

    fig, ax = plt.subplots(1, 1, figsize=(w, h))  # creates the figure object
    ax.scatter(x[:, 0], np.zeros_like(x[:, 0]))  # Plot the points
    ax.spines['left'].set_visible(False)  # Removes frame's left side
    ax.spines['right'].set_visible(False)  # Removes frame's right side
    ax.spines['top'].set_visible(False)  # Removes frame's top side
    ax.set_title(main_label, fontsize=w+h)
    ax.set_yticks([])  # Here it is just removing the ticks from the y-axis

    # Increases the size of the x-axis ticks labels;
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': 16})
    ax.margins(0)
    # Changes the label of x-axis
    ax.set_xlabel(x_label, fontdict={'fontsize': w})


def plot_2d(x, w, h, main_label=None, x_label=None, y_label=None):
    """
    Makes a 2D plot.

    Params:
    -------
    x:  pd.DataFrame
      a numpy array or pandas dataframe. If more than two columns, 
      just the first two will be used.
    w:  int
      width of the figure
    h : int
      height of the figure
    main_label : str, optional
      the title of the plot
    color: pd.Series
      an array of colors for the points
    x_label : str, optional
      the title of x-axis
    y_label : str, optional
      the title of y-axis
    """

    if x_label is None:
        x_label = x.columns[0]
    if y_label is None:
        y_label = x.columns[1]

    x = x.iloc[:, 0:2].to_numpy()

    plt.figure(figsize=(w, h))  # creates the figure object
    plt.scatter(x[:, 0], x[:, 1])  # Plot the points
    ax = plt.gca()  # Retrieve the axis
    ax.spines['top'].set_visible(False)  # Removes frame's top side
    ax.spines['right'].set_visible(False)  # Removes frame's right side

    # Increasing the size of the x-axis ticks labels;
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': 16})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': 16})

    # Changes the label of x-axis
    ax.set_xlabel(x_label, fontdict={'fontsize': w})
    # Changes the label of y-axis
    ax.set_ylabel(y_label, fontdict={'fontsize': w})
    ax.set_title(main_label, fontsize=w+h)  # Define the title of the plot


def plot_3d(x, w, h, main_label=None, x_label=None, y_label=None, z_label=None):
    """
    Makes a 3D plot.

      height of the figure
    main_label : str, optional
      the title of the plot
    color: pd.Series
      an array of colors for the points
    x_label : str, optional
      the title of x-axis
    y_label : str, optional
      the title of y-axis
    z_label : str, optional
      the title of y-axis
    """

    if x_label is None:
        x_label = x.columns[0]
    if y_label is None:
        y_label = x.columns[1]
    if z_label is None:
        z_label = x.columns[2]

    x = x.iloc[:, 0:3].to_numpy()

    # Creates the figure
    fig = plt.figure(figsize=(w, h))

    # Creates a 3D subplot
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x[:, 0], x[:, 1], x[:, 2])  # Plots a 3d scatter
    ax.spines['top'].set_visible(False)  # Removes frame's to side
    ax.spines['right'].set_visible(False)  # Removes frame's right side

    # Increase the size of the ticks labels;
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': w})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': w})
    ax.set_zticklabels(ax.get_zticks(), fontsize=w, horizontalalignment='left')

    # Changes the axes' labels
    ax.set_xlabel('\n' + x_label, fontdict={'fontsize': 1.2*w},
                  linespacing=3.1)
    ax.set_ylabel('\n' + y_label, fontdict={'fontsize': 1.2*w},
                  linespacing=3.2)
    ax.set_zlabel('\n' + z_label, fontdict={'fontsize': 1.2*w},
                  linespacing=6)
    ax.set_title(main_label, fontsize=w+h)


def plot_reduction3d(data, w, h, drop, main_label=None):
    """
    Makes a 3D plot.

      height of the figure
    main_label : str, optional
      the title of the plot
    color: pd.Series
      an array of colors for the points
    drop: list, optional
      a list with the dimensions to drop
    """

    if type(drop) != int:
        raise ValueError

    drop = [drop]

    labels = np.array([data.columns[0], data.columns[1], data.columns[2]])

    x = data.iloc[:, 0:3].to_numpy()

    fig = plt.figure(figsize=(w, h))  # Creates the figure
    fig.subplots_adjust(wspace=.3)
    ax = [None, None]  # Just a list to control the axis
    ax[0] = fig.add_subplot(1, 2, 1, projection='3d')
    ax[0].scatter(x[:, 0], x[:, 1], x[:, 2], s=30)  # Plots a 3d scatter
    ax[0].spines['top'].set_visible(False)  # Removes frame's to side
    ax[0].spines['right'].set_visible(False)  # Removes frame's right side

    # Increase the size of the ticks labels;
    ax[0].locator_params(axis='x', nbins=8)
    ax[0].locator_params(axis='y', nbins=5)
    ax[0].locator_params(axis='z', nbins=5)
    ax[0].set_xticklabels(ax[0].get_xticks(),
                          fontdict={'fontsize': .75*w},
                          rotation=45)
    ax[0].set_yticklabels(ax[0].get_yticks(), fontdict={'fontsize': .75*w})
    ax[0].set_zticklabels(ax[0].get_zticks(), fontsize=.75*w,
                          horizontalalignment='left')

    # Changes the axes' labels
    ax[0].set_xlabel('\n' + labels[0], fontdict={'fontsize': w},
                     linespacing=6)
    ax[0].set_ylabel('\n' + labels[1], fontdict={'fontsize': w},
                     linespacing=3.2)
    ax[0].set_zlabel('\n' + labels[2], fontdict={'fontsize': w},
                     linespacing=7)
    ax[0].set_title(main_label, fontsize=w+h)
    ax[0].set_xlim(-3, 2)
    ax[0].set_ylim(-2, 2.5)
    ax[0].set_zlim(-2.5, 4)

    # Dropping dimension
    dimensions = set([0, 1, 2])
    dimensions = list(dimensions.difference(drop))
    labels = labels[dimensions]

    # This for will draw the red lines in the plot
    for i in range(0, x.shape[0]):
        proj_point = np.array([-2.8 + 2.8*(len(drop) == 2),
                               2 - 2*(len(drop) == 2),
                               -2], dtype=np.float)
        proj_point[dimensions] = x[i, dimensions]

        ax[0].plot([proj_point[0], x[i, 0]],
                   [proj_point[1], x[i, 1]],
                   [proj_point[2], x[i, 2]],
                   color="red",
                   linestyle="-.",
                   alpha=.5)

    if len(dimensions) == 1:
        x[:, 0] = x[:, dimensions[0]]
        dimensions[0] = 0
        dimensions.append(1)
        x[:, dimensions[1]] = 0

    ax[1] = fig.add_subplot(1, 2, 2)  # Creates the second subplot (a 2D one)
    ax[1].scatter(x[:, dimensions[0]], x[:, dimensions[1]])

    ax[1].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)

    # Define the title of the plot
    ax[1].set_title("Projected points", fontsize=w+h)

    ax[1].set_xticklabels(ax[1].get_xticks(), fontdict={'fontsize': .75*w})

    # Changing axes' labels
    ax[1].set_xlabel("$Z_1 = $" + labels[0], fontdict={'fontsize': w})

    if len(labels) > 1:
        ax[1].set_yticklabels(ax[1].get_yticks(), fontdict={'fontsize': .75*w})
        ax[1].set_ylabel("$Z_2 = $" + labels[1], fontdict={'fontsize': w})
    else:
        ax[1].spines['left'].set_visible(False)  # Removes frame's left side
        ax[1].set_yticks([])


def plot_reduction2d(data, w, h, drop):

    dimension = set([0, 1])
    dimension = list(dimension.difference([drop]))[0]

    x_std = data.to_numpy()

    fig, ax = plt.subplots(1, 2, figsize=(w, h))
    ax[0].scatter(x_std[:, 0], x_std[:, 1], zorder=2)  # Plot the points

    # This for will draw the red lines into the plot
    for i in range(0, x_std.shape[0]):
        if dimension == 0:
            ax[0].plot([x_std[i, 0], x_std[i, 0]], [0, x_std[i, 1]],
                       color="red", linestyle="-.", alpha=.4, zorder=1)
        if dimension == 1:
            ax[0].plot([0, x_std[i, 0]],
                       [x_std[i, 1], x_std[i, 1]],
                       color="red", linestyle="-.", alpha=.4, zorder=1)

    # This line plots the black line
    if dimension == 0:
        ax[0].plot([np.min(x_std[:, 0]),
                    np.max(x_std[:, 0])],
                   [0, 0], color="black", zorder=0)
    if dimension == 1:
        ax[0].plot([0, 0], [np.min(x_std[:, 1]), np.max(x_std[:, 1])],
                   color="black", zorder=0)

    # This line plots the red points
    if dimension == 0:
        ax[0].scatter(x_std[:, 0], np.zeros_like(x_std[:, 0]), color="red")
    if dimension == 1:
        ax[0].scatter(np.zeros_like(x_std[:, 1]), x_std[:, 1], color="red")

    # Editing frame
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)

    # Increases the size of the labels' ticks;
    ax[0].set_xticklabels(ax[0].get_xticks(), fontdict={'fontsize': 16})
    ax[0].set_yticklabels(ax[0].get_yticks(), fontdict={'fontsize': 16})

    # Editing labels
    ax[0].set_xlabel(data.columns[0], fontdict={'fontsize': w})
    ax[0].set_ylabel(data.columns[1], fontdict={'fontsize': w})
    ax[0].set_title("Dropping the column $X_" + str(drop+1) +
                    "$ = " + data.columns[drop], fontsize=w+h)

    # The functions called here are the same as above,
    # but this time is for the plot on the right
    ax[1].scatter(x_std[:, dimension], np.zeros_like(x_std[:, 0]), color="red")
    ax[1].spines['left'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    ax[1].set_title("Projected points", fontsize=w+h)
    ax[1].set_yticks([])
    ax[1].set_xticklabels(ax[1].get_xticks(), fontdict={'fontsize': 16})
    ax[1].set_xlabel("$Z_1 = $" + data.columns[dimension],
                     fontdict={'fontsize': w})


def plot_rotation2d(data, w, h, theta, projection=True, projection_line=True, plot_error=True, show_error=False, clear=False):
    """
    Plot different lines for projections;

    Parameters:
    -----------
    w: width of the figure
    h: height of the figure
    theta: angle (in degrees) of the line
    clear: if true the result of the cell will be cleared before plotting;
    """

    x_std = data.to_numpy()

    theta = np.deg2rad(theta)
    fig, ax = plt.subplots(1, 2, figsize=(w, h))

    # Plot the points
    ax[0].scatter(x_std[:, 0], x_std[:, 1])

    r = [[np.cos(theta)], [np.sin(theta)]] / \
        np.linalg.norm([np.cos(theta), np.sin(theta)])
    z = x_std[:, 0:2] @ r
    v = z @ r.reshape(1, -1)
    error = np.round(np.sum((x_std[:, 0:2] - v)**2), 2)
    
    # This line plots the black line
    if projection_line:
        if np.rad2deg(theta) <= 90:
            ax[0].plot([np.min(v[:, 0]), np.max(v[:, 0])],
                       [np.min(v[:, 1]), np.max(v[:, 1])], color="black")
        else:
            ax[0].plot([np.min(v[:, 0]), np.max(v[:, 0])],
                       [np.max(v[:, 1]), np.min(v[:, 1])], color="black")

        
    
    if projection:
        # This for will draw the red lines into the plot
        if plot_error:
            for i in range(0, x_std.shape[0]):
                ax[0].plot([x_std[i, 0], v[i, 0]], [x_std[i, 1], v[i, 1]],
                           color="red", linestyle="-.", alpha=.4)
        
        # This line plots the red points
        ax[0].scatter(v[:, 0], v[:, 1], color="red")

    # Removing frame sides
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)

    # Increasing the size of the ticks labels;
    ax[0].set_xticklabels(ax[0].get_xticks(), fontdict={'fontsize': 16})
    ax[0].set_yticklabels(ax[0].get_yticks(), fontdict={'fontsize': 16})

    # Changes the labels
    ax[0].set_xlabel(data.columns[0], fontdict={'fontsize': w})
    ax[0].set_ylabel(data.columns[1], fontdict={'fontsize': w})
    if projection and show_error:
        ax[0].set_title(f"Original space (reconstruction error: {error})", fontsize=w)
    else:
        ax[0].set_title(f"Projecting points", fontsize=w)

    ax[1].scatter(z, np.zeros_like(z), color="red")
    ax[1].spines['left'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    var = np.round(np.var(z), 4)

    # Define the title of the plot
    ax[1].set_title(f"Projected points (var: {var})", fontsize=w)
    ax[1].set_yticks([])  # Here it is just removing the ticks from the y-axis
    ax[1].set_xticklabels(ax[1].get_xticks(), fontdict={'fontsize': 16})
    ax[1].set_xlabel("$Z_1$", fontdict={'fontsize': w})
    if clear:
        clear_output()

    plt.show()


def plot_pca2d(data, w, h, errors=False):

    x_std = data.to_numpy()

    pca = PCA(n_components=2)

    # These are the points in the new space
    z = pca.fit_transform(x_std[:, 0:2])

    # These are the projected points
    v = z[:, 0, None]@pca.components_[None, 0, :]

    # The min and max values of the projected points
    minv, maxv = np.min(v, axis=0)[0],  np.max(v, axis=0)[0]

    fig, ax = plt.subplots(1, 2, figsize=(w, h))
    ax[0].scatter(x_std[:, 0], x_std[:, 1])
    ax[0].plot([minv, maxv], [minv*pca.components_[0, 1]/pca.components_[0, 0],
                              maxv*pca.components_[0, 1]/pca.components_[0, 0]],
               color="red", label="Direction of highest variance")

    error = np.round(np.sum((x_std[:, 0:2]-v)**2), 2)

    if errors:
        # This for will draw the red lines into the plot
        for i in range(0, x_std.shape[0]):
            ax[0].plot([x_std[i, 0], v[i, 0]], [x_std[i, 1], v[i, 1]],
                       color="red", linestyle="-.", alpha=.4)
        ax[0].scatter(v[:, 0], v[:, 1], color="red")

    # Removes frame's sides
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)

    # Increase the size of the ticks labels;
    ax[0].set_xticklabels(ax[0].get_xticks(), fontdict={'fontsize': 16})
    ax[0].set_yticklabels(ax[0].get_yticks(), fontdict={'fontsize': 16})

    # Changes the labels
    ax[0].set_xlabel(data.columns[0], fontdict={'fontsize': w})
    ax[0].set_ylabel(data.columns[1], fontdict={'fontsize': w})
    ax[0].set_title(f"PCA - projection error:{error}", fontsize=w+h)
    ax[0].legend(fontsize=w, loc="lower right")

    ax[1].scatter(z, np.zeros_like(z), color="red")
    ax[1].spines['left'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    var = np.round(np.var(z, axis=0)[0], 4)
    ax[1].set_title(f"Projected points (var: {var})", fontsize=w+h)
    ax[1].set_yticks([])  # Here it is just removing the ticks from the y-axis
    ax[1].set_xticklabels(ax[1].get_xticks(), fontdict={'fontsize': 16})
    ax[1].set_xlabel("$Z_1 = $" + str(np.round(pca.components_[0, 0], 4)) +
                     " x " + data.columns[0] + " + " + str(np.round(pca.components_[0, 1], 4)) +
                     " x " + data.columns[1], fontdict={'fontsize': w})

    return ax


def plot_pca_mult_solutions2d(data, w, h):

    x_std = data

    # Create a PCA object
    pca = PCA(n_components=2)

    # Fit and transform the pca object
    pca.fit(x_std[:, 0:2])

    fig, ax = plt.subplots(1, 1, figsize=(w, h))
    ax.axis("equal")

    # Plots the black arrow
    ax.quiver(pca.components_[0, 0], pca.components_[0, 1])

    # Plots the red arrow
    ax.quiver(-1*pca.components_[0, 0], -1*pca.components_[0, 1], color="red")

    ax.scatter(x_std[:, 0], x_std[:, 1])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': 16})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': 16})

    return ax


def plot_pca_rotation2d(data, w, h):

    x_std = data.iloc[:, 0:2].to_numpy()

    pca = PCA(n_components=2)
    z = pca.fit_transform(x_std)

    fig, ax = plt.subplots(1, 2, figsize=(w, h))
    ax[0].scatter(x_std[:, 0], x_std[:, 1], alpha=.4)
    ax[0].axis("equal")
    ax[0].quiver(pca.components_[0, 0], pca.components_[0, 1],
                 color="black", label="Direction 1nd PC")
    ax[0].quiver(pca.components_[1, 0], pca.components_[
                 1, 1], color="red", label="Direction 2nd PC")
    ax[0].spines['top'].set_visible(False)  # Removes the top side of the frame
    # Removes the right side of the frame
    ax[0].spines['right'].set_visible(False)
    # Increase the size of the x-axis ticks labels;
    ax[0].set_xticklabels(ax[0].get_xticks(), fontdict={'fontsize': 16})
    # Increase the size of the y-axis ticks labels;
    ax[0].set_yticklabels(ax[0].get_yticks(), fontdict={'fontsize': 16})
    # Define the title of the plot
    ax[0].set_title(f"Original data", fontsize=w+h)
    ax[0].legend(fontsize=w, loc="lower right")
    ax[0].set_xlabel("$X_1$")
    ax[0].set_ylabel("$X_2$")

    ax[1].scatter(z[:, 0], z[:, 1])
    ax[1].axis("equal")
    ax[1].spines['top'].set_visible(False)  # Removes the top side of the frame
    # Removes the right side of the frame
    ax[1].spines['right'].set_visible(False)
    # Increase the size of the x-axis ticks labels;
    ax[1].set_xticklabels(ax[1].get_xticks(), fontdict={'fontsize': 16})
    # Increase the size of the y-axis ticks labels;
    ax[1].set_yticklabels(np.round(ax[1].get_yticks(), 2),
                          fontdict={'fontsize': 16})
    # Define the title of the plot
    ax[1].set_title(f"Transformed data", fontsize=w+h)
    ax[1].set_xlabel("$Z_1$")
    ax[1].set_ylabel("$Z_2$")
    
def plot_pca_regression(data, w, h, error_type='both'):
    """
    Plot different lines for projections;

    Parameters:
    -----------
    w: width of the figure
    h: height of the figure
    theta: angle (in degrees) of the line (between 0 and 180)
    clear: if true the result of the cell will be cleared before plotting;
    """
   
    theta=45
        
    x_std = data.to_numpy()

    theta = np.deg2rad(theta)
    fig, ax = plt.subplots(1, 1, figsize=(w, h))

    # Plot the points
    ax.scatter(x_std[:, 0], x_std[:, 1])

    r = [[np.cos(theta)], [np.sin(theta)]] / \
        np.linalg.norm([np.cos(theta), np.sin(theta)])
    z = x_std[:, 0:2] @ r
    v = z @ r.reshape(1, -1)
    
    m = (np.max(v[:, 1]) - np.min(v[:, 1]))/(np.max(v[:, 0]) - np.min(v[:, 0]))
    error = np.round(np.sum((x_std[:, 0:2] - v)**2), 2)
    
    # This line plots the black line
    if np.rad2deg(theta) <= 90:
        ax.plot([np.min((v[:, 0], x_std[:,0])), np.max((v[:, 0], x_std[:,0]))],
                   [m*np.min((v[:, 0], x_std[:,0])), m*np.max((v[:, 0], x_std[:,0]))], color="black")
    else:
        ax.plot([np.min((v[:, 0], x_std[:,0])), np.max((v[:, 0], x_std[:,0]))],
                   [-m*np.min((v[:, 0], x_std[:,0])), -m*np.max((v[:, 0], x_std[:,0]))], color="black")

    # This for will draw the red lines into the plot
    #if theta > 90:
    #    m = -m
    for i in range(0, x_std.shape[0]):
        #print(error)
        if error_type=='pca' or error_type=='both':
            ax.plot([x_std[i, 0], v[i, 0]], [x_std[i, 1], v[i, 1]],
                       color="red", linestyle="-.", alpha=.4)
        if error_type=='lm' or error_type=='both':
            ax.plot([x_std[i, 0], x_std[i, 0]], [x_std[i, 1], m*x_std[i, 0]],
                       color="green", linestyle="-.", alpha=.4)

    # Removing frame sides
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Increasing the size of the ticks labels;
    ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': 16})
    ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': 16})

    # Changes the labels
    ax.set_xlabel(data.columns[0], fontdict={'fontsize': w})
    ax.set_ylabel(data.columns[1], fontdict={'fontsize': w})
    ax.set_title(f"PCA vs Regression", fontsize=w)

    plt.show()
    
def plot_multicollinearity(directions=False):
    iris_mc = iris_std.iloc[:,0:2]
    iris_mc = np.column_stack((iris_mc, np.sum(iris_mc,1)/2))
    pca = PCA(n_components=3)
    pca.fit(iris_mc)
    
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(1,1,1,projection="3d")
    ax.scatter(iris_mc[:,0], iris_mc[:,1], iris_mc[:,2], alpha=.4)
    ax.set_xlabel("$X_1$", fontsize=12)
    ax.set_ylabel("$X_2$", fontsize=12)
    ax.set_zlabel("$X_3$", fontsize=12)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
    if directions:
        ax.quiver(0,0,0, pca.components_[0,0],pca.components_[0,1],pca.components_[0,2], color="black", label="1st comp.")
        ax.quiver(0,0,0, pca.components_[1,0],pca.components_[1,1],pca.components_[1,2], color="blue", label="2st comp.")
        ax.quiver(0,0,0, pca.components_[2,0],pca.components_[2,1],pca.components_[2,2], color="red", label="3st comp.")
        ax.legend(fontsize=12)

def plot_elbow_plots(w, h):
    w, h = 22, 10

    # Run PCA on the iris dataset
    pca_iris = PCA(n_components=4) 
    pca_iris.fit(iris_std)
    # Calculates the proportion of variance explained
    var_exp_iris = np.cumsum(pca_iris.explained_variance_/np.sum(pca_iris.explained_variance_))

    # Run PCA on the wine dataset
    pca_wine = PCA(n_components=13)
    pca_wine.fit(wine_std)
    
    # Calculates the proportion of variance explained
    var_exp_wine = np.cumsum(pca_wine.explained_variance_/np.sum(pca_wine.explained_variance_))

    # Plots the elbow plot for the iris pca
    fig, ax = plt.subplots(1,2,figsize=(w,h))
    ax[0].plot(range(1,5), var_exp_iris, marker='o')
    ax[0].spines["top"].set_visible(False)
    ax[0].spines["right"].set_visible(False)
    ax[0].set_title("Variance explained - Iris", fontsize=w)
    ax[0].set_xticklabels(ax[0].get_xticks(), fontdict={'fontsize':16})
    ax[0].set_yticklabels(np.round(ax[0].get_yticks(),2), fontdict={'fontsize':16})

    # Plots the elbow plot for the wine pca
    ax[1].plot(range(1,14), var_exp_wine, marker='o')
    ax[1].spines["top"].set_visible(False)
    ax[1].spines["right"].set_visible(False)
    ax[1].set_title("Variance explained - Wine", fontsize=w)
    ax[1].set_xticklabels(ax[1].get_xticks(), fontdict={'fontsize':16})
    ax[1].set_yticklabels(np.round(ax[1].get_yticks(),2), fontdict={'fontsize':16})

def plot_clust(X,W=None,z=None):
    if z is not None:
        if np.any(z<0):
            plt.scatter(X[z<0,0], X[z<0,1], marker="o", 
                        facecolors='none', edgecolor='black', alpha=0.3);
        if np.any(z>=0):
            plt.scatter(X[z>=0,0], X[z>=0,1], marker="o", c=z[z>=0], alpha=0.3);
    else:
        plt.scatter(X[:,0], X[:,1], marker="o", c='black', alpha=0.3);
    if W is not None:
        plt.scatter(W[:,0], W[:,1], marker="^", s=200, c=np.arange(W.shape[0]));
    else:
        plt.title("number of clusters = %d" % len(set(np.unique(z))-set([-1])));