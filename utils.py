# utils.py

def normalize_unit(unit):
    unit = unit.lower().strip()
    if unit in ["celsius", "c"]:
        return "celsius"
    elif unit in ["fahrenheit", "f"]:
        return "fahrenheit"
    elif unit in ["kelvin", "k"]:
        return "kelvin"
    else:
        return None
