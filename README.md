# UBC CPSC 330: Applied Machine Learning (2021W1)

This is the course homepage for CPSC 330: Applied Machine Learning at the University of British Columbia. You are looking at the current version (Sep-Dec 2021). An earlier version from Sep-Dec 2020 can be found [here](https://github.com/UBC-CS/cpsc330/tree/v2.0).

Instructor: Varada Kolhatkar

## Important links

* [Course GitHub page](https://github.com/UBC-CS/cpsc330)
* [Course Jupyter book](https://ubc-cs.github.io/cpsc330/README.html)
* [Course videos YouTube channel](https://www.youtube.com/playlist?list=PLHofvQE1VlGtZoAULxcHb7lOsMved0CuM)
* [Canvas link](https://canvas.ubc.ca/courses/78046)
* [Class + office hours calendar](https://htmlpreview.github.io/?https://github.com/UBC-CS/cpsc330/blob/master/docs/calendar.html)
* [Syllabus / administrative info](docs/course_info.md)
* [Piazza](https://piazza.com/class/kt60nrdhu53454) (this is where all announcements will be made)
* [Other course documents](https://github.com/UBC-CS/cpsc330/tree/master/docs)
* [Past exams](https://github.com/UBC-CS/cpsc330/tree/master/exams)

## Deliverable due dates (tentative)
Usually the homework assignments will be due on Mondays (except next week) and will be released on Tuesdays. 

|Assessment  | Due date |  Where to find? | Where to submit? | 
|-------|-----------|-----------|-----------|
| Syllabus quiz | Sept 14, 11:59pm  | [Canvas](https://canvas.ubc.ca/courses/78046) | [Canvas](https://canvas.ubc.ca/courses/78046) | 
| hw1 | Sept 14, 11:59pm |  [Github repo](https://github.com/UBC-CS/cpsc330/tree/master/hw/) | [Gradescope](https://www.gradescope.ca/courses/5032)|  
| hw2 | Sept 20, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330/tree/master/hw/) | [Gradescope](https://www.gradescope.ca/courses/5032)| 
| hw3 | Oct 04, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330/tree/master/hw/) | [Gradescope](https://www.gradescope.ca/courses/5032)|  
| hw4 | Oct 11, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330/tree/master/hw/) | [Gradescope](https://www.gradescope.ca/courses/5032)|  
| hw5 | Oct 25, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330/tree/master/hw/) | [Gradescope](https://www.gradescope.ca/courses/5032)|  
| **Midterm** | Oct 28, during class time|[Canvas](https://canvas.ubc.ca/courses/78046) | [Canvas](https://canvas.ubc.ca/courses/78046) | 
| hw6 | Nov 15, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330/tree/master/hw/) | [Gradescope](https://www.gradescope.ca/courses/5032)|  
| hw7 | Nov 22, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330/tree/master/hw/) | [Gradescope](https://www.gradescope.ca/courses/5032)|  
| hw8 | Nov 29, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330/tree/master/hw/) | [Gradescope](https://www.gradescope.ca/courses/5032)|  
| **Final exam** | TBD | [Canvas](https://canvas.ubc.ca/courses/78046) | [Canvas](https://canvas.ubc.ca/courses/78046) |



## Lecture schedule (tentative)

**Live lectures**: The lectures will be in-person in **[Hugh Dempster Pavilion (DMP) 110](http://www.maps.ubc.ca/PROD/index.php) from 11am to 12:20pm**. See the [Calendar](https://htmlpreview.github.io/?https://github.com/UBC-CS/cpsc330/blob/master/docs/calendar.html) for more details. The live lecture recordings will be available [here](https://ubc.ca.panopto.com/Panopto/Pages/Sessions/List.aspx?folderID=7cb3d5e9-9fcc-4c76-a287-ad98010bacfe).     

**Lectures**: 
- Try to watch the "Pre-watch" videos before each lecture. 
- I'll be developing lecture notes in this repository. So if you check them before the lecture, they might be in a draft form. Once they are finalized, I'll post them on the [Jupyter book](https://ubc-cs.github.io/cpsc330/README.html). 

| Date  | Topic |  Assigned videos and datasets | vs. CPSC 340 |
|-------|-----------|-------------------------|------------------|
| Sep 7 | _UBC Imagine Day - no class_ | | 
| Sep 9 | Course intro [[notes](lectures/01_intro.ipynb)] | 📹 <li>Pre-watch: None</li><li>During lecture: [1.0](https://youtu.be/-1hTcS5ZE4w)</li> | n/a|
|  | **Part I: ML fundamentals and preprocessing**  | |  
|  | |**Week 2 datasets:** <li>[grade prediction toy dataset](lectures/data/quiz2-grade-toy-classification.csv)</li><li>[Canada USA cities toy dataset](lectures/data/canada_usa_cities.csv)</li> | |
| Sep 14 | Decision trees [[notes](lectures/02_decision-trees.ipynb)] | 📹 <li>Pre-watch: [2.1](https://youtu.be/YNT8n4cXu4A), [2.2](https://youtu.be/6eT5cLL-2Vc)</li> <li>During lecture: [2.3](https://youtu.be/Hcf19Ij35rA), [2.4](https://youtu.be/KEtsfXn4w2E)</li> |   less depth| 
| Sep 16 | ML fundamentals [[notes](lectures/03_ml-fundamentals.ipynb)]| 📹  <li> Pre-watch: [3.1](https://youtu.be/iS2hsRRlc2M), [3.2](https://youtu.be/h2AEobwcUQw)</li> <li>During lecture: [3.3](https://youtu.be/4cv8VYonepA), [3.4](https://youtu.be/Ihay8yE5KTI)</li>| similar |
|        |     |**Week 3 datasets:** <li>[California housing](https://www.kaggle.com/harrywang/housing)</li><li>[Spotify Song Attributes](https://www.kaggle.com/geomack/spotifyclassification/home)</li> | |
| Sep 21 | [$k$-NNs and SVM with RBF kernel]() | 📹  <li> Pre-watch: [4.1](https://youtu.be/hCa3EXEUmQk), [4.2](https://youtu.be/bENDqXKJLmg)</li> <li>During lecture: [4.3](https://youtu.be/IRGbqi5S9gQ), [4.4](https://youtu.be/ic_zqOhi020)</li>  | less depth |
| Sep 23 | Preprocessing, `sklearn` pipelines |  |  more depth|
|        |     | **Week 4 dataset:** <li>[Adult Census Income](https://www.kaggle.com/uciml/adult-census-income#)</li> | |
| Sep 28 | More preprocessing, text features, `sklearn` column transformers | | more depth |
| Sep 30 | _Truth and reconciliation day - no class_ | |   |
|        |     |**Week 5 datasets**: <li>[SMS Spam Collection Dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset)</li> | |
| Oct 5 | Logistic regression, word counts, `predict_proba`| |   less depth |
| Oct 7 | Hyperparameter optimization, overfitting the validation set | | less depth | 
|        |     |**Week 6 datasets**: <li>[Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)</li> | |
| Oct 12 | Outliers |  |   different|
| Oct 14 | Evaluation metrics for classification  |  | more depth |
|        |     |**Week 7 datasets**: <li>[Kaggle House Prices data set](https://www.kaggle.com/c/home-data-for-ml-course/)</li> | |
| Oct 19 | Linear regression, regression metrics |  |   more depth on metrics less depth on regression|
| Oct 21 | Ensembles, prediction intervals | | similar |
|        |     |**Week 8 datasets**: <li>[Adult Census Income](https://www.kaggle.com/uciml/adult-census-income#)</li>  | |
| Oct 26 | feature importances, feature selection | | feature importances is new, less depth on feature selection |
| Oct 28 | **Midterm**  |  |
|  | **Part II: Unsupervised learning, transfer learning, different learning settings**  | | 
|        |     | **Week 9 datasets**: <li>[Credit Card Dataset for Clustering](https://www.kaggle.com/arjunbhasin2013/ccdata)</li> | |
| Nov 2 |   Clustering |   | less depth |
| Nov 4 |   Simple recommender systems | | less depth |
|        |  | **Week 10 datasets**: <li>[Jester 1.7M jokes ratings dataset](https://www.kaggle.com/vikashrajluhaniwal/jester-17m-jokes-ratings-dataset)</li> | |
| Nov 9 |  Text data, embeddings, topic modeling  |  |   new |
| Nov 11 | _Midterm break - no class_  |  |
|        |     | **Week 11 datasets**: <li></li> | |
| Nov 16 | Neural networks and computer vision | |   less depth |
| Nov 18 | Time series data |  | new |
|        |     | **Week 12 datasets**: <li></li> | |
| Nov 23 | Survival analysis |  |   new |
|  | **Part III: Communication and ethics**  | |
| Nov 25 | Communication introduction |  | new |
|        |     | **Week 13 datasets**: <li></li> | |
| Nov 30 | Communication and ethics |  |   new |
| Dec 2 |  Ethics |  | new |
|        |     | **Week 14 datasets**: <li></li> | |
| Dec 7 | Model deployment and conclusion |  |  new |


## Working during the COVID-19 global pandemic

We are working together on this course during a global pandemic. Everyone is struggling to some extent. If you tell me you are having trouble, I am not going to judge you or think less of you. I hope you will extend me the same grace!

Here are some ground rules:

- If you are unable to submit a deliverable on time, please reach out **before** the deliverable is due.
- If you need extra support, the teaching team is here to work with you. Our goal is to help each of you succeed in the course.
- If you are struggling with the material, the new hybrid teaching format, or anything else, please reach out. I will try to find time and listen to you empathetically.
- If I am unable to help you, I might know someone who can. UBC has some [great student support resources](https://students.ubc.ca/support).

### Covid Safety at UBC

**Masks:** This class is going to be in person. Masks are required indoors, including in classrooms, as per the [BC Public Health Officer orders](https://www2.gov.bc.ca/gov/content/covid-19/info/restrictions#masks). For the purposes of this order, the term "masks" refers to medical and non-medical masks that cover our noses and mouths.  Masks are a primary tool to make it harder for Covid-19 to find a new host.  You will need to wear a medical or non-medical mask anytime you are indoors at UBC, for your own protection, and the safety and comfort of everyone else in the class. Please do not eat in the classroom. If you need to drink water/coffee/tea/etc, please keep your mask on between sips. Please note that there are some people who cannot wear a mask. These individuals are equally welcome in our class. 

**Vaccination:** If you have not yet had a chance to get vaccinated against Covid-19, vaccines are available to you, free, and on campus [http://www.vch.ca/covid-19/covid-19-vaccine]. The higher the rate of vaccination in our community overall, the lower the chance of spreading this virus.  You are an important part of the UBC community. Please arrange to get vaccinated if you have not already done so. 

**COVID-19 testing:** UBC will require COVID-19 testing for all students, faculty and staff, with exemptions provided for those who are vaccinated against COVID-19: [https://news.ubc.ca/2021/08/26/ubc-implements-vaccine-declaration-and-rapid-testing-for-covid-19/]

**Your personal health:**
If you're sick, it's important that you stay home – no matter what you think you may be sick with (e.g., cold, flu, other). A daily self-health assessment is required before attending campus. Every day, before leaving home, complete the self-assessment for Covid symptoms using [this tool](https://bc.thrive.health/covid19/en ).

Stay home if you have Covid symptoms, have recently tested positive for Covid, or are required to quarantine. You can check [this website](http://www.bccdc.ca/health-info/diseases-conditions/covid-19/self-isolation#Who) to find out if you should self-isolate or self-monitor. 

Your precautions will help reduce risk and keep everyone safer. In this class, the marking scheme is intended to provide flexibility so that you can prioritize your health and still be able to succeed: 
- All course notes will be provided online. 
- All homework assignments can be done and handed in online. 
- All exams will be held online.  
- Most of the class activity will be video recorded and will be made available to you. 
- Before each class, I'll also try to post some [videos on YouTube](https://www.youtube.com/watch?v=-1hTcS5ZE4w&list=PLHofvQE1VlGtZoAULxcHb7lOsMved0CuM) to facilitate hybrid learning. 
- There will be at least a few office hours which will be held online. 

## Official statement from UBC regarding the online learning experience:

>*During this pandemic, the shift to online learning has greatly altered teaching and studying at UBC, including changes to health and safety considerations. Keep in mind that some UBC courses might cover topics that are censored or considered illegal by non-Canadian governments. This may include, but is not limited to, human rights, representative government, defamation, obscenity, gender or sexuality, and historical or current geopolitical controversies. If you are a student living abroad, you will be subject to the laws of your local jurisdiction, and your local authorities might limit your access to course material or take punitive action against you. UBC is strongly committed to academic freedom, but has no control over foreign authorities (please visit http://www.calendar.ubc.ca/vancouver/index.cfm?tree=3,33,86,0 for an articulation of the values of the University conveyed in the Senate Statement on Academic Freedom). Thus, we recognize that students will have legitimate reason to exercise caution in studying certain subjects. If you have concerns regarding your personal situation, consider postponing taking a course with manifest risks, until you are back on campus or reach out to your academic advisor to find substitute courses. For further information and support, please visit: http://academic.ubc.ca/support-resources/freedom-expression.*
