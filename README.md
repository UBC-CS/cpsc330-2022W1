# CPSC 330: Applied Machine Learning

In this repository you will find the course materials from the inaugural offering for CPSC 330: Applied Machine Learning at the University of British Columbia, which took place Jan-Apr 2020. I learned many lessons during the first run, so these materials definitely represent a work in progress. 

Instructor: [Mike Gelbart](https://www.mikegelbart.com/)

Thank you to [Tomas Beuzen](https://tomasbeuzen.github.io/) and [Varada Kolhatkar](https://kvarada.github.io/) for significant contributions to the course materials.


## Lecture schedule

| # | Date | Topic | Related readings and links | vs. CPSC 340 |
|---|--------|--------|---------------------------|--------------------|
| 1 | [Course intro, Python](lectures/01_syllabus-and-python.ipynb) | Python [videos](https://www.youtube.com/playlist?list=53Q26aQzhknaT3zwWvl7w8wQE) and [notebooks](https://github.com/UBC-MDS/DSCI_511_prog-dsci) |   n/a
| 2 | [More Python: numpy and pandas](lectures/02_numpy-pandas.ipynb) | [Numpy quickstart tutorial](https://docs.scipy.org/doc/numpy/user/quickl), [Learn python3 in Y minutes](https://learnxinyminutes.com/docs/python3/) |  new
| 3 | [Decision trees](lectures/03_decision-trees.ipynb) | **Assumed preparation**: [Decision tree video](https://youtu.be/WYDPYIe3RpQ?t=230) untilnd then continue from 36:35 onwards. | less math
| 4 | [Fundamentals of learning](lectures/04_fundamentals-of-learning.ipynb) | **Assumed preparation**: <ul><li>[Fundamentals of learning video](http.be/dPm-KTrJlFU?t=183) (47 min) <li>[part of the KNN video](https://youtu.be/JRF6oELLn0M?t=1248) **up to 29:00** on cross-validation (8 min)</ul>r
| 5 | [Logistic regression, feature extraction](lectures/05_countvec-and-logreg.ipynb) | no video | less depth on log reg, more on features
| 6 | [Feature preprocessing, SVMs, random forests](lectures/06_feature-preprocessing.ipynb) | no video  | more depth on features, less on SVM/RF
| 7 | [Model comparisons, EDA, missing data, baselines](lectures/07_census-data.ipynb) | [Meaningless comparisons lead to false optimism in medice learning](https://arxiv.org/pdf/1707.06289.pdf), [Damage Caused by Classification Accuracy and Other Discontinuous Improper Accuracy Scori(https://www.fharrell.com/post/class-damage/) | more depth
| 8 | [Evaluation metrics for binary classification, hyperparameter optimization](lectures/08_classification-metrics-hyperopt.ipynb) | Optional watcheo: precision and recall](https://youtu.be/3SD6fgNGZSo?t=214) (until 8:29), [video: ensembles](https://youtu.be/3SD6fgNGZSo?t=1386) (until 37:48ontinuing the same video until 46:33 for random forests; [Classification vs. Prediction](https://www.fharrell.com/post/classification/) | more  |[Regression](lectures/09_regression-housing-data.ipynb) | |  more depth on error metrics
| 10 | [Linear regression, feature importances](lectures/10_feature-importances.ipynb)  |  | more depth on feature importances, less on linear regresion
| 11 | [Ensembles, midterm review](lectures/11_ensembles-review.ipynb) |  | n/a
| 12 | [Pipelines, feature selection](lectures/12_feature-selection-pipelines.ipynb) | [Feature selection article](https://towardsdatascience.com/featuion-techniques-in-machine-learning-with-python-f24e7da3f36e) | pipelines are new, less depth on feature selection
| 13 | [Natural language processing](lectures/13_natural-language-processing.ipynb) |  |  new
| 14 | [Neural networks & computer vision](lectures/14_neural-nets-computer-vision.ipynb) | [But what _is_ a Neural Network?](https://www.youtube.com/wrcAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | less depth
| 15 | [Nearest neighbours, product similarity](lectures/15_nearest-neighbours.ipynb) | | less depth
| 16 | [Time series data](lectures/16_time-series-data.ipynb) | Humour: [The Problem with Time & Timezones](https://www.youtube.com/watch?v=-5w) | new 
| 17 | [Survival analysis](lectures/17_survival-analysis.ipynb) | [Calling Bullshit video 4.1](https://www.youtube.com/watch?v=ITWQ5psx9Sw&list=D1Sje5jWxt-4CSZD7bUI4gSPS&index=19&t=0s), [Medium article](https://towardsdatascience.com/survisis-intuition-implementation-in-python-504fde4fcf8e) (contains some math) | new
| 18 | [Clustering](lectures/18_clustering.ipynb) | | less depth
| 19 | [Outliers](lectures/19_outliers.ipynb) |  | different angle
| 20 | [Miscellaneous leftovers](lectures/20_miscellaneous-leftovers.ipynb) |  | new 
| 21 | [Communicating your results](lectures/21_communication.ipynb) |  [Communication in Data Science](https://ubc-mds.github.io/2017-I-542-communication/) blog post; [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 1 (5 video total) |  new
| 22 | [Communicating your results, continued](lectures/22_communication-continued.ipynb) | [Calling BS videos](https://www.youtube.com/playlist?list=D1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 6 (6 short videos, 47 min total) | new
| 23 | [Ethics, course conclusion](lectures/23_ethics-conclusion.ipynb) |  [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 5 (6 short videos, 50 min total) | new

## Homework

See [here](https://github.com/UBC-CS/cpsc330/tree/master/hw).

## Exams

See [here](https://github.com/UBC-CS/cpsc330/tree/master/exams).