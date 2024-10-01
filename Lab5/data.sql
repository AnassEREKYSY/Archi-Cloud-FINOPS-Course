CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    Name NVARCHAR(100),
    Position NVARCHAR(100),
    Salary DECIMAL(10, 2)
);

INSERT INTO Employees (ID, Name, Position, Salary) VALUES (1, 'Alice Smith', 'Manager', 75000);
INSERT INTO Employees (ID, Name, Position, Salary) VALUES (2, 'Bob Johnson', 'Developer', 60000);
INSERT INTO Employees (ID, Name, Position, Salary) VALUES (3, 'Charlie Brown', 'Designer', 55000);
