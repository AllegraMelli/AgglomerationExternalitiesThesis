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

#def format_real_parameter(full_name, initial_value):
#     lower = initial_value * 0.8
#     upper = initial_value * 1.2
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
RealParameter('Attrition rate in sector[Telecommunication]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Manufacturing of communication equipment]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Average mortality per age[Age0to17]', 0.0026399999856948856, 0.003959999978542328),
RealParameter('Average mortality per age[Age18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Students]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Age25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Graduates25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Age45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Graduates45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Age65toLifeExpectancy]', 0.031999999284744264, 0.04799999892711639),
RealParameter('Average Time to Market in Sector[Telecommunication]', 4.0, 6.0),
RealParameter('Average Time to Market in Sector[Manufacturing of communication equipment]', 4.0, 6.0),
RealParameter('External investments', 8000.0, 12000.0),
RealParameter('"Government funding for public R&D in sector"', 19512000.0, 29268000.0),
RealParameter('Hiring and training time of employees', 1.6, 2.4),
RealParameter('Knowledge obsolescence time', 8.0, 12.0),
RealParameter('Percentage of adults enrolling in studies', 0.007156927883625031, 0.010735391825437545),
RealParameter('Percentage of innovative SMEs collaborating with others', 0.42480001449584964, 0.6372000217437744),
RealParameter('Percentage of profit from revenue in Sector[Telecommunication]', 0.32448000907897956, 0.4867200136184693),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of communication equipment]', 0.28255999088287354, 0.4238399863243103),   
RealParameter('"Percentage of R&D budget on total budget in Sector"[Telecommunication]', 0.2574399948120117, 0.3861599922180175),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of communication equipment]', 0.18503999710083008, 0.2775599956512451),
RealParameter('Percentage of workforce wanting to go the private sector', 0.5599999904632569, 0.8399999856948852),
RealParameter('"Percentage of workforce wanting to go to R&D"', 0.3200000047683716, 0.48000000715255736),
RealParameter('"Public Funding for Private R&D in Sector"[Telecommunication]', 0.010960000008344649, 0.01644000001251697),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of communication equipment]', 0.02903999984264374, 0.04355999976396561),   
RealParameter('"Public R&D expenditure per personel"', 118125.6, 177188.4),
RealParameter('"Public-private collaboration per academic"', 0.0515999972820282, 0.0773999959230423),
RealParameter('Relative share women in fertile age', 0.4, 0.6),
RealParameter('Relatedness[Telecommunication,Manufacturing of communication equipment]', 0.8, 1),
RealParameter('Relatedness[Manufacturing of communication equipment,Telecommunication]', 0.8, 1)
]

    model.outcomes = [
            TimeSeriesOutcome(f'Industry knowledge size[{s}]') for s in sector_names
        ]
    results = perform_experiments(model, 2000)
    save_results(results, "./sobol scenario run Base MAR.tar.gz")

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
    """
    cluster_colors = {'High': 'firebrick', 'Middle': 'darkorange', 'Low': 'royalblue'}

    for i in range(len(sector_names)):
        fig = plt.figure(figsize=(18, 8))
        fig.suptitle("Scenario Cluster Analysis", fontsize=16, y=1.02)

        gs = gridspec.GridSpec(1, 4, width_ratios=[4, 1, 4, 1], wspace=0.1)

        sector1 = sector_names[i]
        ax1_main = fig.add_subplot(gs[0, 0])
        ax1_density = fig.add_subplot(gs[0, 1], sharey=ax1_main)

        process_and_plot_sector(fig, ax1_main, ax1_density, outcomes, sector1, cluster_colors, show_ylabel=True)

        handles, labels = ax1_main.get_legend_handles_labels()
        fig.legend(handles, labels, loc='center right', bbox_to_anchor=(0.5, 0.95), ncol=3, title="Scenario Cluster")

        fig.tight_layout(rect=[0, 0, 1, 0.93])
        plt.show()

def process_and_plot_sector(fig, ax_main, ax_density, outcomes, sector_name, cluster_colors, show_ylabel=True):
    """Helper function to perform clustering and plotting for a single sector."""
    
    outcome_key = f'Industry knowledge size[{sector_name}]'
    data = outcomes[outcome_key]
    full_time = np.arange(data.shape[1])
    mask = (full_time >= 0) & (full_time <= 20)
    time = full_time[mask]
    data = data[:, mask]

    # --- 1. Cluster the scenarios ---
    # Get the final value of each simulation run
    final_values = data[:, -1]
    
    # Find the 33rd and 66th percentiles to define the cluster boundaries
    low_threshold = np.percentile(final_values, 33)
    high_threshold = np.percentile(final_values, 66)
    
    # Create boolean masks to identify which runs belong to which cluster
    low_mask = final_values <= low_threshold
    high_mask = final_values >= high_threshold
    # The middle mask includes runs that are not in the low or high groups
    middle_mask = (~low_mask) & (~high_mask)
    
    clusters = {
        'High': data[high_mask, :],
        'Middle': data[middle_mask, :],
        'Low': data[low_mask, :]
    }

    # --- 2. Plot the time-series trajectories ---
    time = np.arange(data.shape[1])
    for name, cluster_data in clusters.items():
        if cluster_data.shape[0] > 0: # Check if cluster is not empty
            # Plot each run with some transparency (alpha)
            for run in cluster_data:
                ax_main.plot(time, run, color=cluster_colors[name], alpha=0.3)
            # Add a single line for the legend entry
            ax_main.plot([], [], color=cluster_colors[name], label=name)

    ax_main.set_title(sector_name)
    ax_main.set_xlabel("Time")
    if show_ylabel:
        ax_main.set_ylabel("Knowledge Size")
    ax_main.xaxis.grid(False)
    ax_main.yaxis.grid(False)

    # --- 3. Create and plot the density plots for the final time step ---
    # Define a range of values for the y-axis of the density plot
    min_val, max_val = ax_main.get_ylim()
    y_vals = np.linspace(min_val, max_val, 500)
    
    for name, cluster_data in clusters.items():
        if cluster_data.shape[0] > 1: # KDE requires at least 2 data points
            final_time_data = cluster_data[:, -1]
            # Create the Kernel Density Estimate
            kde = gaussian_kde(final_time_data)
            # Evaluate the density over our y-value range
            density = kde(y_vals)
            # Plot the density curve horizontally
            ax_density.plot(density, y_vals, color=cluster_colors[name], label=name)
            # Fill the area under the curve for better visualization
            ax_density.fill_betweenx(y_vals, 0, density, color=cluster_colors[name], alpha=0.4)

    ax_density.set_xlabel("Density")
    ax_density.set_title("Final Time", fontsize=10)
    # Hide the tick labels and the axis line itself for a cleaner look
    ax_density.set_xticks([])
    ax_density.spines['bottom'].set_visible(False)
    ax_density.spines['right'].set_visible(False)
    ax_density.spines['top'].set_visible(False)
    plt.setp(ax_density.get_yticklabels(), visible=False)
    # ————————————————————————
    # 3. call the plotting function
    # ————————————————————————

# Call the main plotting function with your results
plot_clustered_scenarios(experiments, outcomes, sector_names)
    
    # Display all the generated figures
plt.show()