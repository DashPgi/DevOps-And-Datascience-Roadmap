declare @x int = 1;
declare @y char(20) = "hello world";
select @x, @y;

set @x = 2;


-- valid bacth
print 'hello world';
select *
go

-- invalid batch
print 'hello world';
select @s
go

-- conditional statements

if YEAR(GETDATE()) = 2026
BEGIN
    print 'It is 2026';
    PRINT 'HAPPY NEW YEAR';
END
else
    print 'It is not 2026';
print 'It is not 2026';


-- While loop
DECLARE @i INT = 1;
WHILE @i < 11
BEGIN
i++;
if @i = 5
BEGIN
print 'HALF WAY';
BREAK;
END
GO

-- dynamic query
DECLARE @sql NVARCHAR(MAX);

SET @sql = N'SELECT * FROM students WHERE city = @city';

EXEC sp_executesql
    @sql,
    N'@city NVARCHAR(50)',
    @city = N'Tehran';


-- functions
CREATE FUNCTION get_student_count(
    @city NVARCHAR(50)
    @age INT
)
RETURNS INT
as 
BEGIN
    datediff(year, @age, GETDATE())
    -CASE WHEN MONTH(GETDATE()) < MONTH(@age) THEN 1 ELSE 0 END
    RETURN @age;
END

SELECT dbo.get_student_count(18,5);

-- store procedures
CREATE PROC get_student_count
@city NVARCHAR(50)
@age INT
AS
set nocount on; -- -> no count the rows that are affected by the procedure

-- Trigger

CREATE TRIGGER Trigger ON dbo.Department AFTER UPDATE AS