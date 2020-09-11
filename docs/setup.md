# Programming environment

## Python
We will be using Python for this course because it is open source and widely used in machine learning and data science.  We will use Python 3 (in particular 3.7 or 3.8). **Python 2 is not supported in this course.**

We recommend the Anaconda Python distribution because it comes bundled with a bunch of useful packages (NumPy, SciPy, scikit-learn, Jupyter notebook) pre-installed. You can [download Anaconda from their website](https://www.anaconda.com/download/) for free.

For resources on learning Python, see the [resources page](resources.md).


## Virtual environment

### What and Why
A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system. ([https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)) For example, you may want a certain version of tensorflow for one project but another version for a different project. Virtual environments helps us to build environment isolation between different projects and make sure any change to dependencies affects only the projects that need it.

### Setting up a virtual environment
- **Option 1: Conda environments (preferred)**
	1. Make sure that `conda` is installed by running
		```
		conda env list
		```
		You should see a list of environments as the output. If Anaconda/Miniconda is not installed, you can download Anaconda from [here](https://www.anaconda.com/download/) or Miniconda (a small, bootstrap version of Anaconda) from [here](https://docs.conda.io/en/latest/miniconda.html)
	2. Download [cpsc330env.yml](cpsc330env.yml) and put it in your working directory
	3. Create an environment by
		```
		conda env create -f cpsc330env.yml
		```
		which allows `conda` to download the dependencies needed for this course and put them in a virtual environment named `cpsc330env`.
		You can check that the environemnt is installed successfully by running `conda env list` again. `cpsc330env` should show up in the output.
	4. Activate the environment with
		```
		conda activate cpsc330env
		```
		After a successful activation, something like `(cpsc330env)` should show up in the terminal.
	5. We are all set! You can now run homework and lecture materials within the virtual environment.
	6. To deactivate the environment, run
		```
		conda deactivate
		```
	For more information on conda environments, see [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
	
- **Option 2: `Virtualenv`**
	1. You can choose this option if your have python version 3.7.x or 3.8.x installed on your system. To find out, run
		```
		python3 --version
		```
	2. Install `Virtualenv` with
		```
		python3 -m pip install --user virtualenv
		```
	3. Navigate to your working directory and create new virtual environment with
		```
		virtualenv -p python3 cpsc330env
		```
		This will create a folder in your current directory that stores all the packages for this virtual environment.
	4. Activate the environment
		OS X/Linux:
		```
		source cpsc330env/bin/activate
		```
		Windows:
		```
		cpsc330env\Scripts\activate
		```
		If you happen to use csh or fish shell, source the corresponding activate file. 
		After a successful activation, something like `(cpsc330env)` should show up in the terminal.
	5. Download [requirement.txt](requirement.txt) and put it in your working directory. Then install the dependencies listed with
		```
		pip install -r requirements.txt
		```
	6. We are all set! You can now run homework and lecture materials within the virtual environment.
	7. To deactivate the virtual environment, run
		```
		deactivate
		```
	For more information on `virtualenv`, see [here](https://virtualenv.pypa.io/en/latest/index.html).

### Steps to enable canvas utitlity

Activate the virtual environment, then run the following commands
```
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension update --all 
jupyter lab build
```

### Git

Please also see the [git setup instructions](https://github.com/UBC-CS/cpsc330/blob/master/docs/git_installation.md) as you will need git as well for the course.

		
