# File containing the US subsidiary
# crypto called dartc (Zach's suggestion)
# When integrating with the user interface, I tried to put things in triple quotes where I know things will need to be
# plugged in. There are single quotes around sections where variables will be set to something from the user interface

#from DART_Holding_co import *
# from US_user_interface import
import string
import random
import datetime
import PySimpleGUI as sg


# Used to aggregate all US customers and interact with holding company
class UsSubsidiary:

    def __init__(self):
        self.list_pri_acct_num = []
        self.list_transfer_code = []
        self.list_card_number = []
        self.list_of_US_clients = []
        self.subsidiary_balance = 1000000

    # Used to verify a counter-party exists in main database
    def verify_cust_info(self, initiator_input):
        return DartHoldingCo().verify_account(initiator_input)

    # amount of transaction and whether it's sent from balance, card, or crypto
    # will implement 12/3/22
    def record_send_funds(self, initiator_input, amount, transaction_type):
        pass

    # Used to request funds from someone
    def record_receive_funds(self, initiator_input, amount):
        # Returns True or False depending on if the counter-party accepts the request
        confirmation = DartHoldingCo().receive_funds(initiator_input, amount)
        if confirmation is True:
            self.subsidiary_balance -= amount
            return confirmation
        else:
            return confirmation

    # Used to send a confirmation to the user to accept a request of funds
    # Function can most likely be improved if time allows
    def send_confirmation(self, details):
        temp = details[0][2]
        # check list of transfer codes for the one being sent
        for number in self.list_of_US_clients:
            # if found set transfer code to the dict {ssn: transfer_code}. Should be found since Holding co has a
            # comprehensive list
            if temp == list(number.values())[0][7]:
                temp = number
        ssn = list(temp.keys())[0]
        first_name = list(temp.values())[0][0][0]
        last_name = list(temp.values())[0][0][1]
        username= list(temp.values())[0][1][0]
        password = list(temp.values())[0][1][1]
        address =list(temp.values())[0][3]
        phone = list(temp.values())[0][4]
        email= list(temp.values())[0][5]
        UsUserAccount(first_name, last_name, address, ssn, phone, email, username, password).recreate_user_profile(temp)

    # used to receive aggregated details from user
    def user_details(self, details):
        # Separates items and adds them to their respective lists
        pri_acct_number = list(details.values())[0][6]
        transfer_code = list(details.values())[0][7]
        card_number = list(details.values())[0][8]
        ssn = str(list(details.keys())[0])
        self.list_pri_acct_num.append({ssn: pri_acct_number})
        self.list_transfer_code.append({ssn: transfer_code})
        self.list_card_number.append({ssn: card_number})
        self.list_of_US_clients.append(details)


