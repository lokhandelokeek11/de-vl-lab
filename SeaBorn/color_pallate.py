import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

#Qualitative colour paletts
current_palette = sns.color_palette()
sns.palplot(current_palette)
plt.title("Current Color Palette")
plt.show()

#Sequential colour paletts
current_palette2 = sns.color_palette()
sns.palplot (sns.color_palette("Reds",12))
plt.show()
    
#Diverging colour palette

current_palette3 = sns.color_palette()
sns.palplot(sns.color_palette("BrBG",20))
plt.show()