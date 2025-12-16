def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Employee Department: {department}\n"
        f"Employee Salary: {salary}"
    )
    return result


if __name__ == "__main__":
    name = "tanu"
    emp_id = "E190"
    department = "Accounts"
    salary = 100000

    print(employee_details(name, emp_id, department, salary))
