# MySQL Notes - Gregg Bowen

# *Why MySQL and database design?
# In these times, you have probably created dozens of different accounts for different websites and services, all with your own 
# login information. You've probably written posts on forums, "liked" posts or even uploaded and shared images, videos or audio 
# with other people on the Internet. One thing in common on all these different websites is that you are always  creating, 
# manipulating and saving data .

# In addition to the HTML and CSS that make up the  view  of a particular page, and the backend logic that dictates the 
# functionality, there is also the  database  , which takes care of your data! Databases are mere collections of organized 
# information that can be easily accessed, managed and updated. As a full-stack developer, you should be familiar with the 
# creation of your databases and the design of the rules by which data is stored!

# One of the most important things about database design is to organize your data to minimize repetition. Your database is 
# the backbone of your application, and it is very important to understand how to properly organize it to maximize efficiency 
# and minimize data queries. In this chapter, we will explore how to create  relational database models and explore the different 
# ways in which you can relate data using them.

# *Why ERD first?
# ERD is the abbreviation for 'Entity Relationship Diagram'. That is just a fancy way of saying that ERDs are essentially  visual 
# planes  of how your database looks and behaves. ERD and SQL work together very intimately. An ERD is a map of the structure of 
# how we want to store our data, and SQL is the language we use to manipulate the data according to the relationships we define 
# in our ERD. Learning the design of the database first will help us visualize what our relational databases look like, which 
# makes it much easier to choose the actual SQL syntax.

# *Why ERD at all?
# ERD is a process of designing your tables and establishing relationships between them, making your data relational. Almost all 
# imaginable data can be stored in a relational way, there really isn't anything you can't do using a relational database like 
# MySQL. Later, you will learn non-relational databases where everything is stored in a single table. There are advantages and 
# disadvantages for both, but we find that it is much easier to move from a relational database to a non-relational database.

# *What is MySQL Workbench?
# MySQL Workbench is a Graphical User Interface (GUI) for us to interact with MySQL, one of the most popular relational databases 
# in the world - through SQL commands. It is not necessary to use a GUI. We may interact with our MySQL databases through the 
# terminal, but the GUI makes it much easier to see our data and create new databases.

# *Why MySQL Workbench?
# We use MySQL Workbench when we are interacting with our databases because it will help us run some SQL queries. It also has a 
# great interface where we can map out our tables and establish relationships between them.

# *Saving Your ERD as a .mwb File
# You can save your ERD as a .mwb file. This will be useful later for sharing your project to have someone else run it locally, 
# as well as for submitting assignments. You will be required to submit a mwb file on the belt exam.

# To save, simply save as you would any other file, and just be sure to remember what you called it and where you stored it!

# *Conventions
# We will be following a set of conventions to create our database. We don't have to follow these conventions, but we recommend 
# our students to follow them for the following reasons:

# Developers can have a better understanding of your database if you are using a set of industry standards.
# Developers can create software to automate a lot of the queries if some assumptions can be made. In later chapters, you will 
# learn about Object Relational Mappers (ORM), which are programs that other developers use to make database queries easier by providing some handy functions. These functions will only work if we have followed conventions that ORM author expects, which are primarily based on set industry standards.

# *Guidelines
# Down the line, you may find yourself working with a company that has set up their database conventions a little bit differently, 
# but these are the guidelines that we feel are best for this course:

# 1) make the table name plural and ALL lowercase - make it plural (ex. users, leads, sites, clients, chapters, courses, modules)
# 2) use "id" as the primary key - name it id (also make it auto-incremented).
# 3) name foreign keys with the singular of your primary key’s table. (ex: user_id, lead_id, site_id, client_id). In workbench 
# you should always rename the foreign keys, as the default the Workbench gives will be plural, (ex. users_id)
# 4) use created_at and updated_at as columns for the timestamp in EVERY table you create.

# When we do things in ORM or in Ruby on Rails, it becomes extremely important that we follow these naming conventions.

# *Data Types
# The following are the data types that you will be using 95% of the time. Although there are quite a few other data types that you can use, focus on these for now.

# Simple Data Types:

# *VARCHAR(number of characters)
# Used to store strings of characters as non-numeric values that can be up to 255 characters. It is called a VARCHAR because it can store a variable number of characters and will only use the space required for each record that is stored in the database. VARCHAR should be used for values with different character lengths like an email, first_name, or last_name.
# *CHAR(number of characters)
# Also used to store characters as non-numeric values, however, it will use up all space for the set number of characters regardless of what value is added. For instance, if I set CHAR(15), and I try to store the value "Coding", it will use up the equivalent of 15 characters even though "Coding" is only 6 characters long. Char is good to use for things that will always be a given number of characters. Char would work well for something like a state_abbreviation.
# *INT
# Used to store integers.
# The columns that you will find mostly using the INT are things like a unique identifier for each table. The majority of rows in a table will not exceed 2.1 billion records. INT is good to use for most normal number values like a phone_number or a zip_code.
# unsigned (positive numbers only) - can store numerical values from 0 up to 4294967295
# signed (positive and negative numbers) - can store numerical values from -2147483648 up to 2147483647
# *BIGINT
# BIGINT would be used for columns that would need to store huge numbers. In most cases, you wouldn't need BIGINT, but if you wanted to store something like a Facebook id when using Facebook's API, since they have over a billion users the id will need to be a data type of BIGINT.
# unsigned (again positive numbers only) - can store numerical values from 0 up to 18446744073709551615
# signed (positive and negative numbers) - can store numerical values from 9223372036854775807 to -9223372036854775808.
# *TINYINT
# TINYINT would be good to use for numbers that will be relatively small. A good example of something that would use a TINYINT is user level identifier (0 - inactive user, 1 - active user, 9 - admin).
# unsigned - can store numerical values from 0 up to 255
# signed - can store numerical values from -128 up to 127
# *FLOAT
# Used to store floating point numbers (numbers that need to have decimal places). An example column for this would be like an item_cost.
# *TEXT
# Used to store a large amount of text, like a description, message, or comment. Use this for any text that VARCHAR() is too small to handle.
# *DATETIME
# Used for time-stamps, like created_at and updated_at, or to store a date and time in the format YYYY-MM-DD hh:mm:ss
# *DATE
# Used for storing general dates in the format YYYY-MM-DD, for example, a birthdate.

# *Main topics for database design
# There are many different terms and concepts that you will learn throughout this chapter, but they all point to a very simple 
# concept:  Do not repeat data. If you can remember this concept, the rest is to familiarize yourself with the terminology.

# *Database Relations
# One to one
# One to many
# Many to many
# Three (3) forms of normalization
# MySQL Workbench
# Type of data

# *What is the point?
# When we normalize our tables, we do not repeat data. This means that in the long term, we can use our storage space more 
# efficiently. 

# There is also another advantage that we obtain by normalizing our tables and establishing relationships between them. Later 
# we will learn that  identifiers  and  foreign keys  serve as the glue between our tables. With SQL, we can manipulate our tables and create the custom table we need for the job in question. 

# By dividing our data into different tables, we make each table good at one thing: store instances or rows of that data. In 
# addition, if we separate our tables, our database becomes more modular. This means that we can create our own custom tables 
# depending on the task in question using SQL. 

# We will learn this in the next chapter, but it is crucial to understand that we are using the strategy of normalizing our 
# tables and establishing relationships between them because we want to save storage space; and also because it makes our 
# database more modular so we can create more variety of custom tables using SQL.


# *One to One Relationship:
# Although each customer can only have one address, it would seem more fitting and better organized if we separate out the 
# address and put it in its own table. We can then keep better track of specific information about a given address without the 
# fear of our table getting too large to manage.

# Since each address that we have can only belong to a single customer and each customer can only have one address, we call 
# this a One to One Relationship.

# Note that the existence of a relationship can be optional, like having a customer record that has no related address record.

# *What Can We Do with SQL
# Even though we split up our tables into two different tables, we can combine them into one using SQL. No need to know how to do 
# this yet, but it is important to see how a table can be joined as long as there is a foreign key that references another 
# table's id. We'll cover actual SQL syntax in the next chapter.

# *Examples of One-to-One
# The easiest way to check to see if your relationship makes sense for your data is to simply talk through the relationship out 
# loud. Remember that relationships go in two directions. For example, one address has only one ZIP code, but one ZIP code can 
# have many addresses, thus making it a different type of relationship. Check out some of the sample One-to-One relationships 
# below:

