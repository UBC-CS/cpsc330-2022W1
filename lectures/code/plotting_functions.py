from utils import *
import matplotlib.pyplot as plt
import mglearn
from imageio import imread


def plot_tree_decision_boundary(
    model, X, y, x_label="x-axis", y_label="y-axis", eps=None, ax=None, title=None
):
    if ax is None:
        ax = plt.gca()

    if title is None:
        title = "max_depth=%d" % (model.tree_.max_depth)

    mglearn.plots.plot_2d_separator(
        model, X.to_numpy(), eps=eps, fill=True, alpha=0.5, ax=ax
    )
    mglearn.discrete_scatter(X.iloc[:, 0], X.iloc[:, 1], y, ax=ax)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)


def plot_tree_decision_boundary_and_tree(
    model, X, y, height=6, width=16, x_label="x-axis", y_label="y-axis", eps=None
):
    fig, ax = plt.subplots(
        1,
        2,
        figsize=(width, height),
        subplot_kw={"xticks": (), "yticks": ()},
        gridspec_kw={"width_ratios": [1.5, 2]},
    )
    plot_tree_decision_boundary(model, X, y, x_label, y_label, eps, ax=ax[0])
    ax[1].imshow(tree_image(X.columns, model))
    ax[1].set_axis_off()
    plt.show()
    
def plot_fruit_tree(ax=None):
    import graphviz

    if ax is None:
        ax = plt.gca()
    mygraph = graphviz.Digraph(
        node_attr={"shape": "box"}, edge_attr={"labeldistance": "10.5"}, format="png"
    )
    mygraph.node("0", "Is tropical?")
    mygraph.node("1", "Has pit?")
    mygraph.node("2", "Is red?")
    mygraph.node("3", "Mango")
    mygraph.node("4", "Banana")
    mygraph.node("5", "Cherry")
    mygraph.node("6", "Kiwi")
    mygraph.edge("0", "1", label="True")
    mygraph.edge("0", "2", label="False")
    mygraph.edge("1", "3", label="True")
    mygraph.edge("1", "4", label="False")
    mygraph.edge("2", "5", label="True")
    mygraph.edge("2", "6", label="False")
    mygraph.render("tmp")
    ax.imshow(imread("tmp.png"))
    ax.set_axis_off()    