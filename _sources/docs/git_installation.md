# What are git and GitHub?

GitHub uses the [git version control system](https://en.wikipedia.org/wiki/Git). Roughly speaking, git is the system that takes care of different versions of your files and merging together changes from different collaborators (and much more!). git is [free software](https://en.wikipedia.org/wiki/Free_software). 

GitHub is a corporation and the name of the corporation's product. Their site github.com provides servers that host git repositories. This serves as a central place that different collaborators all sync up with. 

We won't be using it in our class but GitHub Enterprise is a product that allows the GitHub software to be installed on the customer's own servers. UBC has done this so that all the data remains in Canada. Hence https://github.students.cs.ubc.ca/.

# GitHub Desktop

The instructions below pertain to using git from the command line. For those who are less comfortable with this sort of thing, I was told that [GitHub Desktop](https://desktop.github.com/) makes things a lot easier. So, feel free to try this route instead of the instructions below.

# Command-line git

## Setting up

GitHub is a web-based application and does not require set-up. Since you will be cloning the [course GitHub repository](https://github.com/UBC-CS/cpsc330) in order to run the lecture notebooks locally, you need git installed locally. Follow the instructions below for this. 

#### Mac Users

Open Terminal (Applications –> Utilities folder or search with Spotlight). From the terminal, run the command:

```
xcode-select --install
```

This will install git and many other very useful applications as well (including Make).

#### Ubuntu Users

Open the terminal and install git using your system package manager. For example

```
sudo apt-get install git
```

should do the trick on Ubuntu.

#### Windows Users

Go to http://git-scm.com. Click on the download link, and accept all defaults in the installation process. 
Installing git will also install for you a minimal UNIX environment with a bash shell and terminal window. 


If the above does not work for you, follow the [installation instructions here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Testing your git installation

Open your Terminal (or Git for Windows) and run `git --version`.  
If you are returned the version of git, it means your install was successful!

## Learning git

There are many free online resources for learning git. One possibility is the [Software Carpentry git tutorial](https://swcarpentry.github.io/git-novice/). 
