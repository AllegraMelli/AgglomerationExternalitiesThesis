import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from ema_workbench import load_results
from matplotlib.gridspec import GridSpec

# Load results
experiments, outcomes = load_results("sobol scenario run Base Jacobs.tar.gz")

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

color_map = plt.get_cmap('tab10')
sector_colors = {s: color_map(i) for i, s in enumerate(sector_names)}

def plot_sectors(sectors, title):
    fig = plt.figure(figsize=(14, 8))
    gs = GridSpec(1, 2, width_ratios=[4, 1], wspace=0.3)
    ax_ts = fig.add_subplot(gs[0])
    ax_den = fig.add_subplot(gs[1], sharey=ax_ts)

    ax_ts.set_title(title)
    ax_ts.set_xlabel("Time")
    ax_ts.set_ylabel("Industry knowledge size")
    ax_den.set_title("Density of final values")
    ax_den.get_yaxis().set_visible(False)
    ax_den.spines['left'].set_visible(False)

    for sector in sectors:
        series = outcomes[f'Industry knowledge size[{sector}]']
        time = outcomes['TIME'][0]
        finals = series[:, -1]

        # Plot trajectories
        for run in series:
            ax_ts.plot(time, run, color=sector_colors[sector], alpha=0.3, linewidth=0.7)

        # Density estimation
        kde = gaussian_kde(finals)
        y = np.linspace(finals.min(), finals.max(), 200)
        d = kde(y)

        ax_den.plot(d, y, color=sector_colors[sector], linewidth=2)
        ax_den.fill_betweenx(y, 0, d, color=sector_colors[sector], alpha=0.3)

    # Legend
    handles = [plt.Line2D([0], [0], color=sector_colors[s], lw=4, label=s) for s in sectors]
    ax_ts.legend(handles=handles, bbox_to_anchor=(.1, 1),
                 loc='upper left', title='Sectors', fontsize='small')
    
    plt.tight_layout()
    plt.show()
    

# Full figure
plot_sectors(sector_names, title="Jacobs Sectors Parameter Sweep Time-Series and Marginal Density Plot")
    # Legend



# Subset 1
subset1 = [
    'Pharmaceutical Industry',
    'Manufacturing of measurement instruments of navigation and watchmaking',
    'Aerospace construction and engineering'
]
plot_sectors(subset1, title="Subset 1 Sectors Parameter Sweep Time-Series and Marginal Density Ploty")

# Subset 2
subset2 = [
    'ICT information and services',
    'Specialistic Technical and scientific activities',
    'Automotive industry'
]
plot_sectors(subset2, title="Subset 2 Sectors Parameter Sweep Time-Series and Marginal Density Plot")

# Subset 2
subset3 = [
    'Production and distribution of gas vapour and AC',
    'Chemical industry',
    'Manufacturing of communication equipment',
]
plot_sectors(subset3, title="Subset 3 Sectors Parameter Sweep Time-Series and Marginal Density Plot")

# Subset 4
subset4 = [
    'Editing audiovisual and diffusion']

plot_sectors(subset4, title="Subset 4 Sectors Parameter Sweep Time-Series and Marginal Density Plot")
