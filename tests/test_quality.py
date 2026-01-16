from app.sigma_metrics import calculate_dpmo, calculate_sigma_level

def test_dpmo_calculation():
    dpmo = calculate_dpmo(4, 24)
    assert round(dpmo, 2) == 166666.67

def test_sigma_level_range():
    sigma = calculate_sigma_level(166666.67)
    assert sigma >= 1.0 and sigma <= 6.0
