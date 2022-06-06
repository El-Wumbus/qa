# qa -- a program that allows for single command compression and extraction an extra feature
#     Copyright (C) 2022  Aidan Neal

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from rich import print as printf
import sys
def ERR(message:str, code:int):
  """
  Prints a message and exits the program with a given exit code
  
  :param message: The message to print to the console
  :type message: str
  :param code: The exit code to exit with
  :type code: int
  """
  if message != None: printf(f"[bold red]{message}[/bold red] \[{code}\]")
  else: printf("[bold red]An unknown error has occured![/bold red]")

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