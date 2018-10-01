'''Here, you will bring together all of the skills you acquired in the previous chapters to work on a real life project! 
From connecting to a database, to populating it, to reading and querying it, you will have a chance to apply all the 
key concepts you learned in this course. 

Enjoy!'''


'''Setup the Engine and MetaData

In this exercise, your job is to create an engine to the database that will be used in this chapter. 
Then, you need to initialize its metadata.
Recall how you did this in Chapter 1 by leveraging create_engine() and MetaData.'''

# Import create_engine, MetaData
from sqlalchemy import MetaData, create_engine

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Initialize MetaData: metadata
metadata = MetaData()

'''
Create the Table to the Database
Having setup the engine and initialized the metadata, you will now define the census table object and then create it in the database using using the metadata and engine from the previous exercise. To create it in the database, you will have to use the .create_all() method on the metadata with engine as the argument.
It may help to refer back to the Chapter 4 exercise in which you learned how to create a table.
INSTRUCTIONS
100XP
Import Table, Column, String, and Integer from sqlalchemy.
Define a census table with the following columns:
'state' - String - length of 30
'sex' - String - length of 1
'age' - Integer
'pop2000' - Integer
'pop2008' - Integer
Create the table in the database using the metadata and engine.
'''
# Import Table, Column, String, and Integer
from sqlalchemy import (Table, Column, String, Integer)

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()))

# Create the table in the database
metadata.create_all(engine)

'''Reading the Data from the CSV

Leverage the Python CSV module from the standard library and load the data into a list of dictionaries.

It may help to refer back to the Chapter 4 exercise in which you did something similar.'''


# Create an empty list: values_list
values_list = []

# Iterate over the rows
for row in csv_reader:
    # Create a dictionary with the values
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3], 'pop2008': row[4]}
    # Append the dictionary to the values list
    values_list.append(data)
    

'''Load Data from a list into the Table

Using the multiple insert pattern, in this exercise, you will load the data from values_list into the table.'''

# Import insert
from sqlalchemy import insert

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)



'''
Build a Query to Determine the Average Age by Population
In this exercise, you will use the func.sum() and group_by() methods to first determine the average age weighted by the population in 2008, and then group by sex.
As Jason discussed in the video, a weighted average is calculated as the sum of the product of the weights and averages divided by the sum of all the weights.
For example, the following statement determines the average age weighted by the population in 2000:
stmt = select([census.columns.sex,
               (func.sum(census.columns.pop2000 * census.columns.age) /
                func.sum(census.columns.pop2000)).label('average_age')
               ])
INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import select from sqlalchemy.
Build a statement to:
Select sex from the census table.
Select the average age weighted by the population in 2008 (pop2008). See the example given in the assignment text to see how you can do this. Label this average age calculation as 'average_age'.
Group the query by sex.
Execute the query and store it as results.
Loop over results and print the sex and average_age for each record.
'''
# Import select
from sqlalchemy import select

# Calculate weighted average age: stmt
stmt = select([census.columns.sex,
               (func.sum(census.columns.pop2008 * census.columns.age) /
                func.sum(census.columns.pop2008)).label('average_age')
               ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the average age by sex
for result in results:
print(result.sex, result.average_age)