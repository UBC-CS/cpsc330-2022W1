import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mglearn
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as pyo
from plotly.subplots import make_subplots
from sklearn.cluster import KMeans, DBSCAN
from scipy.spatial import distance
from sklearn.datasets import make_blobs
from matplotlib.patches import Circle
from sklearn.linear_model import Lasso
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.cm as cm
from sklearn.cluster import DBSCAN, AgglomerativeClustering, KMeans
from random import randint
from scipy.cluster.hierarchy import average, complete, dendrogram, ward
from sklearn.decomposition import PCA
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from sklearn import manifold, datasets
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
from sklearn.manifold import TSNE
import seaborn as sns


import matplotlib.pyplot as plt 

def corr_heatmat(cor, w=6, h=4): 
    plt.figure(figsize=(w, h))
    sns.set(font_scale=1)
    sns.heatmap(cor, annot=True, cmap=plt.cm.Blues)

def plot_perplexity_tsne(
    digits, perplexity_range=[2, 5, 10, 15, 30, 200], title="Digits data"
):

    fig, ax = plt.subplots(
        2, 3, figsize=(24, 12), subplot_kw={"xticks": (), "yticks": ()}
    )
    colors = [
        "#476A2A",
        "#7851B8",
        "#BD3430",
        "#4A2D4E",
        "#875525",
        "#A83683",
        "#4E655E",
        "#853541",
        "#3A3120",
        "#535D8E",
    ]
    k = 0
    for i in range(2):
        for j in range(3):
            tsne = TSNE(perplexity=perplexity_range[k], random_state=42)
            digits_Z = tsne.fit_transform(digits.data)
            ax[i, j].set_xlim(digits_Z[:, 0].min(), digits_Z[:, 0].max())
            ax[i, j].set_ylim(digits_Z[:, 1].min(), digits_Z[:, 1].max())
            for dig in range(len(digits.data)):
                # actually plot the digits as text instead of using scatter
                ax[i, j].text(
                    digits_Z[dig, 0],
                    digits_Z[dig, 1],
                    str(digits.target[dig]),
                    color=colors[digits.target[dig]],
                    fontdict={"weight": "bold", "size": 9},
                )
            ax[i, j].set_title(title + " perplexity = %s"%(perplexity_range[k]))
            ax[i, j].set_xlabel("Transformed feat 1")
            ax[i, j].set_ylabel("Transformed feat 2")
            k += 1

def plot_digits(digits, digits_Z, title="Digits data"):
    colors = [
        "#476A2A",
        "#7851B8",
        "#BD3430",
        "#4A2D4E",
        "#875525",
        "#A83683",
        "#4E655E",
        "#853541",
        "#3A3120",
        "#535D8E",
    ]
    plt.figure(figsize=(8, 6))
    plt.xlim(digits_Z[:, 0].min(), digits_Z[:, 0].max())
    plt.ylim(digits_Z[:, 1].min(), digits_Z[:, 1].max())
    for i in range(len(digits.data)):
        # actually plot the digits as text instead of using scatter
        plt.text(
            digits_Z[i, 0],
            digits_Z[i, 1],
            str(digits.target[i]),
            color=colors[digits.target[i]],
            fontdict={"weight": "bold", "size": 9},
        )
    plt.title(title)
    plt.xlabel("Transformed feat 1")
    plt.ylabel("Transformed feat 2")

def plot_swiss_roll(X, color):
    fig = plt.figure(figsize=(10, 8))
    ax = p3.Axes3D(fig)
    ax.view_init(7, -80)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral);
    
    
def plot_orig_reconstructed_faces(X_train, reconstructed_images, image_shape=(87,65)):    
    fig, axes = plt.subplots(1, 5, figsize=(10, 6), subplot_kw={"xticks": (), "yticks": ()})
    axes[0].set_ylabel('Original')
    for image, ax in zip(X_train, axes.ravel()):
        ax.imshow(image.reshape(image_shape))
    plt.show()

    fig, axes = plt.subplots(1, 5, figsize=(10, 6), subplot_kw={"xticks": (), "yticks": ()})
    axes[0].set_ylabel('Reconstructed')
    for image, ax in zip(reconstructed_images, axes.ravel()):
        ax.imshow(image.reshape(image_shape))
    plt.show()    


def plot_pca(X_pca, y, labels=["dislike", "like"]): 
    mglearn.discrete_scatter(X_pca[:, 0], X_pca[:, 1], y)
    plt.legend(labels, loc="best")
    plt.xlabel("PCA component 1")
    plt.ylabel("PCA component 2")
    plt.show()

