from ema_workbench import (TimeSeriesOutcome, perform_experiments, RealParameter, ema_logging, save_results, load_results, MultiprocessingEvaluator)
from ema_workbench.analysis import lines, Density, pairs_plotting, plotting
from ema_workbench.connectors.vensim import VensimModel

import matplotlib.gridspec as gridspec
from scipy.stats import gaussian_kde
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from sklearn.cluster import KMeans

# def format_real_parameter(full_name, initial_value):
#     lower = initial_value * 0
#     upper = initial_value * 0.01
#     return f"RealParameter('{full_name}', {lower}, {upper}),"

# # Load Excel file — no headers
# df = pd.read_excel('C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/change1 MAR.xlsx', header=None)

# # Loop through rows
# for index, row in df.iterrows():
#     name = str(row[0]).strip()
#     try:
#         value = float(row[1])
#         output = format_real_parameter(name, value)
#         print(output)
#     except ValueError:
#         print(f"Invalid number at row {index + 1}: {row[1]}")


sector_names = ["Telecommunication", "Manufacturing of communication equipment"]

if __name__ == "__main__":
    # turn on logging
    ema_logging.log_to_stderr(ema_logging.INFO)
    wd = r'OneDrive - Delft University of Technology/Master Thesis'

    model = VensimModel("MARModel", wd=wd, model_file=r'MAR region France_improved.vpmx')


    model.uncertainties = [
RealParameter('Attrition rate in sector[Telecommunication]', 0.0, 0.0002500000037252903),
RealParameter('Attrition rate in sector[Manufacturing of communication equipment]', 0.0, 0.0002500000037252903),
RealParameter('Average mortality per age[Age0to17]', 0.0, 3.299999982118607e-05),
RealParameter('Average mortality per age[Age18to24]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Students]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Age25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Graduates25to45]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Age45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Graduates45to65]', 0.0, 2.000000094994903e-05),
RealParameter('Average mortality per age[Age65toLifeExpectancy]', 0.0, 0.0003999999910593033),
RealParameter('Average Time to Market in Sector[Telecommunication]', 0.0, 0.05),
RealParameter('Average Time to Market in Sector[Manufacturing of communication equipment]', 0.0, 0.05),
RealParameter('External investments', 0.0, 100.0),
RealParameter('"Government funding for public R&D in sector"', 0.0, 243900.0),
RealParameter('Hiring and training time of employees', 0.0, 0.02),
RealParameter('Initial Added Value in Sector[Telecommunication]', 0.0, 30000000.0),
RealParameter('Initial Added Value in Sector[Manufacturing of communication equipment]', 0.0, 20000000.0),
RealParameter('"Initial Employed R&D Workforce in Sector"[Telecommunication]', 0.0, 10.93),
RealParameter('"Initial Employed R&D Workforce in Sector"[Manufacturing of communication equipment]', 0.0, 9.88),
RealParameter('Initial knowledge specialisation in Sector[Telecommunication]', 0.0, 1.99),
RealParameter('Initial knowledge specialisation in Sector[Manufacturing of communication equipment]', 0.0, 0.07),
RealParameter('Initial population[Age0to17]', 0.0, 7363.53),
RealParameter('Initial population[Age18to24]', 0.0, 2610.77),
RealParameter('Initial population[Students]', 0.0, 23.35639892578125),
RealParameter('Initial population[Age25to45]', 0.0, 12761.0),
RealParameter('Initial population[Graduates25to45]', 0.0, 20.0),
RealParameter('Initial population[Age45to65]', 0.0, 20.0),
RealParameter('Initial population[Graduates45to65]', 0.0, 19.650000000000002),
RealParameter('Initial population[Age65toLifeExpectancy]', 0.0, 6807.91),
RealParameter('Knowledge obsolescence time', 0.0, 0.1),
RealParameter('Percentage of adults enrolling in studies', 0.0, 8.946159854531288e-05),
RealParameter('Percentage of innovative SMEs collaborating with others', 0.0, 0.00531000018119812),
RealParameter('Percentage of profit from revenue in Sector[Telecommunication]', 0.0, 0.0040560001134872445),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of communication equipment]', 0.0, 0.003531999886035919),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Telecommunication]', 0.0, 0.003217999935150146),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of communication equipment]', 0.0, 0.0023129999637603762),       
RealParameter('Percentage of workforce wanting to go the private sector', 0.0, 0.006999999880790711),
RealParameter('"Percentage of workforce wanting to go to R&D"', 0.0, 0.004000000059604645),
RealParameter('"Public Funding for Private R&D in Sector"[Telecommunication]', 0.0, 0.0001370000001043081),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of communication equipment]', 0.0, 0.00036299999803304675),
RealParameter('"Public R&D expenditure per personel"', 0.0, 1476.57),
RealParameter('"Public-private collaboration per academic"', 0.0, 0.0006449999660253525),
RealParameter('Relative share women in fertile age', 0.0, 0.005)
]

    model.outcomes = [
        TimeSeriesOutcome(f'Industry knowledge size[{s}]') for s in sector_names
    ] + [
        TimeSeriesOutcome(f'Workforce employed in knowledge intensive activities[{s}]') for s in sector_names
    ]

    results = perform_experiments(model, 2000)
    save_results(results, "./Extreme Low values MAR.tar.gz")

    experiments, outcomes = results
   # ————————————————————————
    # 2. plotting function
    # ————————————————————————

