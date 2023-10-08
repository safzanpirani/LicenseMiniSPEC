import re
INDIAN_NUMBER_PLATE_REGEX = r'^[A-Z]{2}\ ?\d{2}\ ?[A-Z]+\ ?\d{4}$'


def is_indian_number_plate(plate):
    return re.match(INDIAN_NUMBER_PLATE_REGEX, plate) is not None



def test_regex():
    test_cases = ["MH 04 JM 8765", "DL-12XY5678", "MH04Z8765"]
    for case in test_cases:
        print(f"'{case}' is valid: {is_indian_number_plate(case)}")

test_regex()
