import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from ema_workbench import load_results
from matplotlib.gridspec import GridSpec

# Load results
experiments, outcomes = load_results("sobol scenario run Base MAR.tar.gz")

sector_names = ["Telecommunication", "Manufacturing of communication equipment"]

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
    handles = [plt.Line2D([0], [0], color=sector_colors[s], lw=4, label=s) for s in sector_names]

    # Place legend outside the figure
    plt.legend(handles=handles,
            loc='lower right',
            bbox_to_anchor=(3.25, 0),
            title='Sectors',
            fontsize='small')

    plt.subplots_adjust(right=0.75)


# Full figure
plot_sectors(sector_names, title="MAR Sectors Time-series and Density")

# Reserve space
plt.tight_layout(rect=[0, 0, 0.8, 1.0])
plt.show()
