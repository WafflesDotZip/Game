# Developed by WafflesDotZip on github


import time
import random
import sys
from tkinter import N
# -----------------------------------------------VARIABLES

Day = 1
BTC = round(random.randint(25000,30000))
ETH = round(random.randint(1900,3000))
DOGE = round(random.randint(26,186))

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
        \/          \/                \/                   """)
print("\n[>] You hear the phone ringing...")
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
    time.sleep(0.2)
    print("\n[ERROR] Invalid response! Must be a number.\n")
    time.sleep(0.2)
    continue
  if Amount > Balance:
    time.sleep(0.2)
    print("\n[ERROR] Insufficient balance.\n")
    time.sleep(0.2)
    continue
  if Amount < 0:
    time.sleep(0.2)
    print("\n[ERROR] Value cannot be negative.\n")
    time.sleep(0.2)
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
      time.sleep(0.5)
    print("\n┏────── Your Wallet ──────┓\n┠ USD  ▌$ {}\n┠ BTC  ▌₿ {}\n┠ ETH  ▌Ξ {}\n┠ DOGE ▌Ð {}\n┗─────────────────────────┛".format(Balance,WalletBTC,WalletETH,WalletDOGE))
    input("[>] press enter to continue.")
    time.sleep(0.2)
    print("\n[ Manager ]: Good job, Eric. Your next days will involve buying and selling.\nYou will see if a currency has fluctuated in price.")
    break
#=====================
#===================== DAY 2 - infinity.
#=====================
#=====================
#=====================
#=====================
#=====================
while True:
  time.sleep(0.2)
  Day += 1
  pastBTC = BTC
  pastETH = ETH
  pastDOGE = DOGE

  BTC += random.randint(-5000,5000)
  ETH += random.randint(-900,900)
  DOGE += random.randint(-20,20)
  if BTC <= 1:
    BTC = 1
  if ETH <= 1:
    ETH = 1
  if DOGE <= 1:
    DOGE = 1
  
  BTCchange = round(((BTC - pastBTC) / (pastBTC)) * 100,2)
  ETHchange = round(((ETH - pastETH) / (pastETH)) * 100,2)
  DOGEchange = round(((DOGE - pastDOGE) / (pastDOGE)) * 100,2)
  #ETHchange = round((pastETH / ETH) * 100,2)
  #DOGEchange = round((pastDOGE / DOGE) * 100,2) #incorrect

  if BTCchange > 0:
    BTCarrow = "⮝ +"
  else:
    BTCarrow = "⮟ "
  if ETHchange > 0:
    ETHarrow = "⮝ +"
  else:
    ETHarrow = "⮟ "
  if DOGEchange > 0:
    DOGEarrow = "⮝ +"
  else:
    DOGEarrow = "⮟ "
  print("=== Day {} | 9:30 AM | Stock Market Opens! ===".format(Day))
  time.sleep(0.2)
  print("[ Your cash : $ {} ]\n".format(Balance))
  time.sleep(0.2)
  print("• [BTC] 1 Bitcoin = ${} {}{} %\n".format(BTC,BTCarrow,BTCchange))
  time.sleep(0.2)
  print("• [ETH] 1 Ethereum = ${} {}{} %\n".format(ETH,ETHarrow,ETHchange))
  time.sleep(0.2)
  print("• [ETH] 1 DogeCoin = ${} {}{} %\n".format(DOGE,DOGEarrow,DOGEchange))
 ################## How much has our wallet changed?
  WalletBTC = round(WalletBTC +(WalletBTC * ( BTCchange / 100 )),5)
  WalletETH = round(WalletETH +(WalletETH * ( ETHchange / 100 )),5)
  WalletETH = round(WalletDOGE +(WalletDOGE * ( DOGEchange / 100 )),5)
  print("\n┏────── Your Wallet ──────┓\n┠ USD  ▌$ {}\n┠ BTC  ▌₿ {}\n┠ ETH  ▌Ξ {}\n┠ DOGE ▌Ð {}\n┗─────────────────────────┛".format(Balance,WalletBTC,WalletETH,WalletDOGE))

  Valid = ["BTC","ETH","DOGE"] # Outline all valid answers


  while True:
    
      Status = input("[>] Will you BUY or SELL a currency today? [ BUY/SELL ]")
      Status = Status.upper()
      if not Buy == "BUY" and not Buy == "SELL":
        print("[ERROR] Invalid response! Select either [ BUY/SELL ]\n")
        continue
      else:
        break
  if Status == "SELL": #============================ SELL
    while True:
      Sell = input("[>] What cryptocurrency will you sell? [ BTC/ETH/DOGE ]\n>>> ")
      Sell = Sell.upper()
      if not Sell in Valid: # IF Sell ( the input ) is not a valid andwer :
        print("[ERROR] Invalid response! Select either [ BTC / ETH / DOGE ]\n")
        continue ########### Check if we actually posess the item we want to sell.
      elif Sell == "BTC":
        if BTC == 0:
          print("[ERROR] You do not own any BTC.\n")
          continue
      elif Sell == "ETH":
        if ETH == 0:
          print("[ERROR] You do not own any ETH.\n")
          continue
      elif Sell == "DOGE":
        if DOGE == 0:
          print("[ERROR] You do not own any DOGE.\n")
          continue
      else:
        break
  
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
  if Status == "BUY": # ======================================= BUY
  
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

  # --------------------------------------------- 
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

