# fixed-income
This project explores practical techniques for bootstrapping swap curves, calibrating swaption pricing models, assessing convexity correction in CMS products, and valuing decompounded options.

# Part I (Bootstrapping Swap Curves):

OIS Data Analysis: Extract Overnight Indexed Swap (OIS) data from a provided spreadsheet and plot the discount curve for a given range of maturities.

Bootstrapping LIBOR Curve: Bootstrap the LIBOR discount factor curve using the provided Interest Rate Swaps (IRS) data and plot it for the same range of maturities.

Forward Swap Rates Calculation: Calculate a series of forward swap rates for various combinations of maturities (e.g., 1-year forward rate starting in 2 years, 5-year forward rate starting in 10 years) using linear interpolation on discount factors when necessary.

# Part II (Swaption Calibration):

Displaced-Diffusion Model Calibration: Calibrate the displaced-diffusion model to the swaption market data and document the sigma (σ) and beta (β) parameters.

SABR Model Calibration: Calibrate the SABR model to the swaption market data with a given beta value and document the alpha (α), rho (ρ), and nu (ν) parameters.

Swaption Pricing: Price a set of payer and receiver swaptions with varying strike rates using the calibrated displaced-diffusion and SABR models.

# Part III (Convexity Correction):

CMS Products Valuation: Use the SABR model to value Constant Maturity Swap (CMS) products, both for a leg receiving CMS with a 10-year maturity semi-annually over 5 years, and for a leg receiving CMS with a 2-year maturity quarterly over 10 years.

Comparison of Swap Rates: Compare the calculated forward swap rates with the CMS rates for various maturity combinations, and discuss the effect of maturity and tenor on convexity correction, which is the difference between forward swap rates and CMS rates.

# Part IV (Decompounded Options):

Decompounded Option Valuation: Value the present value (PV) of a decompounded option with a specified payoff formula, using static replication.

Modified Payoff Valuation: Value the PV of a modified payoff formula using static replication.
