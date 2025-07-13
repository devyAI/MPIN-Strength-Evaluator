# MPIN Strength Checker

## Credits
The `.csv` datasets used in this project for commonly used PINs are sourced from [SecLists](https://github.com/danielmiessler/SecLists), a curated collection of security-related lists maintained by Daniel Miessler. These datasets were selected after thorough research to ensure they represent real-world patterns and commonly used PINs.

## Introduction: What is MPIN?
An MPIN (Mobile Personal Identification Number) is a 4-digit or 6-digit numeric code used by users to secure their mobile banking or payment applications. It acts as a password to authenticate transactions and access sensitive information. Ensuring the strength of an MPIN is critical to prevent unauthorized access and enhance security.

## Why Do Users Choose Weak MPINs?
Many users end up choosing weak MPINs due to:
1. **Convenience**: Easy-to-remember patterns like `1234` or `1111`.
2. **Demographics**: Using personal information such as birthdates, anniversaries, or spouse's birthday.
3. **Lack of Awareness**: Users may not realize the security risks associated with predictable PINs.

Weak MPINs are vulnerable to brute-force attacks and can be easily guessed by attackers, compromising the security of the user's account.

## Approach / Strategy
The assignment is divided into multiple parts to address the problem systematically:

### Part A: Commonly Used PINs
- Identify if the MPIN is one of the commonly used PINs based on a predefined list of patterns.

### Part B: Demographic-Based PINs
- Enhance the program to take user demographics (e.g., DOB, anniversary, spouse's DOB) as input and evaluate the strength of the MPIN.

### Part C: Strength Evaluation
- Provide a detailed evaluation of the MPIN's strength:
  - **Strength**: `WEAK` or `STRONG`
  - **Reasons for Weakness**:
    - `COMMONLY_USED`
    - `DEMOGRAPHIC_DOB_SELF`
    - `DEMOGRAPHIC_DOB_SPOUSE`
    - `DEMOGRAPHIC_ANNIVERSARY`

## Dataset Information
The datasets used for commonly used PINs (both 4-digit and 6-digit) were sourced from [SecLists](https://github.com/danielmiessler/SecLists). SecLists is a well-known repository of security-related lists, including passwords, PINs, usernames, and more. These datasets were selected after careful research to ensure they accurately represent real-world usage patterns.

## How It Works
1. **Load Commonly Used PINs**:
   - The program dynamically loads the top `N` commonly used PINs from the `.csv` dataset.
2. **Generate Demographic-Based PINs**:
   - The program generates PINs based on user-provided demographics (DOB, spouse's DOB, anniversary).
3. **Evaluate PIN Strength**:
   - The program evaluates the strength of the PIN and provides detailed reasons for weakness.

## How to Run
1. Clone the repository.
2. Install Python 3.12 or higher.
3. Run the ```python3 mpin4.py``` command to run the 4_digit PIN program 
4. Run the ```python3 mpin6.py``` command to run the 6_digit PIN program
5. run the ```python3

## Future Enhancements
- Dynamic updates to commonly used PINs list based on external data sources.
- Integration with APIs for real-time PIN strength evaluation.
- Support for alphanumeric PINs.

---
This project aims to educate users about the importance of choosing strong MPINs and provide a robust solution to evaluate their strength.