def plot_hists(df, X, d =4, targets=['dislike', 'like'], target_col='target', w=10, h=6):    
    fig, axes = plt.subplots(2, 2, figsize=(w, h))
    targets_1 = df[df[target_col] == 1]
    targets_0 = df[df[target_col] == 0]

    ax = axes.ravel()
    
    for i in range(d):
        _, bins = np.histogram(X.iloc[:, i], bins=100)
        ax[i].hist(targets_1.iloc[:, i], bins=bins, color=mglearn.cm3(0), alpha=0.5)
        ax[i].hist(targets_0.iloc[:, i], bins=bins, color=mglearn.cm3(2), alpha=0.5)
        ax[i].set_title(X.columns[i])
        ax[i].set_yticks(())
        ax[i].set_ylabel("Frequency")
        ax[i].legend(targets, loc="best")
    fig.tight_layout()
    plt.show()

def plot_pca_compressed(image_orig, image_recon, n_components, w=12, h=4):
    fig, ax = plt.subplots(1, 2, figsize=(w, h))
    ax[0].set_title("Original image")
    ax[0].imshow(image_orig, cmap=plt.cm.gray)
    ax[0].set_title("Original image")
    ax[1].imshow(image_recon, cmap=plt.cm.gray)
    ax[1].set_title("Compressed (n_components={})".format(n_components))
    plt.show()

def plot_faces_cluster_centers(kmeans, pca=None, h=20, w=30, image_shape=(87,65)): 
    fig, axes = plt.subplots(1, 10, subplot_kw={'xticks': (), 'yticks': ()},figsize=(h, w))
    i = 0 
    for center, ax in zip(kmeans.cluster_centers_, axes.ravel()):
        if pca: 
            ax.imshow(pca.inverse_transform(center).reshape(image_shape), vmin=0, vmax=1)
        else:
            ax.imshow(center.reshape(image_shape), vmin=0, vmax=1)
        ax.set_title('Center: %d'%(i))
        i+=1
    plt.show()
        
def get_cluster_images(km, X_people, y_people, target_names, X_pca=None, pca=None, cluster=0):
    image_shape = (87, 65)
    fig, axes = plt.subplots(1, 6, subplot_kw={'xticks': (), 'yticks': ()},
                             figsize=(10, 10), gridspec_kw={"hspace": .3})
    center = km.cluster_centers_[cluster]
    
    mask = km.labels_ == cluster
    
    if pca: 
        dists = np.sum((X_pca - center) ** 2, axis=1)
        dists[~mask] = np.inf
        inds = np.argsort(dists)[:5]
        axes[0].imshow(pca.inverse_transform(center).reshape(image_shape), vmin=0, vmax=1)        
    else: 
        dists = np.sum((X_people - center) ** 2, axis=1)
        dists[~mask] = np.inf
        inds = np.argsort(dists)[:5]
        axes[0].imshow(center.reshape(image_shape), vmin=0, vmax=1)        
        
    axes[0].set_title('Cluster center %d'%(cluster))
    i = 1
    for image, label in zip(X_people[inds], y_people[inds]):
        axes[i].imshow(image.reshape(image_shape), vmin=0, vmax=1)
        axes[i].set_title("%s" % (target_names[label].split()[-1]), fontdict={'fontsize': 9})    
        i+=1
    plt.show()

def plot_with_labels(X, font_size=14): 
    mglearn.discrete_scatter(X[:, 0], X[:, 1], markeredgewidth=1.0); 
    labels = [str(label) for label in list(range(0,len(X)))]
    for i, txt in enumerate(labels):
        plt.annotate(txt, X[i], xytext=X[i] + 0.2, size = font_size)

def plot_X_dendrogram(X, linkage_array, font_size=14, label_n_clusters=False, title='Dendrogram'): 
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    mglearn.discrete_scatter(X[:, 0], X[:, 1], markeredgewidth=1.0, ax = axes[0]); 
    axes[0].set_title('Original data')
    labels = [str(label) for label in list(range(0,len(X)))]
    for i, txt in enumerate(labels):
        axes[0].annotate(txt, X[i], xytext=X[i] + 0.2, size = font_size)
        
    # Credit: Based on the code in Introduction to Machine Learning with Python        
    dendrogram(linkage_array, ax=axes[1])
    axes[1] = plt.gca()    
    axes[1].set_title(title)    
    if label_n_clusters: 
        bounds = axes[1].get_xbound()
        axes[1].plot(bounds, [7.0, 7.0], "--", c="k")
        axes[1].plot(bounds, [4, 4], "--", c="k")
        axes[1].plot(bounds, [2, 2], "--", c="k")    
        #axes[1].plot(bounds, [4, 4], "--", c="k")
        #axes[1].plot(bounds, [2, 2], "--", c="k")        
        #axes[1].plot(bounds, [1.3, 1.3], "--", c="k")            
        axes[1].text(bounds[1], 7.25, " two clusters", va="center", fontdict={"size": 15})
        axes[1].text(bounds[1], 4, " three clusters", va="center", fontdict={"size": 15})
        axes[1].text(bounds[1], 2, " four clusters", va="center", fontdict={"size": 15})    
        #axes[1].text(bounds[1], 1.3, " four clusters", va="center", fontdict={"size": 15})            
    plt.xlabel("Examples")
    plt.ylabel("Cluster distance");        
    
    
