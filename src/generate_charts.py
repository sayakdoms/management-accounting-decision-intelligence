"""Generate charts for the Management Accounting Decision Intelligence project."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHARTS = ROOT / "charts"
CHARTS.mkdir(exist_ok=True)

variance_summary = pd.read_csv(DATA / "variance_summary.csv")
cvp_scenarios = pd.read_csv(DATA / "cvp_scenarios.csv")
abc_vs_traditional = pd.read_csv(DATA / "abc_vs_traditional.csv")
decision_matrix = pd.read_csv(DATA / "decision_matrix.csv")

# Variance impact chart
chart_data = variance_summary[variance_summary["variance_type"] != "Overall Profit Impact"].copy()
plt.figure(figsize=(10, 6))
plt.bar(chart_data["variance_type"], chart_data["amount_rs_million"])
plt.axhline(0, linewidth=1)
plt.title("Variance Impact Summary")
plt.ylabel("Amount (Rs Million)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(CHARTS / "variance_impact_summary.png", dpi=200)
plt.close()

# CVP profit scenario
plt.figure(figsize=(10, 6))
plt.bar(cvp_scenarios["scenario"], cvp_scenarios["profit_rs_million"])
plt.title("CVP Profit Scenario Comparison")
plt.ylabel("Profit (Rs Million)")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig(CHARTS / "cvp_profit_scenarios.png", dpi=200)
plt.close()

# ABC costing distortion
plt.figure(figsize=(10, 6))
x = range(len(abc_vs_traditional))
width = 0.35
plt.bar([i - width/2 for i in x], abc_vs_traditional["oh_per_unit_abc"], width, label="ABC")
plt.bar([i + width/2 for i in x], abc_vs_traditional["oh_per_unit_traditional"], width, label="Traditional")
plt.title("ABC vs Traditional Overhead per Unit")
plt.ylabel("Overhead per Unit (Rs)")
plt.xticks(list(x), abc_vs_traditional["sku"])
plt.legend()
plt.tight_layout()
plt.savefig(CHARTS / "abc_costing_distortion.png", dpi=200)
plt.close()

# Difference chart
plt.figure(figsize=(10, 6))
plt.bar(abc_vs_traditional["sku"], abc_vs_traditional["difference"])
plt.axhline(0, linewidth=1)
plt.title("Costing Distortion: ABC minus Traditional OH per Unit")
plt.ylabel("Difference (Rs per Unit)")
plt.tight_layout()
plt.savefig(CHARTS / "abc_difference_by_sku.png", dpi=200)
plt.close()

# Decision matrix
plt.figure(figsize=(10, 6))
plt.bar(decision_matrix["alternative"], decision_matrix["overall_recommendation_score"])
plt.title("Strategic Alternative Recommendation Score")
plt.ylabel("Score out of 5")
plt.ylim(0, 5)
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig(CHARTS / "decision_matrix_score.png", dpi=200)
plt.close()
