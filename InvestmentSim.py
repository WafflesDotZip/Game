
# Developed by AFK-Waffles on github


import time
import random
import sys
# -----------------------------------------------VARIABLES

Day = 1
BTC = round(random.randint(25000,30000))
ETH = round(random.randint(1900,3000))
DOGE = round(random.randint(2,186))

WalletBTC = 0
WalletETH = 0
WalletDOGE = 0

Afford = 0
Balance = 100

# ---------------------------------------------- VARIABLES




#print("""\n▄█    ▄       ▄   ▄███▄     ▄▄▄▄▄      ▄▄▄▄▀ ▄█    ▄     ▄▀  
#██     █       █  █▀   ▀   █     ▀▄ ▀▀▀ █    ██     █  ▄▀    
#██ ██   █ █     █ ██▄▄   ▄  ▀▀▀▀▄       █    ██ ██   █ █ ▀▄  
#▐█ █ █  █  █    █ █▄   ▄▀ ▀▄▄▄▄▀       █     ▐█ █ █  █ █   █ 
# ▐ █  █ █   █  █  ▀███▀               ▀       ▐ █  █ █  ███  
#   █   ██    █▐                                 █   ██       
#             ▐                                               
#   ▄▄▄▄▄   ▄█ █▀▄▀█   ▄   █    ██     ▄▄▄▄▀ ████▄ █▄▄▄▄      
#  █     ▀▄ ██ █ █ █    █  █    █ █ ▀▀▀ █    █   █ █  ▄▀      
#▄  ▀▀▀▀▄   ██ █ ▄ █ █   █ █    █▄▄█    █    █   █ █▀▀▌       
# ▀▄▄▄▄▀    ▐█ █   █ █   █ ███▄ █  █   █     ▀████ █  █       
#            ▐    █  █▄ ▄█     ▀   █  ▀              █        
#                ▀    ▀▀▀         █                 ▀         
#                                ▀                            """)

print(r"""
_________                        __                        
\_   ___ \_______ ___.__._______/  |_  ____                
/    \  \/\_  __ <   |  |\____ \   __\/  _ \               
\     \____|  | \/\___  ||  |_> >  | (  <_> )              
 \______  /|__|   / ____||   __/|__|  \____/               
        \/        \/     |__|                              
  _________.__              .__          __                
 /   _____/|__| _____  __ __|  | _____ _/  |_  ___________ 
 \_____  \ |  |/     \|  |  \  | \__  \\   __\/  _ \_  __ \
 /        \|  |  Y Y  \  |  /  |__/ __ \|  | (  <_> )  | \/
/_______  /|__|__|_|  /____/|____(____  /__|  \____/|__|   
        \/          \/                \/                   \n""")
print("[>] You hear the phone ringing...")
time.sleep(1)
print("""[ Manager ]: Welcome to your first day on the job.""")
time.sleep(0.5)
print("You must buy and sell cryptocurrencies to make a profit.")
time.sleep(0.2)
print("• You can only make ONE transaction each day, so make it count.")
time.sleep(0.2)
print("• You start with $100. ")
time.sleep(0.2)
print("• If you go bankrupt then we will execute you and probably seize all your assets.")
time.sleep(0.2)
print("• Okay, its almost 9:30. Get to your office, Eric.\n""")
cont = input("[>] press enter to continue.")
print("=== Day {} | 9:30 AM | Stock Market Opens! ===".format(Day))
time.sleep(0.1)
print("[ Your cash : $ {} ]\n".format(Balance))
time.sleep(0.1)
print("• [BTC] 1 Bitcoin = ${}\n".format(BTC))
time.sleep(0.1)
print("• [ETH] 1 DogeCoin = ${}\n".format(DOGE))
time.sleep(0.1)
print("• [ETH] 1 Ethereum = ${}\n".format(ETH))
Valid = ["BTC","ETH","DOGE"] # Outline all valid answers

while True:
  Buy = input("[>] What cryptocurrency will you buy? [ BTC/ETH/DOGE ]\n>>> ")
  Buy = Buy.upper()
  if not Buy in Valid: # IF BUY ( the input ) is not a valid andwer :
    print("[ERROR] Invalid response! Select either [ BTC / ETH / DOGE ]\n")
    continue
  if Buy in Valid: # IF answer is valid :
    break
# ----------------------------------------- CALCULATE AFFORDABILITY 

if Buy == "BTC":
  Afford = round(Balance / BTC,5)

if Buy == "ETH":
  Afford = round(Balance / ETH,5)

if Buy == "DOGE":
  Afford = round(Balance / DOGE,5)

