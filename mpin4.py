import pandas as pd

def load_most_common_pins(pin_file_path, top_n=100):
    try:
        df = pd.read_csv(pin_file_path, header=None, names=["PIN", "frequency"])
        df["PIN"] = df["PIN"].astype(str).str.strip()
        top_pins = df.sort_values(by="frequency", ascending=False).head(top_n)["PIN"].tolist()
        return top_pins
    except FileNotFoundError:
        print("Error: PIN file not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def demographicPins(dob, spouse_dob, anniversary):
    pins = {
        "dob_self": set(),
        "dob_spouse": set(),
        "anniversary": set()
    }
    def permutations(date):
        if len(date) == 8:  
            dd = date[:2]
            mm = date[2:4]
            yyyy = date[4:]
            yy = date[6:]
            return {dd + mm, mm + dd, yyyy, yy + mm, mm + yy}
        return set()
    if dob:
        pins["dob_self"].update(permutations(dob))
    if spouse_dob:
        pins["dob_spouse"].update(permutations(spouse_dob))
    if anniversary:
        pins["anniversary"].update(permutations(anniversary))
    return pins

def evaluate_pin_strength(pin, common_pins, demographic_pins):
    reasons = []
    if pin in common_pins:
        reasons.append("COMMONLY_USED")
    
    if pin in demographic_pins["dob_self"]:
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if pin in demographic_pins["dob_spouse"]:
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if pin in demographic_pins["anniversary"]:
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")
    if reasons:
        return "WEAK", reasons
    else:
        return "STRONG", []


if __name__ == "__main__":
    pin_file_path = "/Users/dev/Desktop/OneBanc_assignment_devyani/most_common_pins/4_digit_freq.csv"  
    common_pins = load_most_common_pins(pin_file_path)

    print("Loaded Common PINs:", common_pins)

    dob = input("Enter your Date of Birth (DDMMYYYY): ")
    spouse_dob = input("Enter your Spouse's Date of Birth (DDMMYYYY): ")
    anniversary = input("Enter your Wedding Anniversary (DDMMYYYY): ")
    demographic_pins = demographicPins(dob, spouse_dob, anniversary)

    print("Generated Demographic PINs:", demographic_pins)

    pin = input("Enter PIN to evaluate its strength: ")
    if len(pin) != 4:
        print("invalid length, enter  digit")
    strength, reasons = evaluate_pin_strength(pin, common_pins, demographic_pins)
    print(f"Strength: {strength}")
    print(f"Reasons: {reasons}")