# - Customers and Credit Cards - Every Customer has one Credit Card, every Credit Card belongs to one Customer.
# - User and Email - Every User has one Email Address, every Email Address has one User.
# - Product and Image - Every Product has an Image, every Image is of a Product.

# *One to Many and Many to One Relationships
# Continuing from our previous example of customers and addresses tables where one customer can only have one address...
# We now want our customers to be able to order items from us. To add our orders table, it will require us to define a 
# different relationship. Each customer is able to have multiple orders, but each order can only belong to one customer

# Since one customer can have many orders for any given user we call this a One to Many Relationship.

# *What Can We Do with SQL
# Notice how the foreign key  and the id  of the table that we want to combine act as the glue. We can join different tables 
# using SQL. Once again, we will learn how to do this later on but it is important to know that we are setting up these 
# relationships so that we can create customized tables like the illustration below by using SQL to join different tables on the 
# foreign key and the primary id.

# *Examples
# One-to-Many is probably the most common relationship you'll encounter while making web applications. Often times a One-to-One relationship is actually much more similar to a One-to-Many. Below are a few examples:

# Messages and Comments - One Comment belongs to one Message, but one Message can have many Comments.
# States and Cities - One City is only in one State, but one State can have many Cities.
# Customers and Orders - One Order only has one Customer, but one Customer can have many Orders.

# *Many to Many Relationships
# We have a table that keeps track of each of the orders the customer placed but we haven't created a way to keep track of the 
# items they are ordering.

# Here we created an items table to hold the name and description of each item that the customer can order.

# Since each order can have many different items and those same items can show up in many different orders, we have to use a 
# different type of relationship to connect orders to items. Orders can have many items and items can have many orders, so we 
# call this a Many to Many Relationship.

# In a Many to Many relationship, we create a connector table (also known as a joiner table) that has both the order_id and the 
# item_id so that we can determine all the items in a particular order.

# *Examples
# Many-to-Many is often the most confusing type of relationship for lots of people, but if you make sure to talk-out the 
# relationship out loud, you'll quickly find if it works or not. Remember, anytime you have a Many-to-Many, it will require 
# some sort of joining table! Check out the below examples and use how we describe the relationship as a guide:

# Users and Interests - One User can have many Interests, one Interest can be applied to many Users.
# Actors and Movies - One Movie can have many Actors, one Actor can be in many Movies.
# Businesses and Cities - One Business can be spread across many Cities, one City can be home to many Businesses.

# *What is Normalization?
# Database normalization is simply a convention for splitting large tables of data into smaller separate tables with the primary 
# goal being to not repeat data. Why is this so important? Let's say that you wear a watch so you can check the time, because 
# it's very important for you to know what the current time is. Would wearing eight watches make it easier? No way! Now we have 
# eight conflicting accounts of what the proper time is. Worse yet, if we ever want to update the time, we'd have to do it for 
# every watch independently. That's not very efficient!

# You can apply a similar concept to database design. If we want to store a user's email address, we'd want to store it in only 
# one place. Then, if we ever need to refer to it again, we'd simply use the id. The id will never change, so even if we update 
# the user's email address, none of the other connections we defined in our database will be damaged. Neat!

# Below are the three main rules of database normalization. You should use these as a guide for designing your ERDs. Always 
# remember, however, that they are common convention, and not absolute rules. It is possible to take normalization to an extreme. 
# For example, a simple address field. One state can have many cities, one city can have many streets, one street can have many 
# buildings, one building can have many apartments, one apartment can have many residents... and so on. Yikes, that can get 
# really crazy really quick! In the next sections, you'll learn more about why this type of complexity can be inefficient, 
# especially for simple assignments.

# *First Form
# Each Column in your table can only have 1 value.

# Ex. You should not have an address column in your table that lists the address, city, state, and zip, all separated by commas.

# *Second Form
# Each Column in your table that is not a key (primary or foreign) must have unique values.

# Ex. If you have a movies table with a categories column, you should not have a category listed more than once.

# *Third Form
# You cannot have a non-key column that is dependent on another non-key column.

# Ex. If you have a books table with columns publisher_name and publisher_address, the publisher_address and publisher_name 
# should be separated into a separate table and linked to books with a foreign key. The publisher_address is dependent on the 
# publisher_name and neither column is a key column.
