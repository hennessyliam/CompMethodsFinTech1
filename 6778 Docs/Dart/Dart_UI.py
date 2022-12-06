# User Interface
# Import Module
import sys
import PySimpleGUI as sg
from dart_backend import *


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
    #UsAccount: UsUserAccount

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
                login_window.hide()
                self.go_home()
                
            if event == 'Create Account':
                login_window.hide()
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
        [sg.Text('Card Type:'), sg.Radio('Virtual', "CardType", default=True, size=(10, 1), k='-R1-'),
            sg.Radio('Physical', "CardType", default=False, size=(10, 1))],
        [sg.Button('Create Account'), sg.Button('Back to Login')]
        ]

    account_creation_window = sg.Window('Account Creation', account_creation_layout)
    
    def create_account_US_user(self, values):
        self.first_name = values['first_name']
        self.last_name = values['last_name']
        self.address = values['address']
        self.ssn = values['tax_id']
        self.phone_number = values['phone_number']
        self.email = values['email']
        self.username = values['username']
        self.password = values['password']

        new_account = UsUserAccount(self.first_name, self.last_name, self.address, self.ssn, self.phone_number, self.email, self.username, self.password)
        print(new_account)
        sg.popup_auto_close('Account created succesfully!', auto_close_duration=1.5)
        self.go_home()
        

    def new_account_creation(self):

        window = self.account_creation_window

        while True:
            event, values = window.read() 
            if event ==  'Exit' or event == sg.WIN_CLOSED:
                break
            if event == 'Create Account':

                window.hide()
                self.create_account_US_user(values)
                
            if event == 'Back to Login':
                window.hide()
                self.go_to(000)

        window.close()

    def on_enter(self):
        self.new_account_creation()
                                       


class TransactionMenu(State):
     
    transaction_layout = [
        [sg.Text('Who would you like transact with?')], 
        [sg.Text("Recipient's First Name:", size=(20, 1)), sg.InputText(key='-RECIPIENT-FIRST-NAME-')],
        [sg.Text("Recipient's Last Name:", size=(20, 1)), sg.InputText(key='-RECIPIENT-LAST-NAME-')],
        [sg.Text("Recipient's Transfer Code:", size=(20, 1)), sg.InputText(key='-RECIPIENT-TRANSFER-CODE-')],
        [sg.Radio('Send', "TransactionType", default=True, size=(10, 1), key='-SEND-'),
        sg.Radio('Request', "TransactionType", default=False, size=(10, 1), key='-RECEIVE-')],
        [sg.Radio('Balance', 'Type', default=True, key='-BALANCE-'), sg.Radio('Card', 'Type', default=False, key='-CARD-'), sg.Radio('Crypto', 'Type', default=False, key='-CRYPTO-')],
        [sg.Text('How Much', size=(15, 1)), sg.InputText(key='-AMOUNT-')],
        [sg.Radio('USD-CAD', "ExchangeType", default=True, size=(12, 1), k='-USD-'),
        sg.Radio('CAD-USD', "ExchangeType", default=False, size=(12, 1), k='-CAD-')],
        [sg.Button('Approve'), sg.Button('Cancel')]
    ]

    transaction_window = sg.Window('Transact', transaction_layout)
    

    def transaction_screen(self):
        clear_inputs = ''

        window = self.transaction_window

        if window._Hidden == True:
            # clears inputs
            window['-RECIPIENT-FIRST-NAME-'].update(clear_inputs)
            window['-RECIPIENT-LAST-NAME-'].update(clear_inputs)
            window['-RECIPIENT-TRANSFER-CODE-'].update(clear_inputs)
            window['-AMOUNT-'].update(clear_inputs)
            window['-SEND-'].update(True)
            window['-BALANCE-'].update(True)
            window['-USD-'].update(True)

            window.un_hide()

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Approve':

                recipient_first_name = values['-RECIPIENT-FIRST-NAME-']
                recipient_last_name = values['-RECIPIENT-LAST-NAME-']
                recipient_transfer_code = values['-RECIPIENT-TRANSFER-CODE-']
                amount = values['-AMOUNT-']
                transaction_type = values['-SEND-']
                holder = 0
            
            
                UsUserAccount.send_funds(holder, recipient_first_name, recipient_last_name, recipient_transfer_code, amount, transaction_type)


                window.hide()
                self.go_to(3)
                break

            if event == 'Cancel':
                window.hide()
                self.go_home()

        #window.close()

    def on_enter(self):
        self.transaction_screen()


class TradeConfirmation(State):

    confirmation_layout = [
            # [sg.Text('Congratulations, your transaction has been completed.')],
            # [sg.Text('Original Balance:'), sg.Output(.balance)],
            # [sg.Text('Curent Balance:')],
            # [sg.Button('Perform Another'), sg.Button('Home')]
        ]
    confirmation_window = sg.Window('Transaction Detail', confirmation_layout)


    def confirmation_screen(self):

        window = self.confirmation_window

        if window._Hidden == True:
            window.refresh()
            window.un_hide()

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Perform Another':
                window.hide()
                self.go_to(2)
            if event == 'Home':
                window.hide()
                self.go_home()


    def on_enter(self):
        self.confirmation_screen()



