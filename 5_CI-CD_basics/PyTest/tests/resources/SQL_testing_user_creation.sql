-- This script is used for Robot Framework user creation and granting access to the TRN database

CREATE LOGIN RobotFrameworkLogin   
    WITH PASSWORD = 'Robot12345';  
GO  

CREATE USER RobotFrameworkUser FOR LOGIN RobotFrameworkLogin;  
GO  

USE TRN;
GRANT SELECT ON hr.locations TO RobotFrameworkUser;
GRANT SELECT ON hr.employees TO RobotFrameworkUser;
GRANT SELECT ON hr.jobs TO RobotFrameworkUser;
GO

DROP LOGIN RobotFrameworkUser;
GO

DROP USER RobotFrameworkUser;
GO