def plot_X_dbscan(X, model):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    colours = []
    if np.any(model.labels_ == -1):
        n_clusters = len(set(model.labels_)) - 1 
    else: 
        n_clusters = len(set(model.labels_))
    
    for i in range(n_clusters + 1):
        colours.append("#%06X" % np.random.randint(0, 0xFFFFFF))
        
    mglearn.discrete_scatter(X[:, 0], X[:, 1], ax=axes[0], markeredgewidth=1.0)

    if np.any(model.labels_ == -1):
        colours = ["w"] + colours
    mglearn.discrete_scatter(X[:, 0], X[:, 1], model.labels_, c=colours, markers="o", markeredgewidth=1.0, ax=axes[1]);
    plt.legend()

def plot_dbscan_with_labels(X, eps=1.0, min_samples = 2, font_size=14):
    model = DBSCAN(eps=eps, min_samples=min_samples) 
    model.fit(X)    
    if np.any(model.labels_ == -1):
        n_clusters = len(set(model.labels_)) - 1 
    else: 
        n_clusters = len(set(model.labels_))
    plt.title('Number of clusters: %d'%(n_clusters))
    colours = []
    for i in range(n_clusters + 1):
        colours.append("#%06X" % np.random.randint(0, 0xFFFFFF))
        
    #colours = [mglearn.cm3(1), mglearn.cm3(0)]
    if np.any(model.labels_ == -1):
        colours = ["w"] + colours
    mglearn.discrete_scatter(
        X[:, 0], X[:, 1], model.labels_, c=colours, markers="o", markeredgewidth=1.0
    );
    plt.legend()
    labels = [str(label) for label in list(range(0,len(X)))]
    for i, txt in enumerate(labels):
        plt.annotate(txt, X[i], xytext=X[i] + 0.2, size = font_size)

def plot_X_k_means(X, k=2):
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))    
    ax[0].set_title("Original dataset")
    ax[0].set_xlabel("Feature 0")
    ax[0].set_ylabel("Feature 1")    
    mglearn.discrete_scatter(X[:, 0], X[:, 1], ax=ax[0]);
    # cluster the data into three clusters
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    colours = list(range(0,k))
    # plot the cluster assignments and cluster centers
    ax[1].set_title("K-Means clusters (K=%d)"%(k))
    ax[1].set_xlabel("Feature 0")
    ax[1].set_ylabel("Feature 1")        
    mglearn.discrete_scatter(X[:, 0], X[:, 1], kmeans.labels_, markers='o', ax=ax[1])
    mglearn.discrete_scatter(
        kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], colours, 
        markers='*', markeredgewidth=1.0, ax=ax[1])
    
def plot_k_means_dbscan_comparison(X, k=3, eps=1.0, min_samples=2):
    fig, ax = plt.subplots(1, 3, figsize=(18, 4))
    mglearn.discrete_scatter(X[:, 0], X[:, 1], ax=ax[0], markeredgewidth=1.0)

    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    colours = list(range(0,k)) 
    # plot the cluster assignments and cluster centers
    ax[1].set_title("K-Means clusters (K=%d)"%(k))
    ax[1].set_xlabel("Feature 0")
    ax[1].set_ylabel("Feature 1")        
    mglearn.discrete_scatter(X[:, 0], X[:, 1], kmeans.labels_, markers='o', ax=ax[1], markeredgewidth=1.0)

    mglearn.discrete_scatter(
        kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], colours, 
        markers='*', markeredgewidth=1.5, ax=ax[1])

    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan.fit(X)
    n_clusters = len(set(dbscan.labels_))
    colours = []
    for i in range(n_clusters):
        colours.append("#%06X" % np.random.randint(0, 0xFFFFFF))

    if np.any(dbscan.labels_ == -1):
        colours = ["w"] + colours
    # plot the cluster assignments and cluster centers
    ax[2].set_title("DBSCAN clusters eps=%0.2f and min_samples=%d"%(eps,min_samples))
    ax[2].set_xlabel("Feature 0")
    ax[2].set_ylabel("Feature 1")        
    mglearn.discrete_scatter(
        X[:, 0], X[:, 1], dbscan.labels_, c=colours, markers='o', markeredgewidth=1.0, ax=ax[2]
    );    
    plt.legend()     
    
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
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
    plt.scatter(centroids[:, 0], centroids[:, 1], s=250,
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
    

def simple_bar_plot(x, y, x_title = "x", y_title ="y"):
    fig = px.bar(x=x, y=y)
    fig.update_layout(
        xaxis_title=x_title,
        yaxis_title=y_title,
        xaxis = dict(
            tickmode = 'linear',        
        )
    )
    return fig 

def plot_pca_w_vectors(W, component_labels, feature_names, width=800, height=600): 
    
    fig = px.imshow(
        W,
        y=component_labels,
        x=feature_names,
        color_continuous_scale="viridis",
    )

    fig.update_layout(
        xaxis_title="Features",
        yaxis_title="Principal Components",
        xaxis = {'side': 'top',  'tickangle':300}, 
    )
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
    )    

    return fig


