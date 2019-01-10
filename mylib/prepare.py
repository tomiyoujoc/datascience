# -*- coding: utf-8 -*-

def split_data(data, y, train_rate=0.7, random_state=0):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(data.drop(y, axis=1), 
                                                        data[y],
                                                        stratify=data[y],
                                                        random_state=random_state,
                                                        train_size=train_rate)
    print("X_train:{}\ny_train:{}".format(X_train.shape, y_train.shape))
    print("X_test :{}\ny_test :{}".format(X_test.shape, y_test.shape))
    return X_train, X_test, y_train, y_test