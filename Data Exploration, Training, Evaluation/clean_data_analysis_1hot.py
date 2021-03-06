import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)
data = pd.read_csv("cardio_train_clean_1hot.csv")
print(data.describe())
#checking the distribution between features of patients who have CVD and who do not have CVD
data_array = data.to_numpy()
string = ["does not have CVD", "has CVD"]
n,m = data_array.shape
str = ['gender', 'chlosterol', 'glucose', 'smoke', 'alcohol', 'active']
id = [2, 7, 8, 9, 10, 11]
d = len(str)

for cvd in range(2):
    index = np.nonzero(data_array[:, -1] == cvd)
    k = len(index[0])
    #print(index)

    bin_array = np.zeros(d)

    for i in range(d):
        bin = 0
        for j in range(k):
            if data_array[index[0][j], id[i]] == 1:
                bin += 1
        bin_array[i] = bin / k

    bin_array2 = np.ones(d)
    bin_array2 -= bin_array
    df = pd.DataFrame({'0': bin_array2, '1': bin_array}, index=str)
    ax = df.plot.bar(title = 'If patient ' + string[cvd], rot=0)
    plt.ylim(0, 1)
    plt.show()

#correlation matrix using r
sns.set(rc={'figure.figsize': (11.7, 8.27)})
corr_matrix = data.corr()
sns.heatmap(corr_matrix, annot=True, fmt='0.2f')
plt.show()
#correction matrix using r^2
corr_matrix = data.corr()
sns.heatmap(corr_matrix*corr_matrix, annot=True, fmt='0.2f')
plt.show()