def plot_pca_reconstructions(X, pca):
    Z = pca.transform(X)
    W = pca.components_
    X_hat = pca.inverse_transform(Z)

    shapes = [
    dict(
        type="line",
        x0=X.iloc[i, 0],
        y0=X.iloc[i, 1],
        x1=X_hat[i, 0],
        y1=X_hat[i, 1],
        line=dict(color="grey", width=2),
    ) for i in range(X.shape[0])]
    
    grid = np.linspace(min(X.iloc[:,0]) - 0.3, max(X.iloc[:,1]) + 0.3, 1000)
    gridplot = (grid - pca.mean_[0]) / W[0, 0] * W[0, 1] + pca.mean_[1]
    # gridplot = (grid) / W[0, 0] * W[0, 1]

    fig = make_subplots(rows=1, cols=2, subplot_titles=("Original data", "Reconstructions (X_hat)"))

    fig.add_trace(
        go.Scatter(
            x=X.iloc[:,0],
            y=X.iloc[:,1],
            mode="markers",
            marker=dict(size=8),
        ),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=X.iloc[:,0],
            y=X.iloc[:,1],
            mode="markers",
            marker=dict(size=8, color="blue"),
            name="Original data (X)",
        ),
        row=1,
        col=2,
    )
        
    fig.add_trace(
        go.Scatter(
            x=grid,
            y=gridplot,
            line_color="green",
            mode="lines",
            line=dict(width=2),
            name="PCA model (W vector)",
        ),
        row=1,
        col=2,
    )

    fig.add_trace(
        go.Scatter(
            x=X_hat[:, 0],
            y=X_hat[:, 1],
            mode="markers",
            marker=dict(size=8, color="red"),
            name="Reconstructions (X_hat)",
        ),
        row=1,
        col=2,
    )        

    for trace in fig["data"]:
        if trace["name"] == None:
            trace["showlegend"] = False


    for shape in shapes:
        fig.add_shape(shape, row=1, col=2)

    #fig.update_shapes(dict(xref='x', yref='y'), row =1, col= 2)
    return fig

def plot_pca_model_reconstructions(X, pca):
    Z = pca.transform(X)
    W = pca.components_
    X_hat = pca.inverse_transform(Z)

    shapes = [
    dict(
        type="line",
        x0=X.iloc[i, 0],
        y0=X.iloc[i, 1],
        x1=X_hat[i, 0],
        y1=X_hat[i, 1],
        line=dict(color="grey", width=2),
    ) for i in range(X.shape[0])]
    
    grid = np.linspace(min(X.iloc[:,0]) - 0.3, max(X.iloc[:,1]) + 0.3, 1000)
    gridplot = (grid - pca.mean_[0]) / W[0, 0] * W[0, 1] + pca.mean_[1]
    # gridplot = (grid) / W[0, 0] * W[0, 1]

    fig = make_subplots(rows=1, cols=3, subplot_titles=("Original data", "Transformed data (Z)", "Reconstructions (X_hat)"))

    fig.add_trace(
        go.Scatter(
            x=X.iloc[:,0],
            y=X.iloc[:,1],
            mode="markers",
            marker=dict(size=8),
        ),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=Z[:,0],
            y=np.zeros(Z.shape[0]),
            mode="markers",
            marker=dict(size=8),
        ),
        row=1,
        col=2,
    )    

    fig.add_trace(
        go.Scatter(
            x=X.iloc[:,0],
            y=X.iloc[:,1],
            mode="markers",
            marker=dict(size=8, color="blue"),
            name="Original data (X)",
        ),
        row=1,
        col=3,
    )
        
    fig.add_trace(
        go.Scatter(
            x=grid,
            y=gridplot,
            line_color="green",
            mode="lines",
            line=dict(width=2),
            name="PCA model (W vector)",
        ),
        row=1,
        col=3,
    )

    fig.add_trace(
        go.Scatter(
            x=X_hat[:, 0],
            y=X_hat[:, 1],
            mode="markers",
            marker=dict(size=8, color="red"),
            name="Reconstructions (X_hat)",
        ),
        row=1,
        col=3,
    )        

    for trace in fig["data"]:
        if trace["name"] == None:
            trace["showlegend"] = False


    for shape in shapes:
        fig.add_shape(shape, row=1, col=3)

    #fig.update_shapes(dict(xref='x', yref='y'), row =1, col= 2)
    return fig

