"""
This file contains test cases for tables hr.jobs, hr.employees, hr.location from database TRN
File variables.py in the folder resources contains credentials for the testing user in the MS SQL SERVER. Testing user
    is the same as in the Robot Framework task
Was used pymssql module to maintain connection between PyTest and MS SQL SERVER. Connection string is the same as in the
    Robot Framework task
Each test uses sql_connector() method that extract data from MS SQL SERVER. When data is extracted, method close
    connection with MS SQL SERVER
"""


"""
These modules are not used in the file. I added them in the file because there are necessary to be installed before 
    running the tests
"""
import pytest
import pytest_html


import pymssql
from resources import variables


def sql_connector(sql_string):
    with pymssql.connect(host=variables.DBHost, user=variables.DBUsername, password=variables.DBPassword,
                         database=variables.DBName) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_string)
        values = cursor.fetchall()
        return values


class TestCaseJobs:
    """
        This test case contains two tests for the table hr.jobs from database TRN.
        First test compare average of the max_salary from the table hr.jobs with hardcode value
        Second test compare value from the column min_salary with the value from the column max_salary from table hr.jobs
        In case min_salary is higher than max_salary then we count it as an error
    """

    def test_hr_jobs_case_1(self):
        assert sql_connector("SELECT ROUND(AVG(max_salary),1) as max_salary FROM hr.jobs;")[0][0] == 13210.5

    def test_hr_jobs_case_2(self):
        assert bool(sql_connector("SELECT job_id FROM hr.jobs WHERE IIF(min_salary < max_salary, 1, 0) != 1;")) is False


class TestCaseEmployees:
    """
        This test case contains two tests for the table hr.employees from database TRN.
        First test checks that values from email column are in the correct format. Check are done using Regular
            Expressions (REGEX)
        Second test compare the lowest value from the column salary table hr.employees with the lowest value from
        the column min_salary from table hr.jobs. In case employees.salary is lower than jobs.min_salary then we
            count it as an error

    """

    def test_hr_employees_case_1(self):
        assert bool(sql_connector("SELECT * FROM hr.employees WHERE email NOT LIKE '%[a-z]%[.]%[a-z][@][a-z]%[.]org%';")
                    ) is False

    def test_hr_employees_case_2(self):
        assert sql_connector("SELECT IIF(MIN(employees.salary) >= MIN(jobs.min_salary), 1, 0) FROM hr.employees,"
                             " hr.jobs;")[0][0] == 1


class TestCaseLocations:
    """
        This test case contains two tests for the table hr.locations from database TRN.
        First test checks values from column country_id should be in the next list ['UK', 'US', 'CA', 'DE']
        Second test validates that percentage of the NULL values in the column postal_code is lower than 20%
        if we count 100% as all number of values from the column postal_code
    """

    def test_hr_locations_case_1(self):
        values = sql_connector("SELECT DISTINCT country_id FROM hr.locations ORDER BY country_id;")
        for key in values:
            for string in key:
                assert string in ['CA', 'DE', 'UK', 'US']

    def test_hr_locations_case_2(self):
        assert sql_connector("SELECT IIF(CAST(null_count.cnt AS FLOAT) / CAST(not_null_count.cnt AS FLOAT) * 100 "
                             "< 20, 1, 0) as value FROM (SELECT COUNT(postal_code) as cnt FROM hr.locations WHERE "
                             "postal_code IS NULL) as null_count,(SELECT COUNT(postal_code) as cnt FROM hr.locations) "
                             "as not_null_count;")[0][0] == 1
