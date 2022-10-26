# Overview

I created a banking system with a user interface in the Python console. The program asks for inputs of options, and will repeat until the option 'Quit Program' is selected. There are various actions such as add client, delete client, withdraw, deposit, and display all clients. It is integrated in a Google Firebase Cloud Database.

My purpose for creating this program is to work with different types of databases. I have only worked with relational databases, so this was a nice introduction to cloud databases.

[Software Demo Video](https://youtu.be/IN0zvbSXPuM)

# Cloud Database

I am using Google's Firebase cloud database. 

The collection I am using is called 'client' and it holds various documents of customers that have fields of 'fname', 'lname', and 'balance'.

# Development Environment

I am using VS Code for my code editor, and the Google Firebase Console to see the structure and any changes to my cloud database.

I used Python in conjunction with the firebase-admin library.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Google Firebase](https://firebase.google.com/docs/firestore/query-data/get-data)
* [Firebase Console](https://console.firebase.google.com/)

# Future Work

* Adding more collections (tables) and more documents could be on my docket to improve this system.
* I could also add more fields to the documents in my client collection.
* More functionality with my program could be nice, as well as creating an actual web user interface, instead of just the Python console.