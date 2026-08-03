"""Activity-Based Costing utilities."""

def calculate_driver_rate(pool_cost, driver_volume):
    if driver_volume == 0:
        raise ValueError("Driver volume cannot be zero.")
    return pool_cost / driver_volume

def costing_distortion(abc_oh_per_unit, traditional_oh_per_unit):
    difference = abc_oh_per_unit - traditional_oh_per_unit
    if difference > 1:
        implication = "Under-costed under traditional costing"
    elif difference < -1:
        implication = "Over-costed under traditional costing"
    else:
        implication = "Minor distortion"
    return difference, implication
