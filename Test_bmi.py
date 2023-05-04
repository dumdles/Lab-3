import Lab2.bmi as bmi

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(height=1.80, weight=75) == 0

def test_bmi_over_weight():
    assert bmi.calculate_bmi(height=1.80, weight=90) == 1

def test_bmi_under_weight():
    assert bmi.calculate_bmi(height=1.80, weight=50) == -1
