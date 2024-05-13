# lab09
week 9 python lab

Exercises

1. Expand the example Fraction in the lecture notes by adding the following features:

Add a method to convert the fraction to a float number.
Add the division operator "/" to class (hint: __truediv__).
Add a method to invert the fraction (eg, 2/3 => 3/2).
Create several Fraction objects and perform conversion, reversion and division operations on these objects.

2. Write a TicketMachine class, which models a ticket machine that issues flat-fare tickets. The price of a ticket is specified via the constructor (you can use price variable).

Your TicketMachine class will have the following methods:

-insertMoney, which receives an amount of money from a customer and updates customer's balance (you can use balance variable).
-getPrice, which return and prints the price of a ticket.
-getBalance, which returns and prints the amount of money already inserted for the ticket.
-printTicket, which prints a ticket, update the total collected by the machine and reduce the balance to zero.
-The ticket will be printed if the customer's balance is greater than or equal to ticket price. You also need to define a variable e.g., total, which keeps track of the total amount of money collected by the machine.

Your program should be able to check if the ticket price and the amount entered by the customer is valid. For example, ticket price and the amount entered by the user cannot be negative.

3. Kevin, a young businessman owns number of ticket machines (similar to the one you designed in Exercise 2 above with some necessary modifications) located at various places in the city. He wants a system to be developed that would help managing all of his machines with following minimal functionalities:

Add a new machine to the system
Remove a machine from the system
See the total of any machine
Get the total sale of all machines.
