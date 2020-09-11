## Homework info & submission guidelines

To find your assignments, go to https://github.students.cs.ubc.ca/cpsc330-2020w-t1.

## Student repositories
For every assignment, we will create a repository (repo) for each student. The repository will be named based on an internal ID
that we generate for each student. For example, 
if your id is `goatcabin` then for assignment 1 there will be a repository called
`hw1_goatcabin`. The assignment will ship with the necessary code/data.

If you visit [the organization homepage](https://github.students.cs.ubc.ca/cpsc330-2020w-t1) you will see a list of all repositories that you have access to.

## How to submit

We anticipate that you will clone your homework-specific repository and do your work from within there. GitHub provides you with a backup, version control for your work, a way to collaborate with others, to show unfinished work to instructors and ask for help, etc. To submit your homework you must both push your work to https://github.students.cs.ubc.ca/ **and submit your rendered HTML file to Canvas** where it will be graded. Your assignment will come bundled (at the very bottom of the notebook) with a short script to render to HTML and push your work to Canvas. To use that script, you will need to create a Canvas token. For a demo on how to do that, see [this video](https://drive.google.com/file/d/1touljci-tGXxBq4lhW1hnlr04-tQ8zMo/view) by my colleague Tomas Beuzen (his video is for another course, but the basic idea is the same).

Once you submit to Canvas, you should go to Canvas and ensure your assignment is there as expected. It is your responsibility to make sure your assignment is submitted to both places and failure to do so will result in a deduction of marks.

## Other submission instructions

#### Datasets

Unless otherwise noted, if you download a dataset for your assignment, please do **not** push the dataset to your repo. (If the dataset in bundled with the assignment, then it's of course fine to leave it there.)

#### Report format

Your final report must be submitted online as a Jupyter notebook, so please do not write up your answers on paper! 

Be sure that your answers are clearly written and easy for the TA to understand. The TAs have the option to reduce your mark if your answers aren't clear or are difficult to understand (even if they are correct). Preparing your answers in LaTeX is one easy way to reduce the chance of this happening.

Finally, you must ensure that all your code output (values, tables, figures, etc.) is displayed in the notebook. For example, if you are required to calculate some value, it is not sufficient to just store the value to a variable, nor is it sufficient to have a `print(value)` in your code - the print code must actually be run and the notebook saved, so that the output is shown on the screen when the notebook is rendered. This allows the TAs to see your results without running your code. Failure to display all output will result in a deduction of marks.

**If you are unsure whether your report is rendering properly, please view your submission in Canvas. This is exactly how your TA will see it.**

#### Figures

In most assignments, you will be asked to produce plots/figures. When including figures in your submission:

- Embed the figures in your report. Make sure your `.ipynb` file includes all the figures you want the TAs to see.
- All figures must include axis labels and, if multiple curves are present on the same figure, a legend.
- All figures must have some accompanying text explaining what the figure is about. You can do this by putting a figure title in the image itself (such as, "Training error vs. k") or you can use LaTeX to add figure captions that appear underneath the figure.
- Regardless of your image formats, all text must be big enough to read without straining or zooming. Please be careful about this for axis labels, legends, titles, etc. Avoid tiny text!

## Groups
You must work alone for Assignment 1. For Assignment 2 onwards (assuming technical issues can be solved - TBD), you may work with a partner or work alone. You can make this decision independently for each assignment. To work with a partner, you must request the partnership **before the assignment is released** (no exceptions!) by **following TBD instructions**.  At present, only one person needs to do this to create the team, although we can revisit this is the system is abused. 

The assignments will probably be released shortly after the previous assignment is due. So, to partner up with someone for hw2, we suggest specifying the partnership by the day hw1 is due. You can specify your partner as early as you want, so for example it's fine to do this for all assignments at the beginning of the course, if you know who your partner will be for all of them.

If you did this successfully, then a single repository will be created for both of you to work on. For example, if your username is `goatcabin` and your partner's username is `rhomboid` then your joint hw1 repository will be named `hw1_goatcabin_rhomboid` (or `hw1_rhomboid_goatcabin`) and you will both have write access to it. If something went wrong and you got individual repositories named `hw1_goatcabin` and `hw1_rhomboid` even though you followed all the above instructions, please contact the instructor.

Suggestion: if you've never used git/GitHub and/or Python before, try to find a partner who has, especially for the early assignments when these tools are new to you.

Note: our primitive system currently doesn't support changing partners. So, please be sure before you make a request.

## Late submissions

By default late submissions will not be accepted. The rationale is that we will be posting the solutions shortly after the assignment deadline, and we cannot accept submissions after the solutions are posted. I do not like this, but I believe the overall policy is best for the class as a whole.

_In exceptional circumstances_ a late submission may be accepted with an academic concession - see [here](https://github.com/UBC-CS/cpsc330/blob/master/docs/course_info.md#academic-concessions) for more info.

## Updates to assignments

If there are errors or other changes that need to be made to an assignment, I will announce them in a pinned Piazza post.

## Citing sources
If you use information from students outside your group or from online sources _including code snippets from Stack Overflow_, cite this at the start of each question. **You will receive a mark of 0 for the assignment (and possibly other consequences) if you are found copying from other sources without citation**.

