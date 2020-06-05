## Homework info & submission guidelines

All assignments will be submitted via [github.students.cs.ubc.ca](https://github.students.cs.ubc.ca/).

### Student repositories
For every assignment, we will create a repository (repo) for each student. The repository will be named based on an internal ID
that we generate for each student. For example, 
if your id is `goatcabin` then for assignment 1 there will be a repository called
`hw1_goatcabin`. The assignment will ship with the necessary code/data.

If you visit [the organization homepage](https://github.students.cs.ubc.ca/cpsc330-2020w-t1) you will see a list of all repositories that you have access to.

## Homework submission instructions

Your homework repo must contain a `README.md` file. **This README must contain a clickable link to your main report**, and every other file you want the TA to look at (if any), so that TA can find them easily. The markdown syntax for creating a link is `[LINK TEXT](PATH TO FILE)`. The path doesn't have to include the full URL if it's all in the same GitHub repository. For example, if you have a file called `hw1.ipynb` in your `doc` directory, you could create a link in your README with `[Here's the link to my report](doc/hw1.ipynb)`. Once you commit the README file you can try clicking the link to make sure it works.

The README can optionally include any additional info related to your assignment, such as:
  - feedback to the instructor about whether you liked/disliked the assignment, how long it took you, etc.
  - extra dependencies needed to run your code.
  - additional explanation of how your repo is organized.

Please push all your finalized work to the `master` branch. (If you don't know what that is, you can ignore this instruction, as it will be the default.)

#### Datasets

Unless otherwise noted, if you download a dataset for your assignment, please do **not** push the dataset to your repo. (If the dataset in bundled with the assignment, then it's of course fine to leave it there.)

#### Report format

Your final report must be submitted online as a Jupyter notebook via GitHub, so please do not write up your answers on paper! 

Be sure that your answers are clearly written and easy for the TA to understand. The TAs have the option to reduce your mark if your answers aren't clear or are difficult to understand (even if they are correct). Preparing your answers in LaTeX is one easy way to reduce the chance of this happening.

Finally, you must ensure that all your code output (values, tables, figures, etc.) is displayed in the notebook. For example, if you are required to calculate some value, it is not sufficient to just store the value to a variable, nor is it sufficient to have a `print(value)` in your code - the print code must actually be run and the notebook saved, so that the output is shown on the screen when the notebook is rendered. This allows the TAs to see your results without running your code. Failure to display all output will result in a deduction of marks.

**If you are unsure whether your report is rendering properly, just open it up inside your web browser on github.students.cs.ubc.ca. This is exactly how your TA will see it.**

#### Figures

In most assignments, you will be asked to produce plots/figures. When including figures in your submission:

- Embed the figures in your report. Make sure your `.ipynb` file includes all the figures you want the TAs to see.
- All figures must include axis labels and, if multiple curves are present on the same figure, a legend.
- All figures must have some accompanying text explaining what the figure is about. You can do this by putting a figure title in the image itself (such as, "Training error vs. k") or you can use LaTeX to add figure captions that appear underneath the figure.
- Regardless of your image formats, all text must be big enough to read without straining or zooming. Please be careful about this for axis labels, legends, titles, etc. Avoid tiny text!

## Groups
You must work alone for Assignment 1. For Assignment 2 onwards, you may work with a partner or work alone. You can make this decision independently for each assignment. To work with a partner, you must request the partnership **before the assignment is released** (no exceptions!) by logging in at https://cs330.students.cs.ubc.ca/, specifying the deliverable (e.g. hw2), and then specifying the CWL username of your partner. At present, only one person needs to do this to create the team, although we can revisit this is the system is abused. 

If you work with a partner, you may be asked to write a short statement explaining how each team member contributed to the submission.

The assignments will probably be released shortly after the previous assignment is due. So, to partner up with someone for hw2, we suggest specifying the partnership by the day hw1 is due. You can specify your partner as early as you want, so for example it's fine to do this for all assignments at the beginning of the course, if you know who your partner will be for all of them.

If you did this successfully, then a single repository will be created for both of you to work on. For example, if your username is `goatcabin` and your partner's username is `rhomboid` then your joint hw1 repository will be named `hw1_goatcabin_rhomboid` (or `hw1_rhomboid_goatcabin`) and you will both have write access to it. If something went wrong and you got individual repositories named `hw1_goatcabin` and `hw1_rhomboid` even though you followed all the above instructions, please contact the instructor.

Suggestion: if you've never used git/GitHub and/or Python before, try to find a partner who has, especially for the early assignments when these tools are new to you.

Note: our primitive (but steadily improving) system currently doesn't support changing partners. So, please be sure before you make a request.

## Late submissions

**Late assignments**. Late submissions will not be accepted. There will be no exceptions made, including illness, so try to start early on your assignments. The rationale is that we will be posting the solutions shortly after the assignment deadline, and we cannot accept submissions after the solutions are posted. Admittedly there will be a handful of unfortunate situations where someone loses marks due to an unforeseeable circumstance. I do not like this, but I believe the overall policy is best for the class as a whole.

## Updates to assignments

It happens sometimes that the instructor needs to make changes to an assignment after it is posted. Because you all have your own personal copies of the assignment, this is a bit tricker than simply updating a posted version. Instead, each group receives a [pull request](https://en.wikipedia.org/wiki/Distributed_version_control#Pull_requests) (PR) with the changes (we will also have a thread on Piazza giving the list of changes and their dates).

Note: when you go to the "Files Changed" tab in the PR, in some cases there are trivial changes of whitespace being added or removed; if they bother you, you can ignore them by appending `?w=1` to the URL in your browser.

I suggest that you _push all your local changes_ before merging, to avoid conflicts down the line. Once you merge through the browser, and then pull locally, you will have the updated version that contains all the prior work you've done, plus the instructor's changes.

Other times you won't see the big green button because there are merge conflicts. If this happens, it's up to you whether you want to sort out the conflicts or just skip the merging. **It is not mandatory to merge these PRs**; you might be fine by just looking at the files changed and manually addressing them.

Finally, if there are multiple pull requests for the same assignment, the behavior depends on whether or not you merged the original ones. If you merged the prior pull request(s), a new one will be created. If not, the new commits will be appended to the original pull request.

## Citing sources
If you use information from students outside your group or from online sources _including code snippets from Stack Overflow_, cite this at the start of each question. **You will receive a mark of 0 for the assignment (and possibly other consequences) if you are found copying from other sources without citation**.

