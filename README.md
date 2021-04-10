# zuri_class_task


## About the code

This is a python script used in instantiating a budget object with categories in food, clothing and entertainment.
There are defined functions to take certain actions.
## Built with

 - Python, v3.9.2

## Prerequisites

Install python on the system

 - **Linux(Ubuntu)**
		Read installation instructions [here](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/)	
		
 - **Windows**
 Read installation instructions [here](https://www.python.org/downloads/windows/)


## Usage

 

 1. Clone the repository


    git clone https://github.com/Chinwendu20/pythonclass.git

 2. Change to repo's directory
	
  ```
    cd pythonclass
   
  ```

3. Open the script  with your favourite editor

4.Create a budget object. Example:

```
budget_object=Budget(food=10, entertainment=90)

```

### Performing operations

1. Performing deposit:

Depositing 20 and 80 unit of money to food and clothing category 

```
budget.deposit(food=20, clothing=80)

```
2. Performing withdrawal:

Withdrawing 20 unit of money from food category.

```
budget.withdraw(food=20)

```
3. Compute category balance:

Computing  category balance for food, entertainment, clothing

```
budget.compute_categories(food, entertainment, clothing)

```
4. Transfer funds between each category

Transferring 50 unit of money fromfood to entertainment category.

```
budget.transfer_balance_among_categories(food, entertainment, 50)

```

## Running the script
 
 

    python .\class.py    


## Functionalities

 - Deposit into eaach category
 - Withdraw from each category
 - Transfer from one category to the other

## Acknowledgement

 - [Ingressive for good](https://ingressive.org/)
 - [Zuri team](https://zuri.team/)



Thanks for putting the zuri training together.
