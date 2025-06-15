class Employee:
    company = "TechCorp"

    @staticmethod
    def get_company():
        print("Company is", Employee.company)

e1 = Employee()
e1.get_company()
