from re import U
from tkinter import E
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Using service account
cred = credentials.Certificate('fir-bankproj-df30f12b62fd.json')

app = firebase_admin.initialize_app(cred)
db = firestore.client()

# CREATE USER MENU

choice = -1
while (choice != 0):
    print("Welcome to Python Bank!")
    print("0. Quit Program")
    print("1. Add customer")
    print("2. Delete customer")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Display customers")
    choice = int(input("Enter your choice: "))
    print()

    if (choice == 1):
        # ADD CLIENT
        # get user input
        fname = str(input("First Name: "))
        lname = str(input("Last Name: "))
        bal = float(input("Current Balance: "))
        print()

        # get first initial
        finitial = fname[0]
        docName = f'{finitial}{lname}'

        # Add inputs into a new document
        doc_ref = db.collection(u'client').document(docName)
        doc_ref.set({
            u'fname': fname,
            u'lname': lname,
            u'balance': bal
        })
    if (choice == 2):
        # DELETE
        # get desired document name (finitial and last name)
        finitial = str(input("Enter first initial of account to delete: "))
        lname = str(input("Enter last name of account to delete: "))

        # Ask if they're sure the record is correct
        check = str(input(f'Are you sure you want to delete {finitial}{lname}? (Y/N) '))
        if (check == 'Y'):
            db.collection(u'client').document(f'{finitial}{lname}').delete()
        else:
            choice = 0
    if (choice == 3):
        # DEPOSIT

        # Ask user for how much to deposit/who to deposit to
        finitial = str(input("Enter the first initial of account holder: "))
        lname = str(input("Enter last name of account holder: "))
        dep = int(input("Deposit amount: "))
        
        doc_ref = db.collection(u'client').document(f'{finitial}{lname}')
        doc = doc_ref.get()
        docdict = doc.to_dict()
        bal = docdict["balance"]

        bal = bal + dep
        doc_ref.update({u'balance': bal})
        print()

    if (choice == 4):
        # WITHDRAW
        
        # Ask user for how much to withdraw/who to withdraw from
        finitial = str(input("Enter the first initial of account holder: "))
        lname = str(input("Enter last name of account holder: "))
        withdraw = int(input("Withdrawal amount: "))
        
        doc_ref = db.collection(u'client').document(f'{finitial}{lname}')
        doc = doc_ref.get()
        docdict = doc.to_dict()
        bal = docdict["balance"]

        bal = bal - withdraw
        doc_ref.update({u'balance': bal})
        print()

    if (choice == 5):
        # DISPLAY
        client_ref = db.collection(u'client')
        docs = client_ref.stream()

        for doc in docs:
            docdict = doc.to_dict()
            print(f'Name: {docdict["fname"]} {docdict["lname"]}  Balance: ${docdict["balance"]}')
            print()
        




# TESTS ####################################################
# doc_ref = db.collection(u'client').document(u'gnielson')
# doc_ref.set({
#     u'fname': u'Garrett',
#     u'lname': u'Nielson',
#     u'balance' : 350
# })

# users_ref = db.collection(u'client')
# docs = users_ref.stream()

# for doc in docs:
#     docdict = doc.to_dict()
#     print(f'Name: {docdict["fname"]} {docdict["lname"]}  Balance: ${docdict["balance"]}')