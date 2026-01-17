import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "name":["yahya","abdessamad","oussama","ali","zakaria","illiasse"],
    "maths":[10,8,9,16,10,14],
    "python":[14,14,16,10,18,16]
}

data_frame = pd.DataFrame(data)
print("data frame")
print(data_frame)
print("1st 5 records")
print(data_frame.head(5))
print("avg python note")
print(data_frame["python"].mean())
print("avg maths note")
print(data_frame["maths"].mean())
data_frame["note"]=(data_frame["maths"]+data_frame["python"])/2
print(data_frame)

plt.figure()
plot = sns.barplot(x='name',y='note',data=data_frame)
plt.title("final note of each student")
plt.xlabel("students")
plt.ylabel("final note")
plt.show()