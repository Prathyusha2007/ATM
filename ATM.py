from time import sleep
def password():
  tries=3
  while tries >= 0:
    pin=int(input("Please enter your pin:"))
    if pin==(1324):
      print("Give us just a moment we are fetching your data...")
      sleep(2)
      return True
    else:
      print("Incorrect pin Authenticantion failed!")
      return False  
def atm_start():
  balance=0
  print("Hello!Welcome to the ATM")
  if password():
    while True:
      print("Press 1 for checking balance in your account")
      print("Press 2 for withdrawing amount from your account")
      print("Press 3 for depositing amount in your account")
      print("Press 4 for exiting the ATM")

      choose=int(input("\nChoose an option that fits your requirment:"))
      if choose ==1:
        print("Please give us a moment we are fetching your data...")
        sleep(2)
        print("\nYour account balance is:",balance)
      elif choose==2:
        print("Please give us a moment we are fetching your data...")
        sleep(2)
        withdrawl=int(input("Please enter the amount you want to withraw from your account:"))
        if withdrawl<balance:
          balance = balance - withdrawl
          print("Amount deducted from your account :",withdrawl)
        else:
          print("You do not have enough balance!Please deposit some amount to increase your account balance.")
      elif choose ==3:
        deposit=int(input("Please enter the amount you want to deposit in your account:"))
        balance=deposit+balance
        print("Amount deposited in your account :",deposit)
      elif choose == 4:
        print("Thanks for using the ATM!Please visit again!")
        break
atm_start()
