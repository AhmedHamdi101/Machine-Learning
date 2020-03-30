from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix, \
    classification_report


def Test(Predicition, TestLabels, Model, Table, CVScore):
    conf_mat = confusion_matrix(Predicition, TestLabels)
    # ratio of correctly predicted observation to the total observations
    accuracy = round(accuracy_score(TestLabels, Predicition), 2)
    # ratio of correctly predicted positive observations to the total
    # predicted positive observations
    precision = round(precision_score(TestLabels, Predicition), 2)
    # ratio of correctly predicted positive observations to the all
    # observations in actual class
    recall = round(recall_score(TestLabels, Predicition), 2)
    # weighted average of Precision and Recall
    f1 = round(f1_score(TestLabels, Predicition), 2)
    # Mean of F1-score cross validated 5 consecutive times (with different splits each time)
    CVScore = round(CVScore, 2)
    print(Model)
    print(classification_report(TestLabels, Predicition))
    Table.add_row([Model, conf_mat, accuracy, precision, recall, f1, CVScore])

