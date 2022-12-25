### Announcements

Dear @v-students and @cl-students ,
Welcome to DSCI 573 course channel! I’m happy to teach you again this block :slightly_smiling_face:. If you have not noticed it yet, our course is open: https://github.ubc.ca/MDS-2021-22/DSCI_573_feat-model-select_students.
Our first lecture is going to be on Monday at 8am. I’ve pushed drafts of the lecture notes in the repository. There are a couple of things I would like you to do before the lecture:
Watch the following videos: 9.1, 9.2, 9.3. There is one more video on the course page for this lecture (9.4). You are welcome to watch it before the lecture but it’s more of a post-lecture video because to fully understand the video you need to understand the material we’ll discuss during the lecture.
Create course conda environment with the help of  instructions here. 
The format of the course will be similar to DSCI 571 except that there will be more live lecturing and less pre-lecture videos. I feel like I was not very effective with supporting remote learners last block. (Sorry, this hybrid learning is a new thing for me and it takes time to adjust to it.) I’ll try to be more organized and approachable to the remote learners this block. In particular, I’m planning to create pinned Slack posts for all lectures, where you’ll be able to post your questions during live streaming. I’ll try to take breaks for Q&A and check your questions during these breaks. Let’s see how it goes. Also, I know 8am is very early for some of you. But, if you are feeling well, it’ll be nice if you try to come to the class in person. It’s nice to see people in the classroom and interact with them.
Have a great weekend and I’ll see you soon


I recall many of you having wifi issues in ESB 2012. If you are having wifi issues in the lab today, can you please open a ticket at https://ubc.service-now.com/selfservice/? As I said before, if we open multiple tickets, the problem is likely to be resolved soon.

Hello @v-students @cl-students !
A few announcements:
I’ve pushed quiz practice questions in the course repository.
I’ve updated lecture notes with my answers to T/F questions.  
Since we rushed through RFE and forward selection in the last lecture, I’ll go through it at the beginning of the next lecture (on Monday). This material will still be included in quiz 1, which is going to be on Tuesday. 
We didn’t quite get a chance to talk about how RFE is different than backward selection and there is a question on it in the lab. RFE and backward selection kind of sound the same in the sense that both of them start with the full feature set and get rid of one feature at a time. But RFE carries out feature selection using feature importances whereas backward selection does not use feature importances. It carries out feature selection only based on cross-validation scores.
I’ve scheduled an extra OH on Monday at 5pm so that you get a chance to ask questions before your quiz on Tuesday.
Finally, we had a meeting with block reps today. Thank you for your feedback!

If you are unwell and have submitted a remote quiz form:
Please DM me to let me know that you’re doing the quiz remotely.
Please join the OH Zoom session in Canvas at least 5 minutes before the quiz time: https://ubc.zoom.us/j/69220982100?pwd=b1UybTdtQlNnWUgxUDBPcjhZcU5iZz09
Keep your camera on and audio on mute.
Keep your ID nearby so that the TA can take attendance. 
You will get the quiz code from the TA who will be invigilating the remote quiz. (I won’t be sending them to you on Slack.)
If you have questions, you can DM me on Slack. But it might take a while for me to respond, as I’ll be giving higher priority to the people in the classroom. 


Now that you are done with the quiz I wanted to share some thoughts with you.
I agree that 573 was not an easy course. But I hope that each of you learned something useful from the course. Actually, I’m looking at your lab4 submissions and I’m impressed to see your solutions and creativity. It’s very rewarding to see you put all the things we have learned in 571 and 573 into practice. I hope that you are feeling more or less confident now about building a supervised machine learning pipeline with preprocessing, feature engineering, feature selection, hyperparameter optimization, model selection, and model interpretation. During your break, I recommend that you focus on getting enough sleep and rest but if you enjoyed this material and if you have the energy, you should be able work on your favourite Kaggle competition task.
There are many things to learn in supervised machine learning and we only managed to scratch the surface of this massive field, as we only had VERY limited amount of time to learn all these concepts. (Sorry that sometimes I got too excited and created long labs :see_no_evil:.) My goal has been to teach you practical side of supervised machine learning, which is likely to be useful for you when you work as a data scientist or a machine learning practitioner. I believe that knowing this big picture and practical side helps if you are interested in digging deeper into a certain topic. Many of you might be interested in knowing the mathematical details of the models or methods we discussed in this course. If so, please check out the Reference Material section in our README. My favourite one is: A Course in Machine Learning (CIML). I’ve also heard great things about  The Elements of Statistical Learning (ESL) but I’ve not read it myself. You can also refer to Mark Schmidt’s CPSC 340 material. Mike has taught this course several times and he has videos associated with this material on YouTube.
Grading of lab3 and lab4 and quiz2 are in progress and I’ll return the grades as they become available.
I’m happy to hear your thoughts on this course. If you get a chance, it will be great if you can fill out the course evaluations before the deadline, which is December 16th 11:59pm: https://canvas.ubc.ca/courses/78168/external_tools/4732
I plan to be there at the Holiday party tomorrow. If you’re there, I’ll see you tomorrow. If not, I’ll see you in block 5. I’ll be teaching you two of my favourite courses next semester: unsupervised learning in block 5 and advanced ML in the context of natural language processing in block 6 :heart_eyes:.


All of you should have received a bunch of emails about 573 grades. I’ve applied appropriate penalties and weights for different assignments to calculate the final grade. (Each lab is worth 15% and each quiz is worth 20%.) Can you please look at your final grade in Canvas and DM me if your grades is looking weird and not as expected? I plan to submit the final grades to FSC early next

