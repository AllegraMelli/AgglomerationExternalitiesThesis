from SALib.analyze import sobol
from ema_workbench.em_framework.salib_samplers import get_SALib_problem
from ema_workbench import (Samplers, TimeSeriesOutcome, perform_experiments, RealParameter, ema_logging, MultiprocessingEvaluator, save_results, load_results)
from ema_workbench.analysis import Density, pairs_plotting, plotting
from ema_workbench.connectors.vensim import VensimModel
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

    # ————————————————————————
    # 1. Function to compute the upper and lower boundary of the uncertainty and lever parameters
    # ### uncomment only if recalculation needed.
    # ————————————————————————
# def format_real_parameter(full_name, initial_value):
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

#experiments, outcomes = load_results("C:/Users/Allis/sobol sensitivy run MAR.tar.gz")

sector_names = ["Telecommunication", "Manufacturing of communication equipment"]

if __name__ == "__main__":
    # turn on logging
    ema_logging.log_to_stderr(ema_logging.INFO)
    wd = r'OneDrive - Delft University of Technology/Master Thesis'

    model = VensimModel("MARModel", wd=wd, model_file=r'MAR region France_improved.vpmx')


    model.uncertainties = [RealParameter('Attrition rate in sector[Telecommunication]', 0.020000000298023225, 0.030000000447034835),
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
RealParameter('Relative share women in fertile age', 0.4, 0.6)
]

    model.levers = [RealParameter('Attrition rate in sector[Telecommunication]', 0.020000000298023225, 0.030000000447034835),
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
RealParameter('Relative share women in fertile age', 0.4, 0.6)
]

    model.outcomes = [
            TimeSeriesOutcome(f'Industry knowledge size[{s}]') for s in sector_names
        ]
    
    sa_results = perform_experiments(model, scenarios=60, uncertainty_sampling=Samplers.SOBOL)
    save_results(sa_results, "./sobol sensitivy run MAR no relatedness.tar.gz")

    experiments, outcomes = sa_results
    ema_logging.log_to_stderr(ema_logging.INFO)

    problem = get_SALib_problem(model.levers)


     # Container for sensitivity data
    sensitivity = {}

    for s in sector_names:
        ts = outcomes[f'Industry knowledge size[{s}]']  # shape (Nruns, T)
        Y = np.max(ts, axis=1)  # scalar summary: max over time

        Si = sobol.analyze(problem, Y, calc_second_order=True, print_to_console=False)
        sensitivity[s] = Si

    df = pd.DataFrame({
    s: sensitivity[s]['ST'] for s in sector_names}, index=problem['names']).T  # sectors×levers
    df['ST_max'] = df.max(axis=1)
    df = df.sort_values('ST_max', ascending=False)
    n_sectors = len(sector_names)
    n_cols = 2
    n_rows = (n_sectors + 1) // n_cols

    # Create DataFrame for ST and sort
    st_df = pd.DataFrame({s: sensitivity[s]['ST'] for s in sector_names}, index=problem['names']).T
    st_df['ST_max'] = st_df.max(axis=1)
    st_df = st_df.sort_values('ST_max', ascending=False)

    # Map levers to letters
    lever_numbers = {name: str(i+1) for i, name in enumerate(problem['names'])}

    for sector in df.index:
        # pull out all indices
        st_all     = sensitivity[sector]['ST']
        s1_all     = sensitivity[sector]['S1']
        st_conf_all= sensitivity[sector]['ST_conf']
        s1_conf_all= sensitivity[sector]['S1_conf']
        names_all  = problem['names']

        # sort by total‐order descending and pick top 25
        sorted_idx = np.argsort(st_all)[::-1][:12]
        top_names    = [names_all[i]       for i in sorted_idx]
        top_st       = st_all[sorted_idx]
        top_s1       = s1_all[sorted_idx]
        top_st_conf  = st_conf_all[sorted_idx]
        top_s1_conf  = s1_conf_all[sorted_idx]

        # create x positions and labels
        x_pos       = np.arange(len(top_names))
        x_labels    = [lever_numbers[n] for n in top_names]

        # plot
        fig, ax = plt.subplots(figsize=(8,4))
        ax.bar(x_pos,       top_st,    yerr=top_st_conf, alpha=0.7, label='Total-order')
        ax.bar(x_pos,       top_s1,    yerr=top_s1_conf, alpha=0.7, label='First-order')

        # tick with lever numbers
        ax.set_xticks(x_pos)
        ax.set_xticklabels(x_labels, rotation=0, fontsize=11)

        ax.set_title(f"{sector}  (sorted by ST)")
        ax.set_ylabel("Sobol index")
        ax.legend()  
        plt.tight_layout()
        plt.show()

# Create the ST matrix and rename columns to lever letters
    st_matrix = df.loc[:, problem['names']].rename(columns=lever_numbers)
    # Plot heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(st_matrix,
                cmap='viridis',
                annot=False,
                ax=ax,
                cbar_kws={'label': 'ST index'})

    # Axis labels
    ax.set_title("Total-order Sobol indices (sectors × levers)")
    ax.set_xlabel("Levers (letter-coded)")
    ax.set_ylabel("Sectors (sorted by max ST)")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

    plt.tight_layout()
    plt.show()

# Create a table with rows = (sector, lever), columns = S1, ST, S1_conf, ST_conf
sobol_table = []

for sector in sector_names:
    Si = sensitivity[sector]  # your precomputed sensitivity results
    for i, lever in enumerate(problem['names']):
        sobol_table.append({
            'Sector': sector,
            'Lever': lever,
            'S1': Si['S1'][i],
            'S1_conf': Si['S1_conf'][i],
            'ST': Si['ST'][i],
            'ST_conf': Si['ST_conf'][i]
        })

# Convert to DataFrame
sobol_df = pd.DataFrame(sobol_table)

# Sort for better readability
sobol_df = sobol_df.sort_values(['Sector', 'ST'], ascending=[True, False])
sobol_df['Lever_no'] = sobol_df['Lever'].map(lever_numbers)

# Save to Excel (or change to .csv if needed)
sobol_df.to_excel('C:/Users/Allis/OneDrive - Delft University of Technology/Master Thesis/sobol_results_by_sector MAR.xlsx', index=False)

# Optional: display preview
print(sobol_df.head())