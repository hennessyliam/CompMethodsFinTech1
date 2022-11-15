import cbpro
import pandas as pd
import string

public_client = cbpro.PublicClient()
product = public_client.get_products()
currency = public_client.get_currencies()
eth = public_client.get_product_order_book('ETH-USD')
btc = public_client.get_product_order_book('BTC-USD')
eth24 = [public_client.get_product_24hr_stats('ETH-USD')]
past_eth_trades = public_client.get_product_trades('ETH-USD')
product_table = pd.DataFrame(product)
currency_table = pd.DataFrame(currency)
eth_table = pd.DataFrame(eth)
btc_table = pd.DataFrame(btc)
eth24_table = pd.DataFrame(eth24)
#past_eth_trades_table = pd.DataFrame(past_eth_trades)                      still working on this

def products(x, y=None, z=None):
    if y is None:
        for row in x:
            print(row)
    if y is not None and z is None:
        for row in x:
            print(row[y])
    elif y and z is not None:
        for row in x:
            print(row[y], '|', row[z])

def past_trades(x, counter=0, print_counter=0):                             # Tied to comments on line 17, 110, and 112. Still working on this
    if counter == 0:
        print("Next we're going to look at the past trades.")
        counter += 1
        past_trades()
    else:
        allowed_characters = string.digits
        answer = input("How many past trades would you like to look at: ")
        input = ''
        for character in answer:
            if character in allowed_characters:
                input = input + character
            else:
                answer = input('Please only enter numbers.\nHow many past trades would you like to look at: ')
                past_trades(answer)
        print_counter = int(input)
        while print_counter != 0:
            print(next(x))
        

#keys = open('hidden.txt', 'r').read().splitlines()

#public_key = keys[1]
#passphrase_key = keys[3]
#secret_key = keys[5]

#authenticated_client = cbpro.AuthenticatedClient(public_key, secret_key, passphrase_key)

#print(authenticated_client.get_accounts())
#print(authenticated_client.buy(product_id='BTC-USD', order_type='limit', price='10000', size='2.0'))

class Exception:
    def __init__(self, answer, input):
        self.answer = answer
        self.input = input

    def continue_example(self):
        allowed_answers = ['y', 'n']
        if len(self.answer) != 1:
            self.answer = input("Ready to continue? (y/n): ").lower()
            Exception(self.answer, None).continue_example()
        else:
            for character in self.answer:
                if character in allowed_answers:
                    if self.answer == 'y':
                        return
                    else:
                        self.answer = input("Ready to continue? (y/n): ").lower()
                        Exception(self.answer, None).continue_example()
                else:
                    self.answer = input("Please only enter y or n. Ready to continue? (y/n): ").lower()
                    Exception(self.answer, None).continue_example()

    def check_if_ready(self):
        self.input = input("Ready to continue? (y/n): ").lower()
        Exception(self.input, None).continue_example()
        return'-----------------------------------------------------------------------------------'

# Driver code
print("Hello and welcome to our showcase of how to use the Coinbase Pro API.\n")
print('Public Client Operations:\n')
print(Exception(None, None).check_if_ready())
products(product, None, None)
print(Exception(None, None).check_if_ready())
products(product, 'id', None)
print(Exception(None, None).check_if_ready())
print(product_table.tail().T)
print(Exception(None, None).check_if_ready())
products(currency, None, None)
print(Exception(None, None).check_if_ready())
print(currency_table.tail().T)
print(Exception(None, None).check_if_ready())
products(currency, 'id', 'name')
print(Exception(None, None).check_if_ready())
print('BTC:\n',btc_table.T)
print(Exception(None, None).check_if_ready())
print('ETH:\n',eth_table.T)
print(Exception(None, None).check_if_ready())
print('Past 24 hours for ETH:\n', eth24_table.T)
print(Exception(None, None).check_if_ready())
#print('Individual past ETH-USD trades:\n', past_eth_trades_table.T)                still working on this
print(Exception(None, None).check_if_ready())
#past_trades(past_eth_trades)                                                       still working on this
print(Exception(None, None).check_if_ready())
print(Exception(None, None).check_if_ready())
print(Exception(None, None).check_if_ready())