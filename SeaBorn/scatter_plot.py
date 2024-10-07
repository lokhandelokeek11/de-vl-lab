import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action="ignore", category= FutureWarning)

# Load the built-in 'tips' dataset
tips = sns.load_dataset("tips")

print(tips.head())

sns.lineplot(x = "day" , y = "total_bill", data = tips)
plt.show()