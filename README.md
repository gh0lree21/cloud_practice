# Overview

This is my first experience working with a cloud database by myself. I adapted a simple shopping cart program to store
the data entered in the cloud. It took me around 10 hours to integrate this component of the software, the longest part of which was 
spent finding the correct syntax to connect the database to my python file. The syntax is intuitive. I enjoyed getting familiar with this tool and look forward to using it in future software/applications. 

The program itself is built in Python and has a simple UI through the terminal. There is a menu where the user can select each action available for use in querying the database. Necessary instruction is given at each point for the user. There is some input validation used throughout to ensure more obvious problems don't arise. It connects to the cloud before an UI appears for the user and interacts with the cloud with each interaction. 

I've always thought that cloud databases are extremely fascinating and getting to use one was satisfying, even if it was just to scratch the surface. My purpose in creating this program was to give me a starting point so that I don't have to go through so much of the first few hours of the sometimes agonizing integration that comes with learning new software. Hopefully when I create a project in the future with a cloud database, I can look back to this repository and learn from my documenation and get into more complicated data storage. 

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](https://youtu.be/efH7XZg7Vy4)

# Cloud Database

Google Firestore through Firebase

Database consists of one table (collection). The program can add items (documents) with details (fields). 

# Development Environment

Python 3.10.1
Libraries: firebase_admin - firebase, credentials
Visual Studio Code

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python Website - Firebase Docs](https://pypi.org/project/firebase/)
* [Packages and Python Pip](https://packaging.python.org/en/latest/tutorials/installing-packages/)
* [Firebase Admin Set Up](https://firebase.google.com/docs/admin/setup#python)
* [Stackoverflow - Libraries](https://stackoverflow.com/questions/58354509/modulenotfounderror-no-module-named-python-jwt-raspberry-pi)
* [Firebase Python Tutorial](https://firebase.google.com/docs/firestore/quickstart#python)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* I would like to add another table to this cloud database - perhaps a 'Payments' collection where the user could query data about different payment options. 
* Would like to store more things than basic datatypes. 
* Give more options for querying the data which could include seperating each 'document' into a whole new collection based upon whether it is an edible, topical, garment, household item etc. 