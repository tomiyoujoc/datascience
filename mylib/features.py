# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

def convert_2Darray(X):
    if hasattr(X, 'values'):
        X = X.values
    if len(X.shape) == 1:
        X = X.reshape(-1, 1)
    else:
        return None
    return X

def make_polynomial_features(X, degree):
    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    X_poly = poly.fit_transform(X)
    return pd.DataFrame(X_poly, columns=poly.get_feature_names()), poly

def select_by_anova(X, y, percentile=.5):
    from sklearn.feature_selection import SelectPercentile
    select = SelectPercentile(percentile=percentile)
    return select.fit_transform(X, y), select

def select_by_model(model, X, y, threshold=None):
    from sklearn.feature_selection import SelectFromModel
    select = SelectFromModel(model, threshold=threshold)
    return select.fit_transform(X, y), select

def select_by_rfe(model, X, y, n=None):
    from sklearn.feature_selection import RFE
    select = RFE(model, n_features_to_select=n)
    return select.fit_transform(X, y), select

def __test_make_polynomial_features():
    #sklearnは、2D配列を受け付ける（たとえ1つの特徴量しかなくても）
    #numpy 1D -> そのままではエラー
    X_np1d = np.arange(10)
    X_np1dto2d = convert_2Darray(X_np1d)
    make_polynomial_features(X_np1dto2d, 2)
    #numpy 2D
    X_np2d = np.arange(10).reshape(-1, 2)
    make_polynomial_features(X_np2d, 2)
    #Series(1D) -> そのままではエラー
    X_ser = pd.Series(np.arange(10))
    X_serto2d = convert_2Darray(X_ser)
    make_polynomial_features(X_serto2d, 2)
    #DataFrame(Seriesを取り出すケース) -> そのままではエラー
    X_df = pd.DataFrame(np.arange(10))
    X_dfto2d = convert_2Darray(X_df[0])
    make_polynomial_features(X_dfto2d, 2)
    #DataFrame（DataFrameのまま渡す）
    make_polynomial_features(X_df, 2)
