import pandas as pd
import streamlit as st
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
sys.path.append(str(ROOT / "src"))

from cvp_model import calculate_cvp
from variance_engine import classify_variance, recommend_action
from abc_model import costing_distortion

st.set_page_config(
    page_title="Management Accounting Decision Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Management Accounting Decision Intelligence Dashboard")
st.caption("Variance Analysis | CVP Modelling | Activity-Based Costing | Strategic Cost Decisions")

st.markdown("""
This dashboard converts a management accounting case into a decision-support analytics tool.
It demonstrates how cost data can be used to diagnose performance issues, test scenarios,
identify costing distortion, and support managerial recommendations.
""")

variance_summary = pd.read_csv(DATA / "variance_summary.csv")
cvp_scenarios = pd.read_csv(DATA / "cvp_scenarios.csv")
abc_vs_traditional = pd.read_csv(DATA / "abc_vs_traditional.csv")
decision_matrix = pd.read_csv(DATA / "decision_matrix.csv")

tab1, tab2, tab3, tab4 = st.tabs([
    "Executive Summary",
    "CVP Simulator",
    "Variance Diagnosis",
    "ABC Costing Intelligence"
])

with tab1:
    st.subheader("Executive Summary")
    col1, col2, col3, col4 = st.columns(4)

    overall_impact = variance_summary.loc[
        variance_summary["variance_type"] == "Overall Profit Impact",
        "amount_rs_million"
    ].iloc[0]

    best_scenario = cvp_scenarios.sort_values("profit_rs_million", ascending=False).iloc[0]
    biggest_distortion = abc_vs_traditional.reindex(
        abc_vs_traditional["difference"].abs().sort_values(ascending=False).index
    ).iloc[0]
    recommended_alt = decision_matrix.sort_values("overall_recommendation_score", ascending=False).iloc[0]

    col1.metric("Profit Impact", f"Rs {overall_impact:.2f} mn", "Unfavourable")
    col2.metric("Best CVP Scenario", best_scenario["scenario"], f"Rs {best_scenario['profit_rs_million']:.1f} mn")
    col3.metric("Largest Costing Distortion", biggest_distortion["sku"], f"Rs {biggest_distortion['difference']:.2f}/unit")
    col4.metric("Recommended Strategy", recommended_alt["alternative"], f"Score {recommended_alt['overall_recommendation_score']}/5")

    st.markdown("### Strategic Recommendation")
    st.success(
        "Adopt a phased implementation of Activity-Based Costing and flexible budgeting. "
        "This balances improved costing accuracy with manageable implementation risk."
    )

    st.markdown("### Decision Matrix")
    st.dataframe(decision_matrix, use_container_width=True)

with tab2:
    st.subheader("Interactive CVP Simulator")
    st.markdown("Change price, variable cost, volume, and fixed cost to test profit sensitivity.")

    col1, col2, col3, col4 = st.columns(4)
    selling_price = col1.number_input("Selling Price per Unit", min_value=1.0, value=100.0, step=1.0)
    variable_cost = col2.number_input("Variable Cost per Unit", min_value=0.0, value=70.0, step=1.0)
    quantity = col3.number_input("Quantity Sold", min_value=1, value=1000000, step=50000)
    fixed_cost = col4.number_input("Fixed Cost (Rs Million)", min_value=0.0, value=20.0, step=1.0)

    result = calculate_cvp(selling_price, variable_cost, quantity, fixed_cost)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Contribution / Unit", f"Rs {result['contribution_per_unit']:.2f}")
    c2.metric("Sales", f"Rs {result['sales_rs_million']:.2f} mn")
    c3.metric("Profit", f"Rs {result['profit_rs_million']:.2f} mn")
    if result["bep_units"] is None:
        c4.metric("Break-even Units", "Not feasible")
    else:
        c4.metric("Break-even Units", f"{result['bep_units']:,.0f}")

    if result["mos_percent"] is not None:
        st.info(f"Margin of Safety: {result['mos_percent']:.2f}%")
    else:
        st.warning("Contribution per unit is zero or negative, so break-even is not feasible.")

    st.markdown("### Original Case Scenarios")
    st.dataframe(cvp_scenarios, use_container_width=True)

with tab3:
    st.subheader("Variance Diagnosis Engine")

    selected_variance = st.selectbox("Select a variance type", variance_summary["variance_type"])
    row = variance_summary[variance_summary["variance_type"] == selected_variance].iloc[0]
    amount = float(row["amount_rs_million"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Variance Amount", f"Rs {amount:.2f} mn")
    col2.metric("Nature", row["nature"])
    col3.metric("Priority", row["priority"])

    st.markdown("### Diagnosis")
    st.write(row["diagnosis"])

    st.markdown("### Engine Classification")
    st.warning(classify_variance(amount))

    st.markdown("### Recommended Managerial Action")
    st.success(recommend_action(selected_variance, amount))

    st.markdown("### Full Variance Table")
    st.dataframe(variance_summary, use_container_width=True)

with tab4:
    st.subheader("ABC Costing Intelligence")

    selected_sku = st.selectbox("Select SKU", abc_vs_traditional["sku"])
    sku = abc_vs_traditional[abc_vs_traditional["sku"] == selected_sku].iloc[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("ABC OH / Unit", f"Rs {sku['oh_per_unit_abc']:.2f}")
    col2.metric("Traditional OH / Unit", f"Rs {sku['oh_per_unit_traditional']:.2f}")
    col3.metric("Difference", f"Rs {sku['difference']:.2f}")

    diff, implication = costing_distortion(
        float(sku["oh_per_unit_abc"]),
        float(sku["oh_per_unit_traditional"])
    )

    st.markdown("### Costing Interpretation")
    st.info(f"{selected_sku}: {implication}")

    st.markdown("### Recommended Action")
    st.success(sku["recommended_action"])

    st.markdown("### ABC vs Traditional Costing Table")
    st.dataframe(abc_vs_traditional, use_container_width=True)
