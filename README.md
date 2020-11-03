# UBC CPSC 330: Applied Machine Learning (2020W1)

This is the course homepage for CPSC 330: Applied Machine Learning at the University of British Columbia. You are looking at the current version (Sep-Dec 2020). An earlier version from Jan-Apr 2020 can be found [here](https://github.com/UBC-CS/cpsc330/tree/1.0).

Instructor: [Mike Gelbart](https://www.mikegelbart.com/)


## Important links

* [syllabus / administrative info](docs/course_info.md)
* [other course documents](docs)
* [past exams](exams/)
* [Piazza](https://piazza.com/class/kb2e6nwu3uj23) (this is where all announcements will be made)
* [class + office hours calendar](https://htmlpreview.github.io/?https://github.com/UBC-CS/cpsc330/blob/master/docs/calendar.html)
* [Zoom links on Canvas](https://canvas.ubc.ca/courses/53561/external_tools/15408)

## Lecture schedule

**Live lectures**: The lectures will be on Zoom. They can be joined through Canvas [here](https://canvas.ubc.ca/courses/53561/external_tools/15408). If you would like to join the lectures but cannot login to Canvas (presumably because you're not enrolled in the course) please email Mike and I will give you the link.

**Lecture recordings**: The lecture recordings can be accessed through the same Zoom page on Canvas [here](https://canvas.ubc.ca/courses/53561/external_tools/15408). From this page, navigate to the "Cloud Recordings" tab and you should see them there. The same lecture recordings will be posted here embedded in the schedule below.

| #  | Date  | Topic | Recording |  Related readings and links | vs. CPSC 340 |
|--- |-------|--------|----------|-------------------------|--------------------|
|   |  Sep 8 | _UBC Imagine Day - no class_ | | |
| 1 | Sep 10 | [Course intro](lectures/01_intro.ipynb) | [recording](https://www.dropbox.com/s/3rol8k4ztd61zzq/CPSC-330_Lecture-1_2020-09-10.mp4?dl=0) ||   n/a
|   |        |      Dataset of the week: [which CPSC 330 students like cilantro?](https://github.com/UBC-CS/cpsc330/blob/master/lectures/data/330-students-cilantro.csv) |  | |
| 2 | Sep 15 | [Decision trees](lectures/02_decision-trees.ipynb) | [recording](https://ubc.zoom.us/rec/share/ieAgJaUW_SoOA6D9gU3zKjeeh4qpUFb2U1K2W30woNe9-mpHvRk2tZuGUL_PqA19._rj95En4-zj3UNc4) pw `!?3niNc^` | | less depth |
| 3 | Sep 17 | [The fundamental tradeoff of ML](lectures/03_fundamental-tradeoff.ipynb) | [recording](https://ubc.zoom.us/rec/share/IfGQAGNokar3X9_ERd26bV6-ZqzU4S3lK7gwtkCUxLW5fksAbh119vx1-TDqqhES.MtCzr-zV6lrPuvsc) pw `90p@qbt4` | [About Train, Validation and Test sets](https://towardsdatascience.com/train-validation-and-test-sets-72cb40cba9e7) | similar |
|   |         |   Dataset of the week: [sentiment analysis of movie reviews](https://www.kaggle.com/utathya/imdb-review-dataset) | | |
| 4 | Sep 22 | [Logistic regression, word counts, `predict_proba`](lectures/04_logreg-countvec-proba.ipynb) | [recording](https://ubc.zoom.us/rec/share/xTVTgILLD2ATXf4WJ4bEgjaVwe2f2q8_3YWzAD58oCvEfaoHzwqAeIkvARPThhPE.saNAIFN0VYwjaCYm) pw `ZsJZ#e29` | [Meaningless comparisons lead to false optimism in medical machine learning](https://arxiv.org/pdf/1707.06289.pdf) | less depth |
| 5 | Sep 24 | [Pipelines & hyperparameter optimization](lectures/05_hyperopt-pipelines.ipynb) | [recording](https://ubc.zoom.us/rec/share/ftSb66tJ7mE7elR8ifjTt7-7zJEb154u0wFZNKbEMCsiscIRYJfwWGt5fOLEzm_U.BmhjY_xrAbV1Po4g) pw `pT2QVE*#` and [supplemental screencast](https://www.dropbox.com/s/i9tt6bmxju3ioj3/BayesOpt.mp4?dl=0) | | more depth | 
|    |        |    Dataset of the week: [Predicting income from census data](https://www.kaggle.com/uciml/adult-census-income) | | | |
|6 | Sep 29 | [Overfitting the validation set & encoding categorical variables](lectures/06_overfitting-validation-and-categoricals.ipynb)  | [recording](https://ubc.zoom.us/rec/share/a48aAcfYHU2Cdt3E2ZN6HrGhQXxg0oSF7ux89a5YMb5Yl_2iiWSfc4mVWlp2reZf.LBVsW07isCcBWqbI) pw `3J10UiO.` | | more depth |
| 7 |  Oct 1 | [Imputation, scaling numeric features, `ColumnTransformer`](lectures/07_missingness-scaling.ipynb) | [recording](https://ubc.zoom.us/rec/share/B0b9mHRa-CEqyVjfD8Jdh9taClf-gPiduRYcQMe9v9_V9-zewMn4B_MpbzXeOPEL.wrlH68yTcewU0zZC) pw `b.+DFR47`  |  | more depth
|    |        |       Dataset of the week: [detecting credit card fraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)  | | |
| 8 | Oct 6 | [Evaluation metrics for classification](lectures/08_classification-metrics.ipynb) | [recording](https://www.dropbox.com/s/yw0uq4mxrnb6x13/08_2020-10-06.mp4?dl=0) | [Damage Caused by Classification Accuracy and Other Discontinuous Improper Accuracy Scoring Rules](https://www.fharrell.com/post/class-damage/), [Classification vs. Prediction](https://www.fharrell.com/post/classification/) | more depth
| 9 | Oct 8 | [Ensembles](lectures/09_ensembles.ipynb) | [recording](https://www.dropbox.com/s/ewzghom1h5h9kwx/lec09_2020-10-08.mp4?dl=0) | | similar |
|    |        |         | Dataset of the week: [predicting housing prices](https://www.kaggle.com/c/home-data-for-ml-course/) |
| 10 | Oct 13 | [Linear regression, regression metrics](lectures/10_regression-metrics.ipynb) | [recording part 1](https://www.dropbox.com/s/jkydpcvr2dyf8uf/lecture10.mp4?dl=0), [recording part 2](https://www.dropbox.com/s/414dedx4f10cpl3/lecture10_part2.mp4?dl=0) |  | more depth on metrics, less on linear regression
| 11 | Oct 15 | [Prediction intervals, feature importances](lectures/11_feature-importances.ipynb) | [recording](https://www.dropbox.com/s/uzn8c5j966lv3v6/lecture11.mp4?dl=0) | | new
| 12 | Oct 20 | [Feature selection, midterm review](lectures/12_feature-selection-and-review.ipynb) | [screencast](https://www.dropbox.com/s/da7lx8kdzxfmna2/lecture12.mp4?dl=0) | [Feature selection article](https://towardsdatascience.com/featuion-techniques-in-machine-learning-with-python-f24e7da3f36e) | less depth
|    | Oct 22 | MIDTERM | [study materials](https://www.youtube.com/watch?v=dQw4w9WgXcQ) | |
| 13 | Oct 27 | [Neural networks & computer vision](lectures/13_computer-vision.ipynb) | [recording](https://www.dropbox.com/s/lyl9f6k8k2sqkkt/lecture13.mp4?dl=0) | [But what _is_ a Neural Network?](https://www.youtube.com/wrcAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | less depth
| 14 | Oct 29 | [Distances and neighbours](lectures/14_distances-neighbours.ipynb) | [recording](https://www.dropbox.com/s/62qgg4cnk0fbcqv/lecture14.mp4?dl=0) | | less depth
| 15 | Nov 3 | [Text data](lectures/15_nlp.ipynb) | | |  new

Below this point is the schedule for future lectures (not yet updated for 2020W1)

| #  | Date  | Topic | Recording |  Related readings and links | vs. CPSC 340 |
|--- |-------|--------|----------|-------------------------|--------------------|
| 16 | Nov 5 | [Time series data](lectures/16_time-series.ipynb) | | Humour: [The Problem with Time & Timezones](https://www.youtube.com/watch?v=-5wpm-gesOY) | new 
| 17 | Nov 10 | [Survival analysis](lectures/17_survival-analysis.ipynb) | | [Calling Bullshit video 4.1](https://www.youtube.com/watch?v=ITWQ5psx9Sw&list=D1Sje5jWxt-4CSZD7bUI4gSPS&index=19&t=0s), [Medium article](https://towardsdatascience.com/survisis-intuition-implementation-in-python-504fde4fcf8e) (contains some math) | new
| 18 | Nov 12 | [Clustering](lectures/18_clustering.ipynb) | | | less depth
| 19 | Nov 17 | [Outliers](lectures/19_outliers.ipynb) | | | different angle
| 20 | Nov 19 | [Communicating your results](lectures/21_communication.ipynb) | | [Communication in Data Science](https://ubc-mds.github.io/2017-I-542-communication/) blog post; [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 1 (5 video total) |  new
| 21 | Nov 24 | [Communicating your results, continued](lectures/22_communication-continued.ipynb) | | [Calling BS videos](https://www.youtube.com/playlist?list=D1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 6 (6 short videos, 47 min total) | new
| 22 | Nov 26 | [Ethics](lectures/23_ethics.ipynb) | | [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 5 (6 short videos, 50 min total) | new
| 23 | Dec 1| Model deployment  | | | new 
| 24 | Dec 3 | [Leftovers; Conclusion](lectures/24_leftovers-conclusion.ipynb) | |  | 

## Homework schedule

| #  | Due Date  | Associated lectures | 
|--- |-----------|---------------------|
| 1  | Tue Sep 15 11:59pm |    prerequisites      |
| 2  | Mon Sep 21 11:59pm |   2, 3      |
| 3  | Mon Sep 28 11:59pm |   4, 5      |
| 4  | Mon Oct 12 11:59pm |   6-9      |
| 5  | Mon Oct 19 11:59pm |   9-11      |
| 6  | Mon Nov 9 11:59pm |   12-15      |
| 7  | Mon Nov 16 11:59pm |   16-18      |
| 8  | Mon Nov 23 11:59pm |   whole course      |
| 9  | Mon Nov 30 11:59pm |   20-22    |


## Attribution

Thank you to [Tomas Beuzen](https://tomasbeuzen.github.io/) and [Varada Kolhatkar](https://kvarada.github.io/) for significant contributions to the course materials.

## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