def plot_current_assinment(X, Z, centers, colours=['black','blue','red']):
    plt.scatter(X[:,0], X[:,1], c=[colours[z] for z in Z], marker='o')
    plt.scatter(centers[:,0], centers[:,1], c=colours, marker='*',s=200)
    plt.title('Current cluster assignment')
    
def plot_interactive_3d(X):
    trace = go.Scatter3d(x=X[:,0], y=X[:,1], z=X[:,2], mode='markers')
    layout = go.Layout(showlegend=False, scene=dict(xaxis={'title':'x1'},yaxis={'title':'x2'},zaxis={'title':'x3'}))
    fig = go.Figure(data=[trace], layout=layout)
    iplot(fig)

def plot_2d_1k(X, pca): 
    # get grid for visualizing plane
    n = X.shape[0]    
    z1 = np.linspace(-7, 7, 100)
    z2 = np.linspace(-7, 7, 100)
    z1grid, z2grid = np.meshgrid(z1, z2)
    Zgrid = np.concatenate((z1grid.flatten()[:, None], z2grid.flatten()[:, None]), axis=1)
    Xgrid = pca.inverse_transform(Zgrid)
    Xgrid_re = np.reshape(Xgrid, (100, 100, 3))

    # get reconstructions of original points
    Z = pca.transform(X)
    Xhat = pca.inverse_transform(Z)

    traces1 = []
    for i in range(n):
        traces1.append(
            go.Scatter3d(
                x=(X[i, 0], Xhat[i, 0]),
                y=(X[i, 1], Xhat[i, 1]),
                z=(X[i, 2], Xhat[i, 2]),
                marker=dict(color="blue"),
                name="original points"
            )
        )

    trace2 = go.Surface(
        x=Xgrid_re[:, :, 0],
        y=Xgrid_re[:, :, 1],
        z=Xgrid_re[:, :, 2],
        showscale=False,
        colorscale=[[0, "rgb(200,300,200)"], [1, "rgb(200,300,200)"]],
        opacity=0.9,
        name="reconstructions"
    )

    trace3 = go.Scatter3d(x=Xhat[:, 0], y=Xhat[:, 1], z=Xhat[:, 2], mode="markers")

    data = traces1 + [trace2, trace3]

    layout = go.Layout(
        showlegend=False,
        scene=dict(xaxis={"title": "x1"}, yaxis={"title": "x2"}, zaxis={"title": "x3"}),
    )

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)

def plot_d3_k1(X, pca): 
    # get grid for visualizing plane
    Zgrid = np.linspace(-7, 7, 100)[:, None]
    Xgrid = pca.inverse_transform(Zgrid)
    n = X.shape[0]
    # get reconstructions of original points
    Xhat = pca.inverse_transform(pca.transform(X))

    traces1 = []
    for i in range(n):
        traces1.append(
            go.Scatter3d(
                x=(X[i, 0], Xhat[i, 0]),
                y=(X[i, 1], Xhat[i, 1]),
                z=(X[i, 2], Xhat[i, 2]),
                marker={"color": "blue"},
            )
        )

    trace2 = go.Scatter3d(
        x=Xgrid[:, 0], y=Xgrid[:, 1], z=Xgrid[:, 2], mode="lines", marker={"color": "black"}
    )

    trace3 = go.Scatter3d(x=Xhat[:, 0], y=Xhat[:, 1], z=Xhat[:, 2], mode="markers")

    data = traces1 + [trace2, trace3]

    layout = go.Layout(
        showlegend=False,
        scene=dict(xaxis={"title": "x1"}, yaxis={"title": "x2"}, zaxis={"title": "x3"}),
    )


    fig = go.Figure(data=data, layout=layout)
    iplot(fig)    
    
