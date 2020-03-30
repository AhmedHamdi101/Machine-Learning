from sklearn.feature_extraction.text import CountVectorizer
from CleanData import Clean


def Count(Train_Texts, Train_Labels, Test_Texts, Test_Labels):
    print("Number of Train Data Sentences :", len(Train_Texts))
    i = 0
    size = 0
    for k in range(len(Train_Labels)):
        if Train_Labels[i] == 1:
            size = size + 1
        i = i + 1
    print("--> Definition :", size, "\n" "--> Not Definition :",
          len(Train_Texts) - size)
    print(" ")
    print("Number of Test Data Sentences :", len(Test_Texts))
    i = 0
    size = 0
    for k in range(len(Test_Labels)):
        if Test_Labels[i] == 1:
            size = size + 1
        i = i + 1
    print("--> Definition :", size, "\n" "--> Not Definition :",
          len(Test_Texts) - size)

    cv = CountVectorizer()
    word_count_vector = cv.fit_transform(Train_Texts)

    print(" ")
    print("Training Vocabulary before pre-processing :", word_count_vector.shape[1])
    word_count_vector = cv.fit_transform(Test_Texts)
    print("Testing Vocabulary before pre-processing :", word_count_vector.shape[1])
    print(" ")

    Clean(Train_Texts)
    Clean(Test_Texts)

    word_count_vector = cv.fit_transform(Train_Texts)
    print("Training Vocabulary after pre-processing :", word_count_vector.shape[1])
    word_count_vector = cv.fit_transform(Test_Texts)
    print("Testing Vocabulary after pre-processing : ", word_count_vector.shape[1])
    print(" ")
    print(" ")