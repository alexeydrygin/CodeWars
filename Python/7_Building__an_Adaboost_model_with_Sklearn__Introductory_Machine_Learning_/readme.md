## 7 kyu - Building  an Adaboost model with Sklearn (Introductory Machine Learning)
[Ссылка на задачу](https://www.codewars.com/kata/5a21bd361f7f7098e800000c "Building  an Adaboost model with Sklearn (Introductory Machine Learning)")

Hi there! Welcome to "Building  an Adaboost model with Sklearn (Introductory Machine Learning)". 

If you get stuck at any point I **strongly recommend** you read the relevant documentation: 
https://scikit-learn.org/stable/index.html

This kata can be broken up into the following steps:

1. Import the relevant sklearn libraries (i.e. AdaBoostClassifier, train_test_split)
2. Create the "train_ada_boost" function (more details below)
3. Split the data (X) into a test set and a training set (you **MUST USE** sklearns train_test_split for this)
4. **TRAIN** an adaBoostClassfier (Once again, you **MUST USE** sklearn for this).
5. Your "train_ada_boost" function **must return a three element tuple** (more details below).


The "train_ada_boost" function accepts the following arguments:

* X -- This would normally be a dataset (but in this kata it is a 1D numpy array)
* Target -- This is a 1D numpy array consisting of 1's and 0's. This argument is the set of values we are trying to predict with our model 
* estimators -- **KEYWORD ARGUMENT** if no argument is passed in the default value should be set to **3**.
* random_seed -- **KEYWORD ARGUMENT** if no argument is passed in the default value should be set to **0**.

Your function should return a 3 element tuple consisting of the following values **in this exact order**:

* A **TRAINED** AdaBoostClassifer (return the actual model)
* A test set (1D numpy array, which was built by sklearns test_train_split function)
* A target array (1D numpy array, which was built by sklearns test_train_split function))

Details:

* Your model should be trained using the specified number of estimators, with a random state equal to seed.
* When splitting the data, be sure to set the random state equal to seed.
* ALL other parameters not mentioned here for both 'test_train_split' and 'AdaBoost' should be set to default values. 
* Even though you are handling Numpy arrays there is no need to actually manipulate the arrays yourself (let sklearn to it for you!).

Good Luck!


*Note, in actual machine learning it is highly unlikely we would ever use AdaBoost with such a small number of estimators. However building models can be very time consuming and codewars.com has a 5000ms timeout.  


---
## Задание:

## 7 KYU - Создание модели Adaboost с Sklearn (Вводное машинное обучение)
[Ssshlca na a зadaчue] (https://www.codewars.com/kata/5a21bd361f7f7098e800000c "Создание модели Adaboost с Sklearn (вводное машинное обучение)")

Всем привет!Добро пожаловать на «Создание модели Adaboost с Sklearn (вступительное машинное обучение)».

Если вы застряли в любой момент, я настоятельно рекомендую ** Вы прочитаете соответствующую документацию:
https://scikit-learn.org/stable/index.html

Эту ката можно разбить на следующие шаги:

1. Импортируйте соответствующие библиотеки Sklearn (то есть Adaboostclassifier, train_test_split)
2. Создайте функцию "TRAIN_ADA_BOOST" (подробнее ниже)
3. Разделите данные (x) на набор тестирования и учебный набор (вы ** должны использовать ** Sklearns Train_test_split для этого)
4. ** Поезд ** adaboostclassfier (еще раз, вы ** должны использовать ** Sklearn для этого).
5. Ваша функция "TRAIN_ADA_BOOST" ** должна вернуть Три -элементный кортеж ** (подробнее ниже).


Функция "train_ada_boost" принимает следующие аргументы:

* X - обычно это был набор данных (но в этой Kata это 1 -й массив Numpy)
* Цель - это 1D Numpy Array, состоящий из 1 и 0.Этот аргумент - набор значений, которые мы пытаемся предсказать с нашей моделью
*Оценки - ** Аргумент ключевого слова ** Если в значении по умолчанию не следует установить аргумент в соответствии с ** 3 **.
*random_seed - ** аргумент ключевого слова ** Если в значении по умолчанию не следует установить аргумент в соответствии с ** 0 **.

Ваша функция должна вернуть 3 -элементный кортеж, состоящий из следующих значений ** в этом точном порядке **:

*** обученный ** adaboostclassifer (вернуть фактическую модель)
* Испытательный набор (1D Numpy Array, который был построен с помощью функции Sklearns test_train_split)
* Целевой массив (1D Numpy Array, который был построен с помощью функции Sklearns test_train_split)))

Подробности:

* Ваша модель должна быть обучена с использованием указанного числа оценок со случайным состоянием, равным семенам.
* При разделении данных обязательно установите случайное состояние, равное семени.
* Все остальные параметры, не упомянутые здесь как для «test_train_split», так и для «Adaboost», должны быть установлены на значения по умолчанию.
* Несмотря на то, что вы обрабатываете массивы Numpy, не нужно на самом деле манипулировать массивами сами (пусть Sklearn для вас для вас!).

Удачи!


*Обратите внимание, что в реальном машинном обучении очень маловероятно, что мы когда -нибудь будем использовать Adaboost с таким небольшим количеством оценок.Однако модели строительства могут занять очень много времени, а Codewars.com имеет тайм -аут 5000 мс.

---

Здесь происходит следующее:

Сначала мы импортируем классы AdaBoostClassifier и train_test_split из Sklearn.
Мы определяем функцию train_ada_boost, которая принимает в качестве аргументов X, target, estimators и random_seed.
Мы используем функцию train_test_split Sklearn для разделения данных на обучающую и тестовую выборки. Аргумент random_seed используется для обеспечения воспроизводимости разделения данных.
Мы обучаем модель AdaBoostClassifier на обучающих данных. Мы устанавливаем аргумент n_estimators равным estimators, аргумент random_state - random_seed.
Мы возвращаем кортеж, содержащий обученную модель, тестовую выборку и целевой массив.
Обратите внимание, что мы изменяем форму X_train, чтобы иметь форму (n_samples, n_features) со значением -1 для n_samples. Это происходит потому, что Sklearn ожидает, что обучающие данные будут иметь именно такой формат. Поскольку X_train является одномерным массивом, мы изменяем его форму, чтобы у него был один признак. Мы можем оставить X_test в виде одномерного массива, так как нам нужно только сделать предсказания на нем, а не обучать модель на нем.

---
Вы можете проверить этот код, создав тестовые данные и вызвав функцию train_ada_boost на этих данных. Например:

```python
import numpy as np

# Создаем случайные данные
X = np.random.rand(100)
target = np.random.randint(2, size=100)

# Обучаем модель AdaBoost
model, X_test, y_test = train_ada_boost(X, target)

# Делаем предсказания на тестовой выборке
y_pred = model.predict(X_test.reshape(-1, 1))

# Вычисляем точность модели
accuracy = np.mean(y_pred == y_test)

print(f"Accuracy: {accuracy}")
```
В этом примере мы создаем случайные данные размера 100 и целевой массив размера 100, состоящий из случайных 0 и 1. Затем мы вызываем функцию train_ada_boost на этих данных, получая обученную модель, тестовую выборку и целевой массив. Затем мы делаем предсказания на тестовой выборке, используя метод predict модели, и вычисляем точность модели, сравнивая предсказанные метки классов с реальными метками классов.