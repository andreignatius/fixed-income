def linear_interpolate(x0, y0, x1, y1, x):
    """Linearly interpolate to find y at a given x."""
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def calculate_forward_rate(df, start, end):
    """Calculate the forward rate between start and end using discount factors."""
    # Get discount factors for the start and end tenors, interpolate if necessary
    if start not in df['Tenor'].values:
        # Find the two closest tenors for interpolation
        closest_tenors = df.iloc[(df['Tenor'] - start).abs().argsort()[:2]]
        D_start = linear_interpolate(closest_tenors.iloc[0]['Tenor'], closest_tenors.iloc[0]['Discount Factor'],
                                     closest_tenors.iloc[1]['Tenor'], closest_tenors.iloc[1]['Discount Factor'], start)
    else:
        D_start = df.loc[df['Tenor'] == start, 'Discount Factor'].values[0]

    if end not in df['Tenor'].values:
        closest_tenors = df.iloc[(df['Tenor'] - end).abs().argsort()[:2]]
        D_end = linear_interpolate(closest_tenors.iloc[0]['Tenor'], closest_tenors.iloc[0]['Discount Factor'],
                                   closest_tenors.iloc[1]['Tenor'], closest_tenors.iloc[1]['Discount Factor'], end)
    else:
        D_end = df.loc[df['Tenor'] == end, 'Discount Factor'].values[0]

    # Calculate the forward rate
    forward_rate = (D_start - D_end) / (D_end * (end - start))
    return forward_rate

