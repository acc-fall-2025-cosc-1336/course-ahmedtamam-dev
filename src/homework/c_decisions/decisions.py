def get_options_ratio(option: float, total: float) -> float:
    if total <= 0:
        raise ValueError("Total must be greater than 0")
    return option / total


def get_faculty_rating(ratio: float) -> str:
    if ratio < 0 or ratio >= 1:
        raise ValueError("Ratio must be between 0 and 1 (exclusive of 1.0)")        
    if 0 <= ratio < 0.6:
        return "Unacceptable"
    elif ratio > 0.6 and ratio <= 0.7:
        return "Needs Improvement"
    elif ratio > 0.7 and ratio <= 0.8:
        return "Good"
    elif ratio > 0.8 and ratio <= 0.9:
        return "Very Good"
    elif 0.9 <= ratio < 1.0:
        return "Excellent"
    else:
        raise ValueError("Ratio must be between 0 and 1 (exclusive of 1.0)")

