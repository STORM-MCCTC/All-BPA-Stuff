import random

# Global variables
name = ""
medical_supplies = random.randint(50, 100)
energy = random.randint(70, 100)
ewoks_treated = 0

def display_status():
    print("\n-----------------------------------")
    print(f"supplies: {medical_supplies}")
    print(f"energy: {energy}")
    print(f"ewoks treated: {ewoks_treated}")
    print("-----------------------------------\n")
    pass

def treat_ewok():
    global medical_supplies
    global ewoks_treated
    choice = ["Minor", "Moderate", "Severe"]
    ewoks_condition = random.choice(choice)
    if ewoks_condition == "Minor" and medical_supplies >= 5:
        medical_supplies -= 5
        ewoks_treated += 1
        print("\nTreated ewok in Minor condition")
        display_status()
    elif ewoks_condition == "Minor" and medical_supplies <= 5:
        print("\nNeed more Medical Supplies")
    else:
        pass
    if ewoks_condition == "Moderate" and medical_supplies >= 10:
        medical_supplies -= 10
        ewoks_treated += 1
        print("\nTreated ewok in Moderate condition")
        display_status()
    elif ewoks_condition == "Moderate" and medical_supplies <= 10:
        print("\n\nNeed more Medical Supplies")
    else:
        pass
    if ewoks_condition == "Severe" and medical_supplies >= 15:
        medical_supplies -= 15
        ewoks_treated += 1
        print("\nTreated ewok in Severe condition")
        display_status()
    elif ewoks_condition == "Severe" and medical_supplies <= 15:
        print("\nNeed more Medical Supplies")
    else:
        pass

def start_shift():
    global name
    print("\nWelcome to the forest moon of Endor!")
    name = input("Enter your name, Medic: ")
    print(f"Welcome, Medic {name}. Ewoks are depending on you.")
    input("Press Enter when ready to begin your shift...\n")
   
    for _ in range(3):
        encounter_ewok()
        if medical_supplies == 0 or energy == 0:
            break
        else:
            pass
        display_status()
    end_shift()


def encounter_ewok():
    print("\nAn injured Ewok needs your help!\n")
    while True:
        try:
            encounter = int(input("| 1 - Help | 2 - Skip | : "))
            if encounter == 1:
                treat_ewok()
            elif encounter == 2:
                break
            else:
                print("Input 1 or 2 please.")
                pass
        except ValueError as e:
            print(e)
    end_shift()
    
def end_shift():
    global energy
    global medical_supplies
    energy += random.randint(10, 50)
    medical_supplies += random.randint(10, 50)
    print("\nShift ended...\n")
    display_status()

start_shift()