def plot_X_k_means(X, k=2):
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))    
    ax[0].set_title("Original dataset")
    ax[0].set_xlabel("Feature 0")
    ax[0].set_ylabel("Feature 1")    
    mglearn.discrete_scatter(X[:, 0], X[:, 1], ax=ax[0]);
    # cluster the data into three clusters
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    colours = list(range(0,k))
    # plot the cluster assignments and cluster centers
    ax[1].set_title("K-Means clusters (K=%d)"%(k))
    ax[1].set_xlabel("Feature 0")
    ax[1].set_ylabel("Feature 1")        
    mglearn.discrete_scatter(X[:, 0], X[:, 1], kmeans.labels_, markers='o', ax=ax[1])
    mglearn.discrete_scatter(
        kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], colours, 
        markers='*', markeredgewidth=1.0, ax=ax[1])        
    
def reconstruction_error(X, X_hat):
    error = np.sum((np.array(X) - np.array(X_hat)) ** 2, axis=1)
    #error = pd.Series(data=error)
    #error = (error - np.min(error)) / (np.max(error) - np.min(error))  # normalize
    return error


def plot_pca_model_search(data, alpha, w=15, h=8):
    X = data.to_numpy()
    W = np.array([[np.cos(np.radians(alpha)), np.sin(np.radians(alpha))]])
    Z = (X) @ (W.T @ W)

    err = np.round(reconstruction_error(X, Z).sum(), 4)    
    #mglearn.discrete_scatter(X[:, 0], X[:, 1], s=8)
    plt.scatter(X[:, 0], X[:, 1], c=X[:, 0], cmap="viridis", s=60, linewidths=3)    
    plt.plot(W[0, 0] * 3.5 * np.array([-1, 1]), W[0, 1] * 3.5 * np.array([-1, 1]), "k", label=f'Recon error: {err}')
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.scatter(Z[:, 0], Z[:, 1], c="r", s=60)
    for i in range(len(data)):
        plt.plot(
            [X[i, 0], Z[i, 0]],
            [X[i, 1], Z[i, 1]],
            color="red",
            linestyle="-.",
            alpha=0.8,
            linewidth=2,
        )

    n = len(X)
    w = W.T @ W
    variance = np.round(((X @ w).T) / (n - 1) @ (X @ w), 5)
    plt.title(f"Which line?", fontsize=20)
    plt.legend();        

def plot_feature_selection(data, w, h, drop):
    dimension = set([0, 1])
    dimension = list(dimension.difference([drop]))[0]

    X = data.to_numpy()

    fig, ax = plt.subplots(1, 2, figsize=(w, h))

    ax[0].scatter(X[:, 0], X[:, 1], c=X[:, 0], cmap="viridis", s=100, linewidths=3)

    # This for will draw the red lines into the plot
    for i in range(0, X.shape[0]):
        if dimension == 0:
            ax[0].plot(
                [X[i, 0], X[i, 0]],
                [0, X[i, 1]],
                color="red",
                linestyle="-.",
                alpha=0.4,
            )
        if dimension == 1:
            ax[0].plot(
                [0, X[i, 0]],
                [X[i, 1], X[i, 1]],
                color="red",
                linestyle="-.",
                alpha=0.4,
                linewidth=2,
            )

    # This line plots the black line
    if dimension == 0:
        ax[0].plot(
            [np.min(X[:, 0]), np.max(X[:, 0])], [0, 0], color="black", linewidth=1
        )
    if dimension == 1:
        ax[0].plot(
            [0, 0], [np.min(X[:, 1]), np.max(X[:, 1])], color="black", linewidth=1
        )

    # This line plots the red points
    if dimension == 0:
        ax[0].scatter(X[:, 0], np.zeros_like(X[:, 0]), s=70, color="red")
    if dimension == 1:
        ax[0].scatter(np.zeros_like(X[:, 1]), X[:, 1], s=70, color="red")

    ax[0].set_title("Dropping the column " + data.columns[drop], fontsize=w + h)
    ax[0].set_xlabel(data.columns[0], fontdict={"fontsize": w})
    ax[0].set_ylabel(data.columns[1], fontdict={"fontsize": w})

    # The functions called here are the same as above,
    # but this time is for the plot on the right
    ax[1].scatter(X[:, dimension], np.zeros_like(X[:, 0]), s=70, color="red")
    ax[1].set_title("Projected points", fontsize=w + h)
    ax[1].set_yticks([])
    ax[1].set_xlabel("$Z_1 = $" + data.columns[dimension], fontdict={"fontsize": w})    
    
    
