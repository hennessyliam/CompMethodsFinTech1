# User Interface
# Import Module
import sys
import PySimpleGUI as sg


# Check out/ select theme
#sg.theme_previewer()
sg.theme('DarkBlue15')

class Account:
    def __init__(self, username, password, first_name, last_name, address, tax_id, phone_number, email, balance, card_type = 'Virtual'):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.tax_id = tax_id
        self.phone_number = phone_number
        self.email = email
        self.card_type = card_type
        self.balance = balance

        self.username_list = ['liamh', 'zachr', 'nicks', 'annaz']
        self.password_list = ['1234', '4567', '7890']


    def display_info(self):
        print(self.username)
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.address)
        print(self.phone_number)
        print(self.card_type)


class State:
    account: Account


    def __init__(self, go_to, set_account, go_home) -> None:
        self.go_to = go_to
        self.set_account = set_account
        self.go_home = go_home
        self.on_enter()

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def go_home(self):
        pass

    def go_to(self, state: int):
        pass

    def set_account(self, account: str):
        pass

    def display_info(self):
        pass


class LoginWindow(State):

 # Login Window
    def welcome_window(self):
        login_layout = [
            [sg.Text('Welcome to Dart', size=(15, 1))],
            [sg.Text('Please enter your Username & Password')],
            [sg.Text('Username', size=(15, 1)), sg.InputText(key='username')],
            [sg.Text('Password', size=(15, 1)), sg.InputText()],
            [sg.Button('Login'), sg.Button('Create Account')]
        ]

        login_window = sg.Window('Login Screen', login_layout)
        

        while True:
            event, values = login_window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Login':
                login_window.close()
                self.go_home()
            if event == 'Create Account':
                login_window.close()
                self.go_to(1)

    def on_enter(self):
         self.welcome_window()
         

class AccountCreation(State):
   
    account_creation_layout = [
        [sg.Text('Please enter your information')],
        [sg.Text('First Name', size=(15, 1)), sg.InputText(key='first_name')],
        [sg.Text('Last Name', size=(15, 1)), sg.InputText(key='last_name')],
        [sg.Text('Address', size=(15, 1)), sg.InputText(key='address')],
        [sg.Text('Tax Identifier', size=(15, 1)), sg.InputText(key='tax_id')],
        [sg.Text('Phone Number', size=(15, 1)), sg.InputText(key='phone_number')],
        [sg.Text('Email', size=(15, 1)), sg.InputText(key='email')],
        [sg.Text('Username', size=(15, 1)), sg.InputText(key='username')],
        [sg.Text('Password', size=(15, 1)), sg.InputText(key='password')],
        [sg.Radio('Virtual', "CardType", default=True, size=(10, 1), k='-R1-'),
            sg.Radio('Physical', "CardType", default=True, size=(10, 1))],
        [sg.Button('Submit')]
        ]

    account_creation_window = sg.Window('Account Creation', account_creation_layout)
    
    
    def new_account_creation(self):

        window = self.account_creation_window
        
        while True:
            event, values = window.read() 
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                new_account = Account(
                    username=values['username'],
                    password=values['password'],
                    first_name=values['first_name'],
                    last_name=values['last_name'],
                    address=values['address'],
                    tax_id=values['tax_id'],
                    phone_number=values['phone_number'],
                    email=values['email'],
                    balance=0,
                    card_type=values['-R1-']
                )

                window.close()
                self.go_home()
                return new_account
        window.close()
        


    def on_enter(self):

        new_account = self.new_account_creation()
        self.set_account(new_account)


class TransactionMenu(State):
     
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

    def transaction_screen(self):

        window = self.transaction_window

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Approve':
                window.close()
                self.go_to(3)
                break
            if event == 'Cancel':
                self.go_home()
                window.close()

        #window.close()

    def on_enter(self):
        self.transaction_screen()


        

class TradeConfirmation(State):
    confirmation_layout = [
            [sg.Text('Congratulations, your transaction has been completed.')],
            [sg.Text('Orginal Balance:')],
            [sg.Text('Curent Balance:')],
            [sg.Button('Perform Another'), sg.Button('Home')]
        ]
    confirmation_window = sg.Window('Transaction Detail', confirmation_layout)

    def confirmation_screen(self):
        window = self.confirmation_window
        

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Perform Another':
                window.close()
                self.go_to(2)
            if event == 'Home':
                self.go_home()
                window.close()


    def on_enter(self):
        self.confirmation_screen()



class AccountDetails(State):
    

    account_details_layout = [
        [sg.Text('Account Details')],
        [sg.Text(str("self.account.display_info()"))],
        [sg.Button('Home')]
        ]

    account_details_window = sg.Window('Account Details', account_details_layout)

    
    def account_details_screen(self):
        window = self.account_details_window

        # show account details and when home button is pressed go to home screen
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Home':
                window.close()
                self.go_home()


    def on_enter(self):
        self.account_details_screen()
        


class Home(State):

    home_layout = [
        [sg.Text('Welcome to Dart')],
        [sg.Button('Transact'), sg.Button('Account Details'), sg.Button('Logout')],
        [sg.Text('Available FX Rate:')], 
        [sg.Text('1.00 USD = 1.25 CAD')]
        
    ]
        
    home_window = sg.Window('Home Screen', home_layout)

    def on_enter(self):
        
        while True:
            event, values = self.home_window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Transact':
                self.home_window.close()
                self.go_to(2)
            if event == 'Account Details':
                self.home_window.close()
                self.go_to(4)
            if event == 'Logout':
                self.home_window.close()
                self.go_to(5)
                

class Exit(State):

    exit_layout = [
        [sg.Text('Thank you for using Dart')],
        [sg.Text('Logging out...')],
    ]

    exit_window = sg.Window('Logging Out', exit_layout, size=(250, 100))


    def on_enter(self):
        # open window then close it after two seconds

        window = self.exit_window

        while True:
            event, values = window.read(timeout=1000)
            if event == sg.WIN_CLOSED:
                break
            else:
                window.close()
                sys.exit(0)




class App:
    states = {
        000: LoginWindow, 
        1: AccountCreation,
        2: TransactionMenu,
        3: TradeConfirmation,
        4: AccountDetails,
        5: Exit,
        99: Home
    }

    state: State = None # type: ignore
    account = None

    def go_home(self):
        self.set_state(99)

    def run_state(self, state):
        state(self.set_state, self.set_account, self.go_home)

    def set_state(self, state: int):
        if self.state:
            self.state.on_exit(self) # type: ignore

        self.state = self.states[state]
        self.run_state(self.state)

    def set_account(self, account: Account):
        self.account = account

    def __init__(self) -> None:
        self.set_state(2)


app = App()

