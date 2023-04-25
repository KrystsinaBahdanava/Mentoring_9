**Directory and files description**

This Readme file describes each folder and artifacts that are used in the 2 part of the HomeWork module Test Automation for DQE - Frameworks.
Also, this file describes necessary steps that you need to do in order to execute AS_HW_2_PyTest.py file.

Folder "HomeTask 2 - PyTest" contains all necessary folders and artifacts for the 1 part of the homework. 
Folder structure:
* HomeTask 2 - PyTest                    &rarr; main folder
  * README.md                            &rarr; readme file
  * PyTestTask.txt                       &rarr; .txt file with the task description
  * requirements.txt                     &rarr; .txt file that contains all necessary libraries. Please, install this libraries by pip
  * tests                                &rarr; folder with main 'AS_HW_1_Robot_Framework.robot' file and artifacts that are generated by this file
    * resources                          &rarr; folder with files that are used by the 'AS_HW_2_PyTest.py' file  
      * SQL_testing_user_creation.sql    &rarr; .sql file with scripts that are used for testing user creation in the MSQ SQL SERVER
      * variables.py                     &rarr; .py file that contains credentials for connection to the MS SQL SERVER
    * AS_HW_2_PyTest.py                  &rarr; main .py file with tests
    * conftest.py                        &rarr; .py file that is used to modify visuals for the .html report file
    * report.html                        &rarr; .html file that is generated each time when 'AS_HW_2_PyTest.py' file is executed. Contains report that can be opened by any browser

  

**Steps to reproduce before execute 'AS_HW_2_PyTest.py' file**
1. Execute scripts from the 'SQL_testing_user_creation.sql' file;
2. Make sure that your MS SQL SERVER have enabled authentication by the SQL Server mode (https://stackoverflow.com/questions/11625899/cannot-login-after-creating-the-user-in-sql-server);
3. Make sure that your SQL SERVER name instance are SQLEXPRESS. In case you have another instance name, please, rename variable DBHost from the file ../resources/variables.py using next pattern: 'localhost//{your_instance_name}';
4. Make sure that you have installed all libraries from the file requirements.txt;
5. Open terminal in the IDE or command prompt. Navigate terminal to the directory, where you clone folder "HomeTask 2 - PyTest" and execute next script: cd "HomeTask 2 - PyTest/tests" or cd "tests";
6. Execute next script from command prompt: pytest --html=report.html  AS_HW_2_PyTest.py;
7. In the terminal you will see result of the execution. For more information, please open report.html file in any browser.