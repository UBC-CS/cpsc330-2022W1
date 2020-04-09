# CPSC 330: Applied Machine Learning (2019W2)

## Important documents

* [administrative info](docs/course_info.md)
* [CPSC 330 vs. CPSC 340](docs/330_vs_340.md)
* [homework submission instructions](docs/homework_instructions.md)
* [textbooks and online resources](docs/resources.md)
* [grading policies](docs/grades.md)
* [git info](docs/git_installation.md)
* [Python info](docs/python_info.md)
* [how to ask for help](docs/asking_for_help.md)

## External links

* [Piazza](https://piazza.com/class/k1gx4b3djbv3ph)
* [office hours calendar](http://www.cs.ubc.ca/~mgelbart/calendar.html)
* [other relevant content](https://www.youtube.com/watch?v=dQw4w9WgXcQ); [what just happened?](https://en.wikipedia.org/wiki/Rickrolling)

## Lecture schedule

Note: links to YouTube videos may have start times embedded in them. You may want to watch them at 1.25x. You can skip the videos if you have already taken CPSC 340.

| # | Date | Topic | Related readings and links | vs. CPSC 340 |
|---|--------|--------|---------------------------|--------------------|
| 1 | Jan 7 | [Course intro, Python](lectures/01_syllabus-and-python.ipynb) | Python [videos](https://www.youtube.com/playlist?list=PLWmXHcz_53Q26aQzhknaT3zwWvl7w8wQE) and [notebooks](https://github.com/UBC-MDS/DSCI_511_prog-dsci) |   n/a
| 2 | Jan 9 | [More Python: numpy and pandas](lectures/02_numpy-pandas.ipynb) | [Numpy quickstart tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html), [Learn python3 in Y minutes](https://learnxinyminutes.com/docs/python3/) |  new
| 3 | Jan 14 | [Decision trees](lectures/03_decision-trees.ipynb) | **Assumed preparation**: [Decision tree video](https://youtu.be/WYDPYIe3RpQ?t=230) until 26:30, and then continue from 36:35 onwards. | less math
| 4 | Jan 16 | [Fundamentals of learning](lectures/04_fundamentals-of-learning.ipynb) | **Assumed preparation**: <ul><li>[Fundamentals of learning video](https://youtu.be/dPm-KTrJlFU?t=183) (47 min) <li>[part of the KNN video](https://youtu.be/JRF6oELLn0M?t=1248) **up to 29:00** on cross-validation (8 min)</ul> | similar
| 5 | Jan 21 | [Logistic regression, feature extraction](lectures/05_countvec-and-logreg.ipynb) | no video | less depth on log reg, more on features
| 6 | Jan 23 | [Feature preprocessing, SVMs, random forests](lectures/06_feature-preprocessing.ipynb) | no video  | more depth on features, less on SVM/RF
| 7 | Jan 28 | [Model comparisons, EDA, missing data, baselines](lectures/07_census-data.ipynb) | [Meaningless comparisons lead to false optimism in medical machine learning](https://arxiv.org/pdf/1707.06289.pdf), [Damage Caused by Classification Accuracy and Other Discontinuous Improper Accuracy Scoring Rules](https://www.fharrell.com/post/class-damage/) | more depth
| 8 | Jan 30 | [Evaluation metrics for binary classification, hyperparameter optimization](lectures/08_classification-metrics-hyperopt.ipynb) | Optional watching: [video: precision and recall](https://youtu.be/3SD6fgNGZSo?t=214) (until 8:29), [video: ensembles](https://youtu.be/3SD6fgNGZSo?t=1386) (until 37:48), then continuing the same video until 46:33 for random forests; [Classification vs. Prediction](https://www.fharrell.com/post/classification/) | more depth
| 9 | Feb 4 | [Regression](lectures/09_regression-housing-data.ipynb) | |  more depth on error metrics
| 10 | Feb 6 | [Linear regression, feature importances](lectures/10_feature-importances.ipynb)  |  | more depth on feature importances, less on linear regression
| 11 | Feb 11 | [Ensembles, midterm review](lectures/11_ensembles-review.ipynb) |  | n/a
|    | Feb 13 | MIDTERM | |  n/a
|    | Feb 18 | NO CLASS ||
|    | Feb 20 | NO CLASS | |
| 12 | Feb 25 | [Pipelines, feature selection](lectures/12_feature-selection-pipelines.ipynb) | [Feature selection article](https://towardsdatascience.com/feature-selection-techniques-in-machine-learning-with-python-f24e7da3f36e) | pipelines are new, less depth on feature selection
| 13 | Feb 27 | [Natural language processing](lectures/13_natural-language-processing.ipynb) |  |  new
| 14 | Mar 3 | [Neural networks & computer vision](lectures/14_neural-nets-computer-vision.ipynb) | [But what _is_ a Neural Network?](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | less depth
| 15 | Mar 5 | [Nearest neighbours, product similarity](lectures/15_nearest-neighbours.ipynb) | | less depth
| 16 | Mar 10 | [Time series data](lectures/16_time-series-data.ipynb) | Humour: [The Problem with Time & Timezones](https://www.youtube.com/watch?v=-5wpm-gesOY) | new 
| 17 | Mar 12 | [Survival analysis](lectures/17_survival-analysis.ipynb) | [Calling Bullshit video 4.1](https://www.youtube.com/watch?v=ITWQ5psx9Sw&list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS&index=19&t=0s), [Medium article](https://towardsdatascience.com/survival-analysis-intuition-implementation-in-python-504fde4fcf8e) (contains some math) | new
| 18 | Mar 17 | [Clustering](lectures/18_clustering.ipynb) | lecture recording [here](https://ca.bbcollab.com/collab/ui/session/playback/load/2236b6e36c9b4d2e8da9e3c7503e63b3) | less depth
|    | Mar 19 | _class cancelled_ | | 
| 19 | Mar 24 | [Outliers](lectures/19_outliers.ipynb) | lecture recording [here](https://ca-lti.bbcollab.com/recording/8ea3c694cafd4ea4976421d712e5c5c7) | different angle
| 20 | Mar 26 | [Miscellaneous leftovers](lectures/20_miscellaneous-leftovers.ipynb) | lecture recording [here](https://ca-lti.bbcollab.com/recording/60589c9dd4754a26a9afff38a9cf005a) | new 
| 21 | Mar 31 | [Communicating your results](lectures/21_communication.ipynb) | lecture recording [here](https://ca-lti.bbcollab.com/recording/108b7c5aa8894f0eb4a6f800c0fc3477); [Communication in Data Science](https://ubc-mds.github.io/2017-11-10-DSCI-542-communication/) blog post; [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 1 (5 videos, 37 min total) |  new
| 22 | Apr 2 | [Communicating your results, continued](lectures/22_communication-continued.ipynb) | lecture recording [here](https://ca-lti.bbcollab.com/recording/2ef8102498bf4ecfa8a6a0568e6e68d8); [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 6 (6 short videos, 47 min total) | new
| 23 | Apr 7 | [Ethics, course conclusion](lectures/23_ethics-conclusion.ipynb) | lecture recording [here](https://ca-lti.bbcollab.com/recording/cd03aa5e3fef48518ddfd44103ac172f); [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 5 (6 short videos, 50 min total) | new

## Homework schedule

|  #  | Deadline |
|-----|------|
| hw1 | Saturday, Jan 11 at 6pm |
| hw2 | Saturday, Jan 18 at 6pm |
| hw3 | Sunday, Jan 26 at 6pm |
| hw4 | Sunday, Feb 9 at 6pm |
| hw5 | ~~Thursday, Feb 27~~ Friday, Feb 28 at 6pm |
| hw6 | Sunday, Mar 15 at 6pm |
| hw7 | Sunday, Mar 29 at 6pm |
| hw8 | Thursday, April 9 at 6pm, with [possible 24 hr extension](https://piazza.com/class/k1gx4b3djbv3ph?cid=367) |

