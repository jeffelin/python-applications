import sklearn
from sklearn import svm, preprocessing
from sklearn.linear_model import SGDRegressor
import pandas as pd


data = pd.read_csv(r'python-applications\data_analysis\diamond\diamond\diamonds.csv')
df = sklearn.utils.shuffle(data) # always shuffle your data to avoid any biases that may emerge b/c of some order.

X = df.drop("price", axis=1).values
y = df["price"].values

test_size = 200
test_size = 200

X_train = X[:-test_size]
y_train = y[:-test_size]

X_test = X[-test_size:]
clf = SGDRegressor(max_iter=1000)
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))

for X,y in list(zip(X_test, y_test))[:10]:
    print(clf.predict([X])[0], y)


def first_model_predition(X_train, y_train, X_test, y_test): 
    clf = svm.SVR()

    clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))
    clf = SGDRegressor(max_iter=10000)

    clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))
    for X,y in list(zip(X_test, y_test))[:10]:
    print(clf.predict([X])[0], y)

    for X,y in list(zip(X_test, y_test))[:10]:
        print(clf.predict([X])[0], y)

def second_model_prediction(data): 

    df = sklearn.utils.shuffle(data) # always shuffle your data to avoid any biases that may emerge b/c of some order.

    X = df.drop("price", axis=1).values
    X = preprocessing.scale(X)
    y = df["price"].values

    test_size = 200

    X_train = X[:-test_size]
    y_train = y[:-test_size]

    X_test = X[-test_size:]
    y_test = y[-test_size:]

    clf = svm.SVR()

    clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test)) # accuracy 

    for X,y in list(zip(X_test, y_test))[:10]:
        print(f"model predicts {clf.predict([X])[0]}, real value: {y}")