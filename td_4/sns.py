import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset("tips")
print(df.head(10))
# scatterplot / nuage de points
plt.figure()
plot = sns.scatterplot(x='total_bill',y='tip',data=df)
plt.show()
# lineplot / courbe
plt.figure()
plot = sns.lineplot(x='day',y='total_bill',data=df)
plt.show()
# barplot
plt.figure()
plot = sns.barplot(x='day',y='total_bill',data=df)
plt.show()
# boxplot / boite a moustaches
plt.figure()
plot = sns.boxenplot(x='day',y='total_bill',data=df)
plt.show()
# histoplot / histogramme
plt.figure()
plot = sns.histplot(x='total_bill',y='tip',data=df)
plt.show()