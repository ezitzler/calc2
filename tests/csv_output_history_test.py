"""Testing the Calculator"""
import pytest
from calc.history.csv_output import csv_output
from calc.calculations.addition import Addition

@pytest.fixture
def csv_output_fixture():
    csv_output.write_test()
