def calculate_dpmo(defects: int, total_opportunities: int) -> float:
    return (defects / total_opportunities) * 1_000_000


def calculate_sigma_level(dpmo: float) -> float:
    if dpmo == 0:
        return 6.0

    # Simple linear approximation (acceptable for demonstration)
    sigma = 6 - (dpmo / 1_000_000) * 5
    return round(max(1.0, sigma), 2)