# --------------------------------------------- DAY ONE
while True:
  try:
    Amount = float(input("[>] How much cash will you invest into {} ? You have ${}.\n>>> ".format(Buy,Balance)))
  except ValueError:
    print("\n[ERROR] Invalid response! Must be a number.\n")
    continue
  if Amount > Balance:
    print("\n[ERROR] Insufficient balance.\n")
    continue
  if Amount < 0:
    print("\n[ERROR] Value cannot be negative.\n")
    continue
  if Amount <= Balance: #valid
#----------------------------------------------
    if Buy == "BTC":
      WalletBTC += round(Amount / BTC,5)
      Purchased = round(Amount / BTC,5)
      

    if Buy == "ETH":
      WalletETH += round(Amount / ETH,5)
      Purchased = round(Amount / ETH,5)
  
    if Buy == "DOGE":
      WalletDOGE += round(Amount / DOGE,5)
      Purchased = round(Amount / DOGE,5)
      
    Balance -= Amount
#------------------------------------------------
    if Amount == 0:
      print("\n[!! $ !!] You have decided to purchase nothing today.".format(Amount,Purchased,Buy))
    if Amount > 0:
      print("\n[!! $ !!] You have converted ${} to {} {}.".format(Amount,Purchased,Buy))
    print("\n┏────── Your Wallet ──────┓\n┠ USD  ▌$ {}\n┠ BTC  ▌₿ {}\n┠ ETH  ▌Ξ {}\n┠ DOGE ▌Ð {}\n┗─────────────────────────┛".format(Balance,WalletBTC,WalletETH,WalletDOGE))
    print("\n[ Manager ]: Good job, Eric. Your next days will involve buying AND selling.\n The symbols ⮟ + ⮝ will indicate if a currency has changed in price.")
    break
#=====================
#===================== DAY 2 - infinity.
#=====================
#=====================
#=====================
#=====================
#=====================
while True:
  Day += 1
  BTC += random.randint(-5000,5000)
  print("=== Day {} | 9:30 AM | Stock Market Opens! ===".format(Day))
  print("[ Your cash : $ {} ]\n".format(Balance))
  print("• [BTC] 1 Bitcoin = ${}\n".format(BTC))
  print("• [ETH] 1 Ethereum = ${}\n".format(ETH))
  print("• [ETH] 1 DogeCoin = ${}\n".format(DOGE))

  Valid = ["BTC","ETH","DOGE"] # Outline all valid answers

  while True:
    Buy = input("[>] What cryptocurrency will you buy? [ BTC/ETH/DOGE ]\n>>> ")
    Buy = Buy.upper()
    if not Buy in Valid: # IF BUY ( the input ) is not a valid andwer :
      print("[ERROR] Invalid response! Select either [ BTC / ETH / DOGE ]\n")
      continue
    if Buy in Valid: # IF answer is valid :
      break
  # ----------------------------------------- CALCULATE AFFORDABILITY 

  if Buy == "BTC": 
    Afford = round(Balance / BTC,5)

  if Buy == "ETH":
    Afford = round(Balance / ETH,5)

  if Buy == "DOGE":
    Afford = round(Balance / DOGE,5)

  # --------------------------------------------- DAY ONE
  while True:
    try:
      Amount = float(input("[>] How much cash will you invest into {} ? You have ${}.\n>>> ".format(Buy,Balance)))
    except ValueError:
      print("\n[ERROR] Invalid response! Must be a number.\n")
      continue
    if Amount > Balance:
      print("\n[ERROR] Insufficient balance.\n")
      continue
    if Amount < 0:
      print("\n[ERROR] Value cannot be negative.\n")
      continue
    if Amount <= Balance:
  #----------------------------------------------
      if Buy == "BTC":
        WalletBTC += round(Amount / BTC,5)
        Purchased = round(Amount / BTC,5)
        

      if Buy == "ETH":
        WalletETH += round(Amount / ETH,5)
        Purchased = round(Amount / ETH,5)
    
      if Buy == "DOGE":
        WalletDOGE += round(Amount / DOGE,5)
        Purchased = round(Amount / DOGE,5)
        
      Balance -= Amount
  #------------------------------------------------
      if Amount == 0:
        print("\n[!! $ !!] You have decided to purchase nothing today.".format(Amount,Purchased,Buy))
      if Amount > 0:
        print("\n[!! $ !!] You have converted ${} to {} {}.".format(Amount,Purchased,Buy))
      print("\n┏────── Your Wallet ──────┓\n┠ USD  ▌$ {}\n┠ BTC  ▌₿ {}\n┠ ETH  ▌Ξ {}\n┠ DOGE ▌Ð {}\n┗─────────────────────────┛".format(Balance,WalletBTC,WalletETH,WalletDOGE))
      break