class AccountDetails(State):

    def display_account_details(self, new_account):

        account_details_layout = [
            [sg.Text(f'Username: {self.new_account.username}')],
            [sg.Text(f'First name: {new_account.first_name}')],
            [sg.Text(f'Last name: {new_account.last_name}')],
            [sg.Text(f'Email: {new_account.email}')],
            [sg.Text(f'Address: {new_account.address}')],
            [sg.Text(f'Phone number: {new_account.phone_number}')],
            [sg.Button('Home')]
            ]


        window = sg.Window('Account Details', account_details_layout)
        
        if window._Hidden == True:
            window.un_hide()

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Home':
                window.hide()
                self.go_home()


    def on_enter(self):
        self.display_account_details(new_account=UsUserAccount)



class DepositFundScreen(State):

    deposit_fund_layout = [
        [sg.Text('Deposit Funds')],
        [sg.Text('Card Number:', size=(15, 1)), sg.InputText(key='-CARD#-')],
        [sg.Text('Expiration Date:', size=(15, 1)), sg.InputText(key='-EXP-')],
        [sg.Text('CVV:', size=(15, 1)), sg.InputText(key='-CVV-')],
        [sg.Radio('USD-CAD', "ExchangeType", default=True, size=(10, 1), k='-USD-'),
        sg.Radio('CAD-USD', "ExchangeType", default=False, size=(10, 1), k='-CAD-')],
        [sg.Button('Approve'), sg.Button('Cancel')]
    ]

    save_card_popup_layout = [
        [sg.Text('Would you like to save this card?')],
        [sg.Button('Yes'), sg.Button('No')]
    ]

    deposit_fund_window = sg.Window('Deposit Funds', deposit_fund_layout)

    save_card_popup_window = sg.Window('Save Card?', save_card_popup_layout)

    def deposit_fund_screen(self):

        window = self.deposit_fund_window

        if window._Hidden == True:
            window.un_hide()

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Approve':
                sg.popup_auto_close('Your deposit has been approved and is being received.', auto_close_duration=3)
                
                def save_card_popup():
                    while True:
                        event, values = self.save_card_popup_window.read()
                        if event == sg.WIN_CLOSED:
                            break
                        if event == 'Yes':
                            self.save_card_popup_window.close()
                            break
                        if event == 'No':
                            self.save_card_popup_window.close()
                            break

                save_card_popup()
                window.hide()
                self.go_home()
                break
            if event == 'Cancel':
                window.hide()
                self.go_home()

    def on_enter(self):
        self.deposit_fund_screen()


class LinkCryptoWallet(State):
    
        link_crypto_wallet_layout = [
            [sg.Text('Link Crypto Wallet')],
            [sg.Text('Wallet Address:', size=(15, 1)), sg.InputText(key='-WALLET-')],
            [sg.Text('Wallet Type:', size=(15, 1)), sg.InputText(key='-WALLET-TYPE-')],
            [sg.Button('Approve'), sg.Button('Cancel')]
        ]
    
        link_crypto_wallet_window = sg.Window('Link Crypto Wallet', link_crypto_wallet_layout)
    
        def link_crypto_wallet_screen(self):
    
            window = self.link_crypto_wallet_window
    
            if window._Hidden == True:
                window.un_hide()
    
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                if event == 'Approve':
                    sg.popup_auto_close('Your wallet has been linked.', auto_close_duration=2)
                    window.hide()
                    self.go_home()

                if event == 'Cancel':
                    window.hide()
                    self.go_home()
    
        def on_enter(self):
            self.link_crypto_wallet_screen()
        


class Home(State):

    home_layout = [
        # Text Welcome to Dart in large font
        [sg.Text('Welcome to Dart', font=('Helvetica, 25'))],
        [sg.Button('Transact', font=('Helvetica, 15')), sg.Button('Account Details', font=('Helvetica, 15'))],
        [sg.Button('Deposit Funds', font=('Helvetica, 15')), sg.Button('Link Crypto Wallet', font=('Helvetica, 15'))],
        [sg.Button('Logout', font=('Helvetica, 15'))],
        [sg.Text('Available FX Rate:')], 
        [sg.Text('1.00 USD = 1.33 CAD')]
        
    ]
        
    home_window = sg.Window('Home Screen', home_layout)

    def on_enter(self):

        if self.home_window._Hidden == True:
            self.home_window.refresh()
            self.home_window.un_hide()
        
        while True:
            event, values = self.home_window.read()
            if event == sg.WIN_CLOSED:
                sys.exit()
            if event == 'Transact':
                self.home_window.hide()
                self.go_to(2)
            if event == 'Account Details':
                self.home_window.hide()
                self.go_to(4)
            if event == 'Logout':
                self.home_window.hide()
                self.go_to(5)
            if event == 'Deposit Funds':
                self.home_window.hide()
                self.go_to(6)
            if event == 'Link Crypto Wallet':
                self.home_window.hide()
                self.go_to(7)
                

class Exit(State):

    exit_layout = [
        [sg.Text('Thank you for using Dart')],
        [sg.Text('Logging out...')],
    ]

    exit_window = sg.Window('Logging Out', exit_layout, size=(250, 100))


    def on_enter(self):


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
        6: DepositFundScreen,
        7: LinkCryptoWallet,
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
        self.set_state(000)


app = App()
window.close()
