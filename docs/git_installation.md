# What are git and GitHub?

GitHub uses the [git version control system](https://en.wikipedia.org/wiki/Git). Roughly speaking, git is the system that 
takes care of different versions of your files and merging together changes from different collaborators (and much more!). 
git is [free software](https://en.wikipedia.org/wiki/Free_software). 

GitHub is a corporation and the name of the corporation's product. Their site github.com provides servers that host git
repositories. This serves as a central place that different collaborators all sync up with. 

GitHub Enterprise is a product
that allows the GitHub software to be installed on the customer's own servers. UBC has done this so that all the data remains
in Canada. Hence https://github.students.cs.ubc.ca/.

# GitHub Desktop

The instructions below pertain to using git from the command line. For those who are less comfortable with this sort of thing, I was told that [GitHub Desktop](https://desktop.github.com/) makes things a lot easier. So, feel free to try this route instead of the instructions below.

# Command-line git

## Setting up

GitHub is a web-based application and does not require set-up. However, you will be working on your homework locally
and therefore need git installed locally. 

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


## Testing your git installation

Open your Terminal (or Git for Windows) and run `git --version`.  
If you are returned the version of git, it means your install was successful!

## Learning git

There are many free online resources for learning git. One possibility is the [Software Carpentry git tutorial](https://swcarpentry.github.io/git-novice/). 

## Authentication

For viewing GitHub content in your web browser, you login with your CWL credentials through the browser. However, you need
to authenticate separately to interact with GitHub through command-line git. In order to authenticate, you need to set up SSH keys.
[Here are instructions](https://help.github.com/en/enterprise/2.19/admin/installation/upgrading-github-enterprise-server) for setting up an SSH key and adding it to GitHub. In the last section, replace `hostname` with `github.students.cs.ubc.ca`. 

When cloning your repository, make sure you get the clone url that starts with `ssh`, not the one that starts with `https`.

# Who can see my repos?

#### Assignment repo
Your homework repo is only visible to you and the course staff, plus your partner if you are working with one.

#### Grades repo
Your grades repo will be visible only to yourself and the course staff.

#### Past commits
Although only the final version will be graded, _all_ of your commits will be viewable, so don't commit something
private (like your email password) to your homework repo. Committing something and then removing it
with another commit doesn't remove it from the git history! It is theoretically possible to pull all traces of
something out of the git history, but it's not fun and uses more advanced git features.

### Finding my repositories

Probably the easiest way to find a repository is to use the search tool from [the cpsc330-2020w-t1 Organization homepage](https://github.students.cs.ubc.ca/cpsc330-2020w-t1).

### Submission
We anticipate that you will clone your assignment repo and do your work from
within there. When you push something back to github.students.cs.ubc.ca then you have submitted the assignment.
You can push changes as many times as you want before the deadline; only the final version will be graded (but see [below](homework_instructions.md#past-commits) on past commits).

### Grades
In addition to the lab-specific repos, you will each have a private repository that will serve as
an inbox for all your grade-related discussions. This repository will be named `goatcabin_grades` if your username is `goatcabin`. There will be an announcement when grades are released. 