Hey everyone. Did anyone write a Randomized/Grid Search to tune hyperparameters of estimators inside the Stacking/Voting methods? (

### Lecture 1
- Thanks for posting the videos. Will you talk about real world examples where we might care more about accuracy and recall respectively in class?
> I guess Fraud detection example in the video is a real-world example? But yeah, there will be some discussion on this in class.
> do we assigned the weights or sklearn takes it basis on the number of observations?
> If weighted average is to observe accuracy for classes with highest samples . Isn't it equal to just seeing the normal accuracy ? As the general accuracy is biased to the target level with more samples.
> Do we get recall and precision of all the cv sets? or we looks at the mean of recall & precision?
> why dont we just look at the best F1- score rather than looking at ROC curve?
> Shouldn't we use the same threshold for training and validation set? Why only validation set 
> I think the true positive rate was defined incorrectly in the lecture notes. Recall was defined with FN in the denominator but true positive rate was defined with FP in the denominator, which is also how precision was defined
> Depends on which side of the confusion matrix do you keep the Actuals. 
> Why would that change the definition of recall and precision?
> TPR = TP/TP+FN and FPR= FP/FP+TN
> I agree with those definitions but that wasn’t what was given in the lecture notes for TPR lol
> Oops. You're right @Daniel King
 . It's incorrect in the ROC curve slide. It should be
> $$ FPR  = \frac{FP}{FP + TN}, TPR = \frac{TP}{TP + FN}$$

> do we assigned the weights or sklearn takes it basis on the number of observations?
Not sure what you're trying to ask 
@Abhiket
If weighted average is to observe accuracy for classes with highest samples . Isn't it equal to just seeing the normal accuracy ? As the general accuracy is biased to the target level with more samples
We are calculating weighted average of precision, recall, and f1 score which have different formulas than accuracy, which is TP + TN / # examples.
Do we get recall and precision of all the cv sets? or we looks at the mean of recall & precision?
You can get cross-validated confusion matrix using cross_val_predict and calculate precision and recall for that.
why dont we just look at the best F1- score rather than looking at ROC curve?
F1-score is based on predict output and ROC is based on predict_proba output. You might miss some subtleties if you only use the F1-score, as we saw in the lecture.
Shouldn't we use the same threshold for training and validation set? Why only validation set?
At the end of the day we want to deploy our model. So we want to get a sense of what threshold satisfies the operating point. Validation data and test data give us a better estimate of this compared to the training data.


Lecture 2: 
- Question1: what will happen if we do OHE on ordinal columns? Will it affect the model, as anyway we are going to have separate columns.
- Question2: Will outlier affect classifications models? What is the best way to do an outlier treatment? Shall we do scaling only after outlier treatment (esp. for regression models) ?
- Question 3: What is the difference between RidgeCV and other's (RandomSearchCV /GridSearchCV)

Lecture3 question thread.
- Is there a way to transform the features using other functions such as log?
- In practice, do we pick only some of the features to do ploynomial transformation using ColumTransformer? How do we know which column is not “linear enough” that we need to apply this transformation?
> Sure. You can apply any transformation you want on the features. I just showed you the most common ones. In sklearn there is something called FunctionTransformer , which you can use to define custom transformations.
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html

> For polynomial transformation, we usually apply them on all columns because usually we don't know how to pick columns on which we need to apply polynomial transformations. In the toy classification example with 2 features, I just applied it on one of the columns because I only wanted 3 features for visualization. As I mentioned in class, you cannot visualize high dimensional data and if you decide to visualize one feature at a time, you're going to miss feature interactions.
> If you want to apply them on specific columns, I guess you could do it in a column transformer.
> What if dropping features first (RFECV)  then apply PolynomialFeatures yield a better CV scores? This is saying assuming adding polynomial terms of these 'weak' features won't help in the final model. This is the case with lab2 q3.3 for me. It results in a much simpler model and a slightly better score - isn't this what we want?
> Yeah, that’s possible. You’re right that we want a simple and interpretable model with better scores. With polynomial transformations, we end up adding many features: the polynomial degree features as well as interaction features. Many of these newly added features might not make sense. Our hope is that the model in our feature selection method (e.g., Ridge in RFE) would take care of getting rid of irrelevant features. And that’s why I would add polynomial transformations before feature selection. But as you can see there could be many different combinations you can try out and whatever method you choose you’re not guaranteed to find the optimal solution because the search space is just huge. So you just try your best.


Lecture4 question thread.
- I am confused about the interpretability of ML models. We were discussing in the class that basis the coefficients, we should not make claims, but isn't that why we would make the models. The aim typically is to come to a model which allows us to make reliable predictions. Not sure what I am missing here?
> Wouldnt we want very  negative features? did we say we us abs value?
> Based on the coefficients or feature importances
Do you believe that’s how the model is going make predictions? YES.
Do you believe that’s how the world works? NO.
> We want both positive and negative coefficients with bigger magnitude. That’s why we are taking abs values.
> Yeah ok, the abs part was only mentioned once in passing so i couldn't quite tell in the context of the other processing. that makes sense to me.


Lecture5 question thread.
- In Forward method , If we start off by making a model on a single feature and so on . How is multicollinearity or interaction between variables handled ?
> Can I assume another termination condition is when the number of selected features is equal to the total number of features ? In forward selection.
> With soft voting - If one of the classifier has a high prediction probability . Wont the average be biased/inclined to that one model's prediction ?
> Yeah, this is a drawback of greedy methods like forward/backward selection where we are "greedily" or locally making decisions on which feature should be discarded. It might happen that you get rid of a feature based on current CV scores but it can become very important in the presence of some other feature which is not already in the subset. In general, the search problem here is intractable because the search space grows quite quickly. (With 100 features you have 2^100 different feature combinations to try!!) So we try out best and use approximate methods which give us good enough solutions.
> With soft voting - If one of the classifier has a high prediction probability . Wont the average be biased/inclined to that one model's prediction ?
Yes, but I think it's for a good cause. Higher prediction probability means the model is more confident about the prediction so we want to trust the model more.


Lecture6 question thread.
- Can you please explain how shap scores for each feature are found in Shap value output ?


Lecture7 question thread.



Here is an attempt to explain macro-average and weighted average better. Consider this toy example with 3 examples of class 0 and 2 examples of class 1:

```
from sklearn.metrics import classification_report
y_true = [0, 1, 0, 1, 0]
y_pred = [0, 0, 0, 1, 0]
target_names = ['class 0', 'class 1']
print(classification_report(y_true, y_pred, target_names=target_names))

          precision    recall  f1-score   support

     class 0       0.75      1.00      0.86         3
     class 1       1.00      0.50      0.67         2

    accuracy                           0.80         5
   macro avg       0.88      0.75      0.76         5
weighted avg       0.85      0.80      0.78         5
```

weighted average is weighted by the proportion of examples in a particular class. So for the toy example above:
weighted_average precision: 3/5 * 0.75 + 2/5 * 1.00 = 0.85
weighted_average recall: 3/5 * 1.00 + 2/5 * 0.5 = 0.80
weighted_average f1-score: 3/5 * 0.86 + 2/5 * 0.67 = 0.78
macro average gives equal weight to both classes. So for the toy example above:
macro average precision: 0.5 * 0.75 + 0.5 * 1.00 =0. 875
macro average recall: 0.5 * 1.00 + 0.5 * 0.5 =0. 75
macro average f1-score: 0.5 * 0.75 + 0.5 * 1.00 =0.765
@Utkarsh
 the thing I mentioned in class was actually micro average, where you globally count total true positives, false negatives and false positives
 
 
Lecture1  is there any intuitive way to understand the ROC curve? Do we plot every single threshold to find out the high recall while keeping low false positive rate?
> As said, the ROC curve is the result of trying many different thresholds.
And which threshold would be the best depends on the business problem.  For instance, if recall needs to be 0.8 or better, then we need to ask ourselves whether we are happy with the corresponding FPR.
And if we are still not happy with either TPR or FPR and it still doesn’t satisfy the business requirement, we may need to consider doing something different, including trying a different model, get more data, etc.
> As an addition, ROC curve on it's own isn't sufficient. You might need a bunch of metrics, weigh them together and see what suits your problem. In general, I found the Precision vs Recall curve pretty helpful for determining how threshold affects your scores.


- Lab1Q1.4 i am having trouble with the fractions entered for F1 score. i am not sure how much to reduce them, considering all the multiplication
> Don't reduce the fractions
> Even though they are compounded?
> also they have to be converted to be added
> I assume you mean for f1-score, for that make a function that calculates the f1-score and jsut assign that value returned from the function to the results_dict


- Is it ok to use commenting`#` when providing reasoning?
> I would use Markdown cells for text. That way it will be more visible and pretty. If you write your reasoning in Python comments, it’s likely that TAs miss it when grading your work.

- lab1Q2.4Has anyone dealt with this error before “ValueError: Shape of passed values is (2333, 1), indices imply (2333, 65)”
> My guess is that you are not passing sparse=False  to OHE. Usually we don’t want to pass it because it’ll create a dense representation of OHE features. But if you want to visualize the encoded features as a dataframe you want dense representation.
> Also, our dataset is rather small and so it’s not going to be a big deal.

- When we are doing hyperparameter optimization using RandomizedSearchCV and optimizing scores like precision, recall, or F1, how does it know which class is "positive"?, Is it always the second class listed when you call .classes_? What if we want to optimize the score for the other class that it chooses as "negative"?
> These “searches” doesn't care which class is which. It just calculates a “score” and ranks it at the end. Normally the “score” is accuracy. Now for our purpose, we might want to use, say, the recall of the class we care about.
> What I'm confused about is, when we are optimizing another score like recall, all we do in the function is tell it to optimize recall. We didn't tell it which class is the one we care about, and the recall score changes depending on which class we care about
> Not 100% sure, but looks like the positive class is defined by pos_label, where the default is 1. Also based on what I found below, for binary classification problem, the class label with the greater value (numerically or lexicographically) is defined as the positive label.
Semantically, one class is often considered the “positive” class. Unless otherwise specified (e.g. using pos_label in evaluation metrics), we consider the class label with the greater value (numerically or lexicographically) as the positive class: of labels [0, 1], 1 is the positive class; of [1, 2], 2 is the positive class; of [‘no’, ‘yes’], ‘yes’ is the positive class; of [‘no’, ‘YES’], ‘no’ is the positive class. This affects the output of decision_function, for instance
https://scikit-learn.org/stable/glossary.html#term-binary
> I guess most of the time, this default setting works out of the box (since 0 < 1, no < yes). But I've encountered cases whereby the default positive class is the wrong one, so it is always good to manually check which one is the positive class.
> (Varada) When you calculate precision, recall, f1 score on their own using sklearn functions or using say cross_validate or RandomizedSearchCV , by default only the
"positive" class is evaluated, assuming that the positive class is the class at index 1 of  model.classes_ . This is configurable through the pos_label parameter.


- lab1ex2.9 Getting this warning when I use class_weight="balanced":

```ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
Did anyone else encounter this? If yes, did you figure out the reason? ```

> Looks like you need to set max_iter for Logistic Regression. The model isn’t able to converge to an optimal solution.

- lab1 2.4 Can we use make_column_transformer  wherever you said using ColumnTransformer ?
> Yes, please use make_column_transformer 

- lab 1, q0.1 I understand that if we call fit_transform on our test data, our model becomes biased, but what happens if we are dealing with CountVectorizer ? Am I right in presuming that our model learns the words from the test data as well and that is how it becomes biased? Or am I missing something?
> Think about the vocabulary size and therefore feature vector sizes when you call fit_transform  on training data vs. test data. You can try it out on a small corpus and check what happens.
> Try this toy example, for instance.

```
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

X_toy = [
    "URGENT!! As a valued network customer you have been selected to receive a £900 prize reward!",
    "Lol you are always so convincing. I'm going to give you a free advice. It's urgent.",
    "Block 2 has interesting courses.",
    "URGENT! You have won a 1 week FREE membership in our £100000 prize Jackpot!",
    "Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free!",
    "Block 2 has been great so far.",
]
y_toy = ["spam", "non spam", "non spam", "spam", "spam", "non spam"]

X_train, X_test, y_train, y_test = train_test_split(X_toy, y_toy, random_state=123)
vec = CountVectorizer(stop_words="english")
X_train_vec = vec.fit_transform(X_train)

vec = CountVectorizer(stop_words="english")
X_test_vec = vec.fit_transform(X_test) # NOOOOOOO.....DON'T DO IT

lr = LogisticRegression()
lr.fit(X_train_vec, y_train)

print('Shape of train feature vector: ', X_train_vec.shape)
print('Shape of test feature vector: ', X_test_vec.shape)

lr.predict(X_test_vec) ### This won't work because the feature vector of train and test data are going to be of different shapes. 
```


- lecture1  in Precision Recall curve, in the following code close_default_lr = np.argmin(np.abs(thresholds_lr - 0.5)) , why are we subtracting 0.5 from thresholds_lr ?
> I think it is trying to find the pair of precision and recall that is closest to 0.5.
> Then why are we subtracting it only for random forest and logistic regression model and not svm model?
> In the lecture notes, SVC uses decision_function instead of predict_proba. The threshold is 0 (distance from the hyperplane),, hence we do not need to subtract 0.5.


- lab1 2.6  What is different between precision and average precision score?
> Precision score is for one threshold value and average precision score is a summarised precision score for many threshold values
> Here you'll find the exact formula for AP score. When you calculate average precision, for each possible threshold, you look at the precision at this threshold times the change in recall.
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html
So for infinite thresholds, it's area under the curve.
> Can AP score ever be 0? No right, because there will always be some area under the PR curve? Is my understanding correct?

- Lecture 1 Any specific examples on when we can ignore class imbalance? Thanks!
> My understanding is that we do NOT have to “correct” class imbalance per se, but we need to be careful in the whole modelling process if it is the case.
> Depends on your problem. I have seen  situations where datasets with 90-10% class imbalance being solved by tree based algorithms, without the use of any method with handles the imbalance.
> The word class imbalance is highly judgemental. People have different thumb rules but one thing for sure is you don't touch class weights for situations such as 60-40%. Its very rare unless you are looking at a really high recall value for the positive class. Hope this helps :v:

- Solved Unable to print the precision-recall curve, what am I missing here?
> You don't need print to display it. Try passing your best estimator from random or grid search like random_search.best_estimator_ as the first argument. Also, you don't need a name argument.
> Got rid of print and name. As for the best hyper parameters, I've created a pipe with the model initialised with those values. Still no luck..
> Actually, random search or grid search whichever you use automatically fits a model based on the best params you got, so try passing that as the first argument instead of you creating a new pipe.
> I changed it, but I dont think thats the issue here..
> Try adding plt.show() at the end. Under the hood, sklearn is calling matplotlib
> Have you imported matplotlib.pyplot as plt?
> Yes, its already imported. I have even restarted the kernel, no luck
> I'm trying to figure out of this is a matplotlib problem. Can you try plotting a super simple plot and see if that works? 
> Looking around, seems like adding this solved it:
%matplotlib inline

- question: you are adding "drop" in your column transformer pipeline in video 10.1. This can also be done by just omitting columns from the pipeline, right? So useful if for eg you grouped your numerics using select_dtypes but redundant if you did column names by hand?
> Spent like half an hour yesterday learning how to get feature names out of preprocessor pipe, should have waited for the video :joy:
> (Well, I think it's useful to try things out yourself before looking at the solution. That way you make better connections in your brain and remember concepts for a long time.) Yes, if you don't include a feature in your column transformer, it will not be included in your pipeline. That said, if you explicitly have drop features in your pipeline, your code is more readable, in the sense that the reader exactly knows what features you are dropping. Also, you need to be careful about it if you get feature names for a particular type of features by subtracting other features, similar to how we did it in class today. Make sure to include the drop features if you do it.
```
categorical_features = list(
    set(X_train.columns)
    - set(numeric_features)
    - set(ordinal_features_reg)
    - set(ordinal_features_oth)
    - set(drop_features)
)
```

- lab1 q2.11 any hints of how can I use RandomizzedSearchCV   to find cross-validation f1 score? Also, while my best performing model is already with classs_weight=balanced , and do I still need to include class_weight hyperparameter in the tuning?
> After lots of google search I found the following command for hyperparameter optimization:
random_search = RandomizedSearchCV (pipe, param, n_iter=200, verbose=1, n_jobs=-1, scoring="f1", random_state=123)
random_search.fit(X_train, y_train)
Now I am not sure how to rank the output:
when doing "random_search.cv_results_" the f1_score does not appear.

> I tried something similar already but I got a super long error screen (part of that is attached); I also don't know why we need to have class_weight  in the param_grid if I already said my model of pipe_svc_balanced has the best performing so far; or should I pass pipe_svc  (which is no class_weight arguments)? If so, what's the point of checking scores in exercise 2.9?
> My best model is also pipe_svc_balanced so I assume we are using pipe_svc to do the hyperparameter optimization? Since we are also comparing class_weight = “balanced” and none? Might be a dumb question but want to confirm.
> I used pipe_svc to do the hyperparameter optimization. Maybe the best model is simply choosing from dummyclassifier, logistic regression and svc? I guess different combinations of hyperparameter may have different accuracies so we need to optimize the class weight with other parameters again.
> You might find some hints on using different scoring metrics with GridSearchCV  and RandomizedSearchCV in lecture 2 notes. And yes, jointly optimize values for class_weight  and other important hyperparameters of your best performing model (e.g., C for logistic regression or C or gamma for SVC), as when you optimize them jointly you might get different values for the hyperparameters.
> thanks; I realized it when we had the lecture 2 today but just to confirm we are supposed to randomized search CV the model of pipe_svc  as opposed to pipe_svc_balanced ?

- For lab1q2.4 Can we use this piece of code to get all column names ? It works.
```
transormed_data = preprocessor.fit_transform(X_train)
bow_df = pd.DataFrame(
    transormed_data, columns=preprocessor.get_feature_names_out()
)
```
> Just that it gives the column names as something like this -
> You have to use named_transformers_ to fetch the names of the features as transformations are embedded in the pipeline steps. standardscaler, onehotencoder , etc are the steps in your pipeline, which is a dictionary, so when you try preprocessor.named_transformers_ , it will print a dictionary of pipeline steps. You can try preprocessor.named_transformers_['standardscaler'].get_feature_names_out().tolist()
> Thanks Navya. But I don't see why we cant just use the pipeline's get_feature_names_out() . It gives out the column names but prefixed with the transformation performed on that particular column.

> Hey, I used the followings and I think it worked. Pipeline 2 was categorical_transformer and Pipeline 3 was binary_transformer
```
column_names = (
    numeric_features
    + preprocessor.named_transformers_["pipeline-2"].get_feature_names_out().tolist()
    + preprocessor.named_transformers_["pipeline-3"].get_feature_names_out().tolist()
)
```
> Sure if it works for you go ahead. I think it's a new thing in sklearn 1.0 . I'm not sure whether it works out of the box for complicated column transformers though.

- Does altering the thresholds count as hyperparameter optimisation? And do we only alter the thresholds on the validation set, and not on the training set?

- For the precision-recall curve, why do we need to -0.5 for random forest classifier and linear regression, but not SVC?
```
close_zero_svm = np.argmin(np.abs(thresholds_svc))
close_default_rf = np.argmin(np.abs(thresholds_rf - 0.5))
close_default_lr = np.argmin(np.abs(thresholds_lr - 0.5))
```

This is from Lecture 1 notes, under “A few comments on PR curve”

> Pre-lecture video for lecture 2 was good, and much needed! Was kinda overwhelmed with so many concepts in 571. This video helped me put together all that stuff! 

- lab 2.12  “ROC curve with AUC” just to clarify — it means plotting ROC curve and report AUC score separately right? Not making the AUC in the graph…? For “Precision-recall curve with average precision score”, the AP score is in the graph if we use PrecisionRecallDisplay . I haven’t seen anything that can put AUC score on the ROC curve graph…I want to make sure I understand the question correctly. 
> You could use RocCurveDisplay  for this:
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html

- When we have categorical features in numeric form, is it a recommended practice to transform them back to text if we know what each number represents before performing one hot encoding? I think it makes things more readable?
> Sure, if you know what they represent, it will help during interpretation if you have more readable names for columns such as MoSold_October instead of MoSold_9.

- Can we see some examples of when MAPE is less good than some other metrics?
> I guess it's more about interpretation. MAPE gives us a more interpretable number which summarizes the performance of our model compared to say r2 or RMSE.

- lecture2 I missed it in lecture, what is the test_score here and why is it close to 0 and negative?
> Hint: Try plugging in appropriate values in this formula for train and validation
> For the train score because y_hat is the same as y_bar the equation becomes 1 - 1 = 0. For test score, however, since we have some randomness and our model has not seen it yet, y_bar and y_hat are close but not similar. I don't get the negative part though. I guess technically it could be positive too because it is random.


- ex 2.7, I found that using mean_std_cross_val_scores(lr_pipe, X_train, y_train, scoring=scoring)) and the method of precision_score(y_train, lr_y_pred), will return different results, is it ok for us to choose any of them to get our scores?
> I guess in the former you're carrying out cross-validation and returning mean cross-validation score and in the latter you are not carrying out cross-validation. So the results are likely to be different.
> but the lr_y_pred came from cross_val_predict?
> Ah I see. Yeah, we are calculating kind of different things in both cases. When you carry out cross-validation with a particular metric, it’ll calculate score with that metric for each fold and return the mean of all scores. Whereas the confusion matrix with  cross_val_predict is based on the predictions on examples when they are in the validation set. So when you call cross_val_predict , you’ll get len(y_train) predictions, as each example gets to be in the validation set only once during cross-validation and you count TP, FP, TN, FN from these predictions.

- lab 1 Ex3.5 reads "Try the best model on the test set."
Is this asking about the model from Ex 3.3 (one of Ridge and RandomForestRegressor) or the ridge model with the best hyperparameter from Ex 3.4 (optional question)?
> Both would be acceptable answers for this question.

- Hi all, I want to use matplotlib to show my plot, it doesn’t happen when I am using the profiler in the above session.
If I don’t load the profiler, the image can be shown. Any idea how to fix it?
Picture is showing AFTER I ran the cell, no plot is shown

> Try to add
```import matplotlib.pyplot as plt
%matplotlib inline```

- lab 1 2.11  would anyone know how to fix the issue of that ConfusionMatrixDisplay  (the actual matrix plot) is not displaying?

- Has anyone used pandas-profiling ? Wanted to discuss something!

- Lab 1 Ex 3.1Since Ridge()can handle multicollinearity in multiple regression data, can I assume it’s safe not to drop some features that are highly correlated? or it might still be better to drop them? Thanks!
>  Yes, it'll be OK if you don't drop them, as you're using Ridge and not vanilla linear regression.

- lecture 2
We know that adjusting threshold can obtain a better result. Can we Incorporate the threshold when we are doing Hyperparameter tuning? If so, how can we do that?
  2. About Transforming the targets
Model A
Example 1: Truth: $50k, Prediction: \$100k
Example 2: Truth: $500k, Prediction: \$550k
RMSE: $50k
MAPE: 45%
How to calculate MAPE?
|50/50 + 50/500|/2 is 0.55
> For 2 - I think .45 is a typo in the lecture notes
> Oops! You’re right. It’s a typo. Should be fixed in the lecture notes now.

- lab1Q3.1  Is there a recommended way to deal with latitude and longitude at this stage (of MDS)? I Googled and it’s more complicated than I thought…
> how did you deal with that column at last? I just dropped the columns
> I kept them cuz I’m not sure what to do …
> In lecture 4 last block we were using just the StandardScaler()


- lab1Q3.5 Should we be using multiple scoring metrics, sticking with the default, or picking the most appropriate-seeming metric?
> Pick the most appropriate-seeming metric.

- lab 1
The file will be extremely large to include two profilings, Gradescope can not show the file if it’s larger than 1MB. Should I also submit a PDF version? 
> Yes, please include a pdf in Gradescope if your ipynb doesn't render on Gradescope. There is a submission instruction for this in the lab write up.
If the .ipynb file is too big and doesn't render on Gradescope, also upload a pdf in addition to the .ipynb.
Also, please don't include everything given by the pandas profiler in your submission. Only include relevant plots and corresponding discussion.
> Pandas profiling doesn’t render in PDF either I guess it’s in HTML format, what should we do?

- lab1_ex3.6.2 One caveat to consider for this question is that, the coefficients that we pull from our best model are fitted on transformed (scaled) features, and because of that it might give misleading information on the magnitude of those coefficients. To identify the feature with most positive contribution on price, should we use the raw non-scaled data?
> I would say that the coefficients are comparable because our features are scaled. If the features are not scaled then you cannot really compare coefficients. For example, coefficient of 0.1 for feature1 with value 1000000 and coefficient of 0.1 for feature2 with value 0.001 will have very different impacts on the prediction.
> You are right. I see the point. Thank you for your explanation :pray::skin-tone-4:

- lecture 2 In the lecture note it says: by default, fit  minimize MSE / maximize R^2. So minimize MSE equals maximize R^2?
> No… it’s two separate things. when we call fit, under the hood,
MSE - looking for the smallest value
R^2 - looking for the largest value
> Thank you Macy! But in that case, when we call fit, which one of the two metrics is the default metrix? Minimize MSE or maximize R^2? 
> I think by minimizing one you are maximizing the other. R^2 is 1 - (sum of squared errors/sum of squared deviations from mean). In this formula, only the sum of squared errors depends on the model. The mean squared error is just the sum of squared errors/n. As you minimize the sum of squared errors, you minimize the mean of squared errors and maximize R^2.
> I went to look at the code, I guess that sentence is just a concept. Different regressors do different things.
linear is using least-squares
https://github.com/scikit-learn/scikit-learn/blob/0d378913b/sklearn/linear_model/_base.py#L630


- lecture 2 About using multiple metrics in GridSearchCV: why do we pass so many different score matrics (like picture 1) into GridSearchCV and refit it with MAPE if we only want to use RMSE for fitting? Why don't we simply set scoring=mape_scorer  like what we did on the above?
> Depends on your purpose, you may also want to examine other matrix before you decide to use MAPE
> One more follow-up question: If we didn't specify refit when passing multiple metrics into scoring , can we still get best_params_ ? If yes, which metrix will be used?
> Just did a testing, seems you can’t do it. At least I got error

- lecture 1  About the interpretation of AUC : If AUC=0.8, is it correct to say: "80% positive points have a higher score than 80% negative points"?
> I think, yes. Another way to phrase it would be, "There's an 80 percent chance that a randomly picked positive point has a higher score than a randomly picked negative point.

- lab1_ex3.3 I'm slightly confused with my output. I'm not really sure why each cell contains a list. Anyone have any ideas?
> It seems that you are using cross_validate function which returns array of scores in each fold. So when you print results it will be a df of lists…
> I had the same problem. So I used mean_std_cross_val_scores() function instead.
> Right. cross_validate  is going to give you results for all folds. If you want one number in each cell, you can take mean of those scores.

- confusion on Q2.11, if I switched the position of these two values  [None, "balanced"]   in "svc__class_weight": [None, "balanced"]  my best params will be different. The best parameter for svc__class_weight  would always be the first hyperparameter value (no matter how I changed n_iter or np.arange for C and gamma) Does anyone have the same issue?
(I had svc_pipe as svc_pipe = make_pipeline(preprocessor, SVC()) in RandomizedSearchCV ) 
> Its because RandomSearchCV has a max iter of 14 (at least in my computer) therefore RandomSearchCV doesn't see many possibilities. Either try GridSearchCV or different random state in RandomizedSearchCV.
> It’s kind of weird that you’re always getting first value in the list "svc__class_weight": [None, "balanced"]  even when you increase number of iterations. I would try changing the random state, as Chris is suggesting.


- For metric's where we give neg_ prefixed. Does it mean higher value is better ? Eg. -0.810 better than -0.514 for test_neg_root_mean_squared_error ? We give neg_ as sklearn generally maximises and since we want to minimise loss metrics we negate it . But not able to understand how do we interpret the results.
> I am loosely associating negative error with accuracy. So, we are maximizing accuracy. While maximizing accuracy, I choose -0.514 over -0.810 as -0.810<-0.514.
> The more positive (or less negative) the value is, the better. In short, larger values on the number line are better.

- Exercise 2.12 Can anyone help with the ConfusionMatrixDisplay? I tried the code in notes, but it did't display the matrix, and I don't know why.  I have the same issue with PrecisionRecallDisplay, and ROC curve as well. All of them doesn't show up.
> I would probably try including the following in the notebook.
%matplotlib inline

- would you to kindly share the data that you have used in the lectures, as I believe you have done some data wrangling/cleaning before using the same in the lectures.
> Hmmm. I believe that I’ve links to the appropriate datasets in the lecture notes. You just need to download them and put it under the data directory and the code should work. Can you tell me exactly which dataset you’re talking about?


- Lab3Ex3 What is our target column? MedHouseVal?
> its a weird value. I am not finding a lot of metadata. is that in millions do we figure
> Based on their explanation, it’s in 100,000$.
https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset


- Lab1q3.3 hi guys, I am not able to decipher, why we take -ve scoring matrices. How do we compare two -ve matrices ?
> The higher the better. So when the signs are flipped, -50 < -40

- About class_weight=balanced, how does changing this training procedure directly affect the number of TPs? Does it change the threshold for an example to be ‘moved’ from one class to another?
> You can take a look at the docs for exactly how it works, but intuitively, it replicates your infrequent class until it reaches the same weight as the other class. It’s same as penalizing more for one class than the other.
https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html

- hi team, would you recommend CIML or feature engineering and selection for conceptual understanding?

- For question 3.5, which scoring metric should I use for assessing test results? MAPE ?
> You can use the mape_scorer in the previous question as scoring for your randomized search, and then just report best params and best scores.

- lab1,q3.5: Random Forest model seems to be performing better even after hyperparameter optimization for Ridge. So, in 3.5, should I use the optimized Ridge model with best alpha or the Random Forest model?
> Any of them should be fine. I would probably use the random forest model if it’s giving the best cross-validation scores.

- Does predict_proba work for SVC in sklearn? The code is working well when using predict, but not when using predict_proba.
> No, we have to use decision_function() instead of predict_proba for svc
> What do you mean it is not working well ? Do you mean its breaking ?
> Yes it does. You have to do this: SVC(probability = True)


- lab1 q3.5 : I am getting a positive mape score of 18.314 on test data , where as I got negative mape score on train data, how should we intrepret this metric?
> As by default the score function (e.g. cross_validate) interprets “higher is better”, and given MAPE score is “lower the better”, we use the parameter of  greater_is_better=False` in make_scorer such that the model still can rank the highest score as the best model. Similar approach is adopted in the built-in score like “neg_root_mean_square_error”.
You can refer the section Using regression metrics with scikit-learn in lecture notes 2.
I guess the MAPE of train data was from cross validate while the MAPE of test data was from a manual predict. :wink:
> FYI, my MAPE for RF from cross_validate is -18.863 and my the MAPE with my test set is 18.459.  I would just explain that they are very close except that cross_validate flipped the sign.

- Does anyone has the issue saving the notebook as webpdf? Mine cannot be exported as pdf.
> Try to do it from base conda env instead of 573


- I have trouble to load the data in Ex3, does anyone know how to solve it? It's may because of my operating system?
> Seems like some permissions issues. I hope you were able to get it working.

- lab1Ex3.4I am having a hard time cleanly printing the results of the cross validation, did anyone have a good strategy? the nested tables are making it hard to iterate through the models and then just print a dict.
> I created a table for each metric with two models each. I found that putting them one in one df was too crazy for me to read. Not sure if this is okay though.

- Regarding pandas profiling: I used
> conda install -c conda-forge pandas-profiling
and also
> conda install -c conda-forge ipywidgets
for good measure based on looking up previous solutions in slack but I'm still getting a module not found error when trying to use
from pandas_profiling import ProfileReport
in jupyter lab on Ubuntu. Restarted my computer as well.
Any suggestions?Also, make sure that it’s using the pip  from your environment. For example, you could try something like this just to make sure.

> /YOUR_MINICONDA_PATH/miniconda3/envs/573/bin/pip install pandas-profiling

> Any idea why the conda way would not have worked in this case?
> Not entirely sure but sometimes the most recent builds are not available via `conda`.

- A little confused how linear regression gives us parabolas or other poly shapes - thought the point is it's always a line/a plane etc?
> Thanks for answering each other's questions. Here is an attempt to explain this again: Suppose our original data is $X$ and the transformed data with degree 2 is $Z$. We pass $Z$ to a linear model which will learn $v$ coefficients associated with all the features in $Z$. So the learned function is going to be a linear function of $Z$ but a polynomial function of $X$ because we have these quadratic features in the augmented data. So in the new space, the boundary is still linear but in the original space $X$ it's going to be non-linear.
> I remember you talking about the model complexity of a liner regression model, in 571. When we talk about model complexity which one of these are true:
y = a^3 *x + b^2+c
y = a*x^2 + b*x+ c
> What do you mean by "...which one of these are true"?
> I mean when talk about model complexity of a linear regression, are we talking about the complexity of the coef or are we talking about feature engineering that we learn today?
> Complexity of the "curve" our model learns. If it's smooth, it is less complex.

- I didn't understand the concept of polynomial transformation on categorical variables :
Lecture3 time 27:06 why are the false class -1 and 1 are there  three classes in targets? 
> at Lecture3 time 30:22  the features have values -5 and 5. How are we choosing these values. Aren't categorical variables just 0,1
> yeah, this is mostly applicable to numeric features. If you take polynomial degrees of one-hot encoded features, it's not really going to give you anything interesting as 1^2 = 1^3 = ... =1^1 = 1.
> Not sure whether I understand your question.
why are the false class -1 and 1 are there three classes in targets?
We just have two classes. The features can have any values.
> We have synthetic data with numeric features. True/False are class names.

- please share some good resources for learning more about the SVM algorithm.
> Something related to handling audio files as well. Thanks!
> his CPSC 340 material might be relevant which goes a bit more in depth on linear classifiers.
Linear classifiers slides and Mike's video (https://www.youtube.com/watch?v=GMEDGjpJycA&list=PLWmXHcz_53Q02ZLeAxigki1JZFfCO6M-b&index=19)
More Linear classifiers slides and Mike's video (https://www.youtube.com/watch?v=yw2AJZ491S0&list=PLWmXHcz_53Q02ZLeAxigki1JZFfCO6M-b&index=20)
Kernel trick slides and Mike's Panapto video (https://ubc.ca.panopto.com/Panopto/Pages/Viewer.aspx?id=22b67bbf-a86d-4a73-8e79-ad97012632c4)

- Re: the “norm” notation used in class, I think I understand now after 
@Utkarsh
 showed me the Euclidean norm as described at the following wiki page: https://en.wikipedia.org/wiki/Norm_(mathematics)#Absolute-value_norm Now I know what it is.  Basically it is the square root of the sum of all the squares.  Please correct me if I’m wrong.


- Since we didn't get a chance to go through T/F questions in class, let's do them here. Select the choices below:
- Sorry for the confusing notation in the lecture today. I've updated the notes with a (hopefully) clearer notation.
- can you give an example of a data set that should not be balanced?
> Spoke about this with Varada in lab. It's sort of a matter of what metrics / errors you care for. If you only care about accuracy, you probably don't need to rebalance. But if you're particularly hung up on, say, minimizing Type II error and the positive class is only 5% of your dataset, you will want to rebalance. IE you probably don't need to balance the "classifying happy moments" dataset, but should def be balancing any click-through type sets.


- At what point can we say the data does not have class imbalance problems ? In our labs, we are getting 15%~18% of target, and we saying that there is class imbalance. In real life however, this is the most optimistic situation. Generally, we have 5-8% of +ve class in target, getting a 50-50% split is very rare. So how do we say the data has class-imbalance or not?
> There's no strict threshold of what percentage can be used to declare imbalance in a dataset. It is mostly a judgement call, which will depend on your problem, your dataset (i.e. how large, how representative it is of the real world) and the methods you intend to use
> IMO: I don't think class imbalance itself is an issue. Your model can be so good to pick up all the minority class (difficult) or your data can be just so good. Then class imbalance is not going to be a problem. But again in reality I think you are right that it is rarely we get even split class. For statistician point of view, sampling are usually done in stratified sampling method and uses sample weights to help "handle" the class imbalance problem or to get a represented sample that present the target population well. In terms of model building for classification purposes, I think you can only conclude that the class imbalance is an issue when you realized your validation scores (accuracy, precision, recall f1 etc.) are bad then maybe you want to deal with. But I don't think you necessarily have to say there is a problem when you see class imbalance. (But I think except for those advanced ML algorithm, class imbalance will hurt you most of the time)
> There isn't really a rule of thumb, it depends on the domain and the problem at hand. One ratio that gets thrown around sometimes is if there is a ratio of 1:10 then there is severe class imbalance, but again that's not an absolute statement that can be generalized for all datasets

- For lab2 1.7 We have to use nltk package to extract two new features for we can  use  anything we want as new features?
> Use anything you want.
> how are the compound score calculated in Lab2q1.7 . Can we use the output from the polarity score in making new features?

- Lab2Q1.9 SOLVED I am having trouble with the offered syntax for get_feature_names_out. I tried googling, looked for an example in the Lectures, and tried stepping through suggestions, but wasnt able to figure it out. Did anyone else get it to work?
> what’s the output of your fe_pipe? I could get the features list in the same way
> I dont understand what you mean by output of fe_pipe. fe_pipe is a pipeline
> here is the declaring code:
> oh yes sorry the last file was what I meant. I was wondering if it’s not working due to transformers having different names but that’s exactly what I have too
> hmm i think it is this: This error happens when the model is not fit. transformers_ is created after the model is trained.
> i didnt fit it :laughing: and there was a hint and everything

- hey guys, is there a way to put countvectorizer on two or more columns, feeling lame doing them separately.

- lecture4 I think there is a typo in the lecture notes. The coefficient shown is for LotArea but what is being explained is LotFrontage.
> Quite confused . In the following lines we again refer to LotArea for checking the predictions .
> I guess you mean lecture 4? The notes are not finalized yet. I tend to work on the notes the day before :sweat_smile:
> Oh my I read the completely wrong notes :see_no_evil::joy: my bad . Sorry.


- lab 2, q1.6
When I run my code, I  get the following error, despite the code working just fine, it is alright?
Also, is it ok to get 'None' as the best class_weight result?
> I ran into this issue as well. As the error message suggests, it worked for me when I set max_iter argument of LogisticRegression  (to something like 1000 or 2000).
> I’m curious to know exactly why this is happening though. It seems to occur again if you increase the number of iterations in RandomSearchCV.
> same issue, any help?
> (Varada) It’s not an error; it’s a warning. As @Khalid is suggesting above, it’ll go away if you do something like below when you define your logistic regression object. LogisticRegression(max_iter=2000)
When you call fit  on LogisticRegression object, it’s going to run some iterative optimization algorithm. It’s complaining here that with the default number of iterations, it was unable to converge. By setting max_iter  we ask asking it run more iterations.

- lab2q1.7 any one with domain knowledge can shed some light on additional features to add :sweat_smile:?
> Do we need to extract the additional features, using functions  as it has been done for the first 3 features?
> Yes, please make functions just like the ones given
> We do not need add any new features I think. That is asking us to choose features from that new data set. Am I correct?>
> For q1.7, one of the tasks is to
Extract at least two more features that you think might be relevant for prediction and store them as new columns in the train and test sets. Briefly explain your intuition on why these features might help the prediction task.
so therefore, you must add two new features that are not yet present in the dataset
> Hi, is it okay for us to download other pre-trained models? or we should just use “vader_lexicon’” when adding features? From my understanding of this question, we are supposed to write two functions (similar to the ones in the question) , apply to the data and store outputs as additional columns to train_df right? Thanks! 
> You can use whichever pre-trained models you want for feature extraction, but make sure not to change the function that uses the Vader lexicon as that is required. And yes you are correct for what you need to do for the question. 

- hi team, the following line returns the top 10 alphabetically ordered features, how do we get the top 10 by occurrences or most important?
```
pipe_lr.named_steps["columntransformer"].named_transformers_["countvectorizer-1"].get_feature_names_out()[:10]
```

- lab2q1.6 When tuning the hyperparameters via RandomizedSearchCV I get the following warning message:
> /Users/kiranphaterpekar/opt/miniconda3/envs/573/lib/python3.9/site-packages/joblib/externals/loky/process_executor.py:702: UserWarning: A worker stopped while some jobs were given to the executor. This can be caused by a too short worker timeout or by a memory leak.
  warnings.warn(
Does anyone know if this warning message is preventable or what this warning message means?
> This seems to be due to the n_jobs. Have you set it to -1? If so, change it to the number of cores you have. This might/might not solve the issue. It could be for many reasons, like some of the jobs for some cores are finishing extremely slowly, or using more cores that are available, etc.
> Controlling n_jobs and cores are not that important here, as this is not a very big dataset and you computer probably don’t have more than a couple!
> I usually wouldn't use n_jobs = -1 unless I have lots of memory. Just set it to however cores you have, and if you still encounter issues then cut it to half of the cores you have

- SOLVED Lab2Q1.10 I think i have missed how we evaluate on the test set using different scoring metrics. we can't specify a scoring matrix to predict or score. How do we do that?
> There are some metrics defined in sklearn which you can use. For example I used sklearn.metrics.recall_score(y_true, y_pred, *, labels=None, pos_label=1, average='binary', sample_weight=None, zero_division='warn')
> hanks 
@Paniz
 really helpful. here is the link to the list. I couldnt figure out how to get the y_pred lol, so anyone else with trouble, y_pred = model.predict(X_test) will return an array of predictions you can submit to all these functions:
https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
> ooks like you could do it iteratively by passing the names to get_scorer() too:
get_scorer(scoring_metric[i])(X_test, y_test)

- Can we do hyperparameter optimization on more than one metric?
> You can show multiple metrics when performing CV (by inputting a list of metrics to the scoring parameter) but when you find the best model, you have to specify a specific metric

- Im trying to create a column on the aggregate of the train data. For ex. Highest occurring level in a categorical column on the whole train and then some transformation . But this breaks the golden rule between train and validation data . In that case do we have to only make features based on each row ? :thinking_face:

- Guys, can some one clarify. I have a basic doubt. While hyperparameter tuning, I have tuned the hyperparameter basis "f1", while scoring the test data set, using  " .score(X_test, y_test) " will the score correspond to "f1" or will it correspond to "accuracy". How can I get the score using "f1" or any other scoring metric?
> So the .score() function uses whatever you defined in the scoring parameter, so in this case it is the mape_scorer. If you do not define a scoring parameter, then it will use the model's default scoring method (which for Ridge Regression and Random Forest Regression is the coefficient of determination or R^2). It seems from your code, that the discrepancy is because for search.best_estimator_.score(X_test, y_test), you are training a Ridge Regression model with hyperparameter optimization, whereas where you call mape(y_predict, y_test), you are doing it on the output of a Random Forest Regression without hyperparameter optimization.
> If you're using multiple metrics for scoring, you must pass one of the metrics for the refit parameter, essentially telling the model which metric it should choose for selecting the best model
> It seems like you passed refit=True rather than something like refit='f1'assuming F1 score is one of the metrics you passed to scoring
> Taking this further, you will still only get one output from score() (which makes sense) and it is the output of what you set refit equal to. so if you want to report multiple scores you still need to use the functions 
@Paniz
 pointed out. get_scorer() was quite useful to iterate through the scoring_metrics easily, as i mentioned above.

- lab2 Q2 Not required on Q2, just curious, do we apply Standard Scaler BEFORE PolynomialFeatures in practice?
The MSE would go down as now the number now is <1, so after square it will be smaller.
However, it completely changed the relationships between features.. which kind of defeats the purpose of PolynomialFeatures.
I found some related discussion online.
https://datascience.stackexchange.com/questions/20525/should-i-standardize-first-or-generate-polynomials-first

- Very disappointed in my model which is not saying that cupcake is negative 100000 correlated with disaster tweets
> You should have added another character instead of trudeau. We are talking about predicting disaster here

- hi, did we discuss random noise in class 
> I guess you’re talking about Exercise 3.1 from lab. Adding random noise in this context just means adding some meaningless column in the data which we know is unlikely to be relevant for the prediction problem.
> np.random.randn(X_train.shape[0], 1)
I don’t think you need any additional reference material for that. You should be able to answer it based on what you know so far.

> I am not clear why would we add a random noise column to the dataset? 
> Does the random noise column aims to solve the overfitting issues of the model?  We can directly tune the regularization term of the ridge regression model so why bother to add a noise column? They are all l2-regularizationand seems redundant to me…
> We are creating a noise column just for that specific question. We’re not using it in the modeling later on. In this question, I want you to observe the non-zero coefficient associated with the noise feature and think about why the model might have assigned a non-zero coefficient to the feature even though we know that this feature can’t be useful.
> Would you say that adding random noise provides a way to find a threshold on the coefficients for feature selection?
> That’s a good point! Yeah, that might be a good idea.

- hi team is anyone receiving an error when calling n_features_
pipe_rfe_ridgecv.named_steps['rfecv'].n_features_ 
error:
AttributeError: 'RFECV' object has no attribute 'n_features_'
> Don't edit your question to just "resolved". This doesn't help your peers if they have the same question.

- countvectorizer If words have spaces between them like mass murder, Count vectorizer is creating features like mass and 20murder Would this not be an issue for the model?
> i mean it should focus on the latter ideally, no?
> So the presence of 20 in the feature is ignored? Would murder match with 20murder?
> 20 is like %20 which represents a space in html encoding :joy:
> Yes I got that but let’s say we train with words which have spaces in it and test on the individual words, how do we make sure the encoded space is not causing any issue
> Yeah, mass murder is a compound noun and your CountVectorizer  with unigrams won’t be aware of that. It’ll treat it as two separate words. It’s not expected in this assignment but if you want to do this properly, you might want to identify compounds in your text as a preprocessing step.
> murder and 20murder will be two different words for CountVectorizer .
>  I assume we can use ngrams to identify compounds. Is that correct?
> Yeah, you could but it’s not that straightforward because compounds don’t have to be just 2-word long. They could have more than 2 or 3 words. Then the question becomes what n-gram range do you want to use. If you use a large range, you’re kind of exploding your vocabulary. Also, you’re going to have a lot of sparsity in your data, as many ngrams occur very rarely.

> Woah thanks for explaining this! I didnt realise it would need special handling. I suppose for ‘keyword’ column, I can use ngram of 2 words straightforward though since it only has two words max

- lab2 Q3.3 and Q3.5 , should we put PolynomialFeatures() before StandardScaler() or after?
I thought it should be before, yet in Q3.5  it seems vise versa.
> standardizing them to [0,1] will make the polynomials smaller and will give smaller weights compared to the original features. So isn't it better to put it before scaling?
>  I would put it after. We use polynomial features so that we can use linear models and still capture non-linear shape of the data. By adding polynomial features of scaled features we’ll still be able to capture non-linear shape of the data.
@Macy Chan
 shared some Stack overflow answer that doing it before scaling is a good idea but I don’t think I entirely agree with it.
UPDATE: I need to think about this a bit more. I don't think there is one correct answer here. If you decide to do it before scaling, it will be a bit messy to include it in a pipeline if you are applying other preprocessing as well
>  I have some questions regarding PolynomialFeatures():
1.Can we apply PolynomialFeatures() on only selected features? or we should apply it on whole data? 2. if we assume we have a,b,c as features and we use degree=3  it will give us {a^3,ab^2,ac^2,b^3,ba^2,bc^2,c^3,ca^2,cb^2,abc} as new features?

> I tried both and scaler before would have a much better MSE in general Bz of the scale :dizzy_face:‍:dizzy: not sure how much that would hit the linearly feature, need some math ppl to answer
Btw,  @Mahsa for q1, she suggested to apply on all the features so that we won’t lost the interactions between features (edited) 

> if we want to apply on all features with degree = 2  then all features are squared and they all multiplied by other features, so in case we have n features, by applying polynomial n^2/2 new features. am I right
> https://stackoverflow.com/questions/51906274/cannot-understand-with-sklearns-polynomialfeatures/51906400#51906400

> The formula for calculating the number of the polynomial features is N(n,d)=C(n+d,d) where n is the number of the features, d is the degree of the polynomial, C is binomial coefficient(combination).
> What I did is I just fitted the model and see how many features I have in result :joy:

- lab2q3.1: anyone getting error in running the initial code block?
> It seems like you’ve still using X_train , y_train  from the previous exercise.
> Check if you changed any names of the variables/ ran previous cells.
The excise is using the same variables so it can be messy if we jump around.
I personally renamed all the X train and y train :joy: coz I like doing question back and forth 
> I noticed that the previous code block was crashing, so the values were not getting updated. Fixed now.

- lab 3 errors3.3
> ValueError: continuous is not supported 3.5
> AttributeError: 'SequentialFeatureSelector' object has no attribute 'predict'
> Are you trying to predict  on SequentialFeatureSelector ? If yes, you won’t be able to do that. You need something like RidgeCV() as the last step in your pipeline.

> See an example of using SequentialFeatureSelector  in the class notes.
> as per the class notes, i couldn't find a RidgeCV at the end of the pipeline
> Because we are using RandomForestRegressor . The point is you need some estimator at the end of the pipeline. 

- lecture 3
Since RFE/ other selection method is in the pipeline, do we do hyperparameter optimisation for
The model we picked for selection (e.g. Ridge, alpha)
The selection model itself (e.g. n_features_to_select)
> Yeah, that’s a good question. You could optimize hyperparameters of the model used to get feature importances but then you’ve to do it in each iteration of RFE. Personally, I wouldn’t worry too much about it, as default hyperparameters usually tend to work OK on many datasets. Also, you have to be careful about optimization bias. You don’t want to train too many models and overfit your validation set.
For n_features_to_select you could try hyperparameter optimization. Or you could just use RFECV.

- Does anyone know how to suppress ConvergenceWarning?
> you can try increasing the number of iterations for learning by increasing the max_iter  hyper param for your model
> In general, you don't want to just suppress warnings. They are there for a reason. As Nico suggested, you can try to increase max_iter, but usually if that doesn't work it means there is either something wrong with the model you've chosen or there is something wrong with the data. 

- From lecture 4,
> select_lr = SelectFromModel(
    Ridge(), threshold="median"
)
We use median as threshold, but let's say my coefficients are [-2,-1, 1, 2]  so it only chooses all the positive correlations aka. [1,2]? What about negative ones? Shouldn't the magnitude be used instead of numeric largeness, ie. it should be [-2,2]?

> Under the hood, sklearn will use the absolute value of coefficients. So in this case the coefficients will be [2, 1, 1, 2], with a median of 1.5 so only the first and last feature will be kept.

- lecture 3, general question I do not fully understand why feature f0 is 1, where did we get it from?
> Thats from the bias term. We make it into a dummy feature that always equal 1 so that its coefficient will equal the bias term.

- lecture 4, general question  Why 130 is an optimal number if we can opt for 90 or 100 with the same scores?
> Yeah, don’t take that number too seriously. I guess I should done this more systematically and found the number of features where we are getting the best r^2 score on the validation set.


- lab 2, q.3.3 A similar question was asked before:
When we add one more step to the pipeline with PolynomialFeatures(), how do we  choose the number of degrees?
> It defaults to deg=2. You can do hyperparam optimization and tinker like with any other step but you don’t have to for this lab.
> Yeah, you don’t have to do it for this lab. But if you want to do it you can define a hyperparameter grid where you can have hyperparameters for all transformers and estimators from your pipeline and you can jointly optimize all these hyperparameters using grid search or random search.

- lab2 q1.4 My model got a fit fail warning:
pipe_dc = make_pipeline(ct, DummyClassifier())
mean_std_cross_val_scores(pipe_dc, X_train, y_train, return_train_score=True, scoring = scoring_metrics)
Changing the pipe_dc into DummyClassifier() returns a scoring fail.
This is my column_transformer :
ct = make_column_transformer(
    (OneHotEncoder(handle_unknown="ignore", sparse=False), ["keyword"]),
    (CountVectorizer(stop_words="english"), ["text"]),
    ("drop", ["location"]), 
)
Need some suggestions here
> try (CountVectorizer(stop_words="english"), "text")
> If you happen to need to do it to several columns, you’ll need to do several vectorizers btw

- lab 2 q1.8
Struggling to make a column transformer applying countvectorizer() to multiple features, given that we cannot pass it a list. Right now, I just make two, but am not sure if it works as it's supposed to, or if there is a better way:
ct18 = make_column_transformer(
    (OneHotEncoder(), OHE_features),
    (CountVectorizer(max_features=10**5), 'word_types'),
    (CountVectorizer(max_features=10**5), 'word_stems'),
    (StandardScaler(), numeric_features)
)

> woah max features 10^5
> lmao yeah, that was what the hyperparameter opt gave out. definitely diminishing returns, but not a terrible train/score time given the small data set
> but to reiterate, the point of this question is how to apply CountVectorizer() to multiple text features simultaneously in a make_column_transformer code segment


- lab2q3.3 Is there any reference for PolynomialFeatures() ? I don't see anything in the notes , what does it do ?
>  you can refer to lecture notes 3. There is a section called Polynomial feature transformations 


- lecture 2 Sorry if I missed this in class or from the video, could someone remind me why these two scores are exactly the opposite? Thanks!
> The greater_is_better=False inside the self-defined scorer make_scorer(mape, greater_is_better=False) flips the sign so that we rank the scores with higher is better during CV.
Similarly for pre-defined scores, such as MSE, we use neg_mean_squared_error as the scoring and it also flips the sign to negative.
Reference of predefined ones: https://scikit-learn.org/stable/modules/model_evaluation.html (edited) 

> scikit-learnscikit-learn3.3. Metrics and scoring: quantifying the quality of predictions
There are 3 different APIs for evaluating the quality of a model’s predictions: Estimator score method: Estimators have a score method providing a default evaluation criterion for the problem they ...
> Ok just to confirm -- models with lower mape scores should be ranked higher? And that's why we would set the parameter greater_is_better to False so that it flips the scores to negative and we would get the lowest scores (as the highest negative actual scores)

- Are there any ways to write the plot created by ConfusionMatrixDisplay to png format?

- How do I access the param C of the logistic regression? Thank you!
> best_params_.get("logisticregression__C"),
> Actually, best_params of your search object is a dictionary. So you can just access it similar to how you access keys and values of a dictionary.  So something like below assuming that srch  is your grid search or random search object should work.
```srch.best_params_["logisticregression__C"]```


- Re: lab2 Q1.2, I’m trying to do some EDA on location.  I’m running into a strange problem with histogram.  My code:
```
location_plot = alt.Chart(train_df[train_df['location'].notna()]).mark_bar(opacity=0.5).encode(
    alt.Y('location:N', bin=alt.Bin(maxbins=200)),
    alt.X('count()'),
    color='target:N'
)
location_plot
```

And the plot looks like the image here.
I don’t know why they look like numbers…
You might wonder why I have the maxbins there.  The reason is that I will get something even more weird that I will get a blank output if it is not there.
I’m trying to visualize how location will be different depending on the target.


- between RFE and backward selection, is backwards selection computationally intensive, as it pairs one variable with other and then grows. Can this be one of the other difference?
> Yes, that’s correct. It’s going to be more computationally intensive.
> Is it fair to also say that the approach taken to select the feature to eliminate per iteration is slightly different, since one relies on the CV score and the other relies on feature importance ranking? I’m asking because some online sources seem to say it’s almost the same… https://stats.stackexchange.com/questions/450518/rfe-vs-backward-elimination-is-there-a-difference
> I don’t think the answer in this post is accurate. Like you’re saying above, they are different in the sense that RFE takes into account feature importances and backward selection doesn’t.
In each iteration RFE trains a model which provides feature importances and removes the least important feature (feature associated with a coefficient with smallest magnitude).
In each iteration, backward selection removes a feature which maximizes cross-validation score when removed from the feature set. So in each iteration, it’ll try removing each feature from the current subset and examine removing which one gives you the best cross-validation scores. So you train many more models here compared to RFE. In backward selection, when the iteration going from m features to m - 1 features using k-fold cross-validation requires fitting m * k models, while RFE would require only a single fit.
> Hi, I have a related question to RFE.  The lecture notes specify that RFE iteratively removes the least important features one by one with this note:
Note: not the same as removing all the less important features in one shot
Is this note just to clarify that the process of removal is one by one? Would the end product of removing all the least important features be the same?

- Can't use .fit(X_train) . How should I fix it?

- 1.6 How do I fix it? I am not sure what I missed? Any help would be thankful!
> There is no column transformer in your pipeline object, but you’re referencing it in your param grid. If you remove that, it should work?
> It is still not working. 
> Your pipeline has the countvectorizer followed by the logistic regression model, therefore, the name of max features parameter in the parameter grid should be `countvectorizer__max_features`. If this doesn't work then you will need to add a column transformer with a countvectorizer and then pass this column transformer to your pipeline. Your parameter grid should then work. 
> I changed the countvectorizer__max_features, and it still not work. :smiling_face_with_tear: Error message
> How did you define your X_train and y_train? Seems to me they are not of the same length as per the error.
> same issue. :smiling_face_with_tear: i used train_df and drop().


- lab2q1.9 The question asks for Most important features .Does that mean an absolute coefficient value or just the highest positive coefficients ?
> I used the absolute value, it’s also in the lecture notes. For example, in the case of predicting house prices, a large negative coefficient on the age predictor is important. In my understanding, important != positive weight
> (Varada) We decide importance of a feature based on how much impact they are going have on the prediction. Bigger magnitude of a coefficient means the feature is going to have a bigger impact on the prediction.

- Re: Lab2 Q3.2, may I presume that I should use X_train_noise instead of X_train as a continuation from Q3.1?
> Or may be the noise part only for Lab2 q3.1
> Please do not use X_train_noise for questions after 3.1. It's only for 3.1. Use X_train  for 3.2, 3.3, 3.4, and 3.5.
> Thanks for your reply, but I have less than 3 minutes before the deadline
>  did try to use X_train before.  The results were not very different.  And the noise feature got removed by RFE.
> It shouldn’t make a huge difference. It’s a good sign that RFE removed it!


- is there  anyone cannot run their 1.7 as well？
> vader_lexicon and punkt is pulled from some github page https://github.com/cjhutto/vaderSentiment. So nothing working beyond Q1.7 of Lab 2
> Worst case you can exclude this particular feature from your pipeline. So you can comment the following lines. Excluding this feature should not affect the later questions.
```
train_df = train_df.assign(vader_sentiment=train_df["text"].apply(get_sentiment))
test_df = test_df.assign(vader_sentiment=test_df["text"].apply(get_sentiment))
```
> I just tried running this cell and it seems like it’s able to download things without problem.
```
import nltk

nltk.download("vader_lexicon")
nltk.download("punkt")
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
```
That said, if you facing issues because Github is down (which is not your fault), as I said above, you can comment out the two lines and skip extracted sentiment features. And I’ll make sure you won’t be penalized for this.

- Lecture 4  Whether it is True or False? The order of features removed given by rfe.ranking_ is the same as the order of original feature importance given by the model. I didn't find the answer in the updated lecture note.
> Oops. Forgot to push my answer for this question. What do you think? Do you think it’s True or False?
> I think it is False because RFE fit a new model at each iteration. Therefore, every time when we remove a feature, the coefficients may be totally different because some features may be correlated and removing one feature may change the coefficients of other features greately.
> Exactly!! In the statement above we are kind of saying that the feature ranking given by model based selection with an estimator is going to be the same as the ranking given by RFE with the same estimator. If that were the case, we would not even bother to do it iteratively, right?

- lecture3 can you elaborate on how this is a XOR-like problem? Screenshot in the thread.
> Imagine this toy sentiment analysis task where you only have three simplistic presence/absence features: good, bad, and not. The word good is indicative of positive sentiment and bad is indicative of -ve sentiment but in the presence of not the categorization flips, as shown in the picture below. Can you draw a linear decision boundary to separate positive and negative classes here?
> Yeah, that works too. My picture above is assuming the three words as three separate features (which is usually the case with bag-of-words representation) and so I have three axes.

- Question 1 : Can the AUC be less that 0.5 (in a binary classification case). Do we look at AUC if the problem is multiclass classification? What is the best metric to track in case of multi-class classification?
> Usually AUC is in the range 0.5 to 1.0. AUC for DummyClassifier is 0.5. (That said, it can be smaller that 0.5  which means that it’s worse than DummyClassifier .) Usually, ROC AUC is used in binary classification. You can extend it to multi-class classification. See here. I would probably go with macro-average or weighted average f-1 score for multi-class classification.
- Question 2: Relating class_weight and ROC curves, following question:
> It depends whether you want to maximise precision or recall.
> Hang on… I think you have to first identify the importance of using ROC and AUC.
ROC is used to help us determine which is the best threshold for our model.
and AUC, when used to compare between different models helps us determine which model is better.
In this case, if you want to determine which is better: class_weight ‘balanced’ or ‘none’, you might be better off using a score method at a given threshold instead
So whatever I said above, this is dependent on which threshold you want, but it is hard to determine with an ROC curve
> perhaps someone else can chime in too

- lecture1 To get probability scores (for SVC here, but in general, any other classifier) instead of getting hard predictions, do we need to use:
```
pipe_svc = make_pipeline(..., SVC())
``
or
```
pipe_svc = make_pipeline(..., SVC(probability=True))
```
In lab, when I used the former, I got an error, so I had to use the latter. But in the lecture notes, the former one is used. Confused.
> For logistic regression we can get prediction probabilities and we exactly know how to get these uncertainty estimates. For SVC there is something called decision function which gives us uncertainty estimates (decision_function method of the classifier object in sklearn ). If you see carefully, I’ve been using that in the lecture notes. You may pass probability=True to be able to use predict_proba  but be careful about it. See the following in the documentation.
will slow down that method as it internally uses 5-fold cross-validation, and predict_proba may be inconsistent with predict. Read more in the User Guide.

> I would probably use decision_function  method instead of passing probability=True .

> Ah! I see, I missed how you used decision_function in case of SVC. Thanks for the clarification, much helpful!
> follow up : is decision_function  for all the models? and how is it different from predict_proba ?
> In sklearn  you can use two methods to get uncertainty estimates: predict_proba  and decision_function . Most classifiers have at least one of them and some classifiers have both of them. You can think of decision function as raw score given by the model. So decision function output doesn’t have to be in the range 0 to 1. You can read more about it in the following book:
Introduction to Machine Learning with Python

- Lecture2T/F. A lower RMSE value indicates a better model. Answer give is "True".
But isn't it subjective? In some cases we care more about relative %error(MAPE)
> Yeah, the question assumes that we are comparing a lower RMSE to a higher RMSE and not different metrics. Probably a more clearer statement would have been:
A lower RMSE value compared to a higher RMSE value indicates a better model.

- lecture1 can someone explain what is happening in this code? precision_lr, recall_lr, thresholds_lr = precision_recall_curve(
    y_valid, pipe_lr.predict_proba(X_valid)[:, 1]
)
where, pipe_lr = make_pipeline(StandardScaler(), LogisticRegression()). My question is the predict_proba() gives probabilities for both classes. In this case, (1) how is precision and recall calculated, (2) which threshold values are considered by the precision_recall_curve() function?
> We are using precision_recall_curve function of sklearn  to get precision and recall for different thresholds. Since it calculates precision recall for different thresholds, we need to pass predict_proba  output of the positive class here. That's why I'm passing predict_proba(X_valid)[:, 1].
How does it know what threshold values to consider? See this in the documentation. It considers all unique predict_proba  values as thresholds.
Increasing thresholds on the decision function used to compute precision and recall. n_thresholds <= len(np.unique(probas_pred)).

- lecture 1 Adding to the question asked by, what are we calculating using this?
 close_default_lr = np.argmin(np.abs(thresholds_lr - 0.5))
> The smallest absolute difference between thresholds_lr and 0.5 will be 0.
 np.argmin finds the index of this smallest absolute difference in thresholds_lr, and we are interested in that index because this will correspond to the default value of the threshold, 0.5.
 If I remember right, later in the code it searches through the precision_lr and the recall_lr arrays for this index and returns the values, which are the precision and recall that correspond to the default threshold
 > Basically, we are getting this info to plot the red dot corresponding to the default threshold in the precision-recall curve.


- wish we would say "grow a tree" rather than "build a tree"
> Even better, “grow a forest”.
> Randomly

- Re: Lecture5, what is the best-practice max_depth of the trees when doing random forest?  Or we control that with n_estimators and don’t care about max_depth any more?
Say that if when using decision tree, the best max_depth is 10, would it be a best practice to keep the depth of the trees in random forest, say, 5?
> Usually random forests grow full deep trees with max_depth=None . In gradient boosted trees, we build shallow trees.

- Re: Lecture5, stacking is like a “lie detector” of the models…:lying_face:  We can actually distrust a model because of that.  Interesting.
> Yeah. Also, one point I missed mentioning is that stacking is like weighted averaging. In averaging, we give equal weight to all models. But we know that some models are more trustworthy than others. So in stacking we train a meta ML model to learn how much weight we should give to each model.

- isn't "stacking" the basis for CNN? (convolutional neural networks)
> Kind of. You can also create stacked CNNs. You'll learn about CNNs in DSCI 572.

- just asked whether there are any practice questions for the topics we are covering in 573 in our online course. You'll find some practice questions on classification and regression metrics here. But we covered things in more depth on these topics in 573 compared to this online course. For example, PR curves and ROC curves are not covered here. Regarding feature engineering and feature selection, unfortunately, these topics are not covered in this online course.

- lab3 Q3.4 part3 The question asks if we can tell the direction of prediction using the feature importances. I did not understand this question very well. The prediction task here is regression not classification. How can regression predictions have directions?
> Yes. They do have a direction. In the Spotify song popularity dataset, for example, if a feature has a negative coefficient, it means that increasing the value of that feature will make the popularity small

- Do we know which model is generating this output?
> use verbose=0 and verbosity=0 in catboost and xgbRegressor respectively, that wont print this output

- lab3ex1 Shouldn't we be adding categorical and text features to our drop features when we are building preprocessor_num_bin? or instead, not include ("drop", drop_features) term so that it drops everything remaining.
> Yeah, I guess that would have been another way to do it. But if we don't include features in a column transformer, they are not going to be included anyway. So it should be fine.
> Interesting. Even if we already have specified "drop" features? 
> Yeah, it won't include the features if they are not in the column transformer even when we have specified drop features. There is an argument remainder which is set to "drop" by default.

- lecture4 when we perform feature selection on encoded categorical features, the issue with the selector dropping one of the encoded features is mentioned in the lecture. However, to what extent is this an issue? Could it be interpreted as that particular category does not improve the predictive power of the model and thus can be ignored - can this category be ignored during scoring on the test set?
> I see the issue with drop first
> Yeah, I would say this is a matter of opinion. Some people believe that it's not that bad to get rid of not-so-useful categories. Other believe that feature selection is the problem of selecting features from the original set of features. But let me think a bit more about this.  Probably, this might cause some problem during deployment time?

- how can we over use our validation set?
> my interpretation is, if you keep using the same dataset to train different models and tuning different hyperparameters, you will have higher chance that you got lucky and have a higher score. That is not the optimal model/ hyperparameters even it has the best validation score.
Since we are trying different models combinations and and methods..

- I was just wondering what the intercept represents intuitively after fitting the StackingRegressor? Like the coefficients of the models represent how much meta model trusts the estimator models , but what does the intercept represent intuitively? (
 > When all the models predict 0 , the default .
Or can we just consider it to be the error term irrespective of the model predictions ?
> I guess it’s more of an offset value rather than error
> I would also say this is more of an offset value. Note that most of our learned coefficients are positive. The feature values, i.e., predict_proba output is also going to be positive for the models we are using. So you might wonder how you do you predict negative class with logistic regression. Intercept would play a role there.

- Hi I wonder what we should run first before this display_tree… seems there’s no package named display_tree, nor did i found any function defining it either…

- The order of standard scaler and polynomial in a pipeline affects the model. Are there scenarios for choosing each order for a problem? I chose scaling after polynomial for 3.5 in lab2 because it made sense to scale the squared numeric features but the solution chose the other order- polynomial after scaling . What could be the reason(s)?
> i guess it makes sense that we dont scale to find non linear relationships and thus choose to add degrees later
> standard scaler would scale the values down to the range (-1, 1). Applying polynomial features on top of this would always give values in the range (0, 1) or (-1, 0) depending on even or odd levels of the degree p
If you do the other way round, you first compute all the polynomial features and scale them all. 
> Min-max scaler transforms to ranges to -1 to 1
> not sure how choosing min-max scaler over standard scaler affects our decision. I thought choosing any scaling after polynomial degree addition is going to negate our intention of finding non linear relationship
> Here is the intuition:
Applying polynomial features only make sense if your current state data follow a polynomial shape (when you plot them for example) and you want to create features to model the polynomial behaviour. In a sense this is the last step in your preprocessing.
standard scaler brings all data points to a ~Normal(0,1) distribution. (min-max on the other hand brings it to (-1,1) range if we have negative values too). Now if you apply standard scaler on your polynomial features (which presumably models your data well), you will skew the whole column to a normal distribution which will defeat the whole purpose of applying polynomial features in the first place.
> Basically, what we are saying is "let's bring our data to a reasonable range, and then see if we can fit a polynomial line through it or not".
> Good discussion. I'm not entirely sure about this and I need to think a bit more. Some problems I see with doing it before scaling are:
If a feature has a large scale, bigger polynomial features can explode.
It'll be tricky to incorporate it in a pipeline and carry out cross-validation etc if we have other non-numeric features in the dataset. 

- is there any difference between forward and backward selection? apart from the fact that on grows, while the  other shrinks? The final number of features for a given set of data by either method should be same....isnt it?


- Re: practice_quiz1 Q3 (about degree of the polynomial and the fundamental trade-off), would the following answer be acceptable too? The features becomes more complicated as $p$ goes up so that the scores may be higher, but the risk of overfitting is also higher.

> I would explicitly mention that the training scores are likely to be higher but the gap between validation and training scores is likely to get bigger, i.e., the risk of overfitting is higher.

- Lecture 5
Inspired by what we did on feature selections and those ROC AUC things..
When we are doing Averaging/ Stacking,
Do we do crazy things like, have something functions to auto pick difference combination of models
Do we give different thresholds to our models? (I think this one is less likely, because it sounds a very high chance to overfit if we do this)
> Sure. If you've a powerful machine and lots of time you can try that.
I've seen people doing this.
I've not really seen people doing this.
But you have to be careful about optimization bias. You don't want to try too many things.

- Re: practice_quiz1 Q5, while I understand that it is looking for a very simple answer, but for the purpose of learning, may I confirm that exhaustive search has a run-time complexity of O(2^d) iterations (where each iteration is actually an n-fold CV) and it obviously will NOT scale well, and Forward selection is more efficient with run-time complexity of O(d^2) iterations?

- practice quiz 4 : does "largest regression weights" include large negative weights?
> I am going to rewatch Lecture3 just in case I missed something. I don’t recall any knowledge being covered in lecture which would enable me to answer Q4 like that.
> This scenario is similar to model-based feature selection. Here we are training a linear regression model and only keep features with coefficients which have bigger magnitude (compared to a threshold). The point is that if we do that we are going to miss some subtleties.
For example, if you delete f1 and f2 because both of them have coefficients whose magnitude is smaller than the threshold. But if you had trained the model without f1 it would have been possible that f2 had a bigger coefficient. That's why we tried something like RFE or forward/backward selection, where we try to do feature selection iteratively. Again, these methods are not perfect but better than model based selection. 
Also, when we are discarding features using this method, we are assuming that the relationship between features and targets is linear, which might not be the case.
Overall feature selection is a messy problem
> I suppose it’s the absolute value of the coefficients/weights that are factored in during the selection criteria and not the actual values? Else a highly negative value will get dropped even though it is strongly (but negatively) associated with our target?
> Yes, we consider magnitude of the coefficients/feature importances during model-based selection.

- A general question regarding linear regression: If our predicted value is less than the observed value, are we under-predicting?
> Yes, if the predicted value is smaller than the target value, we are under-predicting for that example.

- Even theoretically, is a perfect predicative model possible? As there will always be FN and FP, and we can never get them both to be zero. Right? 
> Perfect in terms of what? Defining “perfect” in this context (or any other context) is very hard, considering a variety of ways available to evaluate and assess a model. We have different evaluation metrics. Even if you decide to stick to one metric, if you get a perfect training score (perfect fit), it’s not necessarily going to generalize well on CV, test, and deployment data. If you have perfect train and CV scores, there is a possibility of optimization bias and the model might not generalize well on test data and deployment data. Even if you manage to get great performance on train, CV, test, deployment, it might be harmful for well being of humans because of some implicit biases encoded in the model etc. If I get perfect scores, I would actually be suspicious about my evaluation method or the thing the model is trying to learn. 

- How can we decide whether for a given problem statement we should use consider AP score or AUC score?
> I would generally look at both. If you have severe class imbalance, AP score tends to be more informative. I’ve linked a paper in the lecture notes on this.

- In forward/ backward selection of features, how do we determine the first feature to be selected/ removed?
> In forward selected it is based on the model cross validation score created with that individual feature. ( If error is your scoring function , then minimum )
Not sure on backward selection.
> I guess, the question is which is the first feature being tested? Or, is it that all the features are tested individually and the one with highest individual feature is picked, and then that is checked against all other features?
What if two features become important when combined? are we missing those in this method?
> Or, is it that all the features are tested individually and the one with highest individual feature is picked, and then that is checked against all other features? Yes .What if two features become important when combined? are we missing those in this method? Yes , you can check out 
> In Forward method , If we start off by making a model on a single feature and so on . How is multicollinearity or interaction between variables handled ?
@Chris
 Yeah, this is a drawback of greedy methods like forward/backward selection where we are "greedily" or locally making decisions on which feature should be discarded. It might happen that you get rid of a feature based on current CV scores but it can become very important in the presence of some other feature which is not already in the subset. In general, the search problem here is intractable because the search space grows quite quickly. (With 100 features you have 2^100 different feature combinations to try!!) So we try out best and use approximate methods which give us good enough solutions.
 
- Lecture 1 note Why are the confusion matrix generated from predict and the one from cross_val_predict different? Which one is better in general?
> They are different because the former doesn't use cross-validation and latter is based on cross-validation. See the documentation for the details on how it's exactly calculated from cross-validation.

- Sending a reminder about our quiz at 2pm today. If you have questions and you are not in my room, please DM me on Slack. I'll check my Slack every now and then. If you have submitted a remote quiz form but haven't told me about it on Slack, please DM me soon so that I can schedule a Slack message to send you the access code at 2pm. Good luck!! 

- Lab3 I am having a little trouble interpreting mape; does this score mean the is within 1.34x whatever the predicted value was on average?
> It means on average your predicted value is -134.741% off the true values or  (1+-1.34741~ -0.34741x) on average in terms of index (check calculation).
Hence it is not within the true value on average, I think it indicates it has under estimated the true value by 134.7% on average. (check calculation)
But this may sounded like the model's been "under" predicting the true values on average since MAPE is the mean absolute percentage error, but there would be still a case of extreme outliers that could tilted this scores. Since your std is +/- 7.946%.
The true vs predicted plot can help you understand how the model perform in different ranges of the true value. (under estimated / over estimated) 
> Thanks Steven, thats what i suspected. surprising it is so far off, but i guess when values are low it isnt so surprising.
> It is an average, check the high tail and low tail of the true value (i.e. true vs predicted)
> I think for my model the high popularity values has been consistently under estimated and although happens in low end too, but since underestimating on higher value leads to a greater average negative errors since over estimating on lower value is still lower...(unless the model is real off)
> yea if you think about it it's not that hard for it to happen. If true popularity song value is 2 and you say 5, you are off by 150%. Maybe not the best metric for our case

- Lab 3 2.7 I can't seem to get the coefficients from my Stacked Regressor pipeline. when i try this:
```
sr_pipe.named_steps['stackingregressor'].final_estimator.coef_.flatten()
```
I get this:
'Ridge' object has no attribute 'coef_'
I have run fit on the sr_pipe

> Update - the mistake i was making was not building preprocessors into the models dictionary. This is how it is done in the lecture.

- Shouldn’t feature importances of encoded features be summed up to evaluate the feature importance of the original feature?
> You mean for a categorical feature, for instance, feature importance of the feature should be summation of the feature importances for OHE features?
> Once you apply OHE, they are kind of treated as individual features. When we train a model it does not have any knowledge about how they were created or whether are actually different categories of the same feature.
> So if we train a linear model each encoded feature is going to have its own personal coefficient.
> Yes, but I think the sum provides us with useful information when we compare features.

- Create a stacking model using sklearn's StackingRegressor with the estimators from exercise 2.3, and Ridge as the final estimator. Default estimator is RidgeCV() - we can leave it as default

- Lab3 2.6 Also regarding stacking models: When you use a final model (say, ridge) as an aggregator, do you have to remove it from the stack or is it advised to leave it in?
> Those steps are completely different. Your base estimators in your model, are trained using your data, but the final estimator is trained on the predictions of those base estimators. So, you may or may not include your final estimator in your base estimators (Here, include it). See this as an example: https://scikit-learn.org/stable/modules/ensemble.html#stacking

- Catboost python library is not compatible with M1 Macs currently, is it ok if we do not include it in Lab#3?
> It's fine I guess. Put a comment and mention that you couldn't install/import the library

- lab3 q2.6  Any ideas of why I am getting this error and how I might fix so? My models.keys() are dict_keys(['Ridge', 'RandomForestRegressor', 'XGBRegressor', 'LightGBMRegressor', 'CatBoostRegressor']) ;
> you can leave it empty because default estimator is Ridge
> that seems to not work by taking out the final_estimator =Ridge()  argument; actually I noticed I named my ridge pipeline to be Ridge  I guess I shouldn't use any of key words to name; by renaming this error is not occurred any more.
> Nice. Additionally, Daniel explained later, it's good to pass it explicitly because (1) it will avoid performing CV which we don't need for our purposes here and (2) we will need to select different final_estimator values later on.

- lab3q3.1
 Last week we said that with better features we can get by with simple and more interpretable models. Are you observing it here?
But in our case here , we are adding more features in preprocessor_all . Adding more features does not mean simple and more interpretable models right ? Can anyone explain what this statement means ? As per my understanding last week we learnt how to add features therefore improving model complexity with respect to interpretability .
> The new features you are adding may be better and more influential, which seems to be happening in ex 3. Seems like perhaps in particular some categorical features are good for predicting. So we are being asked to compare scores we get on some simpler models with the use of categorical etc features vs the scores we get on complex models (like ensembles) with only numeric and binary features.
> he point is we have a better representation of the problem we are trying to solve and with that a linear model performs the best. So in this case, with better representation, we can get by with simpler and more interpretable models.
> For some weird reason , I am not sure if I did anything wrong but my best model is a RandomForest with all features. Ridge isn't far from RandomForest thou.
Are we trying to say - With better features we do not really have to make ensemble models and the scores can still improve with a simpler model ? Because the ridge score has improved drastically when adding more features.
> Because the ridge score has improved drastically when adding more features.
That's precisely the point. When you're making a prediction you use a model and some features. If the predictions are bad, you can either improve the model or improve the features (doing both is cool too).
The point of this exercise is just to see how changing only the features can improve predictions even without migrating to a more complicated model.

- lab3q2.3 I got these outputs. How do I hide them?
> most models have verbosity parameter. I think this one is due to lgmregressor, try passing it verbose=-1. XGboost takes verbosity=0

- in lab3q3.5, looks like there are many hyperparameters we could optimize. Should we pick a few?
> Yes, pick a few important once. (It's also fine if you go crazy with it. I know you enjoy hyperparameter optimization :grinning:.)

- so number 3 T/F is the false one?
> My answers for the T/F on random forests. I'll update the notebook later this week with my answers.
T
F
T
F
T

- 

- appreciation post: thank you very much for the step by step with pen and paper 

- There is another open source tool called FACET for model interpretability (Developed by BCG GAMMA).
Github: https://github.com/BCG-Gamma/facet
https://medium.com/bcggamma/gamma-facet-a-new-approach-for-universal-explanations-of-machine-learning-models-b566877e7812
https://www.bcg.com/press/12january2021-facet-open-source-library-for-human-explainable-artificial-intelligence

- If you already wrote the notebook that you said you replaced with regularization, can we have access to it as well?


-  I have few follow up questions from lecture 5
Shall we always make more and more trees for RandomForest, even though we are not getting better score? Wouldnt that give us an even complex model. And how do we select at which point should we stop.
For stacking: Do we need to select all the models? Like if DT is being given a -ve weight, why not to remove it and then again build LR on the rest of the models? Also, given that we are using RandomForest and Gradient models, do we need DT??
I feel lecture5  was the most powerful lecture thus far, and you have explained the concept beautifully. I could relate so much to it with my past work experience and this lecture have clarified so many of my long term doubts.
> Yes, for random forests more trees are always better. Like we saw in class, for random forests with more number of trees, the training score goes up but the gap between train and validation doesn’t really increase and there is still a possibility of better validation scores. Usually you make decisions on the number of trees based on your budget. Interpretability can also play a role here. But I think interpreting 1000 trees vs 2000 trees both are going to be difficult if you want to manually visualize the trees. It’s likely that you’ll be using tools such as eli5 or SHAP for this and in that case it won’t matter much how many tree you have.
No. We don’t have to. Like you said, I would get rid of the decision tree model. I included it just because I thought that the negative coefficient of decision trees was kind of funny :slightly_smiling_face:.
Thanks for your kind words! I’m glad to hear this :slightly_smiling_face:.

- Today Varada talked about interpretability of the models.  Here is an example of that Amazon apparently lets algorithms make all kinds of decisions and the issues caused by doing that:  https://www.bloomberg.com/news/features/2021-06-28/fired-by-bot-amazon-turns-to-machine-managers-and-workers-are-losing-out

- I am wondering what the higher and lower SHAP values for each feature in the summary plot represent for regression problems.
> In the plot we see that higher values for OverallQual have bigger SHAP values, which means that bigger values for this feature are going to push the predictions to a bigger number whereas smaller values for OverallQual are going to push the predictions to a smaller number.

- lab3q3.3
hi team, burned an hour, would appreciate any guidance on the following:
when we fit a ridge pipe
pipe_ridge.fit(X_train, y_train)
and then predict
pipe_ridge.predict(X_train)
and then try to get the feature names
pipe_ridge.named_steps['columntransformer'].feature_names_in_
and then try to flatten their coefficients
pipe_ridge.named_steps['ridge'].coef_.flatten()
the feature names are longer than the previous because our one hot encoder created more columns so now passing index=feature_names into a new data frame with data as the importance coefficients doesn't match
ValueError: Shape of passed values is (153, 1), indices imply (17, 1)

- lab3q4.3 Hi folks, I think we found a bug in this question. I believe that this code:
```
shap.force_plot(
    lgbm_explainer.expected_value,
    test_lgbm_shap_values[8],
    X_test_enc.loc[8, :],
    matplotlib=True,
)
```
should be changed to this
```
shap.force_plot(
    lgbm_explainer.expected_value,
    test_lgbm_shap_values[8],
    X_test_enc.iloc[8, :],  # note iloc instead of loc
    matplotlib=True,
)
```
Can someone please confirm that this is a bug? If not, can someone explain why it should be loc instead of iloc?

> It should be iloc because we are using test_lgbm_shap_values[8].

- lab3q2.2 max_depth for DT is not mentioned? Shall we use 3?
> Use the default values.

- lab 3, Q 2.3   Error: name 'XGBRegressor' is not defined
any help is welcome


- Lab3,Q2.3  I am having doubt in selecting the best model. The difference between train and test state is very huge in all of them. Or we should look at test score (if yes: which metric) ?? Also shall we consider DT in the answer or we have to chose only among the 5 listed models
> Use your judgement and argue your case based on all the things you have learned so far. The point is that usually there is not going to be a single model that’s going to be the best one. Each model is going to have its pros and cons and I want you to learn to be aware of these pros and cons and limitations of each model and pick the model which suits your needs. In the context of lab assignments, we don’t really know the context where the system is going to be used. So in such cases, the expectation is that you compare and contrast different aspects such as overfitting, fit/score times, different scores, and make your best judgement and provide proper justification.

- Lab3 4.3 It seems that the true popularity value is totally different from the predictions. Don't understand why:smiling_face_with_tear:
> Try .iloc[8]

- For people looking for a more in depth explanation of the workings of tree based models like random forests, gradient boosting and XGBoost do check out this book, especially chapters 3, 4 and 5: https://learning.oreilly.com/library/view/hands-on-gradient-boosting/9781839218354/
P.S: Oreilly gives a free 10 day trial without CC info and that’s how I read it! :)

- Hi! I got a problem to run shap. Does anybody here know how to solve it?

```pip install jupyterlab install -i https://pypi.anaconda.org/numba/label/linux_python37_numpy_117/simple numba 
```

- Hi I have a question about the raw score & shapely value in the lecture notes: why we are comparing the raw model score with the base value? I thought the base value is just the average of the total population and since we have a class imbalance here, the average doesn't represent anything. I feel like this raw score should compare to 0 and get the prediction >50K?
> Good point 
@Rong Li
. You are right that for the overall prediction of the model we should be comparing the raw score with 0, if we are looking at decision function output or 0.5 if we are looking at predict_proba. (I think I should word the explanation a bit differently in the notes.) The base value is the mean of raw score (decision function output or predict_proba output; see below). In our case, since there is class imbalance the mean of raw scores is negative. From my understanding, the intuition here is that we have this base value as a reference point (which will have opposite signs for two classes in binary classification BTW, as shown below) and we have a prediction and we want to explain the prediction with reference to this reference point. That is, this base value is the raw score on average, and we want to figure out what’s different with this particular example which makes it lower or higher than this base value.
pipe_lgbm.named_steps["lgbmclassifier"].predict(X_train_enc, raw_score=True).mean()
-2.316317251007937

lgbm_explainer.expected_value[1]
-2.3163172510079377

lgbm_explainer.expected_value[0]
2.3163172510079377
In fact, if you look at an example where the raw score is < 0 (e.g., -0.196 < 1) but > base value (-0.196 > -2.316), we will get this hard prediction of <=50K. SHAP will kind of provide us some more fine grained information that although this the hard prediction is <=50, it’s bigger than this average value and this is the contribution of each feature to this raw prediction.
pipe_lgbm.named_steps["lgbmclassifier"].predict(X_train_enc, raw_score=True)[2]

-0.1961822

pipe_lgbm.named_steps["lgbmclassifier"].predict(X_train_enc)[2]
'<=50K'


- Good morning, for Lab3 Ex4, I am getting the error from running the codes that are already set up prior to answering the questions
pipe_lgbm_all.fit(X_train, y_train);

- When plotting this force plot, the feature names get squished together. Does anyone have a solution to this? I'm not having this issue with the second plot, just the first one.
> Yeah, this is tricky 
@Kiran Phaterpekar
. In force plot documentation it doesn’t look like SHAP provides an argument which lets us control how many features we want to see in the plot. For this assignment you don’t have to do it. But if it’s bothering you, some options would be:
Pass shorter versions of feature names as feature_names to shap.force_plot :
Rounding numeric values, which we are already doing in the code. 

- Hi Varada, thank you for you and the TAs' work! I have a question about Question 9 and hope you may solve my confusion.:pray: I agree that the order of numeric_features and ordinal_features is wrong, but I think it is also wrong to pass ordinal_features directly into the feature_names. ordinal_features only has 1 column article_size , but this 1 ordinal feature will be transformed into 3 columns (long , mediumand short) after preprocessing. Therefore, the final coefficient table should have 5 rows, not 3 rows. It doesn't make sense to put a feature_names  list with 3 column names with a coefficient list of 5 coefficients.
> What’s the difference between ordinal encoding and one-hot encoding? When you apply ordinal encoding to the article_size column, is it going to create a separate column for each category? I suggest that you create some dummy data and try out this code on it on your own.

```
import pandas as pd

from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.pipeline import Pipeline, make_pipeline

data = {'avg_word_len': [5, 3, 4], 
       'n_comments': [10, 2, 0],
       'article_size': ['medium', 'short', 'long'],
        'target': [10, 0, 3]
       }

df = pd.DataFrame(data)

X = df.drop(columns=['target'])
y = df['target']

numeric_features=["avg_word_len", "n_comments"]
ordinal_features = ["article_size"]
size_ordering = ['long', 'medium', 'short']

preprocessor = make_column_transformer(
    (StandardScaler(), numeric_features),
    (OrdinalEncoder(categories=[size_ordering]), ordinal_features)        
)

pipe_lr = make_pipeline(preprocessor, Ridge())
pipe_lr.fit(X, y)

feature_names = (    
     numeric_features
    + ordinal_features
)

coefficients = pipe_lr.named_steps["ridge"].coef_.flatten()

coef_df = pd.DataFrame(coefficients, index=feature_names, columns=['Coefficients'])
coef_df
```

> OMG I didn't realize OrdinalEncoder only transforms character values into number but doesn't generate dummy variables:woman-facepalming: My understanding about OrdinalEncoder was it uses the order that we provided to generate dummy variables! Oh no, I just realize that I understand it wrongly... Thank you for your clarification!> 

- lab3q2.5 As we pass 5 algorithms to the VotingRegressor() and then pass it to cross_validate() .
 How many models are being averaged here?
As in every cv fold 5 algorithms are being averaged to get the test score for each fold ( i.e 1 model of VotingRegressor for each fold ) . Does the question mean how many models are being averaged or algorithms ? If it is algorithms then the answer is always going to be 5 in our case right ?


- lab3 ex4.3  Does anyone know how to fix the error TypeError: can only concatenate tuple (not "str") to tuple that appears when you run the code in this question? I changed loc to iloc and it didn’t help, otherwise the code is the same as how it was given
> Ah I see. Yes, a pdf should be OK.
> If it’s working for you that’s great. But I’m not sure I understand the reasoning here. Probably when I see you next time I’ll follow up on this.

- lab3q2.9 did anyone get something like this ?

- I have a basic doubt, why are we looking at loss functions for classification problems. We have recall. precision, AP, ROC-AUC, F1. To check model performance...what additional information are we getting??
> Maybe just to introduce us to loss functions. This 0-1 loss fn doesn't seem to be very complicated (useful either) anyways. Something interesting about to come(?)
> I would say let’s wait and see…. My gut feeling is that what we learned earlier about optimizing on recall, etc. can be done mathematically with one of these loss functions…. I could be wrong though. 
> Recall, precision etc. are metrics to measure performance of the model whereas the loss functions discussed are to optimize the model to find the best fit to the training data i.e to find the best hyperplane which basically means finding the best coefficients for a line in linear regression for instance.
> She is discussing classification models. For linear regression models we have MAPE, R-square, RMSE
> R-square, MAPE are again metrics to measure perfomance of the model. Least squares would be the loss function in regression.
Both linear regression and logistic regression find coefficients like slope and intercept using loss function and an optimization like gradient descent to find best coefficients.
> Earlier in this course, we learned about recall, precision, ROC AUC, etc. for classification problems.  We can potentially formulate the loss function with the right regularization to deal with the same issues like class imbalance.  Am I right?
> Thanks for pointing out the difference.  What is happening here is that, using Varada’s example of the “crazy” curve for N=19 polynomial, it can provide the same metric of the regularized “non-crazy” one.  So finding the best loss function is not just for a better metric but also “manage” the coefficients.  Please correct me if I’m wrong.
> Yeah with n=19 we are basically overfitting to the training data. By adding regularization we ensure we don’t reach the value too soon and that we don’t have really large coefficients values since those can be finicky!
Yeah, the main aim of loss functions is to fit to the training data well without overfitting. The metrics are used on the validation or test data to quantify the fit made by the model in the first step.

> We learned in 512 how it's difficult to optimize discrete (and non-differentiable) functions. 

- I might have to miss understanding this; how do we interpret this yellow highlights in the loss function?



> As I understand, the question is why don't we directly optimize the metrics we talked about in lecture 1 (e.g., error (1-accuracy)), as that's what we care about in the end. The reason is that error is not a smooth function, which makes it hard to optimize. (This is a bit beyond the scope of the course.
> Error vs. loss is a common point of confusion. Loss is something you try to optimize during fit . Error is something you use to evaluate your model (when you call score). You want them to be aligned because you might as well optimize what you care about. But error (1-accuracy) is not a smooth function and so not easy to optimize. That's why we optimize something else which is convenient for optimization.
> you are right that when we use class_weight  hyperparameter of classifiers, we are directly changing the loss function to give more weight to the class of our interest so that the model will be penalized higher if it makes mistakes for the class of our interest. Since we incorporate this in the loss function, this method is much faster compared to other methods to deal with class imbalance such as SMOTE or oversampling.

- If you are wondering about how come logloss and cross entropy loss (optional material) are equivalent, you can try following functions on a toy problem and check whether you get the same losses from both functions or not.
```
import numpy as np

def my_log_loss(w, X, y): # this formulation assumes classes to be -1 and 1
    return np.sum(np.log(1 + np.exp(-y*(X@w))))

def my_cross_ent_loss(y, probs): # this formulation assumes classes to be 0 and 1
    return np.sum(-y*np.log(probs[:,1])-(1-y)*np.log(probs[:,0]))
```

- lecture 7 Confused about the least square loss function. What exactly is this? Why does w need to be transposed?
> x_i is a feature vector for one of the data points. As a vector, we can think of it having a shape of (N,1), where N is the number of features we are using for each data point.
w is a vector of weights given to each feature. So it too can be thought of having the shape (N,1), as it has one weight for each feature.
We can't multiply an (N,1) matrix by an (N,1) matrix using usual matrix multiplication. But if we transpose w, it turns into a (1,N) matrix, and a (1,N) matrix can multiply an (N,1) matrix from the left, giving a (1,1) matrix, or just a number.
So basically you have to take a transpose when using matrix notation like this in order to multiply all the features by their respective weights and sum up the results. (This is taking the dot product between the vectors w and x_i).

- I just want to make sure that our understanding about the submission is correct for lab4 as a group.  I presume that it should work like how submit the group labs in previous blocks.  For the avoidance of doubt:
We will commit the submission files to 1 lab repo only, and the link of it should be written in the lab Jupyter notebook; and
We will submit to Gradescope.  And there is only one submission needed per group with the other members added to the submission.
Would you confirm that this is how we should do it this time?  Thanks.

- Why are we doing preliminary preprocessing before train test split?- 
> My bad. After telling you again and again the last two months that the first step in your ML pipeline should be data splitting, I'm asking you to to carry out preliminary preprocessing before splitting :woman-facepalming::skin-tone-3:. Please do the splitting as the first step before any preprocessing. I guess here by preprocessing I meant if you want to change column names etc. you can do it before splitting.
> no worries! Was just wondering if I was misinterpreting sth here. Thanks!
> I also fill the Null values with 0 in the preliminary preprocessing before splitting. Is that fine? 3.Carry out any preliminary preprocessing, if needed (e.g., changing feature names, handling of NaN values etc.)
> You passed the ultimate test of the Golden Rule.  :first_place_medal:

- lab4 New York City Airbnb Open Data`
For this dataset we have ~50k rows of data.  If we are planning on working with the entire dataset and if we consider the large number of training instances, is it okay if we perform model selection/tuning with an explicit validation set rather than use cross validation?  For example if we used a 80/10/10 train/validation/test split, rather than 5 fold cross validation with a 80/20 train/test split.
> You have the flexibility in this project. That said, I would go with smaller train split, say 60/40 or even 50/50 and carry out cross-validation rather than using a single validation set.

- What's the best way to use Simple Imputer and Count Vectorizer within a pipeline? Simple Imputer takes an array and count vectorizer doesn't which make the pipeline break, however there are missing values in the text column I want to use.

- Couple gotchas in the Submission guidelines to remember to go back for,:

- Lab 2  I was wondering if everyone can see Lab 2 grades? I am waiting for mine but I know some can see their grade.

- lab-regression-problem just want to see what kind of scores people are getting? I’m using RMSE and R^2.
> I would also think about whether it’s a good idea to include/exclude the total number of reviews feature in your pipeline or not.

- What is the answer for lab2 Q1.7.3? “Usually we split the data before doing anything and we even avoid to look at the data. But when you are changing one row at a time and not using any global information, which we’ll be in this exercise, feature engineering is one of those things which you could be done before splitting the data.” seems not answering that question?
> I’m having hard time understanding your question here. If you have specific questions about your submission/grading, please approach the TAs directly unless  you think the discussion is going to be useful for your classmates.

- Hi, I feel that for Lab 2 Exercise1 quite a few questions were unnecessarily deducted, either my answers were somehow overlooked or just incorrectly graded. So they added up to a substantial amount of deduction in total. Did anyone else experience this? Thanks.

- Lab 4 Airbnb data  I was wondering how we should deal with the feature last_review  — it seems to be a date time object, but we have yet covered any feature engineering or column transformer on it. Should I simply drop it? Or is there any suggestion on how I should convert it into numeric feature so that I can pass into my model? Thanks
> You can extract month / quarter / time of day / weekend vs weekday as new features to see if there are say seasonal effect on reviews. (given summer traveler maybe different to winter travelers I think. 
> Yeah, that sounds like a good idea. For the purpose of this assignment, it’s also fine if you drop it.

- lab4 Did anyone notice text like below in the name column of Airbnb data? If yes, did you remove it? 

- lab 4, classification
Any idea on how to preprocess PAY_0 feature? Is StandardScaler() ok? It does look like a categorical rather than numeric feature
> For me it looks like an ordinal feature, which is already encoded. So I would either passthrough or treat it as a numeric feature and apply scaling.
> hi 
@varada
, i have related questions on this:
similar to PAY_0, EDUCATION seems to be ordinal feature that is already encoded as well? but there are some levels that are not well-defined (i.e. 0=undefined, 4=others, 5-6=unknown). what's the best way to preprocess EDUCATION then?
i think we didn't discuss much about collinearity, but PAY_0 to PAY_6 are highly correlated. should we then only keep 1 feature of this repayment status group? say PAY_0 as it's the most recent month?
p/s: i'm doing lab and i know it's late so please reply to me when it's convenient for you. thank you!!
> Hi 
> @LG I agree that EDUCATION column looks like an already encoded ordinal column. But the undefined/unknown values here are kind of problematic and the documentation doesn’t provide enough information to deal with them properly. So I would encode this feature with OHE.
Right. This is a time series problem and these kind of features are called lag features, which are going to be correlated. (You will learn about time series next semester.) If you are going to use linear models without regularization then this will be a problem and you should be careful about collinear features. But since in 571/573 we have been using regularized models, this is not going to be an issue. So I would just keep all these features and let the model take care of it.
 p/s: i’m doing lab and i know it’s late so please reply to me when it’s convenient for you. thank you!!
It’s nice of you to say this :slightly_smiling_face:!


- lab4  We are already doing hyper parameter optimization in section 7 why are we doing again in section 10? Do we have to optimize the best model in section 10?
>  In Section 7 you are doing it on a linear (simple) model. In Section 8 you are expected to try fancier models. The you pick the most promising looking ones and carry out hyperparameter optimization on then in Section 10.
> so as far as I understand, in Section 8 we try 3 different models, then we pick the best ONE to carry out hyperparameter optimization in Section 10. So just  hyperparameter optimization for 1 model. Right now I am doing hyperparameter optimization for all 3 models in Section 8.
> In Section 10, doing hyperparameter optimization on just your best model is fine.
Not sure why you’re doing hyperparameter optimization for all 3 models in this section.
Right now I am doing hyperparameter optimization for all 3 models in Section 8.
> Oh sorry, my bad. I mean I am doing hyperparameter optimization for all 3 models in Section 10.
>  i have a related question on hyperparameter optimization: we see a class imbalance in the data set; hence, our group decide to include class_weight="balanced" to deal with the class imbalance. however, we are not sure as to whether we should include that even before doing any hyperparameter optimization or let hyperparameter optimization decide? what's the best practice here? thank you!
> There is no one correct answer here but here is what I would do: I would try class_weight="balanced"  before hyperparameter optimization. If it’s resulting in markedly better scores, I would fix this in hyperparamter optimization and search for other hyperparameters.


- Lecture8: I understand that we are lowering the weight of higher degree polynomials. But then there is tradeoff, we will get lower score (on both training and test), how to gauge the optimal point? 
> With regularization, we are likely to get lower training score but higher validation/test score. We can find the optimal point by optimizing the regularization hyperparameter.

- Re: Lecture8, is it true that if we have more features (dimensions), there is a bigger need for regularization?  The reason I ask this is that if the number of features is small, too much “smoothing” with regularization might “simplify” the model too much and risk underfitting.
> Yes, you’re likely to overfit with more features and regularization will help by making the weights of irrelevant features either close to zero (L2-regularization) or zero (L1-regularization).

- How does l2 regularization help in feature selection as the weights don't become 0 ?
> I think the weight of a feature need not be zero to drop a feature as least significant at each step during feature selection.
> Agreed but what I meant was to do in a single step . I think Varada answered it now that if you need to do feature selection in the model we need to use l1 only .
> I think so far in many cases we used Ridge for feature selection which uses L2 penalty.
> True but that's an additional step after model building but when we use l1 regularization the model does feature selection by assigning weights for certain features to be 0
> L1-regularization (Lasso) will do feature selection for you in the sense that it will set some of the coefficients to zero. That said, you can also use Ridge (L2-regulaization) with SelectFromModel with a threshold for feature selection. Remember that for this method we need feature importances and a threshold and we discard features whose coefficients are smaller than the threshold. L2-regularization is going to make your coefficients small. So you can set a threshold to a non-zero value and use L2-regularization for feature selection.


- I’ve posted some practice questions for quiz2 in the course repository.
I’m sensing some anxiety about quiz2. I don’t intend to put tricky questions on the quiz. In general, if you paid attention during lectures, if you understand the notes well, and if you feeling comfortable when working on labs, you should be OK. I’ve scheduled a quiz review OH on Zoom on Friday at 3pm just in case it helps your anxiety.
I’ll update the lecture notes (lectures 5 to 8) with my answers to T/F questions sometime today or tomorrow.

- Though we are done with the labs now, but putting this out after checking the score for lab2: One of the major struggle that I have faced with 573/ 571 labs is that there are way way too many subparts to each question, so much that it gets difficult to keep a track of every thing that needs to be explained and submitted. Before submitting lab2, I went through every thing a couple of times, but I seem to have missed out one small part in a long question, and lost 6 points (30% of the whole) for it 
> I lost 10+ points in lab2 from similar issues. We need to be careful about EVERY word.
> Yeah in each subpary there are multiple questions
> For me, it is the lack of time for review in MDS, so it is not that 573 Labs are problematic. I personally just don't have time to double-check work my work for labs to the full extent. With autograded labs it is good because I catch mistakes but with open-ended labs it is a problem.
> Thanks for your feedback 
@Anupriya
. I understand your frustration. I guess I get too excited and put too many questions in the labs :see_no_evil:. In general, I want you to be able to reflect on what you are doing and why are you doing it and communicate your rationale, results, and observations clearly. I think this is an important part of machine learning and that’s why I put open-ended reasoning questions in labs. Also, I think if you have some results, you need to be able to say something about them and give them some meaning. Otherwise you are just throwing a bunch of numbers at the reader. It would have been useful to know this earlier. In general, the scores of the labs look typical/little bit on the higher side to me (median of lab1 is is 96.0 and lab 2 is 91.0). So it didn’t occur to me that you’ve been struggling with this.
@Chaoran Wang
 I think it’s a good habit to be careful about what you say but of course your answers don’t have to exactly match the solution key, as many of these are subjective questions where there is no one correct answer. In general, marking subjective answers is not easy. You should reach out to the appropriate TAs if you think your rationale/reasoning is correct but you didn’t get the points.
@katia_aristova
 Yeah, autograding is good suggestion.  Not that it helps you but probably for some of the exercises in 571 I will try to incorporate it next year. In ML, there are so many different ways to apply preprocessing and building your pipeline and your results are going to change based on that, which makes autograding difficult for these types of topics. And I do want to provide you some flexibility there. If I tell you what exact steps I want you to apply in preprocessing, you’ll miss out on learning an important part of building ML pipelines.
 
> If I tell you what exact steps I want you to apply in preprocessing, you'll miss out on learning an important part of building ML pipelines.
> I absolutely agree. I just find that I make mistakes and don't catch them because the workload is high in general. So it is not that the 573 labs are a problem but I find MDS challenging in terms of time allocation in general.

> Hi 
@varada
, appreciate the quick response. I understand that it is good to test the reason why we are doing something, but my frustration was because I lost 6 marks in q1.7.2 for missing to  'briefly explain your intuition on why these features might help'. It was just a 10 min job and I could have easily done that once the new features were working. I guess I missed it as it seemed to be mentioned as a passing comment in a long question with many subparts. I am also a bit surprised that this part (1.7.2.2) had a weightage of 6% of the lab, when there were many advanced level concepts tested! Please look into the distribution of marks within a question.
> We’ll discuss this during our meeting today. But I disagree with your comment 
@Anupriya
. I do not see this as a passing comment in a long question. The following subpart of the exercise is about feature engineering, which is one of the main goals of Exercise 1. This subpart asks you to come up with new features and explain the rationale behind your features. If you came up with new features you should have put some thought into this, and explaining your thoughts and rationale behind your features is an important part of this question. Otherwise how does the reader know why you came up with these particular features and why do you think they are relevant for the given problem. Imagine that you are reading someone else’s ML solution for a problem and they add a bunch of features without any explaination. Would you be happy with that? 2. Extract at least two more features that you think might be relevant for prediction and store them as new
columns in the train and test sets. Briefly explain your intuition on why these features might help the prediction task.

> In general, I share the feeling with 
@Anupriya
 that it is very easy to lose points if we are not carefully reading every word in the question.  I have also lost points here and there.  So I do appreciate that some of the exercises have been broken up into tasks.  A lot of times is just mere overlooking at 3am rather than being lazy when there are so many things being asked in one paragraph.
There is another issue related to the labs even though I have seen some improvements in certain labs with 573 (compared to 571) being that if we are being asked a lot of small questions in the same lab, the lab becomes very lengthy.  Even though I do not know the standard, I believe that there should be a standard of how many hours an MDS student should put in per course per week for assignments.  If, for each lab, there is a focus on certain parts, then we should be asked to do less in the other parts.  In general, I can say that while 573 labs are long but I can see some clear focus, like even some code being provided for non-focus parts.  FYI, I logged 8h55m on 571 lab2, twice as long as the 531, 551 and 512 labs of the same week.  (Just to be fair, 531 had 2 labs and they logged 9.5 hours in total so 571 lab2 was not the longest.) I think the lengths of 573 labs are more “under control” and I hope this can be true for all courses at MDS.
> I second 
@Steven Leung
 comment. I believe the biggest struggle is on those questions with long pieces of code and several questions all together. Maybe just a simple tweak like separating  coding tasks from the interpretation, and adding a cell to answer to each subquestion right below each question would help.
> Thanks for your constructive feedback! I would say that the typical time taken to complete an MDS lab is 4 to 6 hours. Also, the expectation is that you are able to do the previously learned things quickly. For example, I made you go through data preprocessing process in most of the labs because that’s going to be the first step in any ML project you work on and repetition of that process is useful/important. And the expectation was that you don’t spend hours in this step. In general, I see that reasoning/interpretation questions have been a problem probably because some of you are not used to answering such questions? But I think that it’s going to be a useful skill to answer such questions and being skeptical about each and every step in your ML pipeline. It’s not that we are looking for exact words in your answers but we are looking for some evidence of your understanding of the material in your reasoning.
Overall, I’m feeling sad that these labs have caused some of you a lot of stress and frustration :disappointed:. Just so that you know I deeply care about your learning as well as your well being. I just want you to learn the material and I tried my best to create lab questions and lecture notes so that you get to learn, reflect on, and practice the material we learn in class. The length and structure of the labs have worked in the past and I’m not entirely sure what has changed this year. I’ll think about this so that you have better experience in my next course. Happy to hear your thoughts! Again, thank you for bringing this up and providing useful feedback!

- lab 4 classification
I am a bit at a loss as to how ethical it is to include demographic information when predicting financial outcomes (e.g. would someone pay or not at the end of the month). We dropped the SEX feature but others are just as problematic. 
> I’m glad that you’re thinking about this. Yeah, demographic information is tricky especially because if you get rid of a feature say race, you could infer it from other features such as location. For the purpose of this assignment, I wouldn’t worry too much about it because your model is not going to cause direct harm to a particular group. In fact, if you include these features in your model, you could do an analysis of results for certain groups later, similar to how we did it in lecture 1 on adult census dataset. That said, I would be very careful about including/excluding such information when your model is going to be used in some real-world application because there would be some serious consequences of doing this. (edited) 

- lecture 8 Any suggested material to explain why L2 has unique solution? Feel like my algebra training has failed me 
> You can also find some material on this in CPSC 340 lecture notes. It’s great if you want to explore this more and understand this better. But just want to make it clear that for the purpose of this class, it’s not necessary. I would like you know at a high level that the solution w  for L2-regularization is unique and L1-regularization is not unique but there is no expectation that you should be able explain this.
> Yea, I actually had the question after reading this webpage. After some sleep it seems to make sense now. (How could you also be awake at 4 lol)
@varada
 Yup! just want to learn more in my ample free time (jk) I think it is easier to understand if I know the whole picture, otherwise, it is hard to pick up next time when I revisit the topic. Thanks for the resource and I will take a look of it later during the break =]
 
- Lab 4 q9
I'm finding that selecting the features is taking way too long. Does anyone have any recommendations for shortening the amount of time it takes to run this step using RFECV or forward selection
> Here are a couple of suggestions:
Use L1 regularized models with SelectFromModel instead of RFE/RFECV or forward selection. This will be much faster.
If you want to use RFE or forward selection, I would try feature selection on a sample instead of the full training set.

- jupyter notebook kernel idle  when I re-run the lab4 q8 for regression problem my noteboooek showed as  "kernel idle" and the cell still run as [*] but it looks like the cell is not running for 30+ mins.  I tried re-start kernel but the same problem is occurred.  Wondering how I can ensure to re-run this and generate the output? (the screenshot is in the thread chat)


- I'm trying to use shap.KernelExplainer to get the shap values for my SVM model but it is taking >2hours to run on 100 examples. Is this supposed to happen? Is there any way to speed this up?
> Wow! I’ve not used shap.KernelExplainer  myself before. But I’ve heard that it’s slow. Did you check this issue? Do you have too many features? They are suggesting grouping features.
> For the purpose of this assignment, I would stick to TreeExplainer , as they have fast implementation for tree-based models.
> I did see that issue, but in this case I only have 25 features, so I don't think that's too many. I also noticed that the runtime for KernelExplainer seems to scale exponentially with the number of examples I give it. E.g. if I give it 2 examples, it takes 2 seconds per example; if I give it 20, it takes 18 seconds per example. And for 100, it took 90 seconds/iteration. :shrug:
If my best model was an SVM, then the TreeExplainer is not compatible with this model. Should I just use the TreeExplainer with a tree based model that performed well? 
> Yeah, that’s what I would do. Are tree-based models giving comparable scores? Writing a sentence explaining why you are using TreeExplainer would help the TA.

- lab2_grading
@Daniel Ramandi
 and I just discussed lab 2 grading. It seems like the main problem was with grading 1.9.3.
3. Examine the coefficients of the features we have extracted above. Do they make sense?
The question is asking to examine the coefficients of extracted, i.e., your engineered features. ~50% of you got that and showed the coefficients of your engineered features. This interpretation was kind of natural to me because if I engineer new features, I would be curious to examine their coefficients. But since many of you missed it, apparently, it was not that clear in the given context. So we decided to give a smaller penalty here. Before we were deducting 3 points for the accuracy part of this question and 2 points for reasoning. But now we are only deducting 1.5 points in total if you are not displaying coefficients of the engineered features. And if you are interpreting the coefficients correctly, irrespective of which coefficients you are showing, you should get all the points for reasoning. I hope this makes you feel a bit better about this.
Another concern was about including/excluding keyword  feature from column transformer. It was a mistake/misunderstanding from our side. 
@Daniel Ramandi
 is taking care of it and I’ll let him comment on this one.
If you have any other concerns, I’ve my OH starting in 10 minutes.

- This is kind of a vague question, sorry for that!
I'm getting this error when I train any model on my data:
UserWarning: Scoring failed. The score on this train-test partition for these parameters will be set to nan. Details: 
Traceback (most recent call last):
  File "/home/utkarshsaboo45/miniconda3/envs/573/lib/python3.9/site-packages/sklearn/metrics/_scorer.py", line 71, in _cached_call
    return cache[method]
KeyError: 'predict'
ValueError: Found unknown categories [8] in column 2 during transform
This looks like a warning but I'm getting the scores. Has anyone encountered something like this before?
Edit:
I get this when I pass my data and model to mean_std_cross_val_score, not when I score on test set.
> if an ordinal feature is already encoded with ordered numeric values, why do you want to apply ordinal encoding on it? I would either treat it as a numeric feature (e.g., if you want to apply scaling) or a passthrough feature.

- lab4 Is it okay if we have worked on a single repository for the group project ? Just double checking as I have not committed anything in my repo .


- lab 4, SHAP
I am trying to create two force plots, but before that I encountered a problem with the dataframes that we need to get shap values, it says:
'numpy.ndarray' object has no attribute 'toarray'
> I ran into the same issue. Removing .toarray() worked for me. It seems preprocessor.transform(X_train) isn’t returned as a sparse matrix this time, so this method does not exist…

- lab4 (a bit of a general question). Is the addition of polynomial features only helpful when you are using a linear model? Is there ever a time where it would be beneficial to add polynomial features when you are using a classifier like RandomForest , for example? 
> Yes, I would say so. I’ve not seen people doing this for non-linear models and it’s likely to be ineffective.

- lab 4, SHAP As a follow up to my previous question:  I tried to remove toarray() , however, I seem to have encountered a different problem: something is wrong with my test_lgbm_shap_values
Its shape if I turn it into nparray is (2, 9000, 27)
> If you’re trying it on a classification problem, it’s going to return SHAP values for each class (similar to what we saw on adult census dataset we looked at in class). In such cases, it’s useful to create and interpret your plots using SHAP values for one class.

- a question about feature importances: I’m curious why are the important features returned by eli5 different from the important features with the feature_importances_ attribute for lgbmclassifier (but they output identical top features for the other models, like randomforestclassifier)
> LGBMClassifier is not a sklearn  classifier. You’re using a different package for that. That said, I see that this package also supports feature_importances_  attribute. So are you saying that the feature importances returned with feature_importances_ attribute are not the same as the ones returned by eli5  for LGBMClassifier?
> Yeah, probably you could try different values for importance_type  ?

- Re: lab4, is it OK if we move Ex4 (optional question for feature engineering) to another place?  The reason for asking is that based on what we are doing, it comes more natural AFTER we have tried the original set of features (with some preprocessing) with a linear model (Ex8).
> Yes, that’s fine, as long as you clearly explain it in the notebook for the TA grading your work.

- LAB4 SHAP, I am getting below errors when trying to create lr_explainer. Anyone with an idea?
> It’s exactly what it’s saying. Linear models (logistic regression) is not supported by TreeExplainer . For linear models you can use their LinearExplainer : https://shap-lrjball.readthedocs.io/en/latest/generated/shap.LinearExplainer.html

> Also, logistic regression is a linear model and you know how it makes predictions based on the learned coefficients. So also think about whether you really need SHAP  to explain predictions made by logistic regression or not.

- Hi team, I'm having trouble interpreting the meaning behind these plots in lecture 8. Would anyone be able to summarize the takeaway info from these plots?
> First of all, if you are worried about this showing up on the quiz, it’s not going to be there. These pictures are there mostly for your understanding.
The main point I want you to take away from these pictures is that
In L1-regularization we are adding L0 penalty.  So we are adding this discontinuity in the loss function. So you cannot really optimize it.
In L2-regularization you are adding L2 penalty and the shape of the resulting loss function is as shown in the picture. It’s convex and smooth, which are both desirable properties for optimization.
In L1-regularization you are adding L1 penalty and the shape of the resulting loss function is this V-shape, as shown in the picture. It’s convex but it’s not smooth.
Because of these differences in the shape of these functions, all of them have different properties. L2-regularization moves the weights to zero but they quite become exactly zero whereas L1 regularization sets feature weights to exactly zero. You can find more mathematical details on this in CPSC 340 material.
> Yes, for the purpose of this class it’s enough to remember this main difference. As you increase lambda , both L1- and L2-regularization shrink weights. But in L2-regularization (ridge) weights do not quite become exactly zero, as the slope is going to zero smoothly whereas for L1-regularization (lasso) some weights become exactly zero. Because of this L1-regularization can be used for feature selection.


- Lecture 5 Questions
What is the relation between the model complexity and overfitting? In the past I thought we referred to models with higher complexity as more likely to overfit, but in this lecture it seems that increasing model complexity is a good thing?
Does increasing random forests’ max_feature increase overfitting? If you increase max_feature high enough doesn’t that get rid of all the randomness gained from selecting a random subset of features, since each decision tree will have the same exact subset of features to select the best possible test from?
One of the strengths of random forests models was stated to be that it is less likely to overfit, but at least in my experience so far the gap between training and validation scores are usually much higher for random forest models even though the random forest model provides a higher validation score than the other models. Do we still choose the random forest model in this case because even though the train-validation score gap is high it still performs better on unseen data? If it performs better on unseen data does that mean that even though the train-validation gap is larger it isn’t actually more likely to overfit?
> By setting max_features to 1.0 for all means we are basically choosing the same features for all the sub trees in random forest and despite bootstrapping each of the trees would only select some features to make selections and thus they’re in a way the same tree all averaged together. By reducing the max_features we allow random features to be selected at each node for every tree which ensures that we cover every tree and thus not overfitting to certain features that would generally dominate in a majority of data points but also give chance to certain features that are useful in predicting a niche set of data points. In this case adding randomness as I understand it helps in considering all features and all portions of data and thus we get a more generalizable model.
> I found the overfitting thing to be true as well and I was reading some stuff online that said that when you have time series data, random forest fails quite a bit since the entire averaging happens on the train data and it can’t predict the future for instance since it’s always basically averaging out the training data…


- Lecture 6 Note  There is a typo(?) in the code chunk for the force plot.
> I was wondering why the results is class 0 (<=50k) even though the value (= -0.1961822) is greater than  the base value (= -2.3), and found out that there was a typo in the code chunk;;;;;;

- Since some of us may submit lab4 as a group, would you enable the function of adding members to a submission on Gradescope?  currently I can’t see it to be possible.

- Hi Varada, we finished lab4 as a group and have our group repo in github. I have already added you in our group. I wonder which TAs I should be adding in as well?
> Yeah, upload the ipynb and pdf to Gradescope. Make sure to provide GitHub link in your submission. If your repo is under UBC-MDS, you should be able to add all MDS TAs group as collaborators in your repo. If you want to add individual TAs, here are the GitHub enterprise handles of our TAs.

- f we get a linear model as the best model, how are we supposed to create a SHAP force plot for it as asked in q12? How can we do that?
> You can either use SHAP’s LinearExplainer or argue that you don’t really need to use SHAP for linear models and explain the predictions using coefficients. But in the latter case you won’t get pretty plots.

- I hope you had fun working on lab 4. I thought about creating a leaderboard for this lab on Gradescope but didn’t do it for several reasons. That said, I’m very curious to see what kind of scores you managed to get. So I’ve created this issue in our course repository. If you feel comfortable, it will be great if you can share your test scores along with the metric you used there. Thank you!
> We did not get a great score but big point of pride is our engineered feature made it to most influential features!!
> I had a lot of fun with this lab too :blush: One of my favourites thus far
> Added three features:
AVG_LATE (-1 if was never late, otherwise averages num of late months)
MISSED_PMT (1 if missed any of 6 recorded, 0 otherwise)
AVG_BILL (ave bill amount)
AVG_LATE was the most impactiful! 
> I am happy with my engineered features  as long as they appear in the shap report. It is really hard to come up with features with high importance.
> I liked exploring the bias in this exercise. I am looking forward to learning more about the ethics of using demographic info! The confusion matrix showed our model was a bit biased (as in discriminatory) towards males and married people.
edit: score was 0.54 for f1 (so not spectacular) 
> We started off with CV recall of 0.644 very early on with LogisticRegression with class_weight=‘balanced’, but then after that we tried so many different models, features, etc. Nothing got any better.
> Hey Varada
In airbnb regression problem, I wanted to create new features having certain interactions of numerical and categorical (OHE) features
I tried to achieve it by passing everything in column transformer in Polynomial feature with interaction_only = True but it generates interactions of OHE columns as well (which results in lots of column with 0 value )
so basically I couldn't find any option to get only real interactions like [num1_cat1, num1_cat2, num2_cat1, num2_cat2 etc.]
Not sure if they would have been important features but just wanted to see their interaction impact on model result.
Any suggestion if we should look for such interactions and how can we get them? 
> That’s a tricky one 
@Karanpreet Kaur
. I guess I would use a FunctionTransformer  (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html) in this case where you can define your own custom  transformation.
> We did enable the class_weight='balanced' for all the models that we have tried.  We have tried all the models we have been taught since 571.  CatBoost was the 1st runner-up with similar CV recall, but train recall was worse, thus some risk of overfitting.  Plus CatBoost is much slower than Logistic Regression.
What we didn’t try was stacking the models with a linear model…

- For Soft Voting classifiers the Sklearn docs define the prediction as follows and I’m not sure what it exactly means.  Does it mean the max of the predict_proba of the constituent classifiers? ‘argmax of the sum of probabilities’ is confusing…
> From my understanding it sums the predict_proba output of different constituent models and picks the class associated with the highest summation value. My suggestion is trying things out on your own in such cases. Let’s consider the example with index 1 In the following example from class, for instance. Here:
```
# Sum of probabilities for the class at index 0 (<=50k)
sum_prob_class_0 = np.sum([classifier.predict_proba(test_g50k)[1, 0] for name, classifier in averaging_model.named_estimators_.items()])
sum_prob_class_0
1.5827921487449172

# Sum of probabilities for the class at index 1 (>50k)
np.sum([classifier.predict_proba(test_g50k)[1, 1] for na
sum_prob_class_1 = np.sum([classifier.predict_proba(test_g50k)[1, 1] for name, classifier in averaging_model.named_estimators_.items()])
sum_prob_class_1
4.417207851255083

# Average probability over 6 constituent classifiers
sum_prob_class_0/6, sum_prob_class_1/6
(0.2637986914574862, 0.7362013085425138)

# The above average probability scores match with the following scores. 
averaging_model.predict_proba(test_g50k)[1] 
array([0.26379869, 0.73620131])
```

> Ahh! That makes a lot sense now. Thanks a lot for the detailed explanation 
@varada
! :slightly_smiling_face:
I’m assuming we don’t have to also average over the 6 models since it would be the same effect for both sums of probs of each class and can just calculate the arg max directly which sort of correlates with the sklearn documentation which didn’t make sense to me before…


- Can someone explain this tree to me?
> Each split at every node is the best split found for that feature for that particular value which is decided based on which value gives the most homogeneous split based on gini impurity and information gain etc. So for example education at level 12.5 was the most homogeneous split.
The class indicates the majority of the y for that split in particular. Here since the random forest max_depth is clipped at 2 we don’t really get homogeneous split.
The main idea imo was to show that different trees choose different features to make decisions since at every node random features are selected… 
> Thanks for your response Harish!
I get feature selection part. What confuses me is that for each split, it predicts class 0. If the class doesn't depend on the feature, then how can we call it a homogeneous split?
It's like: check for x0_private. Oh, if it's <= 0.5, predict class 0. Oh, if it's > 0.5, predict class 0 anyways.
There's no information gain here whatsoever. Then why was this feature selected in the first place?
Am I missing something?
> Does that, by any chance, mean that the features that were randomly selected at each node, were all useless?
> Not really. I might be wrong but the main idea is that information gain is the entropy at parent node which in the 1st case is prior to education split minus the weighted average of entropy at child which after the split.
So for the subset of features for this tree this feature of education gave the highest difference in entropy between parent and child split at education level of 12.5…The final split at each level is irrelevant. Since we are still are lower depth we can’t really expect homogeneous splits also…
> Didn't get the first part. Too much technicality:exploding_head:
Also, why is the final split irrelevant? 
> Taking a stab at this: homogenous split means all the data gets the same prediction (perfectly homogenous split means everything is classified as same class, and won't get split further). However, if it's not perfect, it'll keep going - For eg. the first split may get 60% class 0 and 40% class 1, but based on majority it'll be class 0. And so on and so forth. Until you reach max_depth or complete homogeneity.
So in this particular diagram, it seems like all the splits are not great, there's some mixture of predictions for each node with majority leaning towards class 0.
> Thanks for explaining things through. I understand how what homogeneous splits are.
However, I'm still confused about the end predictions.
But now that I think about it, the purpose of this example was to show how different features are selected at each node, so the end predictions are not something we need to focus on this example I guess. They are just some values.

- Lecture 5
A reasonable implementation of predict_proba for random forests would be for each tree to “vote” and then normalize these vote counts into probabilities.
Given solution: True
Say, we have 10 probability pairs:
6 of them are (0.55, 0.45) for (positive, negative) respt.
4 of them are (0.05, 0.95) again for (positive, negative) respt.
The model predicts positive (majority wins).
But the actual class should likely be negative here for obvious reasons.
How is this a reasonable implementation of predict_proba?
> For VotingClassifer, there is an option of voting="hard" or "soft".  The first is by the majority votes of the class, and the latter is the average probability.  This is from Lecture 5.
> Thanks for your reply Steven.
I see, so basically we have both the approaches in hand and we can decide which one to choose depending on how much confident we are about our predict_proba scores.
Am I correct?

- Check out this cheatsheet on sklearn website. It oversimplifies things but it’s still a good reference: https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

- (for quiz2) re: lecture6, it talks about feature importances coming from scikit-learn and also from eli5.  They provide the same values.  From scikit-learn documentation, it says that the definition of feature importance is:
computed as the (normalized) total reduction of the criterion brought by that feature.
So if I understand it correctly, the importances for all the features would add up to 1, right?
So we can use them to rank the features during feature selection.
But we can’t use them for prediction or interpreting how much increase or decrease of the prediction per the change in the feature value, especially when feature importances aren’t even “signed” (no direction) and are normalized (i.e. no longer on the same scale as the features).  Am I right?
> Yes and yes. They should add up to 1.0 and you cannot tell the direction of prediction from these feature importances as they do not have a sign.

- What are we trying to say here?

> This plot appears in the context of L2-regularization and the point we are trying to make here is that as we increase lambda  (regularization strength) the w coefficients of L2-regularization get close to zero but they never become exactly zero.
> Oh got it, and different lines symbolizes different w_i 
> Yes. We are showing how different weights change as we increase lambda .

- Could I clarify my understanding of SHAP? 
    - the total weight of all feature variables = 1 [the weight must be positive]
    - the output SHAP value is weight x marginal contribution [the MC can be either positive or negative]
    this above is for local feature importance.
    For global feature importance, it is simply the mean of each SHAP value associated with each feature 
> Given this page I'm not so sure about this interpretation. https://christophm.github.io/interpretable-ml-book/shapley.html


- In lecture7, I can see that in the “regularization demo”, you demonstrated 2 solutions of how to reduce overfitting.  Solution 1 is about controlling the degree of the polynomials while Solution 2 is by regularization in the loss function.  I have 21 questions:
Solution 1 might as well be generalized to any kind of hyperparameter tuning, right?  And Solution 2 will always be a bit more flexible compared to hyperparameter tuning because with regularization, we may not totally miss out on a good model with some complexity.
Can we arbitrarily assign a loss function and give it to a model (like Ridge() in your example)?  Am I seeing that Ridge only has L2 regularization built in and be controlled by alpha?

- In quiz 2 practice question q3,  I am not sure why linear regression does not give unique solution for w?
> Linear regression should be fine too. That’s why I’m explicitly saying  “(Multiple answers are possible.)” there.

- SolvedA quick question. Why do we need  the  1/2 in the least squares equation?  where is the 1/2 come from? Thanks. 
> When we differentiate the L2 norm to get the optimal value for loss function, the denominator of 2 gets cancelled by the degree of the norm.
d/dx( 1/2 * x^2) = (1/2) * 2 * x = x.
> The solution which will minimise the convex function f(w) is the same which will minimise f(w)/2, so the scaling doesn't impact the unique solution we are looking for.


- Lecture 7: f(w)=1/2‖Xw−y‖^2+λ‖w‖0
In the above equation, larger λ means aggressive feature pruning, i.e., aggressively making many weights zero.
Answer: True.
How exactly?

> When lambda is high that means that the L0 norm of w must be smaller to minimize f(w), since the L0 norm is the number of non-zero elements in w, that means there will be more features with weights of 0

> Ah! Makes sense. Was confused with words. That's like, the basic idea behind regularization.

- In the requation below of L0-regularization, smaller value for ||w_0|| means we discard most of the features: f_w = 1/2 ||X_w - y||^2 + lambda ||w_0||

> smaller value means many weights will likely be 0 right?

> likely zero, but not zero. So it does not mean we disregard the feature
> The L0 norm of the weight vector is just the number of non-zero weights, if it decreases it means that there are more zeroes
> but it is talking about w. Not about L0 norm
> ||w||_0 is the L0 norm of w, smaller ||w||_0 means more zero weights
> so both question 1 and question 2 is same?
> If you’re referring to the question that Utkarsh asked, no, because it is asking the effect that lambda has on the loss function, whereas this question is asking you to interpret what a small L0 norm of w means (

- lab 3 solution - Ex4.3 I'm going through the solutions of interpreting the SHAP force plots and I have a few questions: Plot 1: What does it mean by the raw score is pushed higher by  'absence of value of genre_alternative and genre_children_music'? Should we find the features in the plot with values equal to 0? I did not see the feature of 'children music' in the plot. Plot 2: Why is the raw score pushed down by the 'negative value of liveliness'? The SHAP plot shows a positive value 1.5 for liveliness 
> My bad. It should be fixed now. (I was trying out force plots for examples in the solutions and forgot to update the associated description after finalizing the plots :woman-facepalming::skin-tone-3:.)