from sklearn.metrics.cluster import silhouette_score


def plot_silhouette_scores(X, y, algorithms = [KMeans(n_clusters=2), DBSCAN()]): 
    # rescale the data to zero mean and unit variance
    fig, axes = plt.subplots(1, 3, figsize=(12, 3),
                             subplot_kw={'xticks': (), 'yticks': ()})

    # create a random cluster assignment for reference
    random_state = np.random.RandomState(seed=0)
    random_clusters = random_state.randint(low=0, high=2, size=len(X))

    # plot random assignment
    axes[0].scatter(X[:, 0], X[:, 1], c=random_clusters,
                    cmap=mglearn.cm3, s=60)
    axes[0].set_title("Random: Silhouette score={:.2f}".format(
        silhouette_score(X, random_clusters)))

    

    for ax, algorithm in zip(axes[1:], algorithms):
        clusters = algorithm.fit_predict(X)
        # plot the cluster assignments and cluster centers
        ax.scatter(X[:, 0], X[:, 1], c=clusters, cmap=mglearn.cm3,
                   s=60)
        ax.set_title("{}: Silhouette score={:.2f}".format(algorithm.__class__.__name__,
                                          silhouette_score(X, clusters)))    
        
def hc_truncation_toy_demo(linkage_array):
    # Credit: adapted from here: https://stackoverflow.com/questions/66180002/scipy-cluster-hierarchy-dendrogram-exactly-what-does-truncate-mode-level-do
    fig, ax_rows = plt.subplots(ncols=5, nrows=2, sharey=True, figsize=(14, 5))

    for ax_row, truncate_mode in zip(ax_rows, ['level', 'lastp']):
        dendrogram(linkage_array, p=4, truncate_mode="level", ax=ax_row[0])
        ax_row[0].set_title('default, no truncation')
        for ind, ax in enumerate(ax_row[1:]):
            if truncate_mode == 'level':
                p = len(ax_row) - ind - 1
            else:
                p = len(ax_row) - ind
            dendrogram(linkage_array, truncate_mode=truncate_mode, p=p, ax=ax)
            ax.set_title(f"truncate_mode='{truncate_mode}', p={p}")
    plt.tight_layout()
    plt.show()        
    
def print_dbscan_noise_images(X_people, y_people, dbscan, labels, image_shape=(87, 65)):
    noise = X_people[labels == -1]

    fig, axes = plt.subplots(
        2, 9, subplot_kw={"xticks": (), "yticks": ()}, figsize=(12, 4)
    )
    for image, ax in zip(noise, axes.ravel()):
        ax.imshow(image.reshape(image_shape), vmin=0, vmax=1)
    
def print_dbscan_clusters(X_people, y_people, labels, image_shape=(87, 65)):
    i = 0
    for cluster in range(max(labels) + 1):
        mask = labels == cluster
        n_images = np.sum(mask)
        fig, axes = plt.subplots(
            1,
            n_images,
            figsize=(n_images * 1.5, 4),
            subplot_kw={"xticks": (), "yticks": ()},
        )
        for image, label, ax in zip(X_people[mask], y_people[mask], axes):
            ax.imshow(image.reshape(image_shape), vmin=0, vmax=1)
            ax.set_title("cluster %d" % (i))
        i += 1    
        
def print_hierarchical_clusters(X_people, y_people, target_names, cluster_labels, unique_cluster_labels=[2, 3, 6, 29, 30, 36, 38], image_shape=(87, 65)):
    for cluster in unique_cluster_labels: # hand-picked "interesting" clusters
        mask = cluster_labels == cluster
        fig, axes = plt.subplots(
            1, 15, subplot_kw={"xticks": (), "yticks": ()}, figsize=(15, 8)
        )
        cluster_size = np.sum(mask)
        axes[0].set_ylabel("#{}: {}".format(cluster, cluster_size))
        for image, label, asdf, ax in zip(
            X_people[mask], y_people[mask], cluster_labels[mask], axes
        ):
            ax.imshow(image.reshape(image_shape), vmin=0, vmax=1)
            ax.set_title(target_names[label].split()[-1], fontdict={"fontsize": 9})
        for i in range(cluster_size, 15):
            axes[i].set_visible(False)        
            
def plot_swiss_roll(X, colour, swiss_tsne):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1,2,1, projection="3d")
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=colour, cmap=plt.cm.Spectral)

    ax.set_title("Original data")
    ax = fig.add_subplot(122)
    ax.scatter(swiss_tsne[:, 0], swiss_tsne[:, 1], c=colour, cmap=plt.cm.Spectral)
    #plt.axis("tight")
    plt.xticks([]), plt.yticks([])
    plt.title("Projected data with t-SNE")
    plt.show()            
    
