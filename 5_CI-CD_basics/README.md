**Directory and files description**


This Readme file describes each folder and artifacts that are used in the 5 module CI_CD basics for DQE.
Also, this file describes necessary steps that you need to do in order to create Docker container with Jenkins.


Folder structure:
  * PyTest                                          &rarr; folder with a PyTest files from a previous homework that are used to test SQL SERVER
  * README.md                                       &rarr; Readme file
  * CI_pytest.jenkins                               &rarr; .jenkins file with code for CI pipeline that test SQL SERVER database 
  * Docker configuration file                       &rarr; folder with configuration file for Docker image
    * Dockerfile                                    &rarr; docker configuration file for image with Jenkins
  * CI-CD basics for DQE_Practice Instructions.docx &rarr; .docx file with maintenance instruction 
  * CI-CD basics for DQE_HW.docx                    &rarr; .docx file with Hometask
  * HW_Merging_strategy_description                 &rarr; .docx file with description of chosen merging strategy


**Steps to reproduce to create Docker container with Jenkins and maintain CI pipeline**
1. Install Docker from the official site https://www.docker.com/get-started/
2. In the Git Bash execute next script: "docker pull jenkins/jenkins". And scripts below
3. Change directory in the Git Bash to the folder Docker configuration file and execute next script: "docker build -t "jenkins:test_1" ."
4. Execute next script: "docker run --rm --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins:test_1". Docker container with name 'Jenkins' should be created
5. In the Jenkins install all recommended plugins and plugin 'HTML Publisher report'. This plugin allows to look at .html pytest report in the Jenkins
6. Create new pipeline: connect to the git 'https://github.com/alehshylin/Data_Quality_Engineering_Intermediate_9', branch: 'main'. Jenkins file with script: '5_CI-CD_basics/CI_pytest.jenkins'
7. Since we are testing SQL Server database, we need to maintain connection between Docker and SQL Server. To do this, repeat steps from 'CI-CD basics for DQE_Practice Instructions' file

After that steps Jenkins CI pipeline should be created and run successfully


**Description of Jenkins CI pipeline from file CI_pytest.jenkins**
This pipeline take PyTest scripts from the Git repository and execute it on the Jenkins environment. PyTest scripts test 
data from SQL Server database that is installed locally on your computer and generate .html report after each test. 
Jenkins additionally generate it own .html report from the PyTest report. You can look at this report in the Jenkins UI.
CI pipeline is executed by click: there are no time or git triggers.