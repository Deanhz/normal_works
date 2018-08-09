# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:43:57 2018

@author: Dean
python机器学习及实践 p122
网格搜索
"""
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV

news = fetch_20newsgroups(subset="all")
X_train,X_test,y_train,y_test = train_test_split(news.data[:3000],news.target[:3000],test_size=0.25,random_state=33)

clf=Pipeline([('vect',TfidfVectorizer(stop_words='english',analyzer='word')),('svc',SVC())])

parameters = {'svc_gamma':np.logspace(-2,1,4),'svc_C':np.logspace(-1,1,3)}

gs = GridSearchCV(clf,parameters,verbose=2,refit=True,n_jobs=-1)

time_=gs.fit(X_train,y_train)

print(gs.best_params_,gs.best_score_)
print(gs.score(X_test,y_test))
print(time_)
