def annuity(lifetime: float, discount_rate: float) -> float:
    return discount_rate / (1.0 - (1.0 + discount_rate) ** lifetime)


def annualised_cost(
    investment: float, fom_percent: float, lifetime: float, discount_rate: float
) -> float:
    return (annuity(lifetime, discount_rate) + fom_percent / 100.0) * investment
