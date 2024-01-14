import numpy as np

class SABRModel:
    def __init__(self, F, K, T, alpha, beta, rho, nu):
        self.F = F
        self.K = K
        self.T = T
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.nu = nu

    def calculate_volatility(self):
        F, K, T, alpha, beta, rho, nu = self.F, self.K, self.T, self.alpha, self.beta, self.rho, self.nu
        if abs(F - K) < 1e-12:  # ATM case
            numer1 = (((1 - beta) ** 2) / 24) * alpha * alpha / (F ** (2 - 2 * beta))
            numer2 = 0.25 * rho * beta * nu * alpha / (F ** (1 - beta))
            numer3 = ((2 - 3 * rho * rho) / 24) * nu * nu
            VolAtm = alpha * (1 + (numer1 + numer2 + numer3) * T) / (F ** (1 - beta))
            sabr_vol = VolAtm
        else:  # non-ATM case
            z = (nu / alpha) * ((F * K) ** (0.5 * (1 - beta))) * np.log(F / K)
            zhi = np.log((((1 - 2 * rho * z + z * z) ** 0.5) + z - rho) / (1 - rho))
            numer1 = (((1 - beta) ** 2) / 24) * ((alpha * alpha) / ((F * K) ** (1 - beta)))
            numer2 = 0.25 * rho * beta * nu * alpha / ((F * K) ** ((1 - beta) / 2))
            numer3 = ((2 - 3 * rho * rho) / 24) * nu * nu
            numer = alpha * (1 + (numer1 + numer2 + numer3) * T) * z
            denom1 = ((1 - beta) ** 2 / 24) * (np.log(F / K)) ** 2
            denom2 = (((1 - beta) ** 4) / 1920) * ((np.log(F / K)) ** 4)
            denom = ((F * K) ** ((1 - beta) / 2)) * (1 + denom1 + denom2) * zhi
            sabr_vol = numer / denom
        return sabr_vol


        