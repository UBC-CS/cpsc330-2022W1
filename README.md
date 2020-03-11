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

## TENTATIVE lecture schedule

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
| 8 | Jan 30 | [Evaluation metrics for binary classification, hyperparameter optimization](lectures/08_metrics-binary-class.ipynb) | Optional watching: [video: precision and recall](https://youtu.be/3SD6fgNGZSo?t=214) (until 8:29), [video: ensembles](https://youtu.be/3SD6fgNGZSo?t=1386) (until 37:48), then continuing the same video until 46:33 for random forests; [Classification vs. Prediction](https://www.fharrell.com/post/classification/) | more depth
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
| 16 | Mar 10 | [Time series data](lectures/16_time-series-data.ipynb) | | new 

Topics that will hopefully fit in somewhere:

- Outliers: detection, X vs. y, implications for preprocessing (0.5-1 class)
- Feature engineering(?) for time series/other data, multi-class classification, combining multiple tables (0-1 class)
- Time series data (1 class)
- Survival analysis (1 class)
- Unsupervised learning: clustering, network data (1-2 classes)
- Open source software, licenses, technical debt (0-1 classes)
- Deploying a trained model (0-1 classes)
- Communicating your results in writing/viz (1-2 classes)
- Fairness and ethics (0-1 classes) - can someone find a guest lecturer?
- LightGBM and other models / model comparison (0-1 classes)

The rest of the table:

| # | Date | Topic | Related readings and links | vs. CPSC 340 |
|---|--------|--------|---------------------------|--------------------|
| 17 | Mar 12 | ? | | new
| 18 | Mar 17 | ? | | new
| 19 | Mar 19 | ? | | new
| 20 | Mar 24 | ? | | new
| 21 | Mar 26 | ? | | new 
| 22 | Mar 31 | ? | |  new
| 23 | Apr 2 | ? | | new
| 24 | Apr 7 | Review/conclusion | | n/a


## TENTATIVE homework schedule

Homework is due every Saturday at 6pm unless otherwise noted. 

|  #  | Deadline |
|-----|------|
| hw1 | Saturday, Jan 11 at 6pm |
| hw2 | Saturday, Jan 18 at 6pm |
| hw3 | Sunday, Jan 26 at 6pm |
| hw4 | Sunday, Feb 9 at 6pm |
| hw5 | ~~Thursday, Feb 27~~ Friday, Feb 28 at 6pm |
| hw6 | Sunday, Mar 15 at 6pm |
| hw7 | TBD |
| hw8 | TBD |
| hw9 | TBD |
