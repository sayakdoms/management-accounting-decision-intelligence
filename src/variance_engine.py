"""Variance diagnosis engine."""

def classify_variance(amount_rs_million):
    if amount_rs_million > 1:
        return "Unfavourable - High attention"
    if amount_rs_million > 0:
        return "Unfavourable - Monitor"
    if amount_rs_million < 0:
        return "Favourable"
    return "Neutral"

def recommend_action(variance_type, amount_rs_million):
    vt = variance_type.lower()
    if "material" in vt and amount_rs_million > 0:
        return "Separate price-driven and usage-driven causes; review procurement, wastage, and yield losses."
    if "labour" in vt and amount_rs_million < 0:
        return "Capture best practices behind labour efficiency and replicate across units."
    if "overhead" in vt and amount_rs_million > 0:
        return "Investigate setup frequency, machine utilization, quality checks, and indirect cost drivers."
    if "sales price" in vt and amount_rs_million > 0:
        return "Evaluate discounting strategy against contribution margin and market-share gains."
    if "overall" in vt:
        return "Prioritize material cost control, pricing discipline, and faster variance reporting."
    return "Monitor trend and assign responsibility based on controllability."
