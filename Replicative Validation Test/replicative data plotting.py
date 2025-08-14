import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/Python Replicative Validation.xlsx"
sheet_mar = pd.read_excel(file_path, sheet_name="Validation MAR", engine="openpyxl", header=None)

# Extract the years for the MAR sheet (2001–2012)
years_mar = list(map(int, sheet_mar.iloc[0, 1:13]))

# Define variable groups
population_vars = [
    "Regional Population", "Regional Population: model",
    "Children", "Children: model",
    "Young Adults", "Young adults: model",
    "Adults in the workforce", "Adults in the workforce: model",
    "Adults after retirement", "Adults after retirement: model"
]

workforce_vars = [
    "Workforce employed in knowledge intensive activities in sector", 
    "Workforce employed in knowledge intensive activities[Telecommunication]: model",
    "Students", "Students: model",
    "Knowledge workforce in public R&D", "knowledge workforce in public R&D: model"
]

knowledge_vars = [
    "Internal knowledge size", 
    "Industry knowledge size[Telecommunication]: model"

]

rd_vars = [
    "R&D expenditure in Sector", 
    "R&D expenditure in Sector[Telecommunication]: model"
]

# Create a mapping from variable name to row index
var_to_index = {sheet_mar.iloc[i, 0]: i for i in range(1, len(sheet_mar))}

# Function to plot grouped variables
def plot_grouped_variables(var_list, title, years, filename):
    plt.figure(figsize=(14, 8))
    used_colors = {}
    color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
    color_index = 0

    for i in range(0, len(var_list), 2):
        var_measured = var_list[i]
        var_model = var_list[i+1]

        if var_measured not in var_to_index or var_model not in var_to_index:
            continue

        idx_measured = var_to_index[var_measured]
        idx_model = var_to_index[var_model]

        data_measured = sheet_mar.iloc[idx_measured, 1:1+len(years)].astype(float)
        data_model = sheet_mar.iloc[idx_model, 1:1+len(years)].astype(float)

        # Assign a color for this pair
        color = color_cycle[color_index % len(color_cycle)]
        color_index += 1

        # Plot measured and modelled
        plt.plot(years, data_measured, label=var_measured, linestyle='-', color=color)
        plt.plot(years, data_model, label=var_model, linestyle='--', color=color)

    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.grid(False)  # Remove gridlines
    plt.tight_layout()
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=8, frameon=False)
    plt.show()

# Plot each group MAR
plot_grouped_variables(population_vars, "Population (Replicative Validation MAR)", years_mar, "C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/population_plot MAR.png")
plot_grouped_variables(workforce_vars, "Workforce (Replicative Validation MAR)", years_mar, "C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/workforce_plot MAR.png")
plot_grouped_variables(knowledge_vars, "Knowledge Size (Replicative Validation MAR)", years_mar, "C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/knowledge_plot MAR.png")
plot_grouped_variables(rd_vars, "R&D Expenditure (Replicative Validation MAR)", years_mar, "C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/rd_plot MAR.png")