# Used to interact with an individual user
class UsUserAccount:
    def __init__(self, first_name, last_name, address, ssn, phone_number, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.ssn = ssn
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password
        self.user_balance = 0
        self.external_card_info = None
        self.crypto_wallet = None
        # Returns a string of 3 randomly selected letters + 7 randomly selected numbers
        self.private_acct_num = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=3)
                                        + random.choices(string.digits, weights=None, cum_weights=None, k=7))
        # Returns a string of 4 randomly selected letters + 4 randomly selected numbers
        self.transfer_code = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=4)
                                     + random.choices(string.digits, weights=None, cum_weights=None, k=4))
        # Finds future date that the card will expire
        x = str(datetime.datetime.now() + datetime.timedelta(days=1460))
        # Returns a string with 16 random digits for the acct. number, the month-year for expiration,
        # And 3 random digits for a CVV code
        self.dart_card_number = {
            self.ssn: [''.join(random.choices(string.digits, weights=None, cum_weights=None, k=16)), x[0:7],
                       ''.join(random.choices(string.digits, weights=None, cum_weights=None, k=3))]}
        # Puts all the client data into a dictionary to be accessed by subsidiary database and holding co.
        self.client_details = {self.ssn: [[self.first_name, self.last_name], [self.username, self.password],
                                          [self.external_card_info, self.crypto_wallet], self.address,
                                          self.phone_number, self.email, self.private_acct_num, self.transfer_code,
                                          self.dart_card_number, self.user_balance]}

    # Function to pass aggregated details to US Subsidiary
    """call this function after the client confirms all their information. This returns nothing to the user interface"""
    def account_details(self):
        UsSubsidiary().user_details(self.client_details)
        pass

    # Used to re populate user back-end from US subsidiary database
    def recreate_user_profile(self, details):
        self.ssn = list(details.keys())[0]
        self.first_name = list(details.values())[0][0][0]
        self.last_name = list(details.values())[0][0][1]
        self.username = list(details.values())[0][1][0]
        self.password = list(details.values())[0][1][1]
        self.external_card_info = list(details.values())[0][2][0]
        self.crypto_wallet = list(details.values())[0][2][1]
        self.address = list(details.values())[0][3]
        self.phone_number = list(details.values())[0][4]
        self.email = list(details.values())[0][5]
        self.private_acct_num = list(details.values())[0][6]
        self.transfer_code = list(details.values())[0][7]
        self.dart_card_number = list(details.values())[0][8]
        self.user_balance = list(details.values())[0][9]

    # from credit/debit card
    # Using a dummy card as actual ones                                                                 still need to determine fee structure ASAP!!!!!!!!!!!!!!
    # deposit amount should be int while the rest are strings
    # answer should be 'y' or 'n'
    def deposit_funds(self, deposit_amount):
        # check if any payment info is linked
        if self.external_card_info is None:
            """Get card_number, expiration, cvv. Confirm details are correct. Ask if client wants to save card.
                return card_number,expiration, cvv, and answer here"""
            card_number = 'output from ui here'
            expiration = 'output from ui here'
            cvv = 'output from ui here'
            answer = 'output from ui here'
            if answer == 'y':
                UsUserAccount.link_external_card(self, card_number, expiration, cvv)
                self.user_balance += deposit_amount
            else:
                self.user_balance += deposit_amount
        else:
            self.user_balance += deposit_amount

    # Function to link card. Get info with UI and exception check it. Pass info along as strings
    def link_external_card(self, card_number, expiration, cvv):
        external_card_info = {self.ssn: [card_number, expiration, cvv]}
        """show confirmation page. return answer as 'y' or 'n'"""
        answer = 'output from ui here'
        if answer == 'y':
            self.external_card_info = external_card_info
            return self.external_card_info
        else:
            """Return this to the client and return to the home page"""
            return 'A '

    # Function to link crypto wallet. recovery phrase is a list of 12 entered by the user already exception checked (that check still needs implementing)
    # Get the above with the UI
    def link_crypto_wallet(self, recovery_phrase):
        """Show confirmation page. Return answer as 'y' or 'n'"""
        answer = 'output from ui here'
        if answer == 'y':
            self.crypto_wallet = {self.ssn: recovery_phrase}
            return self.crypto_wallet
        else:
            """Return this and direct them back to the home page"""
            return 'A valid crypto wallet must be linked to facilitate transfers this way.'

    # wallet is a variable equal to a dictionary where the key is the SSN.
    # values are a list first value is a list of the recovery phrase
    # second value is another dictionary where the assets in the wallet are the keys with the currency amount as the values
    # i.e.{ssn: [[recovery_phrase], {'BTC': 2, 'ETH': 10, 'DARTC': 500}]}
    def check_crypto_balance(self, wallet):
        assets = list(wallet.values())[0][1]
        for key, amount in assets.items():
            if 'DARTC' == key:
                return amount

    # Used to send funds to receiver
    # recipient_first_name, recipient_last_name, recipient_transfer_code should be strings while amount is int
    # transaction_type should be 'balance' 'card' or 'crypto'
    # UI should already confirm the info is correct
    def send_funds(self, recipient_first_name, recipient_last_name, recipient_transfer_code, amount, transaction_type):
        initiator_input = [recipient_first_name, recipient_last_name, recipient_transfer_code]
        # Verify the counter-party exists
        if UsSubsidiary().verify_cust_info(initiator_input) is True:
            # If balance is chosen
            if transaction_type == 'balance':
                # Makes sure user has enough funds
                if amount <= self.user_balance:
                    self.user_balance -= amount
                    UsSubsidiary().record_send_funds(initiator_input, amount, transaction_type)
                else:
                    sg.popup(f'You currently have ${self.user_balance} in your account.\nTo facilitate your transfer '
                            f'of ${amount}, please deposit ${amount - self.user_balance} more to your account.')


            # If card is chosen
            elif transaction_type == 'card':
                # make sure a card is on file
                if self.external_card_info is not None:
                    UsSubsidiary().record_send_funds(initiator_input, amount, transaction_type)
                else:
                    """Ask client to put in card info and if they want to save the card on file. return answer as 'y' or 'n'"""
                    card_number = 'insert ui here'
                    expiration = 'insert ui here'
                    cvv = 'insert ui here'
                    answer = 'insert ui here'
                    if answer == 'y':
                        UsUserAccount(self.first_name, self.last_name, self.address, self.ssn, self.phone_number,
                                      self.email, self.username, self.password).link_external_card(card_number,
                                                                                                   expiration, cvv)
                        UsSubsidiary().record_send_funds(initiator_input, amount, transaction_type)
                    else:
                        UsSubsidiary().record_send_funds(initiator_input, amount, transaction_type)
            # If crypto is chosen
            else:
                # Make sure a wallet has been linked
                if self.crypto_wallet is not None:
                    dartc_quantity = UsUserAccount(self.first_name, self.last_name, self.address, self.ssn, self.phone_number,
                                      self.email, self.username, self.password).check_crypto_balance(self.crypto_wallet)
                    # make sure there's enough to cover the transfer
                    if amount <= dartc_quantity:
                        asset = list(self.crypto_wallet.values())[0][1].get('DARTC')
                        asset -= amount
                        UsSubsidiary().record_send_funds(initiator_input, amount, transaction_type)
                    # Not enough DARTC to cover the transfer
                    else:
                        """Direct client back to the transfer page."""
                        return 'There are not enough DARTC tokens in your wallet to cover the transfer. Please visit an' \
                               'exchange to purchase more tokens or you can try transferring via another method.'
                # Client must link their crypto wallet to make a transfer using DARTC
                else:
                    """Return client to the page to link their crypto wallet before trying to complete a transfer"""
                    return 'You must link your crypto wallet and have enough DARTC tokens to place a transfer by this method.'
        # If counter-party does not exist
        else:
            """return this to user and direct them back to the transaction page"""
            return 'There is no one in our system with that name and account code. Please check your information ' \
                   'and try again.'

    
    # Used to request funds from someone. Initiated on receiver's side
    # sender_first_name, sender_last_name, sender_transfer_code should be strings while amount should be type int
    def receive_funds(self, sender_first_name, sender_last_name, sender_transfer_code, amount):
        initiator_input = [sender_first_name, sender_last_name, sender_transfer_code]
        # Verify counter-party exists
        if UsSubsidiary().verify_cust_info(initiator_input) is True:
            # Returns True or False depending on if the counter-party accepts the request
            confirmation = UsSubsidiary().record_receive_funds(initiator_input, amount)
            if confirmation is True:
                self.user_balance += amount
            else:
                """ Return this to user and direct back to home page"""
                return 'The person you requested the funds from has denied your request.'
        # If counter-party doesn't exist
        else:
            """Return this to user and direct back to home page"""
            return ('There is no one in our system with that name and transfer code. Please check your information'
                    'and try again.')

    # function called when the other party requests funds from this user
    # Answer should be a string of either 'y' or 'n'
    """pop-up/page necessary to show incoming request details and ask client to confirm/deny"""
    def confirmation_request_for_funds(self, details):
        answer = 'insert ui here'
        first_name = details[0][0]
        last_name = details[0][1]
        transfer_code = details[0][2]
        amount = details[1]
        # client rejects
        if answer == 'n':
            return False
        # Client accepts
        else:
            # default is balance on DART card. Return true if accepted and there's enough in Dart acct to cover it
            if amount <= self.user_balance:
                self.user_balance -= amount
                UsUserAccount(self.first_name, self.last_name, self.address, self.ssn, self.phone_number,
                              self.email, self.username, self.password).send_funds(first_name, last_name,
                                                                                   transfer_code, amount, 'balance')
                """Return below and take customer back to home page"""
                return 'Funds sent successfully!'
            # Not enough in user's acct
            else:
                """ask user if they want to send it via external debit card or crypto and return answer as 
                'card' or 'crypto'"""
                answer = 'insert ui here'
                UsUserAccount(self.first_name, self.last_name, self.address, self.ssn, self.phone_number,
                              self.email, self.username, self.password).send_funds(first_name, last_name,
                                                                                   transfer_code, amount, answer)
                """Return below and take customer back to home page"""
                return 'Funds sent successfully!'

    # Used to return aggregated details to user_interface
    def show_user_details(self):
        return self.client_details




