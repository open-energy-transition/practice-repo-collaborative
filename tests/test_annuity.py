from costs import annualised_cost


def test_annualised_cost_is_positive() -> None:
    assert annualised_cost(1000.0, 3.0, 25, 0.07) > 0
