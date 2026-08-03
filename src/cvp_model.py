"""CVP model utilities."""

def calculate_cvp(selling_price, variable_cost, quantity, fixed_cost_rs_million):
    contribution_per_unit = selling_price - variable_cost
    sales_rs_million = (selling_price * quantity) / 1_000_000
    variable_cost_rs_million = (variable_cost * quantity) / 1_000_000
    profit_rs_million = sales_rs_million - variable_cost_rs_million - fixed_cost_rs_million

    if contribution_per_unit <= 0:
        bep_units = None
        mos_percent = None
    else:
        bep_units = (fixed_cost_rs_million * 1_000_000) / contribution_per_unit
        mos_units = quantity - bep_units
        mos_percent = (mos_units / quantity) * 100 if quantity else None

    return {
        "contribution_per_unit": contribution_per_unit,
        "sales_rs_million": sales_rs_million,
        "variable_cost_rs_million": variable_cost_rs_million,
        "profit_rs_million": profit_rs_million,
        "bep_units": bep_units,
        "mos_percent": mos_percent,
    }
