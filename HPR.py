#____Hospital Patient Rejistration(HPR)______

def patient_rejistartion():
    rejisterd = False
    if rejisterd:
        print("Go and see the doctor direct..")
    else:
        rejisterd = False
        Full_name = input("- ")
        Age = int(input("- "))
        Place_of_resident =input("- ")
        print("Payment required for all rejistration and file creating.")


while True:
    patient = patient_rejistartion()
    print(patient)
