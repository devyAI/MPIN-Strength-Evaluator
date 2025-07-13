import pandas as pd
import datetime

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

def validateDOB(dob):
    try:
        if len(dob) != 8 or not dob.isdigit():
            return False, "Invalid format. Please enter DOB in DDMMYYYY format."
        dob_date = datetime.datetime.strptime(dob, "%d%m%Y").date()
        
        if dob_date > datetime.date.today():
            return False, "DOB cannot be in the future."
        
        return True, "Valid DOB."
    except ValueError:
        return False, "Invalid date. Please enter a valid DOB."

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
            return {dd + mm, mm + dd, yy + mm, mm + yy, dd + yy, yy + dd}
        return set()

    pins["dob_self"] = permutations(dob)
    pins["dob_spouse"] = permutations(spouse_dob)
    pins["anniversary"] = permutations(anniversary)
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
    pin_file_path = "/Users/dev/Desktop/OneBanc_assignment_devyani/most_common_pins/4_digit_freq.csv"  
    common_pins = load_most_common_pins(pin_file_path)

    print("Loaded Common PINs:", common_pins)

    while True:
        dob = input("Enter your Date of Birth(DDMMYYYY): ")
        is_valid, message = validateDOB(dob)
        print(message)
        if is_valid:
            break
    while True:
        spouse_dob = input("Enter your Spouse's Date of Birth(DDMMYYYY): ")
        is_valid, message = validateDOB(spouse_dob)
        print(message)
        if is_valid:
            break

    while True:
        anniversary = input("Enter your Anniversary Date(DDMMYYYY): ")
        is_valid, message = validateDOB(anniversary)
        print(message)
        if is_valid:
            break

    demographic_pins = demographicPins(dob, spouse_dob, anniversary)
    print("Generated Demographic PINs:", demographic_pins)

    pin = input("Enter a PIN to evaluate its strength: ")
    strength, reasons = evaluate_pin_strength(pin, common_pins, demographic_pins)
    print(f"PIN Strength: {strength}")
    print("Reasons:", reasons)