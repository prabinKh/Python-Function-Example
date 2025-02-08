# hospital management system

"""
.1 Add patients to the system.
2. Add doctors to the system
3. Schedule oppointments between patients and doctors
4. medical records for patients
5. view all patients and their medical records
6. view all doctors and their oppointments
7. Calculat the total revenue from all oppointments

"""
# Global variables to store hospital data
patients = {}  # Dictionary to store patients and their medical records
doctors = {}  # Dictionary to store doctors and their appointments
appointments = {}  # Dictionary to store appointments
medical_records = {}  # Dictionary to store medical records

# Function to add a patient
def add_patient(patient_id, name, age, gender):
    if patient_id in patients:
        print(f"Patient with ID {patient_id} already exists.")
    else:
        patients[patient_id] = {
            "name": name,
            "age": age,
            "gender": gender,
            "medical_records": []  # List to store medical records
        }
        print(f"Patient {name} with ID {patient_id} added to the system.")

# Function to add a doctor
def add_doctor(doctor_id, name, specialization):
    if doctor_id in doctors:
        print(f"Doctor with ID {doctor_id} already exists.")
    else:
        doctors[doctor_id] = {
            "name": name,
            "specialization": specialization,
            "appointments": []  # List to store appointments
        }
        print(f"Doctor {name} with ID {doctor_id} added to the system.")

# Function to schedule an appointment
def schedule_appointment(appointment_id, patient_id, doctor_id, date, time):
    if appointment_id in appointments:
        print(f"Appointment with ID {appointment_id} already exists.")
        return
    if patient_id not in patients:
        print(f"Patient with ID {patient_id} does not exist.")
        return
    if doctor_id not in doctors:
        print(f"Doctor with ID {doctor_id} does not exist.")
        return
    appointments[appointment_id] = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time,
        "status": "Scheduled"
    }
    patients[patient_id]["medical_records"].append(appointment_id)
    doctors[doctor_id]["appointments"].append(appointment_id)
    print(f"Appointment {appointment_id} scheduled for patient {patients[patient_id]['name']} with doctor {doctors[doctor_id]['name']} on {date} at {time}.")

# Function to record medical records for a patient
def record_medical_record(record_id, patient_id, diagnosis, treatment):
    if record_id in medical_records:
        print(f"Medical record with ID {record_id} already exists.")
        return
    if patient_id not in patients:
        print(f"Patient with ID {patient_id} does not exist.")
        return
    medical_records[record_id] = {
        "patient_id": patient_id,
        "diagnosis": diagnosis,
        "treatment": treatment
    }
    patients[patient_id]["medical_records"].append(record_id)
    print(f"Medical record {record_id} recorded for patient {patients[patient_id]['name']}.")

# Function to view all patients and their medical records
def view_all_patients():
    if not patients:
        print("No patients in the system.")
    else:
        print("\nAll Patients and Their Medical Records:")
        for patient_id, patient in patients.items():
            print(f"Patient ID: {patient_id}, Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}")
            print("Medical Records:")
            for record_id in patient["medical_records"]:
                if record_id in medical_records:
                    print(f"  Record ID: {record_id}, Diagnosis: {medical_records[record_id]['diagnosis']}, Treatment: {medical_records[record_id]['treatment']}")
                elif record_id in appointments:
                    print(f"  Appointment ID: {record_id}, Date: {appointments[record_id]['date']}, Time: {appointments[record_id]['time']}, Status: {appointments[record_id]['status']}")

# Function to view all doctors and their appointments
def view_all_doctors():
    if not doctors:
        print("No doctors in the system.")
    else:
        print("\nAll Doctors and Their Appointments:")
        for doctor_id, doctor in doctors.items():
            print(f"Doctor ID: {doctor_id}, Name: {doctor['name']}, Specialization: {doctor['specialization']}")
            print("Appointments:")
            for appointment_id in doctor["appointments"]:
                if appointment_id in appointments:
                    print(f"  Appointment ID: {appointment_id}, Patient: {patients[appointments[appointment_id]['patient_id']]['name']}, Date: {appointments[appointment_id]['date']}, Time: {appointments[appointment_id]['time']}, Status: {appointments[appointment_id]['status']}")

# Function to calculate the total revenue from all appointments
def calculate_total_revenue(price_per_appointment):
    total_revenue = len(appointments) * price_per_appointment
    print(f"Total revenue from all appointments: ${total_revenue:.2f}")

# Main function to interact with the user
def __main__():
    while True:
        print("\nWelcome to the Hospital Management System!")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Schedule Appointment")
        print("4. Record Medical Record")
        print("5. View All Patients")
        print("6. View All Doctors")
        print("7. Calculate Total Revenue")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            patient_id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            add_patient(patient_id, name, age, gender)

        elif choice == "2":
            doctor_id = input("Enter doctor ID: ")
            name = input("Enter doctor name: ")
            specialization = input("Enter doctor specialization: ")
            add_doctor(doctor_id, name, specialization)

        elif choice == "3":
            appointment_id = input("Enter appointment ID: ")
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            schedule_appointment(appointment_id, patient_id, doctor_id, date, time)

        elif choice == "4":
            record_id = input("Enter medical record ID: ")
            patient_id = input("Enter patient ID: ")
            diagnosis = input("Enter diagnosis: ")
            treatment = input("Enter treatment: ")
            record_medical_record(record_id, patient_id, diagnosis, treatment)

        elif choice == "5":
            view_all_patients()

        elif choice == "6":
            view_all_doctors()

        elif choice == "7":
            price_per_appointment = float(input("Enter price per appointment: "))
            calculate_total_revenue(price_per_appointment)

        elif choice == "8":
            print("Thank you for using the Hospital Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    __main__()