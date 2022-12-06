# User Interface
# Import Module
import PySimpleGUI as sg

# Check out/ select theme
# sg.theme_previewer()
sg.theme('DarkTeal2')


# Holds the user interface
class UserInterface:
    
    # Initializes variables (might need to add other user inputs i.e. info in account creation menu. Thoughts?)
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Function Nick and Zach were messing with on 11/30 to display info
    def display(self):
        UserInterface(None, None).welcome()
        #return self.username, self.password

    # Function Nick and Zach were messing with on 11/30 to display info
    def s(self):
        print(self.username, self.password)
        
    # Login Window
    def welcome(self):
        login_layout = [
            [sg.Text('Welcome to Dart', size=(15, 1))],
            [sg.Text('Please enter your Username & Password')],
            [sg.Text('Username', size=(15, 1)), sg.InputText(key='username')],
            [sg.Text('Password', size=(15, 1)), sg.InputText()],
            [sg.Button('Login'), sg.Button('Create Account')]
        ]

        login_window = sg.Window('Login Screen', login_layout)
        # event, values = login_window.read()
        # UserInterface.username = values['username']

        while True:
            event, values = login_window.read()
            # Nick and Zach were messing with this on 11/30 to work on displaying info
            # I (Zach) think this if statement should set the self.username to the client's input after it's exception cheked. Then go to transaction menu
            if event == ('Login'):
                self.username = values['username']
                print('test', self.username)
                return UserInterface(self.username, None).s()

#                UserInterface(self.username, self.password).transaction()
            # Goes to account creation page
            if event == 'Create Account':
                UserInterface(self.username, self.password).account_creation()
    
    # Winow that pops up when "Create Account" is clicked
    def account_creation(self):
        account_creation_layout = [
            [sg.Text('Please enter your information')],
            [sg.Text('First Name', size=(15, 1)), sg.InputText(key='first_name')],
            [sg.Text('Last Name', size=(15, 1)), sg.InputText(key='last_name')],
            [sg.Text('Address', size=(15, 1)), sg.InputText(key='address')],
            [sg.Text('Tax Identifier', size=(15, 1)), sg.InputText(key='ssn')],
            [sg.Text('Phone Number', size=(15, 1)), sg.InputText(key='phone_number')],
            [sg.Text('Email', size=(15, 1)), sg.InputText(key='email')],
            [sg.Text('Username', size=(15, 1)), sg.InputText(key='username')],
            [sg.Text('Password', size=(15, 1)), sg.InputText(key='password')],
            [sg.Radio('Virtual', "CardType", default=True, size=(10, 1), k='-R1-'),
             sg.Radio('Physical', "CardType", default=True, size=(10, 1))],
            [sg.Button('Correct'), sg.Button('Incorrect')]
        ]

        account_creation_window = sg.Window('Account Creation', account_creation_layout)

        while True:
            event, values = account_creation_window.read()
            
            # Go to transaction page
            if event == ('Correct'):
                UserInterface(self.username, self.password).transaction()
            # Go back to account creation page
            if event == 'Incorrect':
                UserInterface(self.username, self.password).account_creation()

    # Winow to display transaction info
    def transaction(self):
        # self.amount = amount
        transaction_layout = [
            [sg.Text('Who would you like transact with?'), sg.Combo(values=('Liam', 'Zachary', 'Nicholas', 'Anna'))],
            [sg.Radio('Send', "TransactionType", default=True, size=(10, 1), k='-R1-'),
             sg.Radio('Request', "TransactionType", default=True, size=(10, 1))],
            [sg.Text('How Much', size=(15, 1)), sg.InputText(key='-INPUT-')],
            [sg.Radio('USD-CAD', "ExchangeType", default=True, size=(10, 1), k='-R1-'),
             sg.Radio('CAD-USD', "ExchangeType", default=True, size=(10, 1))],
            [sg.Button('Approve'), sg.Button('Cancel')]
        ]
        transaction_window = sg.Window('Transact', transaction_layout)

        while True:
            event, values = transaction_window.read()
            # amount = values['-INPUT-']
            # print(amount)
            # Breaks program
            if event == 'Cancel':
                break
            # Go to confirmation windo
            if event == 'Approve':
                UserInterface(self.username, self.password).confirmation()
    
    # Window to give transaction confirmation
    def confirmation(self):
        # super().__init__(amount)
        # current_balance = (starting_balance + self.amount)
        confirmation_layout = [
            [sg.Text('Congratulations, your transaction has been completed.')],
            [sg.Text('Orginal Balance:')],
            [sg.Text('Curent Balance:')],
            [sg.Button('Perform Another'), sg.Button('Exit')]
        ]
        confirmation_window = sg.Window('Transaction Detail', confirmation_layout)

        while True:
            event, values = confirmation_window.read()
            # Breaks program
            if event == 'Exit':
                break
            # Make another transaction
            if event == 'Perform Another':
                UserInterface(self.username, self.password).transaction()


# Execute
# Below code was used to test some above functions to return data
def run_interface():
    print(UserInterface(None, None).display())

run_interface()
# name = UserInterface.username