def plot_clustered_scenarios(experiments, outcomes, sector_names):
    """
    Analyzes and plots simulation outcomes by clustering them into three groups
    (high, middle, low) based on their final values.

    For each sector, it generates:
    1. A time-series plot showing the trajectories of each cluster.
    2. A density plot showing the distribution of final values for each cluster.

    The function creates 5 plot windows, each displaying the results for two sectors.

    Args:
        experiments (pd.DataFrame): The experimental design.
        outcomes (dict): A dictionary where keys are outcome names and values are
                         numpy arrays of the simulation results.
        sector_names (list): A list of the sector names to be plotted.

    Modified to plot both 'Industry knowledge size' and 
    'Workforce wanting to work in academia & public research' per sector.
    """
    cluster_colors = {'High': 'firebrick', 'Middle': 'darkorange', 'Low': 'royalblue'}

    for i in range(len(sector_names)):
        fig = plt.figure(figsize=(18, 8))
        fig.suptitle("Scenario Cluster Analysis", fontsize=16, y=1.02)

        # Adjusted to 2 outcomes per sector: 2 main plots and 2 density plots
        gs = gridspec.GridSpec(1, 4, width_ratios=[4, 1, 4, 1], wspace=0.1)

        sector = sector_names[i]

        # Plot for 'Industry knowledge size'
        ax1_main = fig.add_subplot(gs[0, 0])
        ax1_density = fig.add_subplot(gs[0, 1], sharey=ax1_main)
        process_and_plot_sector(fig, ax1_main, ax1_density, outcomes, sector, 
                                'Industry knowledge size', cluster_colors, show_ylabel=True)

        # Plot for 'Workforce wanting to work in academia & public research'
        ax2_main = fig.add_subplot(gs[0, 2])
        ax2_density = fig.add_subplot(gs[0, 3], sharey=ax2_main)
        process_and_plot_sector(fig, ax2_main, ax2_density, outcomes, sector, 
                                'Workforce employed in knowledge intensive activities', cluster_colors, show_ylabel=False)

        handles, labels = ax1_main.get_legend_handles_labels()
        fig.legend(handles, labels, loc='center right', bbox_to_anchor=(0.5, 0.95), ncol=3, title="Scenario Cluster")

        fig.tight_layout(rect=[0, 0, 1, 0.93])
        plt.show()

def process_and_plot_sector(fig, ax_main, ax_density, outcomes, sector_name, outcome_prefix, cluster_colors, show_ylabel=True):
    """Helper function to perform clustering and plotting for a single outcome of a sector."""
    
    outcome_key = f'{outcome_prefix}[{sector_name}]'
    data = outcomes[outcome_key]
    full_time = np.arange(data.shape[1])
    mask = (full_time >= 0) & (full_time <= 20)
    time = full_time[mask]
    data = data[:, mask]

    final_values = data[:, -1]
    low_threshold = np.percentile(final_values, 33)
    high_threshold = np.percentile(final_values, 66)

    low_mask = final_values <= low_threshold
    high_mask = final_values >= high_threshold
    middle_mask = (~low_mask) & (~high_mask)

    clusters = {
        'High': data[high_mask, :],
        'Middle': data[middle_mask, :],
        'Low': data[low_mask, :]
    }

    time = np.arange(data.shape[1])
    for name, cluster_data in clusters.items():
        if cluster_data.shape[0] > 0:
            for run in cluster_data:
                ax_main.plot(time, run, color=cluster_colors[name], alpha=0.3)
            ax_main.plot([], [], color=cluster_colors[name], label=name)

    ax_main.set_title(f"{outcome_prefix} - {sector_name}")
    ax_main.set_xlabel("Time")
    if show_ylabel:
        ax_main.set_ylabel("Value")
    ax_main.xaxis.grid(False)
    ax_main.yaxis.grid(False)

    min_val, max_val = ax_main.get_ylim()
    y_vals = np.linspace(min_val, max_val, 500)

    for name, cluster_data in clusters.items():
        if cluster_data.shape[0] > 1:
            final_time_data = cluster_data[:, -1]
            kde = gaussian_kde(final_time_data)
            density = kde(y_vals)
            ax_density.plot(density, y_vals, color=cluster_colors[name], label=name)
            ax_density.fill_betweenx(y_vals, 0, density, color=cluster_colors[name], alpha=0.4)

    ax_density.set_xlabel("Density")
    ax_density.set_title("Final Time", fontsize=10)
    ax_density.set_xticks([])
    ax_density.spines['bottom'].set_visible(False)
    ax_density.spines['right'].set_visible(False)
    ax_density.spines['top'].set_visible(False)
    plt.setp(ax_density.get_yticklabels(), visible=False)
    
    # ————————————————————————
    # 3. call the plotting function
    # ————————————————————————

# Call the main plotting function with your results
#plot_clustered_scenarios(experiments, outcomes, sector_names)
    
    # Display all the generated figures
#plt.show()