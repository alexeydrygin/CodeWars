# 7 kyu - Building  an Adaboost model with Sklearn (Introductory Machine Learning)
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

def train_ada_boost(X, target, estimators=3, random_seed=0):
    # Разделим данные на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, target, random_state=random_seed)
    
    # Обучим классификатор AdaBoost на обучающих данных
    model = AdaBoostClassifier(n_estimators=estimators, random_state=random_seed)
    model.fit(X_train.reshape(-1, 1), y_train)
    
    # Вернем обученную модель, тестовую выборку и целевой массив
    return model, X_test, y_test