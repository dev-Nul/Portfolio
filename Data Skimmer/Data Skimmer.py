#BS4 is a module that can sift through HTML for tags.
from bs4 import BeautifulSoup as bs
#Opens up result webpages in browser.
import webbrowser
#Captures information from websites.
import requests as req
#Sleeps program.
from time import sleep
#For determining existance of file.
from os import path as p
#For copying files.
from shutil import copyfile as cp

print(""" _____     ______     ______   ______                                        
/\  __-.  /\  __ \   /\__  _\ /\  __ \                                       
\ \ \/\ \ \ \  __ \  \/_/\ \/ \ \  __ \                                      
 \ \____-  \ \_\ \_\    \ \_\  \ \_\ \_\                                     
  \/____/   \/_/\/_/     \/_/   \/_/\/_/                                     
                                                                             
 ______     __  __     __     __    __     __    __     ______     ______    
/\  ___\   /\ \/ /    /\ \   /\ "-./  \   /\ "-./  \   /\  ___\   /\  == \   
\ \___  \  \ \  _"-.  \ \ \  \ \ \-./\ \  \ \ \-./\ \  \ \  __\   \ \  __<   
 \/\_____\  \ \_\ \_\  \ \_\  \ \_\ \ \_\  \ \_\ \ \_\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/\/_/   \/_/   \/_/  \/_/   \/_/  \/_/   \/_____/   \/_/ /_/ 

        By Zachary Morritt""")

#Make a class for skimming information.
class skimInformation ():
	def __init__(self, hook, dataType):
		self.hook = f"{hook}"
		self.dataType = dataType

		try:
			r = req.get(self.hook).text
		except Exception:
			print("NON-URL OR NON-EXISTANT SERVER INPUTTED.")
			quit
			

		self.r = req.get(self.hook).text
		
		print("Captured page! Sifting Information...")
		sleep(1.5)
		
		self.soup = bs(self.r, features="html.parser")

	#Write result to skimmer.html and copy from the blueprint if it
	#doesn't already exist.
	def writeResult (self):
		if p.isfile('./skimming.html') is not True:
			cp('./Source/blueprint.html', './skimming.html')

		with open('skimming.html', 'a', encoding='utf-8') as paste:
			for item in self.soup.find_all(self.dataType):
				paste.write(str(item))

	#Print result of skimming to console
	def printResult (self):
		for item in self.soup.find_all(self.dataType):
			print(item)

	#Opens website in browser.
	def openWebsite (self):
		input("\n\nPress Enter to Open Site")
		webbrowser.open(self.hook)

def wait (message="Press ENTER to continue..."):
	input(f"\n{message}")
	print("")


print("""
Welcome to the skimmer program. After inserting a data you want to
select for, and the URL (starting with HTTP://), the program will
skim the data from the website and collect it in skimming.html.""")
wait()

print("\n-----------------------------------------------\n")

print("""You can sift for certain html tags in this program. The
options are <img>*, <table> (along with <td>, <tr>, and <th>), <h1>
(or its subheader variants), <div>, and <p>.

*If the img is stored locally on the web server, <img> may not work.
""")
wait()

options = ['<img>', '<table>', '<h1>', '<h2>', '<h3>', '<h4>', '<div>', '<p>', '<th>', '<tr>', '<td>']

formatDictionary = {'<img>' : 'img', '<table>' : 'table', '<h1>' : 'h1', '<h2>' : 'h2',
		    '<h3>' : 'h3', '<h4>' : 'h4', '<div>' : 'div', '<p>' : 'p',
                    '<th>' : 'th', '<tr>' : 'tr', '<td>' : 'td'}

formattedOptions = ['img', 'table', 'h1', 'h2', 'h3', 'h4', 'div', 'th', 'tr', 'td', 'p']


while True:
	print("Insert a Data Tag.")
	data = input("Data Format > ")
	
	if data in options:
		data = formatDictionary[data]
		print(f"\nData Type Set... \"{data}\".")
		
		break
	elif data in formattedOptions:
		print(f"\nData Type Set... \"{data}\".")

		break
	else:
		print("\nInvalid Data Tag... Please try again.")
		sleep(2)
		continue

while True:
	print("\nPlease input a URL.\n")
	
	request = f'{input("URL > ")}'

	#Create skimmer class.
	skimmer = skimInformation(request, data)
	skimmer.writeResult()

	#Asking the user if they want to print the URL.
	print("\nCompleted operation! Would you like to print the output? (y/n)")
	
	while True:
		yesno = input("(y/n) > ")
		
		if yesno == "yes" or yesno == "y":
			print("")
			skimmer.printResult()
			break
		elif yesno == "no" or yesno == "n":
			print("\nAlright!")
			break
		print("Your input is invalid, repeat that?\n")

	#Asking if the user has another URL, and repeats above if they do.
	print("\nDo you have another URL to enter?")

	while True:
		yesno = input("(y/n) > ")
		
		if yesno == "yes" or yesno == "y":
			print("")
			del skimmer
			quitProgram = False
			break
		elif yesno == "no" or yesno == "n":
			del skimmer
			quitProgram = True
			break
		print("Your input is invalid, repeat that?\n")

	if quitProgram == True:
		break

#Fairwell message.
print("\nThank you for using the skimmer program.")
wait("Press ENTER to exit...")

print("""\n ______     __  __     ______    
/\  == \   /\ \_\ \   /\  ___\   
\ \  __<   \ \____ \  \ \  __\   
 \ \_____\  \/\_____\  \ \_____\ 
  \/_____/   \/_____/   \/_____/ 
                                 """)
sleep(2)
