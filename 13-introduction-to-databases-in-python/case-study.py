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



