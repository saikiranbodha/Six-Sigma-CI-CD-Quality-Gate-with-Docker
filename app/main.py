from data_quality import check_data_quality
from sigma_metrics import calculate_dpmo, calculate_sigma_level

MIN_SIGMA_LEVEL = 4.5

def main():
    defects, opportunities = check_data_quality("data/sample_data.csv")
    dpmo = calculate_dpmo(defects, opportunities)
    sigma = calculate_sigma_level(dpmo)

    print(f"Defects detected: {defects}")
    print(f"Total opportunities: {opportunities}")
    print(f"DPMO: {dpmo}")
    print(f"Sigma Level: {sigma}")

    if sigma < MIN_SIGMA_LEVEL:
        raise Exception(" Quality gate failed: Sigma level below threshold")

    print(" Quality gate passed")

if __name__ == "__main__":
    main()
