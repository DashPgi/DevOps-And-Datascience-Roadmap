select *
From Person.Person
WHERE PersonType like 'E_' and 
	Title is not null
-- Group By Title
Order by BusinessEntityID