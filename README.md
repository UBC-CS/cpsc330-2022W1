# UBC CPSC 330: Applied Machine Learning (2020W1)

This is the course homepage for CPSC 330: Applied Machine Learning at the University of British Columbia. You are looking at the current version (Sep-Dec 2020). An earlier version from Jan-Apr 2020 can be found [here](https://github.com/UBC-CS/cpsc330/tree/1.0).

Instructor: [Mike Gelbart](https://www.mikegelbart.com/)


## Important links

* [syllabus / administrative info](docs/course_info.md)
* [other course documents](docs)
* [past exams](exams/)
* [Piazza](https://piazza.com/class/kb2e6nwu3uj23)
* [class + office hours calendar](https://htmlpreview.github.io/?https://github.com/UBC-CS/cpsc330/blob/master/docs/calendar.html)
* [Zoom links on Canvas](https://canvas.ubc.ca/courses/53561/external_tools/15408)

## Lecture schedule

The lectures will be on Zoom. They can be joined through Canvas [here](https://canvas.ubc.ca/courses/53561/external_tools/15408). If you would like to join the lectures but cannot login to Canvas (presumably because you're not enrolled in the course) please email Mike and I will give you the link.

| #  | Date  | Topic | Related readings and links | vs. CPSC 340 |
|--- |-------|--------|---------------------------|--------------------|
|   |  Sep 8 | _UBC Imagine Day - no class_ | |
| 1 | Sep 10 | [Course intro](lectures/01_intro.ipynb) ||   n/a
| 2 | Sep 15 | [Decision trees](lectures/02_decision-trees.ipynb) |[Decision tree video](https://youtu.be/WYDPYIe3RpQ?t=230) until 26:30, and then continue from 36:35 onwards. | less math
| 3 | Sep 17 | [The fundamental tradeoff of ML](lectures/03_fundamental-tradeoff.ipynb) (and the Golden Rule) | [Fundamentals of learning video](http.be/dPm-KTrJlFU?t=183) (47 min), [part of the KNN video](https://youtu.be/JRF6oELLn0M?t=1248) **up to 29:00** on cross-validation (8 min) |
| 4 | Sep 22 | [k-nearest neighbours, transforming numeric features](lectures/04_knn-scaling.ipynb) (and the Golden Rule) | | 
| 5 | Sep 24 | [Encoding categorical variables](lectures/05_categorical-variables.ipynb) (and the Golden Rule) | | 
| 6 | Sep 29 | [Hyperparameter optimization, pipelines](lectures/06_hyperopt-pipelines.ipynb) (and the Golden Rule) | |

Needs to go somewhere:

|  | | [Our first end-to-end analysis](lectures/07_end-to-end.ipynb) | [Meaningless comparisons lead to false optimism in medical machine learning](https://arxiv.org/pdf/1707.06289.pdf), [Damage Caused by Classification Accuracy and Other Discontinuous Improper Accuracy Scoring Rules](https://www.fharrell.com/post/class-damage/) | 

| #  | Date  | Topic | Related readings and links | vs. CPSC 340 |
|--- |-------|--------|---------------------------|--------------------|
| 7 |  Oct 1 | [Logistic regression (binary and multi-class), `CountVectorizer`, `predict_proba`](lectures/08_logreg-countvec-proba.ipynb) | no video | less depth on log reg, more on features
| 8 | Oct 6 | [Evaluation metrics for classification](lectures/09_classification-metrics.ipynb) | Optional watching: [video: precision and recall](https://youtu.be/3SD6fgNGZSo?t=214) (until 8:29), [video: ensembles](https://youtu.be/3SD6fgNGZSo?t=1386) (until 37:48), then continuing the same video until 46:33 for random forests; [Classification vs. Prediction](https://www.fharrell.com/post/classification/) | more depth
| 9 | Oct 8 | [Linear regression, feature importances](lectures/10_feature-importances.ipynb)  |  | more depth on feature importances, less on linear regression
| 10 | Oct 13 | [Evaluation metrics for regression](lectures/11_regression-metrics.ipynb) | |  more depth on error metrics
| 11 | Oct 15 | [Ensembles](lectures/12_ensembles.ipynb) |  | n/a
|    | Oct 20 | MIDTERM | |
| 12 | Oct 22 | [Feature engineering, feature selection](lectures/13_feature-engineering-selection.ipynb) | [Feature selection article](https://towardsdatascience.com/featuion-techniques-in-machine-learning-with-python-f24e7da3f36e) | feature engineering is new, less depth on feature selection
| 13 | Oct 27 | [Natural language processing](lectures/14_natural-language-processing.ipynb) |  |  new
| 14 | Oct 29 | [Neural networks & computer vision](lectures/15_computer-vision.ipynb) | [But what _is_ a Neural Network?](https://www.youtube.com/wrcAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | less depth
| 15 | Nov 3 | [Nearest neighbours for product similarity](lectures/16_similar-items.ipynb) | | less depth
| 16 | Nov 5 | [Time series data](lectures/17_time-series.ipynb) | Humour: [The Problem with Time & Timezones](https://www.youtube.com/watch?v=-5wpm-gesOY) | new 
| 17 | Nov 10 | [Survival analysis](lectures/18_survival-analysis.ipynb) | [Calling Bullshit video 4.1](https://www.youtube.com/watch?v=ITWQ5psx9Sw&list=D1Sje5jWxt-4CSZD7bUI4gSPS&index=19&t=0s), [Medium article](https://towardsdatascience.com/survisis-intuition-implementation-in-python-504fde4fcf8e) (contains some math) | new
| 18 | Nov 12 | [Clustering](lectures/19_clustering.ipynb) | | less depth
| 19 | Nov 17 | [Outliers](lectures/20_outliers.ipynb) |  | different angle
| 20 | Nov 19 | Model deployment (or move to Dec 1) | | new 
| 21 | Nov 24 | [Communicating your results](lectures/22_communication.ipynb) |  [Communication in Data Science](https://ubc-mds.github.io/2017-I-542-communication/) blog post; [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 1 (5 video total) |  new
| 22 | Nov 26 | [Communicating your results, continued](lectures/23_communication-continued.ipynb) | [Calling BS videos](https://www.youtube.com/playlist?list=D1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 6 (6 short videos, 47 min total) | new
| 23 | Dec 1 | [Ethics](lectures/24_ethics.ipynb) | [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 5 (6 short videos, 50 min total) | new
| 24 | Dec 3 | [Leftovers; Conclusion](https://github.com/UBC-CS/cpsc330/blob/master/lectures/25_leftovers-conclusion.ipynb) |   | 

## Homework schedule

| #  | Due Date  | Topic | Associated lectures | 
|--- |-----------|-------|---------------------|
| 1  | Mon Sep 14 | numpy/pandas |   n/a      |
| 2  | Mon Sep 21 | TBD |   2, 3, 4      |


## Attribution

Thank you to [Tomas Beuzen](https://tomasbeuzen.github.io/) and [Varada Kolhatkar](https://kvarada.github.io/) for significant contributions to the course materials.

## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
