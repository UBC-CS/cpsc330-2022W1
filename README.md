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

**Update**: the videos are now available as a YouTube playlist [here](https://www.youtube.com/playlist?list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC).

| #  | Date  | Topic | Recording |  Related readings and links | vs. CPSC 340 |
|--- |-------|--------|----------|-------------------------|--------------------|
|   |  Sep 8 | _UBC Imagine Day - no class_ | | |
| 1 | Sep 10 | [Course intro](lectures/01_intro.ipynb) | [recording](https://www.youtube.com/watch?v=N3LrOoPwYnU&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=1) ||   n/a
|   |        |      Dataset of the week: [which CPSC 330 students like cilantro?](https://github.com/UBC-CS/cpsc330/blob/master/lectures/data/330-students-cilantro.csv) |  | |
| 2 | Sep 15 | [Decision trees](lectures/02_decision-trees.ipynb) | [recording](https://www.youtube.com/watch?v=kSSvoT-D5kA&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=2) | | less depth |
| 3 | Sep 17 | [The fundamental tradeoff of ML](lectures/03_fundamental-tradeoff.ipynb) | [recording](https://www.youtube.com/watch?v=arrhrBjOPhY&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=3) | [About Train, Validation and Test sets](https://towardsdatascience.com/train-validation-and-test-sets-72cb40cba9e7) | similar |
|   |         |   Dataset of the week: [sentiment analysis of movie reviews](https://www.kaggle.com/utathya/imdb-review-dataset) | | |
| 4 | Sep 22 | [Logistic regression, word counts, `predict_proba`](lectures/04_logreg-countvec-proba.ipynb) | [recording](https://www.youtube.com/watch?v=7-n1RgiybsE&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=4) | [Meaningless comparisons lead to false optimism in medical machine learning](https://arxiv.org/pdf/1707.06289.pdf) | less depth |
| 5 | Sep 24 | [Pipelines & hyperparameter optimization](lectures/05_hyperopt-pipelines.ipynb) | [recording](https://www.youtube.com/watch?v=5_bnR4ageu4&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=5) and [supplemental recording](https://www.youtube.com/watch?v=fkGCN0ysDos&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=6) | | more depth | 
|    |        |    Dataset of the week: [Predicting income from census data](https://www.kaggle.com/uciml/adult-census-income) | | | |
|6 | Sep 29 | [Overfitting the validation set & encoding categorical variables](lectures/06_overfitting-validation-and-categoricals.ipynb)  | [recording](https://www.youtube.com/watch?v=1cFiS8i3dBI&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=7) | | more depth |
| 7 |  Oct 1 | [Imputation, scaling numeric features, `ColumnTransformer`](lectures/07_missingness-scaling.ipynb) | [recording](https://www.youtube.com/watch?v=oXBZ37UZ7ig&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=8) |  | more depth
|    |        |       Dataset of the week: [detecting credit card fraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)  | | |
| 8 | Oct 6 | [Evaluation metrics for classification](lectures/08_classification-metrics.ipynb) | [recording](https://www.youtube.com/watch?v=V9ef1-7vVOM&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=9) | [Damage Caused by Classification Accuracy and Other Discontinuous Improper Accuracy Scoring Rules](https://www.fharrell.com/post/class-damage/), [Classification vs. Prediction](https://www.fharrell.com/post/classification/) | more depth
| 9 | Oct 8 | [Ensembles](lectures/09_ensembles.ipynb) | [recording](https://www.youtube.com/watch?v=v3D7pzT7eW0&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=10) | | similar |
|    |        |         | Dataset of the week: [predicting housing prices](https://www.kaggle.com/c/home-data-for-ml-course/) |
| 10 | Oct 13 | [Linear regression, regression metrics](lectures/10_regression-metrics.ipynb) | [recording](https://www.youtube.com/watch?v=GIsnHm8afdE&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=11) |  | more depth on metrics, less on linear regression
| 11 | Oct 15 | [Prediction intervals, feature importances](lectures/11_feature-importances.ipynb) | [recording](https://www.youtube.com/watch?v=eimV_DQ7RTc&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=12) | | new
| 12 | Oct 20 | [Feature selection, midterm review](lectures/12_feature-selection-and-review.ipynb) | [recording](https://www.youtube.com/watch?v=pZldySwtNSk&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=13) | [Feature selection article](https://towardsdatascience.com/featuion-techniques-in-machine-learning-with-python-f24e7da3f36e) | less depth
|    | Oct 22 | MIDTERM | [study materials](https://www.youtube.com/watch?v=dQw4w9WgXcQ) | |
| 13 | Oct 27 | [Neural networks & computer vision](lectures/13_computer-vision.ipynb) | [recording](https://www.youtube.com/watch?v=x3hbyrrTrVE&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=14) | [But what _is_ a Neural Network?](https://www.youtube.com/wrcAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | less depth
| 14 | Oct 29 | [Distances and neighbours](lectures/14_distances-neighbours.ipynb) | [recording](https://www.youtube.com/watch?v=M-dW7XkRtkk&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=15) | | less depth
| 15 | Nov 3 | [Text data](lectures/15_nlp.ipynb) | [recording](https://www.youtube.com/watch?v=Po_nELT3ctc&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=16) - note: unfortunately the first 9 min of the recording was corrupted | |  new
| 16 | Nov 5 | [Outliers](lectures/16_outliers.ipynb) | [recording](https://www.youtube.com/watch?v=eIbwca3V2VY&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=17) | | different
| 17 | Nov 10 | [Time series data](lectures/17_time-series.ipynb) | [recording](https://www.youtube.com/watch?v=mJVI-rF7chc&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=18) | Humour: [The Problem with Time & Timezones](https://www.youtube.com/watch?v=-5wpm-gesOY) | new 
| 18 | Nov 12 | [Survival analysis](lectures/18_survival-analysis.ipynb) | [recording](https://www.youtube.com/watch?v=9EnlN-yFtIg&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=19) | [Calling Bullshit video 4.1](https://www.youtube.com/watch?v=ITWQ5psx9Sw&list=D1Sje5jWxt-4CSZD7bUI4gSPS&index=19&t=0s), [Medium article](https://towardsdatascience.com/survisis-intuition-implementation-in-python-504fde4fcf8e) (contains some math) | new
| 19 | Nov 17 | [Clustering](lectures/19_clustering.ipynb) | [recording](https://www.youtube.com/watch?v=2Qd6Eo3O8aM&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=20) | | less depth
| 20 | Nov 19 | [Communicating your results](lectures/20_communication.ipynb) | [recording](https://www.youtube.com/watch?v=ix119FI1QT0&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=21) | [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 1 (5 short videos, 37 min total); [Communication in Data Science](https://ubc-mds.github.io/2017-I-542-communication/) blog post |  new
|    |  Nov 19 | [Bonus material: SGD for big datasets](lectures/bonus_sgd.ipynb) | [recording](https://www.youtube.com/watch?v=nnzltuniT_E&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=24) | | less depth
| 21 | Nov 24 | [Communicating your results, continued](lectures/21_communication-continued.ipynb) | [recording](https://www.youtube.com/watch?v=sOO29czleXY&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=22) | [Calling BS videos](https://www.youtube.com/playlist?list=D1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 6 (6 short videos, 47 min total); [Can you read graphs? Because I can't.](https://www.youtube.com/watch?v=vbDObzI-CTc) by Sabrina (7 min) | new
| 22 | Nov 26 | [Ethics](lectures/22_ethics.ipynb) | [recording](https://www.youtube.com/watch?v=fspH_AGVZpw&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=23) | [Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 5 (6 short videos, 50 min total); Humour: [Game of Thrones deepfake video](https://www.youtube.com/watch?v=4GdWD0yxvqw) | new
|    | Nov 26 | [Bonus material: combining multiple tables](lectures/bonus_multiple_tables.ipynb)  | [recording](https://www.youtube.com/watch?v=E1UCnT-vfZ8&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=25) | | new 
| 23 | Dec 1| [Ethics continued](lectures/23_guest-lecture.md): guest lecture by [Sina Fazelpour](https://sinafazelpour.com/)  | recording is available on Canvas only | | new 
| 24 | Dec 3 | [Model deployment; Conclusion](lectures/24_deployment-conclusion.ipynb) | [recording](https://www.youtube.com/watch?v=km-5DWAITPg&list=PLWmXHcz_53Q2BXsWviGgEqdlSHmfsjSzC&index=24) |  | new | 

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
