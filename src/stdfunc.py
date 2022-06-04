import sys
def ERR(message:str, code:int):
  if message != None: print(message)
  else: print("An unknown error has occured")

  if code != None: sys.exit(code)
  else: sys.exit(1)

def uconfirm(message:str):
  """Ask the user for conformation on a message (Favors the 'N' answer)

  Args:
      message (str): The message to print
  """
  
  print(f"{message} [y/N]: ", end = '')
  answer = input()

  if answer != 'y' or 'Y': return(False)
  else: return(True)