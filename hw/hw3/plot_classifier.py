import numpy as np
import matplotlib.pyplot as plt

def make_meshgrid(x, y, num_pts=300, lims=None):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis meshgrid on
    y: data to base y-axis meshgrid on
    h: stepsize for meshgrid, optional

    Returns
    -------
    xx, yy : ndarray
    """

    if lims is None:
        x_min, x_max = x.min() - 1, x.max() + 1
        y_min, y_max = y.min() - 1, y.max() + 1
    else:
        x_min, x_max, y_min, y_max = lims
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, num_pts),
                         np.linspace(y_min, y_max, num_pts))
    return xx, yy


def plot_contours(ax, clf, xx, yy, proba=False, transformation=None, labels=None, **params):
    """Plot the decision boundaries for a classifier.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """

    X = np.c_[xx.ravel(), yy.ravel()]
    if transformation is not None:
        X = transformation(X)

    if proba == "raw":
        Z = clf.decision_function(X)
        Z = Z.reshape(xx.shape)
        # out = ax.contourf(xx, yy, Z, **params)
        out = ax.imshow(Z,extent=(np.min(xx), np.max(xx), np.min(yy), np.max(yy)), origin='lower', **params)
        ax.contour(xx, yy, Z, levels=[0])
    elif proba:
        Z = clf.predict_proba(X)[:,-1]
        Z = Z.reshape(xx.shape)
        out = ax.imshow(Z,extent=(np.min(xx), np.max(xx), np.min(yy), np.max(yy)), origin='lower', vmin=0, vmax=1, aspect="auto", **params)
        ax.contour(xx, yy, Z, levels=[0.5])
    else:
        Z = clf.predict(X)

        # in case the labels are strings instead of indices, convert them to numerical
        if labels is not None:
            Z2 = Z
            for i, label in enumerate(labels):
                Z2[Z2==label] = i
            Z = Z2

        Z = Z.reshape(xx.shape)
        out = ax.contourf(xx, yy, Z, **params)
    return out

# adapted from http://scikit-learn.org/stable/auto_examples/svm/plot_iris.html
def plot_classifier(X, y, clf, ax=None, ticks=False, proba=False, lims=None, transformation=None, show_data=True, gray_photocopy=False, proba_showtitle=True, **kwargs): # assumes classifier "clf" is already fit
    try: 
        X = X.to_numpy()
    except:
        pass
    
    try:
        y = np.squeeze(y.to_numpy())
    except:
        pass

    X0, X1 = X[:, 0], X[:, 1]
    xx, yy = make_meshgrid(X0, X1, lims=lims)

    if ax is None:
        plt.figure()
        ax = plt.gca()
        show = True
    else:
        show = False

    labels = np.unique(y)

    if gray_photocopy:
        kwargs["cmap"] = kwargs.get("cmap", plt.cm.YlOrRd) # default cmap for photocopied grayscale exams
    else:
        kwargs["cmap"] = kwargs.get("cmap", plt.cm.coolwarm) # default cmap, but user can overrule it

    # can abstract some of this into a higher-level function for learners to call
    cs = plot_contours(ax, clf, xx, yy, proba=proba, transformation=transformation, labels=labels, alpha=0.8, **kwargs)

    if proba == "raw":
        cbar = plt.colorbar(cs)
        cbar.ax.set_ylabel('raw model output', fontsize=20, rotation=270, labelpad=30)
        cbar.ax.tick_params(labelsize=14)
    elif proba:
        cbar = plt.colorbar(cs)
        if proba_showtitle:
            cbar.ax.set_ylabel('probability of red $\Delta$ class', fontsize=20, rotation=270, labelpad=30)
        cbar.ax.tick_params(labelsize=14)

    if show_data:
        #ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=30, edgecolors='k', linewidth=1)
        if len(labels) == 2:
            ax.scatter(X0[y==labels[0]], X1[y==labels[0]], s=60, c='b', marker='o', edgecolors='k')
            ax.scatter(X0[y==labels[1]], X1[y==labels[1]], s=60, c='r', marker='^', edgecolors='k')
        elif len(labels) == 3:
            ax.scatter(X0[y==labels[0]], X1[y==labels[0]], s=60, c='b', marker='o', edgecolors='k')
            ax.scatter(X0[y==labels[1]], X1[y==labels[1]], s=60, c='r', marker='^', edgecolors='k')
            ax.scatter(X0[y==labels[2]], X1[y==labels[2]], s=60, c='k', marker='x', edgecolors='k')
        else:
            ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=50, edgecolors='k', linewidth=1)
            # plt.legend(labels) # doesn't work
            # see https://stackoverflow.com/questions/43967663/scatter-plot-with-legend-colored-by-group-without-multiple-calls-to-plt-scatter

    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
#     ax.set_xlabel(data.feature_names[0])
#     ax.set_ylabel(data.feature_names[1])
    if not ticks:
        ax.set_xticks(())
        ax.set_yticks(())
#     ax.set_title(title)
    # if show:
        # plt.show()
    # else:
    return ax

def plot_4_classifiers(X, y, clfs):

    # Set-up 2x2 grid for plotting.
    fig, sub = plt.subplots(2, 2)
    plt.subplots_adjust(wspace=0.2, hspace=0.2)

    for clf, ax, title in zip(clfs, sub.flatten(), ("(1)", "(2)", "(3)", "(4)")):
        # clf.fit(X, y)
        plot_classifier(X, y, clf, ax, ticks=True)
        ax.set_title(title)
    plt.show()


def plot_loss_diagram(labels_inside=False):
    grid = np.linspace(-2,2,1000)
    plt.figure()
    plt.xlabel('$y_iw^T x_i$', fontsize=18)
    # plt.xlabel('raw model output')
    plt.ylabel('$f_i(w)$', fontsize=18)
    plt.xlim(-2,2)
    plt.ylim(-0.025,3)
    plt.fill_between([0, 2], -1, 3, facecolor='blue', alpha=0.2);
    plt.fill_between([-2, 0], -1, 3, facecolor='red', alpha=0.2);
    plt.yticks([0,1,2,3]);

    if labels_inside:
        plt.text(-1.95, 2.73, "incorrect prediction", fontsize=15) # 2.68
        plt.text(0.15, 2.73, "correct prediction", fontsize=15)
    else:
        plt.text(-1.95, 3.1, "incorrect prediction", fontsize=15) # 2.68
        plt.text(0.15, 3.1, "correct prediction", fontsize=15)


    plt.tight_layout()

