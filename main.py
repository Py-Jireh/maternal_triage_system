# Mini Patient Database + Maternal Risk Checker
# Author: Jireh Mbah
# Date: 16/03/2026

print("=== HOSPITAL PATIENT DATABASE ===")
print("Welcome to the mini patient tracker!")
print("Manage patients and check maternal risk")
print()

# List to store patient data
patients = []

while True:
    print("1. Add new patient")
    print("2. Show all patients")
    print("3. Count patients")
    print("4. Exit")
    
    choice = input("Select option: ")
    print()
    
    if choice == "1":
        patient = {}
        patient["name"] = input("Enter patient name: ")
        patient["age"] = int(input("Enter age: "))
        patient["bp"] = int(input("Enter BP (systolic): "))
        patient["weeks"] = int(input("Enter weeks pregnant: "))
        
        # Risk calculation
        risk = "Normal"
        if patient["age"] < 18 or patient["age"] > 35 or patient["bp"] >= 140:
            risk = "HIGH RISK"
        patient["risk"] = risk
        
        patients.append(patient)
        print("Patient added.\n")
    
    elif choice == "2":
        if len(patients) == 0:
            print("No patients in the system yet.\n")
        else:
            print("----- PATIENT LIST -----")
            print("Name | Age | BP | Weeks | Risk")
            print("-------------------------------")
            for i, p in enumerate(patients):
                print(f"{i+1}. {p['name']} | Age: {p['age']} | BP: {p['bp']} | Weeks: {p['weeks']} | Risk: {p['risk']}")
            print("-------------------------------\n")
    
    elif choice == "3":
        print(f"Total patients: {len(patients)}\n")
    
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.\n")
