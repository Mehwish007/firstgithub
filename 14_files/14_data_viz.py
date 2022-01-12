#steps involved in data visualization
#import libraries
import seaborn as sns
import matplotlib.pyplot as plt
#step-2 set a theme
sns.set_theme(style="ticks",color_codes=True)
#step-3 import data set you can also import your own data
titanic=sns.load_dataset("titanic")
#print(titanic.describe)
# step-4 plot basic graph with one variable
p=sns.countplot(x="sex", data=titanic)
plt.show()

#step-5  plot basic graph with two variables
p=sns.countplot(x="sex", data=titanic, hue="class")
plt.show()
 
#step-6  plot basic graph with two variables and setting a title for graph
p=sns.countplot(x="sex", data=titanic, hue="class")
p.set_title("plot for basic count")
plt.show()
