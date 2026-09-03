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

-- READ COMMITED

SET ISOLATION LEVEL READ COMMITTED
 
-- REPEATABLE READ

BEGIN TRANS
SET ISOLATION LEVEL REPEATABLE READ

SELECT * 
FROM Porduction.Product
WHERE Productid = 2

UPDATE  Porduction.Product
SET unitprice += 1.00

COMMIT TRANS

-- SERIALIZABLE

SET ISOLATION LEVEL SERIALIZABLE