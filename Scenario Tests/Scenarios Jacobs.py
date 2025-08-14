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

    # ————————————————————————
    # 1. set up & run experiments
    # ————————————————————————

# def format_real_parameter(full_name, initial_value):
#     lower = initial_value * 0.8
#     upper = initial_value * 1.2
#     return f"RealParameter('{full_name}', {lower}, {upper}),"

# # Load Excel file — no headers
# df = pd.read_excel('C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/current Jacobs.xlsx', header=None)

# # Loop through rows
# for index, row in df.iterrows():
#     name = str(row[0]).strip()
#     try:
#         value = float(row[1])
#         output = format_real_parameter(name, value)
#         print(output)
#     except ValueError:
#         print(f"Invalid number at row {index + 1}: {row[1]}")

if __name__ == "__main__":
    # turn on logging
    ema_logging.log_to_stderr(ema_logging.INFO)
    wd = r'OneDrive - Delft University of Technology/Master Thesis'

    model = VensimModel("JacobsModel", wd=wd, model_file=r'RECOVERED_Simple model Endgame.vpmx')

    model.uncertainties = [RealParameter('Relative share women in fertile age', 0.4, 0.6),
                           RealParameter('Attrition rate in sector[Pharmaceutical Industry]', 0.02960000038146973, 0.04440000057220459),
                           RealParameter('Attrition rate in sector[Chemical industry]', 0.020000000298023225, 0.030000000447034835),
                           RealParameter('Attrition rate in sector[Automotive industry]', 0.0239999994635582, 0.0359999991953373),
                           RealParameter('Attrition rate in sector[ICT information and services]', 0.012639999389648441, 0.01895999908447266),
                           RealParameter('Attrition rate in sector[Aerospace construction and engineering]', 0.020000000298023225, 0.030000000447034835),
                           RealParameter('Attrition rate in sector[Specialistic Technical and scientific activities]', 0.020000000298023225, 0.030000000447034835),
                            RealParameter('Attrition rate in sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.020000000298023225, 0.030000000447034835),
                            RealParameter('Attrition rate in sector[Editing audiovisual and diffusion]', 0.19440000057220458, 0.29160000085830684),
                            RealParameter('Attrition rate in sector[Manufacturing of communication equipment]', 0.020000000298023225, 0.030000000447034835),
                            RealParameter('Attrition rate in sector[Production and distribution of gas vapour and AC]', 0.020000000298023225, 0.030000000447034835),
                            RealParameter('Average Time to Market in Sector[Pharmaceutical Industry]', 9.600000000000001, 14.399999999999999),
                            RealParameter('Average Time to Market in Sector[Chemical industry]', 8.0, 12.0),
                            RealParameter('Average Time to Market in Sector[Automotive industry]', 4.800000000000001, 7.199999999999999),
                            RealParameter('Average Time to Market in Sector[ICT information and services]', 1.6, 2.4),
                            RealParameter('Average Time to Market in Sector[Aerospace construction and engineering]', 12.0, 18.0),
                            RealParameter('Average Time to Market in Sector[Specialistic Technical and scientific activities]', 4.0, 6.0),
                            RealParameter('Average Time to Market in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 4.0, 6.0),
                            RealParameter('Average Time to Market in Sector[Editing audiovisual and diffusion]', 1.6, 2.4),
                            RealParameter('Average Time to Market in Sector[Manufacturing of communication equipment]', 3.2, 4.8),
                            RealParameter('Average Time to Market in Sector[Production and distribution of gas vapour and AC]', 2.4000000000000004, 3.5999999999999996),       
                            RealParameter('External investments', 8000.0, 12000.0),
                            RealParameter('"Government funding for public R&D in sector"', 640000000.0, 960000000.0),
                            RealParameter('Hiring and training time of employees', 1.6, 2.4),
                            RealParameter('Knowledge obsolescence time', 8.0, 12.0),
                            RealParameter('Percentage of adults enrolling in studies[Health18to24]', 0.001001456007361412, 0.0015021840110421181),
                            RealParameter('Percentage of adults enrolling in studies[Chemistry18to24]', 0.00044844560325145726, 0.0006726684048771858),
                            RealParameter('Percentage of adults enrolling in studies[Process Engineering18to24]', 5.684560164809227e-05, 8.52684024721384e-05),
                            RealParameter('Percentage of adults enrolling in studies[Audiovisual18to24]', 0.0013902479782700536, 0.00208537196740508),
                            RealParameter('Percentage of adults enrolling in studies[Multidisciplinary Sciences18to24]', 0.0012498959898948672, 0.0018748439848423005),        
                            RealParameter('Percentage of adults enrolling in studies[Digital18to24]', 0.001444287970662117, 0.002166431955993175),
                            RealParameter('Percentage of adults enrolling in studies[Industry18to24]', 0.0044606000185012816, 0.006690900027751923),
                            RealParameter('Percentage of adults enrolling in studies[Mechanics18to24]', 0.00033896639943122866, 0.0005084495991468429),
                            RealParameter('Percentage of adults enrolling in studies[Physics18to24]', 0.0005712599959224463, 0.0008568899938836694),
                            RealParameter('Percentage of adults enrolling in studies[Information and communication studies18to24]', 0.0007109167985618115, 0.001066375197842717),
                            RealParameter('Percentage of profit from revenue in Sector[Pharmaceutical Industry]', 37.679998779296874, 56.5199981689453),
                            RealParameter('Percentage of profit from revenue in Sector[Chemical industry]', 36.72000122070313, 55.080001831054695),
                            RealParameter('Percentage of profit from revenue in Sector[Automotive industry]', 32.83999938964844, 49.25999908447265),
                            RealParameter('Percentage of profit from revenue in Sector[ICT information and services]', 33.23999938964844, 49.859999084472655),
                            RealParameter('Percentage of profit from revenue in Sector[Aerospace construction and engineering]', 22.0, 33.0),
                            RealParameter('Percentage of profit from revenue in Sector[Specialistic Technical and scientific activities]', 25.119999694824216, 37.679999542236324),
                            RealParameter('Percentage of profit from revenue in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 34.960000610351564, 52.44000091552734),
                            RealParameter('Percentage of profit from revenue in Sector[Editing audiovisual and diffusion]', 33.2, 49.8),
                            RealParameter('Percentage of profit from revenue in Sector[Manufacturing of communication equipment]', 22.0, 33.0),
                            RealParameter('Percentage of profit from revenue in Sector[Production and distribution of gas vapour and AC]', 63.279998779296875, 94.91999816894531),
                            RealParameter('"Percentage of R&D budget on total budget in Sector"[Pharmaceutical Industry]', 27.720001220703132, 41.580001831054695),
                            RealParameter('"Percentage of R&D budget on total budget in Sector"[Chemical industry]', 14.727999877929689, 22.091999816894532),
                            RealParameter('"Percentage of R&D budget on total budget in Sector"[Automotive industry]', 15.847999572753904, 23.771999359130856),
                            RealParameter('"Percentage of R&D budget on total budget in Sector"[ICT information and services]', 5.231999969482422, 7.847999954223632),
                            RealParameter('"Percentage of R&D budget on total budget in Sector"[Aerospace construction and engineering]', 77.67999877929688, 116.5199981689453),
                            RealParameter('"Percentage of R&D budget on total budget in Sector"[Specialistic Technical and scientific activities]', 31.504000854492183, 47.25600128173827),
                            RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 19.119999694824216, 28.679999542236324),
                            RealParameter('"Percentage of R&D budget on total budget in Sector"[Editing audiovisual and diffusion]', 10.576000213623049, 15.864000320434572),  
                            RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of communication equipment]', 25.864001464843753, 38.79600219726562),
                            RealParameter('"Percentage of R&D budget on total budget in Sector"[Production and distribution of gas vapour and AC]', 6.1200000762939455, 9.180000114440917),
                            RealParameter('Percentage of workforce wanting to go the private sector', 0.5599999904632569, 0.8399999856948852),
                            RealParameter('"Percentage of workforce wanting to go to R&D"', 0.3200000047683716, 0.48000000715255736),
                            RealParameter('"Public Funding for Private R&D in Sector"[Pharmaceutical Industry]', 1.0960000038146978, 1.6440000057220463),
                            RealParameter('"Public Funding for Private R&D in Sector"[Chemical industry]', 2.9040000915527346, 4.356000137329102),
                            RealParameter('"Public Funding for Private R&D in Sector"[Automotive industry]', 0.6639999866485596, 0.9959999799728393),
                            RealParameter('"Public Funding for Private R&D in Sector"[ICT information and services]', 3.815999984741211, 5.723999977111816),
                            RealParameter('"Public Funding for Private R&D in Sector"[Aerospace construction and engineering]', 21.672000122070315, 32.508000183105466),       
                            RealParameter('"Public Funding for Private R&D in Sector"[Specialistic Technical and scientific activities]', 8.55199966430664, 12.827999496459961),
                            RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 16.90399932861328, 25.355998992919922),
                            RealParameter('"Public Funding for Private R&D in Sector"[Editing audiovisual and diffusion]', 3.2159999847412113, 4.823999977111816),
                            RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of communication equipment]', 20.69600067138672, 31.044001007080077),      
                            RealParameter('"Public Funding for Private R&D in Sector"[Production and distribution of gas vapour and AC]', 1.3920000076293944, 2.0880000114440915),
                            RealParameter('"Public R&D expenditure per personel"[Pharmaceutical Industry]', 267302.4, 400953.6),
                            RealParameter('"Public R&D expenditure per personel"[Chemical industry]', 32418.48125, 48627.721874999996),
                            RealParameter('"Public R&D expenditure per personel"[Automotive industry]', 83022.40000000001, 124533.59999999999),
                            RealParameter('"Public R&D expenditure per personel"[ICT information and services]', 113997.6, 170996.4),
                            RealParameter('"Public R&D expenditure per personel"[Aerospace construction and engineering]', 314883.2, 472324.8),
                            RealParameter('"Public R&D expenditure per personel"[Specialistic Technical and scientific activities]', 1034200.0, 1551300.0),
                            RealParameter('"Public R&D expenditure per personel"[Manufacturing of measurement instruments of navigation and watchmaking]', 102107.20000000001, 153160.8),
                            RealParameter('"Public R&D expenditure per personel"[Editing audiovisual and diffusion]', 32418.48125, 48627.721874999996),
                            RealParameter('"Public R&D expenditure per personel"[Manufacturing of communication equipment]', 32418.48125, 48627.721874999996),
                            RealParameter('"Public R&D expenditure per personel"[Production and distribution of gas vapour and AC]', 32418.48125, 48627.721874999996),
                            RealParameter('"Public-private collaboration per person"', 333.316, 499.974)]
    # list of all the TimeSeriesOutcome of interest
    sector_names = [
        'Pharmaceutical Industry',
        'Chemical industry',
        'Automotive industry',
        'ICT information and services',
        'Aerospace construction and engineering',
        'Specialistic Technical and scientific activities',
        'Manufacturing of measurement instruments of navigation and watchmaking',
        'Editing audiovisual and diffusion',
        'Manufacturing of communication equipment',
        'Production and distribution of gas vapour and AC'
    ]
    model.outcomes = [
        TimeSeriesOutcome(f'Industry knowledge size[{s}]') for s in sector_names
    ]
    results = perform_experiments(model, 2000)
    save_results(results, "./sobol scenario run Endgame Jacobs.tar.gz")

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
#plot_clustered_scenarios(experiments, outcomes, sector_names)
    
    # Display all the generated figures
#plt.show()