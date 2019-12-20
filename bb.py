import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import bayesian_blocks
import pandas as pd

nbins = 25
p0 = 0.01
AP_header = ["time", "latitude", "longitude", "energy", "theta", "ph_earth", "phasec", "dist"]

AP3_header = ["tstart", "tstop", "exp", "cts", "normAB11", "normAB12", "normAB13", "normAB14", "normAB21",
              "normAB22", "normAB23", "normAB24", "normAB11aa", "normAB21aa", "ratediffR1", "ratediffR2",
              "ratediffR3", "ratediffR4", "ratediffR1AA", "rate", "rate_error", "flux_ratediffR4",
              "flux_ratediffR4_error", "TS", "flux_rate", "flux_rate_error", "cts_expBKG4"]

binned_2018dq1_86400_r4 = pd.read_csv("2018dq1_86400s_emin100_emax10000_r4.ap.ap3", header=None, names=AP3_header, sep=" ")

r2_2018dq1 = pd.read_csv("2018dq1_emin100_emax10000_r2.ap.ph", header=None, names=AP_header, sep=" ")
r3_2018dq1 = pd.read_csv("2018dq1_emin100_emax10000_r3.ap.ph", header=None, names=AP_header, sep=" ")
r4_2018dq1 = pd.read_csv("2018dq1_emin100_emax10000_r4.ap.ph", header=None, names=AP_header, sep=" ")

fig, axes = plt.subplots(3,1)

#PlotR2
ncp_prior = 4 - np.log(73.53 * p0 * (len(r2_2018dq1["time"]) ** -0.478))
bb = bayesian_blocks(t=r2_2018dq1["time"], fitness="events", ncp_prior=ncp_prior)
axes[0].hist(r2_2018dq1["time"], bins=nbins, density=True)
axes[0].hist(r2_2018dq1["time"], bins=bb, density=True, histtype="step")
axes[0].set_title("2018dq1_emin100_emax10000_r2.ap.ph")

#PlotR3
ncp_prior = 4 - np.log(73.53 * p0 * (len(r3_2018dq1["time"]) ** -0.478))
bb = bayesian_blocks(t=r3_2018dq1["time"], fitness="events", ncp_prior=ncp_prior)
axes[1].hist(r3_2018dq1["time"], bins=nbins, density=True)
axes[1].hist(r3_2018dq1["time"], bins=bb, density=True, histtype="step")
axes[1].set_title("2018dq1_emin100_emax10000_r3.ap.ph")

#PlotR4
ncp_prior = 4 - np.log(73.53 * p0 * (len(r4_2018dq1["time"]) ** -0.478))
bb = bayesian_blocks(t=r4_2018dq1["time"], fitness="events", ncp_prior=ncp_prior)
axes[2].hist(r4_2018dq1["time"], bins=nbins, density=True)
axes[2].hist(r4_2018dq1["time"], bins=bb, density=True, histtype="step")
axes[2].set_title("2018dq1_emin100_emax10000_r4.ap.ph")


plt.show()

exit()