import pandas as pd


def load_top_pins(pin_file_path, top_n=100):
    try:
        df = pd.read_csv(pin_file_path, header=None, names=["PIN", "Frequency"])
        df["PIN"] = df["PIN"].astype(str).str.strip()
        top_pins = df.sort_values(by="Frequency", ascending=False).head(top_n)["PIN"].tolist()
        return top_pins
    except FileNotFoundError:
        print("Error: PIN file not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def generate_demographic_pins(dob, spouse_dob, anniversary):
    pins = {
        "dob_self": set(),
        "dob_spouse": set(),
        "anniversary": set()
    }
    def extract_combinations(date):
        if len(date) == 8:  
            dd = date[:2]
            mm = date[2:4]
            yyyy = date[4:]
            yy = date[6:]
            return {dd + mm + yy,mm + dd + yy, yyyy[:2] + dd + mm, yyyy[:2] + mm + dd}
        return set()
    if dob:
        pins["dob_self"].update(extract_combinations(dob))
    if spouse_dob:
        pins["dob_spouse"].update(extract_combinations(spouse_dob))
    if anniversary:
        pins["anniversary"].update(extract_combinations(anniversary))
    
    return pins

def evaluate_pin_strength(pin, common_pins, demographic_pins):
    reasons = []
    if pin in common_pins:
        reasons.append("common_pin")
    
    if pin in demographic_pins["dob_self"]:
        reasons.append("demographic_dob_self")
    if pin in demographic_pins["dob_spouse"]:
        reasons.append("demographic_dob_spouse")
    if pin in demographic_pins["anniversary"]:
        reasons.append("demographic_anniversary")
    
    if reasons:
        return "WEAK", reasons
    else:
        return "STRONG", []


if __name__ == "__main__":
    pin_file_path = "/Users/dev/MPIN_OneBanc_Assignment/most_common_pins/6_digit_pins.csv"  # Replace with your actual file path
    common_pins = load_top_pins(pin_file_path)
    print("Loaded Common PINs:", common_pins)

    dob = input("Enter your Date of Birth (DDMMYYYY): ")
    spouse_dob = input("Enter your Spouse's Date of Birth (DDMMYYYY): ")
    anniversary = input("Enter your Wedding Anniversary (DDMMYYYY): ")
    demographic_pins = generate_demographic_pins(dob, spouse_dob, anniversary)
    print("Generated Demographic PINs:", demographic_pins)

    pin = input("Enter PIN to evaluate its strength: ")
    if len(pin) != 6:
        print("invalid length, enter 6 digit")
    else:
        strength, reasons = evaluate_pin_strength(pin, common_pins, demographic_pins)
        print(f"Strength: {strength}")
        print(f"Reasons: {reasons}")