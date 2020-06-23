# Programming environment: Python

We will be using Python for this course because it is open source and widely used in machine learning and data science.  We will use Python 3 (in particular 3.7 or 3.8). **Python 2 is not supported in this course.**

We recommend the Anaconda Python distribution because it comes bundled with a bunch of useful packages (NumPy, SciPy, scikit-learn, Jupyter notebook) pre-installed. You can [download Anaconda from their website](https://www.anaconda.com/download/) for free.

If you don't want to use Anaconda, you can install the individual packages with `pip`. The annoying thing about Python is that the name of the package doesn't necessarily match the name in the code. For example if you see `import sklearn` in the code, you might (naively believing that we live in a sane world) try `pip install sklearn` but in fact it should be `pip install scikit-learn`. (Also, `pip` should be installing packages for Python 3 by default, but if you have both Python 2 and 3 installed with Python 2 as your default, you may need to use `pip3` in place of `pip`.)

For resources on learning Python, see the [resources page](resources.md).
