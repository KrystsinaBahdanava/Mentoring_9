"""
This file is used by python-html module in order to modify visuals of report.html file.
Module pytest contains methods that are used to change report titles, summary, etc.
Module py.xml contains namespace html that contains different options to modify html report
"""

import pytest
from py.xml import html


# This method updates report title
def pytest_html_report_title(report):
    report.title = "Report page of the tests for the 2 Home-task of 4 Module"


# This method add description of test cases, test steps and expected results to the .html report
@pytest.hookimpl
def pytest_html_results_summary(prefix):
    prefix.extend([html.h2("This report contains tests for tables hr.jobs, hr.employees, hr.location from database TRN"
                           )])

    prefix.extend([html.h2("Test cases description")])

    prefix.extend([html.h4("Test cases for the table hr.jobs:")])
    prefix.extend([html.h5("1. Comparing average of the max_salary from the table hr.jobs with hardcode value;")])
    prefix.extend([html.h5("2. Comparing value from the column min_salary with the value from the column max_salary "
                           "from table hr.jobs. In case min_salary is higher than max_salary then we count it as "
                           "an error.")])

    prefix.extend([html.h4("Test cases for the table hr.employees:")])
    prefix.extend([html.h5("1. Checking that values from email column are in the correct format. Check are done using "
                           "Regular Expressions (REGEX);")])
    prefix.extend([html.h5("2. Comparing the lowest value from the column salary table hr.employees with the lowest "
                           "value from the column min_salary from table hr.jobs. In case employees.salary is "
                           "lower than jobs.min_salary then we count it as an error.")])

    prefix.extend([html.h4("Test cases for the table hr.locations:")])
    prefix.extend([html.h5("1. Checking that values from column country_id are in the next list ['UK', 'US', 'CA', "
                           "'DE'];")])
    prefix.extend([html.h5("2. Validating that percentage of the NULL values in the column postal_code is lower than "
                           "20% if we count 100% as all number of values from the column postal_code.")])

    prefix.extend([html.h2("Test steps & test results description")])

    prefix.extend([html.h4("HR.JOBS_case_1:")])
    prefix.extend([html.h4("Test steps:")])
    prefix.extend([html.h5("1. Select average of the column max_salary and round it to 1 number after comma from "
                           "the MS SQL SERVER")])
    prefix.extend([html.h5("2. Compare average value from MS SQL SERVER with hardcoded value")])
    prefix.extend([html.h4("Expected result:")])
    prefix.extend([html.h5("1. Average value is equal to the 13210.5")])

    prefix.extend([html.h4("HR.JOBS_case_2:")])
    prefix.extend([html.h4("Test steps:")])
    prefix.extend([html.h5("1. Select all job_id where min_salary is higher than max_salary from MS SQL SERVER")])
    prefix.extend([html.h5("2. Check that MS SQL SERVER doesn't return anything by bool() function")])
    prefix.extend([html.h4("Expected result:")])
    prefix.extend([html.h5("1. MS SQL SERVER should not return any value: min_salary should be always lower than "
                           "max_salary for each job_id")])

    prefix.extend([html.h4("HR.EMPLOYEES_case_1:")])
    prefix.extend([html.h4("Test steps:")])
    prefix.extend([html.h5("1. Select rows where email is not fitted into the format [letters.letters@letters.com]. "
                           "Example: aleh.shylin@gmail.com")])
    prefix.extend([html.h5("2. Check that MS SQL SERVER doesn't return anything by bool() function")])
    prefix.extend([html.h4("Expected result:")])
    prefix.extend([html.h5("1. MS SQL SERVER should not return any value: all emails should fit the format")])

    prefix.extend([html.h4("HR.EMPLOYEES_case_2:")])
    prefix.extend([html.h4("Test steps:")])
    prefix.extend([html.h5("1. Calculate pseudo-boolean variable using condition that lowest employee salary should be"
                           " equal or higher than lowest salary from the table hr.jobs")])
    prefix.extend([html.h5("2. Verify that MS SQL SERVER returns 1 using simple comparison with 1")])
    prefix.extend([html.h4("Expected result:")])
    prefix.extend([html.h5("1. MS SQL SERVER should return True: lowest salary from table hr.employee should be equal "
                           "or higher than lowest salary from table hr.jobs")])

    prefix.extend([html.h4("HR.LOCATIONS_case_1:")])
    prefix.extend([html.h4("Test steps:")])
    prefix.extend([html.h5("1. Select distinct country_id from the table hr.locations")])
    prefix.extend([html.h5("2. Verify that MS SQL SERVER returns only those values that are in the list "
                           "('UK', 'US', 'CA', 'DE')")])
    prefix.extend([html.h4("Expected result:")])
    prefix.extend([html.h5("1. Column country_id should contain only values ('UK', 'US', 'CA', 'DE')")])

    prefix.extend([html.h4("HR.LOCATIONS_case_2:")])
    prefix.extend([html.h4("Test steps:")])
    prefix.extend([html.h5("1. Calculate pseudo-boolean variable using condition that percentage of the NULL values "
                           "in the column location_id is lower than 20%")])
    prefix.extend([html.h5("2. Verify that MS SQL SERVER returns 1 using simple comparison with 1")])
    prefix.extend([html.h4("Expected result:")])
    prefix.extend([html.h5("1. MS SQL SERVER should return True: percentage of the NULL values in the column "
                           "postal_code is lower than 20%")])
