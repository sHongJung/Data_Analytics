create database Second_International_Bank;
use Second_International_Bank;

create table Customers (
	ID int(50) auto_increment,
    FirstName varchar(50),
    LastName varchar(50),
    Loan decimal(20,2),
    Checking decimal(20,2),
    Savings decimal(20,2),
    primary key(ID)
);

insert into Customers(FirstName,LastName,Loan,Checking,Savings)
values("Jacob", "Deming", 2000.00, 1000.00, 20000.50);

insert into Customers(FirstName,LastName,Loan,Checking,Savings)
values("Bob", "Someone", 50000.00, 10.75, 2.05);

insert into Customers(FirstName,LastName,Loan,Checking,Savings)
values("Shelly", "RichRich", 0.00, 1000000.00, 50000025.00);

insert into Customers(FirstName,LastName,Loan,Checking,Savings)
values("Ryan", "Middleman", 100.00, 250.00, 10000.00);

insert into Customers(FirstName,LastName,Loan,Checking,Savings)
values("Shannon", "Waffles", 2000.00, 1000.00, 20000.50);

select * from Customers;