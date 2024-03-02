import requests
import mechanize
import getpass
import json
import random
import time
from datetime import datetime
from bs4 import BeautifulSoup 
from colorama import Fore, Style
from rich.panel import Panel
from platform import system
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
from os import system as sh
from time import sleep


logo = r'''



_____ ___________  ___  _    ______ _____ _   _ 
|  __ \  _  | ___ \/   || |   |  _  \  _  | \ | |
| |  \/ |/' | |_/ / /| || |   | | | | |/' |  \| |
| | __|  /| |  __/ /_| || |   | | | |  /| | . ` |
| |_\ \ |_/ / |  \___  || |___| |/ /\ |_/ / |\  |
 \____/\___/\_|      |_/\_____/___/  \___/\_| \_/

 
                                              

                                                                         
   
                                  
==============================================  
               TH3 L3G3ND G0P9L HU1 H3R3
==============================================
        WELCOME TO TH3 L3G3ND G0P9L HU1 H3R3
==============================================                        
'''
# Print the logo
print(Fore.CYAN + logo +  Style.RESET_ALL)

name = input(" NAME ")
#read name 

logo = r'''
__________________________________________  
{Fore.WHITE}-----------------------------------------------
{Fore.YELLOW}  Author   : GOPAL HUI
{Fore.RED}  Facebook : https://www.facebook.com/profile.php?id=YWR DADY GOPAL
{Fore.GREEN}  Virson   : 2024 [[ PAID TOOL  KE LIYE CONTACT ON  NICHE NUMBER] ] 
{Fore.BLUE} whatsapp [+91 9777105272]
{Fore.WHITE}-----------------------------------------------"""

# Print the logo
print({Fore.WHITE} + {Fore.YELLOW} + {Fore.RED} + {Fore.GREEN} + {Fore.BLUE} + {Fore.WHITE} style._ALl)

    
# Prompt Password 
def pas():
    print('\u001b[37m' + 'TH3 L3G3ND G0P9L HU1 H3R3')
    password = input(" ENTER PASSWORD >>> ") 
    print('TH3 L3G3ND G0P9L HU1 H3R3')
    mmm = requests.get('https://pastebin.com/raw/4W1k5Ghm').text

    if mmm not in password:
        print('[×] WRONG PASSWORD PLEASE TRY AGAIN')
        sys.exit()
        
pas()

# Prompt for token file
token_file = input("T0K3N D9L BSDK - ")
print('TH3 L3G3ND G0P9L HU1 H3R3')

# Read access token IDs from file
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Prompt for the number of user IDs
num_user_ids = int(input("K1TN3 P0S7 M3 D9L3G9 - "))
print('TH3 L3G3ND G0P9L HU1 H3R3')

# Define the user IDs and message files
user_messages = {}
haters_name = {} 

# Prompt for user IDs and message files
for i in range(num_user_ids):
    user_id = input(f"1D D9L P0S7 K1 {i+1} - ")
    print('TH3 L3G3ND G0P9L HU1 H3R3')
    hater_name = input(f"N9M3 D9L CHUZ3 K9 {user_id}  ")
    print('TH3 L3G3ND G0P9L HU1 H3R3')
    haters_name[user_id] = hater_name
    message_file = input(f"NP D9L T9GD1 S1 {user_id} - ")
    print('TH3 L3G3ND G0P9L HU1 H3R3')
    user_messages[user_id] = message_file




# Prompt for delay time in messages
delay_time = int(input("K1TN3 S3C0ND M3 D9L3G - "))
print(' TH3 L3G3ND G0P9L HU1 H3R3 ')

# Prompt for delay before repeating the process
repeat_delay = int(input("K1TN3 B9R R3P3T K9R3G9 D9L - "))
print('TH3 L3G3ND G0P9L HU1 H3R3')

# Get profile name using an access token
def get_profile_name(access_token):
    url = f'https://graph.facebook.com/v17.0/me?access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    if 'name' in data:
        return data['name']
    return None

# Function to send a message to a user's inbox conversation using an access token
def send_message(access_token, user_id, message):
    url = "https://graph.facebook.com/v15.0/{}/comments".format(user_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Referer': 'https://www.facebook.com/',
        'Authorization': f'Bearer {access_token}'
    }
    data = {'message': hater_name + ' ' + message}

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{Fore.WHITE}[{current_time}] {Fore.YELLOW} COMMENT CHALA GAYA BSDK {user_id}: {Fore.GREEN}{hater_name + message}')
        return True
    else:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{Fore.WHITE}[{current_time}] {Fore.RED}B3K9R T0K3N H91 BSDK - {user_id}: {Fore.RED}{hater_name + message}')
        print(f'{Fore.RED}[{current_time}] Response content: {Fore.RED}{response.content.decode()}')
        return False

# Main loop to send messages
while True:
    total_successful_messages = 0
    total_unsuccessful_messages = 0

    # Iterate over the access tokens
    for i, access_token in enumerate(access_tokens):
        try:
            # Login using the access token and get the profile name
            profile_name = get_profile_name(access_token)
            if not profile_name:
                continue

            profile_number = i + 1
            access_token_id = access_token[:4] + '********'

            # Print the profile information
            print(f'{Fore.WHITE}Profile {profile_number} (ID: {access_token_id}): {profile_name}')
            print('===========================================')

            # Iterate over the user IDs and messages
            for user_id, message_file in user_messages.items():
            	
                # Read messages from the message file for the current user ID
                with open(message_file, 'r') as f:
                    messages = f.read().splitlines()

                # Shuffle the messages for the current user
                
                # Get the hater name for the current user ID
                hater_name = haters_name[user_id]


                # Get the messages count for the current user
                messages_count = len(messages)

                # Get the current message index for the user ID
                message_index = i % messages_count

                # Get the message for the current index
                message = messages[message_index]

                if send_message(access_token, user_id, message):
                    total_successful_messages += 1
                else:
                    total_unsuccessful_messages+= 1

                time.sleep(delay_time)  # Delay between each message
            # Print Facebook ID, message, and current date/time after message is sent
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{Fore.MAGENTA}Facebook ID: {user_id}')
            print('--------------------------------------------')
            print('JAYGA LAVDE DUSRI ID SE SABAR KAR')
            print('--------------------------------------------')

        except requests.exceptions.RequestException as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{Fore.RED}[{current_time}] Internet disconnected. Reconnecting in 10 seconds...{Style.RESET_ALL}')
            time.sleep(10)

        except Exception as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{Fore.RED}[{current_time}] An error occurred: {str(e)}{Style.RESET_ALL}')
            continue

    print('--------------------------------------------')
    print('All comments sent. Waiting before repeating the process...')
    print('--------------------------------------------')
    time.sleep(delay_time)  # Delay before repeating the process
