from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

# Test get_employees_by_age_range() function
def test_get_employees_by_age_range():
    # Test case where age range is 25-30
    result = get_employees_by_age_range(25, 30)
    assert len(result) == 2
    assert result[0]['name'] == 'John'
    assert result[1]['name'] == 'Jane'

    # Test case where age range is 30-40
    result = get_employees_by_age_range(30, 40)
    assert len(result) == 4
    assert result[0]['name'] == 'John'
    assert result[1]['name'] == 'Chloe'
    assert result[2]['name'] == 'Mike'
    assert result[3]['name'] == 'Peter'

    # Test case where age range is 20-50
    result = get_employees_by_age_range(20, 50)
    assert len(result) == 6
    assert result[0]['name'] == 'John'
    assert result[1]['name'] == 'Jane'
    assert result[2]['name'] == 'Mary'
    assert result[3]['name'] == 'Chloe'
    assert result[4]['name'] == 'Mike'
    assert result[5]['name'] == 'Peter'

# Test calculate_average_salary() function
def test_calculate_average_salary():
    result = calculate_average_salary()
    assert round(result, 1) == 60500.0

# Test get_employees_by_dept() function
def test_get_employees_by_dept():
    # Test case where department is 'Marketing'
    result = get_employees_by_dept('Marketing')
    assert len(result) == 2
    assert result[0]['name'] == 'Jane'
    assert result[1]['name'] == 'Mary'

    # Test case where department is 'Sales'
    result = get_employees_by_dept('Sales')
    assert len(result) == 2
    assert result[0]['name'] == 'John'
    assert result[1]['name'] == 'Peter'

    # Test case where department is 'Engineering'
    result = get_employees_by_dept('Engineering')
    assert len(result) == 2
    assert result[0]['name'] == 'Chloe'
    assert result[1]['name'] == 'Mike'
