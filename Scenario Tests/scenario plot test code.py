import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from ema_workbench import load_results

# Scenario files and colors
scenario_files = [
    "sobol scenario run Endgame Jacobs.tar.gz",
    "sobol scenario run Opposing views Jacobs.tar.gz",
    "sobol scenario run Storms Jacobs.tar.gz",
    "sobol scenario run Struggling Synergies Jacobs.tar.gz",
    "sobol scenario run Base Jacobs.tar.gz"
]

colors = ['purple', 'teal', 'crimson', 'navy', 'green']

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

# load scenario outputs
scenario_data = []
for fname in scenario_files:
    exp, outcomes = load_results(fname)
    scenario_data.append((fname, outcomes))

# Loop through each sector
for sector in sector_names:
    plt.figure(figsize=(10, 6))
    plt.title(f"Sector: {sector}\nGrey = all runs; colored = highest-density per scenario")

    for (fname, outcomes), col in zip(scenario_data, colors):
        key = f'Industry knowledge size[{sector}]'
        time = outcomes['TIME'][0]
        series = outcomes[key]  # shape: (nruns, timesteps)
        nruns, nt = series.shape

        # plot all trajectories in grey
        for run in series:
            plt.plot(time, run, color='grey', alpha=0.2, linewidth=0.8)

        # compute KDE for each trajectory separately:
        # here we use the final time value to pick density over scalar distribution
        final_values = series[:, -1]
        kde = gaussian_kde(final_values)
        # density scores:
        density_scores = kde(final_values)
        best_idx = np.argmax(density_scores)
        best_traj = series[best_idx]

        plt.plot(time, best_traj, color=col, linewidth=2.5,
                 label=f"{fname.replace('.tar.gz','')} peak density")
    plt.axvline(10, color='black', linestyle='--', alpha=0.3, label='Shock time')
    plt.axvline(15, color='black', linestyle='--', alpha=0.3, label='Recovery time')
    plt.xlabel('Time')
    plt.ylabel('Industry knowledge size')
    plt.legend()
    plt.tight_layout()
    plt.show()
