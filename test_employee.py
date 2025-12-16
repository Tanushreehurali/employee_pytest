from employee import employee_details


def test_employee_details_output():
    result = employee_details("Riya", "E190", "Accounts", 100000)

    expected = (
        "Employee Name: tanu\n"
        "Employee ID: E190\n"
        "Employee Department: Accounts\n"
        "Employee Salary: 100000"
    )

    assert result == expected
