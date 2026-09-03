-- Transaction 

BEGIN TRANS;

UPDATE account
SET Balance = Balance - 100
WHERE Id = 1;

UPDATE account
SET Balance = Balance + 100
WHERE Id = 2;

COMMIT TRANS;

-- Isolation Level 
-- READ UNCOMMITTED

SET ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM account; -- Dirty Page    
FROM Porduction.Profuct with(nolock); -- Lock free read

