# Метод опорных векторов (SVM - support vector machine) - классификация и
# регрессия
# Разделяющая классификация

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.svm import SVC


# iris = sns.load_dataset('iris')
# print(iris.head())

# data = iris[["sepal_length", "petal_length", "species"]]
# data_df = data[(data["species"] == "setosa") | (data["species"] == "versicolor")]

# X = data_df[["sepal_length", "petal_length"]]
# y = data_df["species"]

# data_df_setosa = data_df[data_df["species"] == "setosa"]
# data_df_versicolor = data_df[data_df["species"] == "versicolor"]

# plt.scatter(data_df_setosa["sepal_length"], data_df_setosa["petal_length"])
# plt.scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])

# model = SVC(kernel='linear', C=10000)
# model.fit(X, y)

# print(model.support_vectors_)

# plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=200, facecolor='none', edgecolors='black')

# x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]))
# x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]))

# X1_p, X2_p = np.meshgrid(x1_p, x2_p)

# X_p = pd.DataFrame(
#     np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
# )
# y_p = model.predict(X_p)
# X_p["species"] = y_p

# X_p_setosa = X_p[X_p["species"] == "setosa"]
# X_p_versicolor = X_p[X_p["species"] == "versicolor"]

# plt.scatter(X_p_setosa["sepal_length"], X_p_setosa["petal_length"], alpha=0.4)
# plt.scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha=0.4)

# ДЗ. Убрать из данных iris часть точек, на которых обучаемся, и убедиться,
# что на предсказание влияют только опорные векторы.

# В случае, если данные перекрываются, то идеальной границы не существует. Для
# этого нужен гиперпараметр, который определяет размытие отступа.

iris = sns.load_dataset('iris')
print(iris.head())

data = iris[["sepal_length", "petal_length", "species"]]
data_df = data[(data["species"] == "virginica") | (data["species"] == "versicolor")]

X = data_df[["sepal_length", "petal_length"]]
y = data_df["species"]

data_df_virginica = data_df[data_df["species"] == "virginica"]
data_df_versicolor = data_df[data_df["species"] == "versicolor"]

c_value = [[10000, 1000, 100, 10], [1, 0.1, 0.01, 0.001]]
fig, ax = plt.subplots(2, 4)

x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]))
x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]))

X1_p, X2_p = np.meshgrid(x1_p, x2_p)

X_p = pd.DataFrame(
    np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
)
# print(X_p.head())

for i in range(2):
    for j in range(4):
        ax[i, j].scatter(data_df_virginica["sepal_length"], data_df_virginica["petal_length"])
        ax[i, j].scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])

# plt.scatter(data_df_virginica["sepal_length"], data_df_virginica["petal_length"])
# plt.scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])

        # Если C большое, то отступ задается жестко. Чем меньше C, тем более размытый отступ.
        model = SVC(kernel='linear', C=c_value[i][j])
        model.fit(X, y)

        # print(model.support_vectors_)

        ax[i, j].scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=200, facecolor='none', edgecolors='black')
        
        x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]))
        x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]))

        X1_p, X2_p = np.meshgrid(x1_p, x2_p)

        X_p = pd.DataFrame(
            np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
        )

        y_p = model.predict(X_p)
        X_p["species"] = y_p

        X_p_virginica = X_p[X_p["species"] == "virginica"]
        X_p_versicolor = X_p[X_p["species"] == "versicolor"]

        ax[i, j].scatter(X_p_virginica["sepal_length"], X_p_virginica["petal_length"], alpha=0.1)
        ax[i, j].scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha=0.1)


plt.show()

# Достоинства
# - зависимость от небольшого числа опорных векторов - компактность модели
# - после обучения предсказания проходят очень быстро
# - на работу метода влияют ТОЛЬКО точки, находящиеся возле отступов, поэтому эти методы подходят для многомерных данных

# Недостатки:
# - при большом количестве обучающих образцов могут быть значительные вычислительные затраты
# - большая зависимость от параметра C. Поиск может привести к большим вычислительным затратам.
# - у результатов отсутствует вероятностная интерпретация
