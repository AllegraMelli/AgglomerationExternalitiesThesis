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
# df = pd.read_excel('C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/change1 Jacobs.xlsx', header=None)

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

    model = VensimModel("JacobsModel", wd=wd, model_file=r'RECOVERED_Simple model 4.vpmx')

    model.uncertainties = [RealParameter('Attrition rate in sector[Pharmaceutical Industry]', 0.02960000038146973, 0.04440000057220459),
RealParameter('Attrition rate in sector[Chemical industry]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Automotive industry]', 0.0239999994635582, 0.0359999991953373),
RealParameter('Attrition rate in sector[ICT information and services]', 0.012639999389648441, 0.01895999908447266),
RealParameter('Attrition rate in sector[Aerospace construction and engineering]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Specialistic Technical and scientific activities]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Editing audiovisual and diffusion]', 0.19440000057220458, 0.29160000085830684),
RealParameter('Attrition rate in sector[Manufacturing of communication equipment]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Attrition rate in sector[Production and distribution of gas vapour and AC]', 0.020000000298023225, 0.030000000447034835),
RealParameter('Average mortality per age[Zeroto17]', 0.003200000151991844, 0.004800000227987766),
RealParameter('Average mortality per age[Eighteento24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[twentyfiveto45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[fortyfiveto65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Above65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Health18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Chemistry18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Process Engineering18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Audiovisual18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Multidisciplinary Sciences18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Digital18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Industry18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Mechanics18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Physics18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Information and communication studies18to24]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Health25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Chemistry25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Process Engineering25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Audiovisual25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Multidisciplinary Sciences25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Digital25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Industry25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Mechanics25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Physics25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Information and communication studies25to45]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Health45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Chemistry45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Process Engineering45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Audiovisual45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Multidisciplinary Sciences45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Digital45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Industry45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Mechanics45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Physics45to65]', 0.0016000000759959225, 0.0024000001139938836),
RealParameter('Average mortality per age[Information and communication studies45to65]', 0.031999999284744264, 0.04799999892711639),
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
RealParameter('Percentage of innovative SMEs collaborating with others', 0.49039998054504397, 0.7355999708175659),
RealParameter('Percentage of profit from revenue in Sector[Pharmaceutical Industry]', 0.37679998874664306, 0.5651999831199646),
RealParameter('Percentage of profit from revenue in Sector[Chemical industry]', 0.367199993133545, 0.5507999897003174),
RealParameter('Percentage of profit from revenue in Sector[Automotive industry]', 0.3283999919891358, 0.4925999879837036),
RealParameter('Percentage of profit from revenue in Sector[ICT information and services]', 0.3323999881744385, 0.4985999822616577),
RealParameter('Percentage of profit from revenue in Sector[Aerospace construction and engineering]', 0.2200000047683716, 0.33000000715255734),     
RealParameter('Percentage of profit from revenue in Sector[Specialistic Technical and scientific activities]', 0.251200008392334, 0.376800012588501),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of measurement instruments of navigation and watchmaking]', 0.3496000051498413, 0.5244000077247619),
RealParameter('Percentage of profit from revenue in Sector[Editing audiovisual and diffusion]', 0.33199999332427976, 0.4979999899864196),
RealParameter('Percentage of profit from revenue in Sector[Manufacturing of communication equipment]', 0.2200000047683716, 0.33000000715255734),   
RealParameter('Percentage of profit from revenue in Sector[Production and distribution of gas vapour and AC]', 0.6328000068664551, 0.9492000102996826),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Pharmaceutical Industry]', 0.2772000074386597, 0.4158000111579895),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Chemical industry]', 0.14728000164031985, 0.22092000246047977),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Automotive industry]', 0.15848000049591066, 0.23772000074386596),
RealParameter('"Percentage of R&D budget on total budget in Sector"[ICT information and services]', 0.05231999754905701, 0.0784799963235855),      
RealParameter('"Percentage of R&D budget on total budget in Sector"[Aerospace construction and engineering]', 0.7768000125885011, 1),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Specialistic Technical and scientific activities]', 0.3150399923324585, 0.47255998849868774),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.19119999408721922, 0.28679999113082877),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Editing audiovisual and diffusion]', 0.10576000213623049, 0.15864000320434574),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Manufacturing of communication equipment]', 0.25864000320434566, 0.3879600048065185),
RealParameter('"Percentage of R&D budget on total budget in Sector"[Production and distribution of gas vapour and AC]', 0.061199998855590826, 0.09179999828338622),
RealParameter('Percentage of workforce wanting to go the private sector', 0.5599999904632569, 0.8399999856948852),
RealParameter('"Percentage of workforce wanting to go to R&D"', 0.3200000047683716, 0.48000000715255736),
RealParameter('"Public Funding for Private R&D in Sector"[Pharmaceutical Industry]', 0.010960000008344649, 0.01644000001251697),
RealParameter('"Public Funding for Private R&D in Sector"[Chemical industry]', 0.02903999984264374, 0.04355999976396561),
RealParameter('"Public Funding for Private R&D in Sector"[Automotive industry]', 0.006639999896287919, 0.009959999844431877),
RealParameter('"Public Funding for Private R&D in Sector"[ICT information and services]', 0.038159999251365664, 0.05723999887704849),
RealParameter('"Public Funding for Private R&D in Sector"[Aerospace construction and engineering]', 0.2167200088500977, 0.3250800132751465),       
RealParameter('"Public Funding for Private R&D in Sector"[Specialistic Technical and scientific activities]', 0.0855199992656708, 0.1282799988985062),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.16904000043869016, 0.25356000065803525),
RealParameter('"Public Funding for Private R&D in Sector"[Editing audiovisual and diffusion]', 0.03215999901294708, 0.048239998519420624),
RealParameter('"Public Funding for Private R&D in Sector"[Manufacturing of communication equipment]', 0.2069600105285645, 0.31044001579284675),    
RealParameter('"Public Funding for Private R&D in Sector"[Production and distribution of gas vapour and AC]', 0.013920000195503233, 0.020880000293254847),
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
RealParameter('"Public-private collaboration per academic"[Pharmaceutical Industry]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Chemical industry]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Automotive industry]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[ICT information and services]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Aerospace construction and engineering]', 0.07200000286102295, 0.10800000429153442),    
RealParameter('"Public-private collaboration per academic"[Specialistic Technical and scientific activities]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Manufacturing of measurement instruments of navigation and watchmaking]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Editing audiovisual and diffusion]', 0.07200000286102295, 0.10800000429153442),
RealParameter('"Public-private collaboration per academic"[Manufacturing of communication equipment]', 0.07200000286102295, 0.10800000429153442),  
RealParameter('"Public-private collaboration per academic"[Production and distribution of gas vapour and AC]', 0.07200000286102295, 0.10800000429153442),
RealParameter('Relative share women in fertile age', 0.4, 0.6)
]
                                
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
    save_results(results, "./sobol scenario run Base Jacobs.tar.gz")

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

# # Call the main plotting function with your results
# plot_clustered_scenarios(experiments, outcomes, sector_names)
    
#     # Display all the generated figures
# plt.show()