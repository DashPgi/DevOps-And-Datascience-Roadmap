Select custid ,orderid,val,
LOG(val) as pval,
LEAD(val) as nval
First_Value(val) as fval,   
Last_Value(val) OVER(Partition by custid order by orderid rows between current row and 2 following) as last_3val
Last_Value(val) OVER(Partition by custid order by orderid rows between unbounded preceding and current row) as last_val
