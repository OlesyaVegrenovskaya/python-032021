import pandas
import requests

from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    accuracy_score,
)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/reviews.csv")
open("reviews.csv", "wb").write(r.content)
data = pandas.read_csv("reviews.csv")
X = data["review"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
y_train.value_counts(normalize=True).plot(kind="bar")

pipeline = Pipeline(
    [
        ("vec", TfidfVectorizer(stop_words="english")),
        ("clf", KNeighborsClassifier(n_neighbors=10)),
    ]
)
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(f"accuracy: {round(accuracy_score(y_test, y_pred), 2)}", f"f1 score: {round(f1_score(y_test, y_pred, average='weighted'), 2)}")
