class Employee:
    """
    Employee class consisting of member variables and methods to define an employee
    """

    def __init__(self, first_name, last_name, department, age=None, salary=0.0):
        """
        Method to initialize an instance of employee
        :param first_name: First name of employee
        :param last_name: Last name of employee
        :param age: Age (years)
        :param department: Name of department
        :param salary: salary (as float)
        :return: None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary

    def __repr__(self):
        """
        Just to make class instances human readable
        :return:
        """
        return '%s %s, %s' % (self.first_name, self.last_name, self.department)

    def __lt__(self, other):
        """
        Defining the sorting based on less than operator
        :param other: Other class variable
        :return: The lesser value
        """
        return self.first_name < other.first_name


emp = Employee('Tarun', 'Chhabra', 'Department of Computer Science', 27, 17.0)
print emp

employees = [emp]

emp = Employee('Devika', 'Desai', 'Department of Computer Science')
employees.append(emp)

emp = Employee('Sudipto', 'Biswas', 'Department of Computer Science')
employees.append(emp)

employees.sort()
print employees
