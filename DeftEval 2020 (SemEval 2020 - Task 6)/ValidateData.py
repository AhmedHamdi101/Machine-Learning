from sklearn.model_selection import train_test_split, cross_val_score


def Validate(TrainTexts, TrainLabels, fitModel):
    # X_train, X_test, y_train, y_test = train_test_split(TrainTexts, TrainLabels, test_size=0.3, random_state=0)
    Score = cross_val_score(fitModel, TrainTexts, TrainLabels, cv=5, scoring='f1_macro').mean()
    return Score
