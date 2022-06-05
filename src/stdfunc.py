import sys
def ERR(message:str, code:int):
  """
  Prints a message and exits the program with a given exit code
  
  :param message: The message to print to the console
  :type message: str
  :param code: The exit code to exit with
  :type code: int
  """
  if message != None: print(message)
  else: print("An unknown error has occured")

  if code != None: sys.exit(code)
  else: sys.exit(1)

def uconfirm(message:str):
  """
  Asks the user a question and returns True if the user answers 'y' or 'Y' and False otherwise
  
  :param message: The message to display to the user
  :type message: str
  :return: True or False
  """
  
  # Printing the message and then waiting for the user to input something.
  print(f"{message} [y/N]: ", end = '')
  answer = input()

  # Checking if the answer is not equal to 'y' or 'Y' and returning False if it is not.
  if answer != 'y' or 'Y': return(False)
  else: return(True)