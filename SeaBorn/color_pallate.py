import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Display the current color palette
current_palette = sns.color_palette()
sns.palplot(current_palette)
plt.title("Current Color Palette")
plt.show()

# Set a new color palette (e.g., "deep")
sns.set_palette("deep")
plt.show()

qualitative_palette = sns.color_palette("Set2")
sns.palplot(qualitative_palette)
plt.title("Qualitative Palette: Set2")
plt.show()