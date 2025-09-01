import re

def validate_codes(codes):
    pattern = r'^[A-Z]{2}[a-z]{2}\d{4}$'
    valid_codes = []
    for code in codes:
        if re.fullmatch(pattern, code):
            valid_codes.append(code)
    return valid_codes

codes = ["ABcd1234", "ZZzz9999", "aaBB1234", "XYab5678", "QWoh9624", "koWT2613"]
print(validate_codes(codes))



