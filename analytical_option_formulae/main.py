from option_types.vanilla_option import VanillaOption

if __name__ == "__main__":
    # Sample usage for a vanilla option using BM model
    S = 1
    K = 1
    r = 1
    sigma = 1
    T = 1

    vanilla_option = VanillaOption()
    vanilla_bm_model = vanilla_option.black_scholes_model(S, K, r, sigma, T)
    print(vanilla_bm_model.calculate_call_price())
    print(vanilla_bm_model.calculate_put_price())
