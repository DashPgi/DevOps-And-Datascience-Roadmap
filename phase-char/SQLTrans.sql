-- Transaction 

BEGIN TRANS;

UPDATE account
SET Balance = Balance - 100
WHERE Id = 1;

UPDATE account
SET Balance = Balance + 100
WHERE Id = 2;

COMMIT TRANS;