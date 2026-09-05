SELECT *
FROM students
WHERE name = 'Ali';

SELECT *
FROM students
ORDER BY id
LIMIT 10 OFFSET 20;


Select custid ,orderid,val,
LOG(val) as pval,
LEAD(val) as nval
First_Value(val) as fval,   
Last_Value(val) OVER(Partition by custid order by orderid rows between current row and 2 following) as last_3val
Last_Value(val) OVER(Partition by custid order by orderid rows between unbounded preceding and current row) as last_val




select empid,custid,Qty
FROM dbo.empcustomer
Pivot(sum(Qty) for custid in ([1],[2],[3])) as pvt

select empid,custid,Qty
FROM dbo.empcustomer
Unpivot(Qty) for custid in ([1],[2],[3])) as unpvt


CREATE TABLE dbo.Employee(  
    empid int,
    CONSTRAINT PK_Employee PRIMARY KEY (empid)
    empname varchar(20),
    department varchar(20),
    salalry int
    sysstart datetime,
      GENERATED ALWAYS AS ROW START HIDDEN NOT NULL,
    sysend datetime,
      GENERATED ALWAYS AS ROW END HIDDEN NOT NULL,
    PERIOD FOR SYSTEM_TIME (sysstart, sysend)
) WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.EmployeeHistory));