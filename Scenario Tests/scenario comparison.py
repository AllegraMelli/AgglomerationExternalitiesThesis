import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from ema_workbench import load_results
from matplotlib.gridspec import GridSpec

# Scenario files and highlight colors
scenario_files = [
    "sobol scenario run Endgame Jacobs.tar.gz",
    "sobol scenario run Opposing views Jacobs.tar.gz",
    "sobol scenario run Storms Jacobs.tar.gz",
    "sobol scenario run Struggling Synergies Jacobs.tar.gz",
    "sobol scenario run Base Jacobs.tar.gz"
    ]

colors = ['purple', 'teal', 'crimson', 'navy', 'green']

sector_names = [ 
    'Pharmaceutical Industry', 'Chemical industry', 'Automotive industry',
    'ICT information and services', 'Aerospace construction and engineering',
    'Specialistic Technical and scientific activities',
    'Manufacturing of measurement instruments of navigation and watchmaking',
    'Editing audiovisual and diffusion',
    'Manufacturing of communication equipment',
    'Production and distribution of gas vapour and AC'
]

# Load all scenario data
scenario_data = []
for fname in scenario_files:
    exp, outcomes = load_results(fname)
    scenario_data.append((fname, outcomes))

for sector in sector_names:
    fig = plt.figure(figsize=(12, 5))
    gs = GridSpec(1, 2, width_ratios=[4, 1], wspace=0.3)

    ax_ts = fig.add_subplot(gs[0, 0])
    ax_den = fig.add_subplot(gs[0, 1], sharey=ax_ts)

    ax_ts.set_title(f"Sector: {sector}")
    ax_ts.set_xlabel("Time")
    ax_ts.set_ylabel("Industry knowledge size")
    ax_ts.axvline(10, color='black', linestyle='--', alpha=0.3, label='Shock interval')
    ax_ts.axvline(15, color='black', linestyle='--', alpha=0.3)
    ax_ts.axvspan(10, 15, color='grey', alpha=0.1, zorder=0)

    ax_den.set_title("Density (final values)")
    ax_den.get_yaxis().set_visible(False)
    ax_den.spines['left'].set_visible(False)

    for (fname, outcomes), col in zip(scenario_data, colors):
        key = f'Industry knowledge size[{sector}]'
        time = outcomes['TIME'][0]
        series = outcomes[key]  # shape (nruns, timesteps)

        # Plot all runs
        for run in series:
            ax_ts.plot(time, run, color='grey', alpha=0.2, linewidth=0.8, zorder=1)
    
        # Compute density on final values
        final_vals = series[:, -1]
        kde = gaussian_kde(final_vals)
        density_vals = kde(final_vals)
        best_idx = np.argmax(density_vals)
        best_run = series[best_idx]

        # Highlight best run
        ax_ts.plot(time, best_run, color=col, linewidth=1.5, label=f"{fname.replace('sobol scenario run ','').replace(' Jacobs.tar.gz','')} peak", zorder=3)

        # Plot marginal density
        y = np.linspace(final_vals.min(), final_vals.max(), 200)
        d = kde(y)
        ax_den.plot(d, y, color=col, linewidth=2)
        ax_den.fill_betweenx(y, 0, d, color=col, alpha=0.3)
    
    ax_ts.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
