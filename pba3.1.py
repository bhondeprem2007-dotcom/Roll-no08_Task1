
class Resident:
    def __init__(self, name, flat_no, fee, category, status):
        self.name = name
        self.flat_no = flat_no
        self.fee = fee
        self.category = category
        self.status = status

    def display(self):
        print("\nResident Name:", self.name)
        print("Flat No:", self.flat_no)
        print("Maintenance Fee:", self.fee)
        print("Category:", self.category)
        print("Payment Status:", self.status)


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)
        print("Resident record added successfully!")

    def display_all(self):
        print("--- Apartment Maintenance Records ---")
        for resident in self.residents:
            resident.display()


society = Society()

r1 = Resident("Ansh", "A-101", 2500, "Monthly", "Paid")
r2 = Resident("Ananya", "A-102", 2500, "Monthly", "Pending")
r3 = Resident("Nehal", "B-201", 3000, "Quarterly", "Paid")

society.add_resident(r1)
society.add_resident(r2)
society.add_resident(r3)

society.display_all()
