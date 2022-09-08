# Homework info & submission guidelines

You will be submitting your homework assignments on Gradescope. Check out [Gradescope Student Guide](https://lthub.ubc.ca/guides/gradescope-student-guide/). 

## Accessing homework assignments
Every homework assignment will be made available on the [course GitHub page](https://github.com/UBC-CS/cpsc330) under the `hw` folder. Once it's available, I'll make an announcement on Piazza. The assignment will generally consist of a Jupyter notebook along with necessary code and data or links to download the data. You will have to setup your computer so that you can work on these assignments locally. See this document for [setup instructions](setup.md).       

## How to submit

We anticipate that you will do `git pull` in your local course repository when the homework is made released. You may work on your homework locally or in a private GitHub repository, which provides you with a backup, version control for your work, a way to collaborate with others, to show unfinished work to instructors and ask for help, etc. To submit your homework you must **submit your final version of the notebook to [Gradescope](https://www.gradescope.ca/courses/5032)** where it will be graded. 

Once you submit to Gradescope, you should go there and ensure your assignment is there as expected and all the output and plots are rendered properly. **It is your responsibility to make sure your assignment is submitted properly and failure to do so will result in a deduction of marks.**

## Other submission instructions

### Datasets

Unless otherwise noted, if you download a dataset for your assignment, please do **not** submit the datasets. (If the dataset in bundled with the assignment, then it's of course fine to leave it there.)

### Report format

Your final report must be submitted online as a Jupyter notebook, so please do not write up your answers on paper! 

Be sure that your answers are clearly written and easy for the TA to understand. The TAs have the option to reduce your mark if your answers aren't clear or are difficult to understand (even if they are correct). 

Please do not delete the question cells or move the questions around. This will make things easier for the TAs.

**You must ensure that all your code output (values, tables, figures, etc.) is displayed in the notebook.** For example, if you are required to calculate some value, it is not sufficient to just store the value to a variable, nor is it sufficient to have a `print(value)` in your code - the print code must actually be run and the notebook saved, so that the output is shown on the screen when the notebook is rendered. Likewise, if there are tests (e.g. `assert` statements) provided in the code, make sure these are left in so we can see the output of the tests. This allows the TAs to see your results without running your code. Failure to display all output will result in a deduction of marks.

**If you are unsure whether your report is rendering properly, please view your submission in Gradescope. This is exactly how your TA will see it.**

### Figures

In most assignments, you will be asked to produce plots/figures. When including figures in your submission:

- Embed the figures in your report. Make sure your `.ipynb` file includes all the figures you want the TAs to see.
- All figures must include axis labels and, if multiple curves are present on the same figure, a legend.
- All figures must have some accompanying text explaining what the figure is about. You can do this by putting a figure title in the image itself (such as, "Training error vs. k") or you can use LaTeX to add figure captions that appear underneath the figure.
- Regardless of your image formats, all text must be big enough to read without straining or zooming. Please be careful about this for axis labels, legends, titles, etc. Avoid tiny text!

## Partners
**You must work alone for hw1 and hw2.** For hw3 onwards, I might consider allowing group submissions. (I'll update the instructions soon.) 

## Late submissions
By default late submissions will not be accepted. The rationale is that we will be posting the solutions shortly after the assignment deadline, and we cannot accept submissions after the solutions are posted. I do not like this, but I believe the overall policy is best for the class as a whole.

_In exceptional circumstances_ a late submission may be accepted with an academic concession - see [here](https://github.com/UBC-CS/cpsc330/blob/master/docs/course_info.md#academic-concessions) for more info.

## Updates to assignments

If there are errors or other changes that need to be made to an assignment, I will announce them in a pinned Piazza post.

## Citing sources
If you use information from students outside your group or from online sources _including code snippets from Stack Overflow_ or lecture notes, cite this at the start of each question. **You will receive a mark of 0 for the assignment (and possibly other consequences) if you are found copying from other sources without citation**.

