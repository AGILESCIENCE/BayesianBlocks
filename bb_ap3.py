import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import bayesian_blocks
import pandas as pd
import sys

nbins = 10
p0 = 0.01
AP_header = ["time", "latitude", "longitude", "energy", "theta", "ph_earth", "phasec", "dist"]

AP3_header = ["tstart", "tstop", "exp", "cts", "normAB11", "normAB12", "normAB13", "normAB14", "normAB21",
              "normAB22", "normAB23", "normAB24", "normAB11aa", "normAB21aa", "ratediffR1", "ratediffR2",
              "ratediffR3", "ratediffR4", "ratediffR1AA", "rate", "rate_error", "flux_ratediffR4",
              "flux_ratediffR4_error", "TS", "flux_rate", "flux_rate_error", "cts_expBKG4"]




"""axes[0].hist(binned_2018dq1_43200_r4["rate"], bins=len(binned_2018dq1_43200_r4["tstart"]), density=True)
ncp_prior = 4 - np.log(73.53 * p0 * (len(binned_2018dq1_43200_r4["rate"]) ** -0.478))
bb = bayesian_blocks(t=binned_2018dq1_43200_r4["rate"], fitness="events", ncp_prior=ncp_prior)
#axes[0].hist(binned_2018dq1_43200_r4["rate"], bins=nbins, density=True)
axes[0].hist(binned_2018dq1_43200_r4["rate"], bins=bb, density=True, histtype="step")"""


#bb = bayesian_blocks(t=binned_2018dq1_43200_r4["flux_ratediffR4"], fitness="events", ncp_prior=ncp_prior)
#entries, edges, _ = axes[1].hist(binned_2018dq1_43200_r4["flux_ratediffR4"], bins=len(binned_2018dq1_43200_r4["tstart"]), density=True, color='k', alpha=0.5)
#bin_centers = 0.5*(edges[1:] + edges[:-1])
#axes[1].errorbar(x=binned_2018dq1_43200_r4["tstart"], y=binned_2018dq1_43200_r4["flux_ratediffR4"], yerr=binned_2018dq1_43200_r4["flux_ratediffR4_error"], fmt="b.")
#axes[1].hist(binned_2018dq1_43200_r4["flux_ratediffR4"], bins=bb, density=True, histtype="step")

#axes[2].plot(binned_2018dq1_43200_r4["tstop"], binned_2018dq1_43200_r4["cts"])

def main(filename):

    fig, axes = plt.subplots(1, 2)
    data = pd.read_csv(filename, header=None, names=AP3_header, sep=" ")
    ncp_prior = 4 - np.log(73.53 * p0 * (len(data["rate"]) ** -0.478))
    bb = bayesian_blocks(t=data["flux_ratediffR4"], fitness="events", ncp_prior=ncp_prior)

    fig.suptitle(filename)
    axes[0].errorbar(x=data["tstart"], y=data["flux_ratediffR4"], yerr=data["flux_ratediffR4_error"], fmt="b.")
    axes[0].set_title("flux_ratediffR4 & error")
    axes[1].hist(data["flux_ratediffR4"], bins=bb, density=False, histtype="step")
    axes[1].set_title("Bayesian Blocks flux_ratediffR4")

    plt.show()


if __name__ == "__main__":
    main(sys.argv[1])
    exit()
