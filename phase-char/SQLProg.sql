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