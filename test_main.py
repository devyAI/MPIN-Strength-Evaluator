from mpin4 import evaluate_pin_strength


test_cases = [
    # Format: (pin, common_pin, demographic_pins, expected_strength, expected_reasons)
    ("1234", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "WEAK", ["COMMONLY_USED"]),
    ("0201", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("0302", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("0506", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("7890", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "STRONG", []),
    ("1998", "1234", {"dob_self": {"0201", "1998"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("1995", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302", "1995"}, "anniversary": {"0506"}}, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("2010", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506", "2010"}}, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("1111", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "STRONG", []),
    ("0000", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "STRONG", []),
    ("0102", "1234", {"dob_self": {"0201", "0102"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("0203", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302", "0203"}, "anniversary": {"0506"}}, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("0605", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506", "0605"}}, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("9801", "1234", {"dob_self": {"0201", "9801"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("9502", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302", "9502"}, "anniversary": {"0506"}}, "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("1050", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506", "1050"}}, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("5010", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506", "5010"}}, "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("5678", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "STRONG", []),
    ("4321", "1234", {"dob_self": {"0201"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "STRONG", []),
    ("0198", "1234", {"dob_self": {"0201", "0198"}, "dob_spouse": {"0302"}, "anniversary": {"0506"}}, "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
]


for i, (pin, common_pin, demographic_pins, expected_strength, expected_reasons) in enumerate(test_cases):
    strength, reasons = evaluate_pin_strength(pin, common_pin, demographic_pins)
    print(f"Test Case {i + 1}:")
    print(f"PIN: {pin}")
    print(f"Expected Strength: {expected_strength}, Actual Strength: {strength}")
    print(f"Expected Reasons: {expected_reasons}, Actual Reasons: {reasons}")
    print(f"Result: {'PASS' if strength == expected_strength and set(reasons) == set(expected_reasons) else 'FAIL'}")
    print("-" * 50)