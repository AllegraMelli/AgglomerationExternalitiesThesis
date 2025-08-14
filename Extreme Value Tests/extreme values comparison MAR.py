import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from ema_workbench import load_results
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D


# Scenario files and highlight colors
scenario_files = [
    "Extreme High Values MAR.tar.gz",
    "Extreme Low values MAR.tar.gz"
]

colors = ['purple', 'teal']

sector_names = [
    'Telecommunication',
    'Manufacturing of communication equipment'
]

# Load all scenario data
scenario_data = []
for fname in scenario_files:
    exp, outcomes = load_results(fname)
    scenario_data.append((fname, outcomes))

# Define the outcomes to plot
outcome_types = [
    'Industry knowledge size',
    'Workforce employed in knowledge intensive activities'
]

# Plotting
for outcome_type in outcome_types:
    for sector in sector_names:
        fig = plt.figure(figsize=(12, 5))
        gs = GridSpec(1, 2, width_ratios=[4, 1], wspace=0.3)

        ax_ts = fig.add_subplot(gs[0, 0])
        ax_den = fig.add_subplot(gs[0, 1], sharey=ax_ts)
        ax_ts.set_title(f"{outcome_type} - Sector: {sector}")
        ax_ts.set_xlabel("Time")
        ax_ts.set_ylabel(outcome_type)

        legend_elements = []

        for (fname, outcomes), col in zip(scenario_data, colors):
            key = f'{outcome_type}[{sector}]'
            time = outcomes['TIME'][0]
            series = outcomes[key]  # shape (nruns, timesteps)

            # Plot all runs with color based on source file
            for run in series:
                ax_ts.plot(time, run, color=col, alpha=0.2, linewidth=0.8, zorder=1)

            # Compute density on final values
            final_vals = series[:, -1]
            kde = gaussian_kde(final_vals)

            # Plot marginal density
            y = np.linspace(final_vals.min(), final_vals.max(), 200)
            d = kde(y)
            ax_den.plot(d, y, color=col, linewidth=2)
            ax_den.fill_betweenx(y, 0, d, color=col, alpha=0.3)

            label = fname.replace(' MAR.tar.gz', '')
            legend_elements.append(Line2D([0], [0], color=col, lw=2, label=label))

        ax_ts.legend(handles=legend_elements, loc='upper left')
        plt.tight_layout()
        plt.show()

