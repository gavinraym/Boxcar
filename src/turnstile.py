import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor


def grid_search():
    ''' 
    Here I have defined a great random forest model using gridsearch. 

    Moving forward, I will use a random forest with 225 estimators,
    and a max depth of 17. This conclusion came after testing multiple
    times with n_estimators ranging from 50 to 500, and a max_depth 
    ranging from 1 to 20. 

    This model received a test score of 97.5, which is plenty good for 
    our purposes here.
    '''
    X_data = pd.read_csv('../data/samples.csv', names=[1,2,3,4,5,0,'score'])
    y_data = X_data.pop('score')
    X_train, X_test, y_train, y_test = train_test_split(
        X_data, y_data, test_size=.5, shuffle=True)

    gf = GridSearchCV(
        RandomForestRegressor(),
        {'n_estimators': [175, 200,225],
        'max_depth' : [16,17,18]},
        scoring='r2',
        n_jobs=-1
        )

    gf.fit(X_train, y_train)
    print(gf.cv_results_)
    print(f'Best estimator = {gf.best_params_}, with score of {gf.score(X_test, y_test)}')

def graph_scores():
    '''
    Here I am making a graph that shows how changing the max_depth affects
    the train and test scores. Notice that the training score continues to
    increase even after the test score has reversed. This indicates an 
    overfit model at those depths.

    The best model is at the highest point for the test scores.
    '''
    X_data = pd.read_csv('../data/samples.csv', names=[1,2,3,4,5,0,'score'])
    y_data = X_data.pop('score')
    X_train, X_test, y_train, y_test = train_test_split(
        X_data, y_data, test_size=.5, shuffle=True)

    fig, ax = plt.subplots()

    max_depth_list = range(12,21)
    training_scores = []
    test_scores = []
    for max_depth in max_depth_list:
        model = RandomForestRegressor(
        n_estimators = 225,
        max_depth = max_depth,
        n_jobs=-1)
        model.fit(X_train, y_train)
        training_scores.append(model.score(X_train, y_train))
        test_scores.append(model.score(X_test, y_test))


    ax = sns.lineplot(max_depth_list, training_scores, label='training scores')
    ax = sns.lineplot(max_depth_list, test_scores, label='testing scores')
    ax.axvline(max_depth_list[test_scores.index(max(test_scores))],
                 linestyle=':', color = 'k')
    plt.title('Comparing train vs test error within max depth range.')
    plt.xlabel('Varying max depth.')
    plt.ylabel('Model scores using R2.')
    plt.savefig('../images/rf_test.png')

    plt.close('all')
    

    

if __name__ == '__main__':
    pass