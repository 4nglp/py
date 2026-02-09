import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

data = pd.read_csv('students_data.csv')
print(data.head(5))
print(data.info())
print(data.describe())
# null vals
print(data.isnull().sum())
print('total avg: ',data['note'].mean())
# u hear par u group by
fil_note = data.groupby('filiere')['note'].mean()
print(fil_note)
sex_note = data.groupby('sex')['note'].mean()
print(sex_note)
# when asked for a number use len
nbr_passed = len(data[data['note']>=10])
print(nbr_passed)
# index which is the name of the fil
best_fil = fil_note.idxmax()
best_fil_note = fil_note.max()
print(best_fil, best_fil_note)



plt.figure()
sns.histplot(data['note'])
plt.xlabel("notes")
plt.show()

plt.figure()
sns.boxplot(x='filiere',y='note',data=data)
plt.xlabel("fil")
plt.ylabel("note")
plt.show()

plt.figure()
sns.countplot(x='filiere',data=data)
plt.show()

plt.figure()
sns.regplot(x='absences',y='note',data=data)
plt.show()

data['passed'] = np.where(data['note'] >= 10, 'passed', 'failed')
print(data)
passed_counts = data[data['passed'] == 'passed'].groupby('filiere')['passed'].count()