def plot_update_centroid(data, w, h, new_centroids, centroids, dist):
    colors = np.array(['black', 'blue', 'red', 'green', 'purple'])
    plt.figure(figsize=(w, h))
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1],
                c=colors[np.argmin(dist, 1)])
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

def plot_sup(data, w, h, title=None):
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
    # Colors to be used (upt to 5 classes)
    colors = np.array(['black', 'blue', 'red', 'green', 'purple'])
    
    col_names = data.columns.to_numpy()
    target_names = data['target'].to_numpy()

    # Getting numerical values for the classes labels
    target = np.unique(data['target'].to_numpy(), return_inverse=True)

    # Getting X1 and X2
    data = data.iloc[:, 0:2].to_numpy()
    
    plt.figure(figsize=(w, h))
    plt.title(title, fontdict={'fontsize': 1.2*(w + h)})
    ax = plt.gca()
    for i, label in enumerate(target[0]):
        plt.scatter(data[target_names == label, 0],
                    data[target_names == label, 1],
                    c=colors[i], label=label)
    

    
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

#     ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': w + h})
#     ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': w + h})

    # Creates the unsupervised subplot.
    plt.subplot(1, 2, 2)
    ax = plt.gca()
    plt.scatter(data[:, 0], data[:, 1])
    plt.title("Unsupervised", fontdict={'fontsize': 2 * (w + h)})
    plt.xlabel(col_names[0], fontsize=1.5*(w + h))
    plt.ylabel(col_names[1], fontsize=1.5*(w + h))
#     ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': w + h})
#     ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': w + h})


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
        
def plot_iterative(data, w, h, starting_centroid):
    k = starting_centroid.shape[0]
    colors = np.array(['black', 'blue', 'red', 'green', 'purple'])
    x = data.iloc[:, 0:2].to_numpy()
    plt.figure(figsize=(w, h))
    centroids = starting_centroid.copy()
    for i in range(0, 5):
        dist = distance.cdist(x, centroids)
        u = np.zeros((k, x.shape[0]))
        u[np.argmin(dist, axis=1), range(0, data.shape[0])] = 1
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

    plt.scatter(df[p, 0], df[p, 1], c="green", zorder=10, s=200)

    c1 = Circle((.1, -.12), 0.27, fill=False, linewidth=2, color='black')
    c2 = Circle((1.03, 1.04), 0.27, fill=False, linewidth=2, color='blue')
    c3 = Circle((2.48, 0.1), 0.27, fill=False, linewidth=2, color='red')
    ax.add_artist(c1)
    ax.add_artist(c2)
    ax.add_artist(c3)
    plt.xlabel("X1", fontdict={'fontsize': w})
    plt.ylabel("X2", fontdict={'fontsize': w})
    plt.title("Distances for silhouette", fontdict={'fontsize': w+h})        
    
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
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], marker='o')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=250,
                marker='*', color=colors[0:n_clusters])
    plt.xlabel(data.columns[0], fontdict={'fontsize': w})
    plt.ylabel(data.columns[1], fontdict={'fontsize': w})
    plt.title(title, fontdict={'fontsize': (w + h)})
    ax = plt.gca()
    #ax.set_xticklabels(ax.get_xticks(), fontdict={'fontsize': 0.8*w})
    #ax.set_yticklabels(ax.get_yticks(), fontdict={'fontsize': 0.8*w})

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
                c=colors[np.argmin(dist, 1)])
    plt.scatter(centroids.iloc[:, 0],
                centroids.iloc[:, 1],
                s=300, marker='*', color=colors[0:k])
    plt.xlabel(data.columns[0], fontdict={'fontsize': w})
    plt.ylabel(data.columns[1], fontdict={'fontsize': w})

    plt.title("First round of assignment - Step #1",
              fontdict={'fontsize': w+h})

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

    plt.scatter(df[p, 0], df[p, 1], c="green", zorder=10, s=200)

    c1 = Circle((.1, -.12), 0.27, fill=False, linewidth=2, color='black')
    c2 = Circle((1.03, 1.04), 0.27, fill=False, linewidth=2, color='blue')
    c3 = Circle((2.48, 0.1), 0.27, fill=False, linewidth=2, color='red')
    ax.add_artist(c1)
    ax.add_artist(c2)
    ax.add_artist(c3)
    plt.xlabel("X1", fontdict={'fontsize': w})
    plt.ylabel("X2", fontdict={'fontsize': w})
    plt.title("Distances for silhouette", fontdict={'fontsize': w+h})    
    