class ExceptionCheck:
    def __init__(self, first_name, last_name, address, ssn, phone_number, email, username, password,
                 card_number, expiration, cvv, deposit_amount, yn, recovery_phrase):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.ssn = ssn
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password
        self.card_number = card_number
        self.expiration = expiration
        self.cvv = cvv
        self.deposit_amount = deposit_amount
        self.yn = yn
        self.recovery = recovery_phrase

    def check_first_name(self):
        self.first_name = (self.first_name.replace(" ", "")).upper()
        forbidden_characters = string.punctuation + string.digits + '\t' + '\n' + '\v' + '\f' + '\r' + '\x0b' + '\x0c'
        if self.first_name.isspace() is False:

            while len(self.first_name) < 2:
                self.first_name = input("Please enter your full name: ")

            while len(self.first_name) > 30:
                self.first_name = input("You have reached the character limit. \nPlease enter a name with 30"
                                        "or less characters: ")

            for letter in self.first_name:
                if letter in forbidden_characters:
                    self.first_name = input("Please only enter characters from the English alphabet: ")
                    return ExceptionCheck(self.first_name, None, None, None, None, None, None, None, None,
                                          None, None, None, None, None).check_first_name()

            if self.first_name.isspace() is True:
                self.first_name = input('Please enter your full name: ')
                return ExceptionCheck(self.first_name, None, None, None, None, None, None, None,
                                      None, None, None, None, None, None).check_first_name()
        else:
            self.first_name = input("Please enter your full name: ")
            return ExceptionCheck(self.first_name, None, None, None, None, None, None, None, None,
                                  None, None, None, None, None).check_first_name()
        return self.first_name

    def check_last_name(self):
        self.last_name = (self.last_name.replace(" ", "")).upper()
        forbidden_characters = string.punctuation + string.digits + '\t' + '\n' + '\v' + '\f' + '\r' + '\x0b' + '\x0c'
        if self.last_name.isspace() is False:

            while len(self.last_name) < 2:
                self.last_name = input("Please enter your full name: ")

            while len(self.last_name) > 30:
                self.last_name = input("You have reached the character limit. \nPlease enter a name with 30"
                                       "or less characters: ")

            for letter in self.last_name:
                if letter in forbidden_characters:
                    self.last_name = input("Please only enter characters from the English alphabet: ")
                    return ExceptionCheck(self.last_name, None, None, None, None, None, None, None, None, None,
                                          None, None, None, None).check_last_name()

            if self.last_name.isspace() is True:
                self.last_name = input('Please enter your full name: ')
                return ExceptionCheck(self.last_name, None, None, None, None, None, None, None, None, None,
                                      None, None, None, None).check_last_name()
        else:
            self.last_name = input("Please enter your full name: ")
            return ExceptionCheck(self.last_name, None, None, None, None, None, None, None, None, None,
                                  None, None, None, None).check_last_name()
        return self.last_name

    def check_address(self):
        forbidden_characters = '\t' + '\n' + '\v' + '\f' + '\r' + """!"#$%&'()*+,-./:;?@[\]^_`{|}~"""
        if len(self.address) > 115:
            self.address = input('You have exceeded the character limit. Please re-enter your address: ')
            return ExceptionCheck(None, None, self.address, None, None, None, None, None, None, None,
                                  None, None, None, None).check_address()
        else:
            for character in self.address:
                if character in forbidden_characters:
                    self.address = input('Please enter your address without using any special characters: ')
                    return ExceptionCheck(None, None, self.address, None, None, None, None, None, None,
                                          None, None, None, None, None).check_address()
            return self.address

    def check_ssn(self):
        self.ssn = self.ssn.replace(" ", "")
        forbidden_characters = string.ascii_letters + string.whitespace + string.punctuation
        if len(self.ssn) != 9:
            self.ssn = input('Please enter your Social Security Number or Tax Identification Number without any'
                             ' letters, spaces, or special characters: ')
            return ExceptionCheck(None, None, None, self.ssn, None, None, None, None, None, None,
                                  None, None, None, None).check_ssn()
        else:
            for number in self.ssn:
                if number in forbidden_characters:
                    self.ssn = input('Please enter your Social Security Number or Tax Identification Number without any'
                                     ' letters, spaces, or special characters: ')
                    return ExceptionCheck(None, None, None, self.ssn, None, None, None, None, None, None,
                                          None, None, None, None).check_ssn()
            return self.ssn

    def check_phone_number(self):
        self.phone_number = self.phone_number.repalce(" ", "")
        forbidden_characters = string.ascii_letters + string.whitespace + string.punctuation
        if len(self.phone_number) != 10:
            self.phone_number = input('Please enter a U.S. phone number without any letters, spaces, or '
                                      'special characters: ')
            return ExceptionCheck(None, None, None, None, self.phone_number, None, None, None, None, None,
                                  None, None, None, None).check_phone_number()
        else:
            for number in self.phone_number:
                if number in forbidden_characters:
                    self.phone_number = input('Please enter a U.S. phone number without any letters, spaces, or '
                                              'special characters: ')
                    return ExceptionCheck(None, None, None, None, self.phone_number, None, None, None, None, None,
                                          None, None, None, None).check_phone_number()
            return self.phone_number

    # Rudimentary email check. Does not look for every syntax rule, but should be good enough for the project
    def check_email(self):
        self.email = self.email.replace(" ", "")
        forbidden_characters = string.whitespace + '"(),:;[\]'
        # Max email length
        if len(self.email) > 320:
            self.email = input('You have exceeded the character limit. Please enter an email that is 320 characters'
                               ' or less: ')
            return ExceptionCheck(None, None, None, None, None, self.email, None, None, None, None,
                                  None, None, None, None).check_email()
        else:
            for character in self.email:
                if character in forbidden_characters:
                    self.email = input('Please enter a valid email address: ')
                    return ExceptionCheck(None, None, None, None, None, self.email, None, None, None, None,
                                          None, None, None, None).check_email()
            return self.email

            # check to see if the created username is already in use

    def check_username(self):
        self.username = self.username.lower()
        forbidden_characters = string.whitespace + string.punctuation
        if 5 < len(self.username) < 21:
            self.username = input('Please enter a username that is at least 6 charters long and no more'
                                  ' than 20 characters long: ')
            return ExceptionCheck(None, None, None, None, None, None, self.username, None, None, None,
                                  None, None, None, None).check_username()
        else:
            for character in self.username:
                if character in forbidden_characters:
                    self.username = input('Please enter a username using only letters or numbers: ')
                    return ExceptionCheck(None, None, None, None, None, None, self.username, None, None, None,
                                          None, None, None, None).check_username()
            return self.username

    def check_password(self):
        password_list = []
        counter = 0
        forbidden_characters = string.whitespace + """"&'()*+,-./:;?[\]^_`{|}~"""
        if len(self.password) < 7 or len(self.password) > 25:
            self.password = input('Please enter a password that is at least 8 characters long and no more '
                                  'than 24 characters long: ')
            return ExceptionCheck(None, None, None, None, None, None, None, self.password, None, None,
                                  None, None, None, None).check_password()
        else:
            for character in self.password:
                password_list.append(character)
                if character in forbidden_characters:
                    self.password = input('Passwords can only contain letters, numbers, or the following'
                                          ' special characters: !, @, #, $, %. Please re-enter your password: ')
                    return ExceptionCheck(None, None, None, None, None, None, None, self.password, None, None,
                                          None, None, None, None).check_password()
                # Makes sure there are three repeated characters in a row
                if len(password_list) >= 3:
                    if password_list[counter + 2] is not None:
                        if password_list[counter] == password_list[counter + 1] == password_list[counter + 2]:
                            self.password = input('Please do not enter the same three characters in a row. '
                                                  'Please enter your password: ')
                            return ExceptionCheck(None, None, None, None, None, None, None, self.password, None, None,
                                                  None, None, None, None).check_password()
                        counter += 1
            return self.password

    def check_card_number(self):
        self.card_number = self.card_number.replace(" ", "")
        forbidden_characters = string.ascii_letters + string.whitespace + string.punctuation
        if len(self.card_number) != 16:
            self.card_number = input('Please enter a valid card number: ')
            return ExceptionCheck(None, None, None, None, None, None, None, None, self.card_number,
                                  None, None, None, None, None).check_card_number()
        else:
            for number in self.card_number:
                if number in forbidden_characters:
                    self.card_number = input('Please enter your card number without any letters, special characters, '
                                             'or spaces: ')
                    return ExceptionCheck(None, None, None, None, None, None, None, None, self.card_number,
                                          None, None, None, None, None).check_card_number()
            return self.card_number

    def check_expiration(self):
        self.expiration = self.expiration.replace(" ", "")
        forbidden_characters = string.ascii_letters + string.whitespace + """!"#$%&'()*+,-.:;?@[\]^_`{|}~"""
        if len(self.expiration) != 5:
            self.expiration = input("Please enter your card's expiration in the format of month/year (i.e. 08/24): ")
            return ExceptionCheck(None, None, None, None, None, None, None, None, None, self.expiration,
                                  None, None, None, None).check_expiration()
        if self.expiration[2] != '/':
            self.expiration = input("Please enter your card's expiration in the format of month/year (i.e. 08/24): ")
            return ExceptionCheck(None, None, None, None, None, None, None, None, None, self.expiration,
                                  None, None, None, None).check_expiration()
        else:
            for character in self.expiration:
                if character in forbidden_characters:
                    self.expiration = input("""Please enter your card's expiration without any letters, special "
                                            "characters besides "/", or spaces in the format of month/year 
                                            (i.e. 08/24): """)
                    return ExceptionCheck(None, None, None, None, None, None, None, None, None, self.expiration,
                                          None, None, None, None).check_expiration()
            return self.expiration

    def check_cvv(self):
        self.cvv = self.cvv.replace(" ", "")
        forbidden_characters = string.ascii_letters + string.whitespace + string.punctuation
        if len(self.cvv) != 3:
            self.cvv = input(
                'Please enter a valid CVV code. It should be a three digit code beneath your card number: ')
            return ExceptionCheck(None, None, None, None, None, None, None, None, None, None,
                                  self.cvv, None, None, None).check_cvv()
        else:
            for number in self.cvv:
                if number in forbidden_characters:
                    self.cvv = input('Please enter your CVV code without any letters, special characters, '
                                     'or spaces: ')
                    return ExceptionCheck(None, None, None, None, None, None, None, None, None, None,
                                          self.cvv, None, None, None).check_cvv()
            return self.cvv

    #                                                                                                                               Need to determine if there's a deposit limit and what it will be
    def check_deposit_amount(self):
        self.deposit_amount = self.deposit_amount.replace(" ", "")
        forbidden_characters = string.ascii_letters + string.whitespace + string.punctuation
        for number in self.deposit_amount:
            if number in forbidden_characters:
                self.deposit_amount = input('The minimum deposit is $10. Please enter your deposit amount '
                                            'without any letters, special characters, or spaces: ')
                return ExceptionCheck(None, None, None, None, None, None, None, None, None, None, None,
                                      self.deposit_amount, None, None).check_deposit_amount()
        self.deposit_amount = int(self.deposit_amount)
        if self.deposit_amount > 1000:
            self.deposit_amount = input('Currently the maximum deposit amount is $1,000. Please enter your '
                                        'deposit amount: ')
            return ExceptionCheck(None, None, None, None, None, None, None, None, None, None, None,
                                  self.deposit_amount, None, None).check_deposit_amount()
        elif self.deposit_amount < 10:
            self.deposit_amount = input('The minimum deposit amount is $10. Please enter your deposit amount: ')
            return ExceptionCheck(None, None, None, None, None, None, None, None, None, None, None,
                                  self.deposit_amount, None, None).check_deposit_amount()
        else:
            return self.deposit_amount

    def check_yn(self):
        self.yn = self.yn.replace(" ", "")
        allowed_answers = 'yn'
        if len(self.yn) != 1:
            self.yn = input('Please only enter a "y" for yes or a "n" for no. Would you like to save this card for '
                            'future use: ')
            return ExceptionCheck(None, None, None, None, None, None, None, None, None, None, None,
                                  None, self.yn, None).check_yn()
        else:
            for character in self.yn:
                if character not in allowed_answers:
                    self.yn = input('Please only enter a "y" for yes or a "n" for no. Would you like to save '
                                    'this card for future use: ')
                    return ExceptionCheck(None, None, None, None, None, None, None, None, None, None,
                                          None, None, self.yn, None).check_yn()
            return self.yn

    def check_recovery_phrase(self):
        forbidden_characters = string.punctuation + '\t' + '\n' + '\v' + '\f' + '\r' + '\x0b' + '\x0c'
        pass



# Used to test above code
# answer = input('what is your password? ')

# print(answer[0], answer[1])
# correct_name = ExceptionCheck(None, None, None, None, None, None, None, answer, None, None, None, None).check_password()
# UsUserAccount(None, None, None, None, None, None, None, correct_name, None, None, None, None).show_first_name()

# UsUserAccount(None, None, None, None, None, None, None, None, None, None, None, None).deposit_funds(123,12,12, 100)


# make instance where client has a bunch of funds on their credit/debit card