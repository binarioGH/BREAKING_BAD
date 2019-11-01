#-*-coding: utf-8-*-
from tkinter import *
from json import loads
HEIGHT = 377
WIDTH = 605
BORDER = "#80c1ff"

class API:
	def __init__(self, file):
		self.file = file
		self.content = self.loadfile()
		self.msgerror = 0
		if not self.content:
			self.msgerror = "There was an error during the loading." 
	
	def loadfile(self):
		try:
			with open(self.file, "r") as f:
				content = f.read()
		except:
			return 0
		else:
			try:
				return loads(content)
			except:
				return 0

	def getInfo(self, atom, display):
		atom = atom.title()
		display.delete(0, END)
		if atom not in self.content and atom != "List":
			display.insert(END, "    Atom '{}' not found.".format(atom))
		else:
			if atom == "List":
				lst = []
				#lst = list(self.content)
			else:
				lst = self.content[atom]
				display.insert(END, "    Name : {}\n".format(atom))
			for info in lst:
				if atom == "List":
					display.insert(END, "    {}".format(info))
				else:
					if self.content[atom][info] == None:
						continue
					else:
						display.insert(END,"    {} : {}\n".format(info, self.content[atom][info]))

def main():
	elements = API("elements.json")
	root = Tk()
	root.title("Atom Gui")
	root.geometry("{}x{}".format(WIDTH, HEIGHT))
	initial = Frame(root, bg="white")
	initial.place(relx=0, rely=0, relwidth=1, relheight=1)
	bgimage = PhotoImage(file="atoms.png")
	background = Label(initial, image=bgimage, bg="white")
	background.place(relx=0, rely=0, relwidth=1, relheight=1)
	displayCanvas = Canvas(root, bg=BORDER)
	displayCanvas.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)
	scrollbar = Scrollbar(displayCanvas)
	#xscrollbar = Scrollbar(displayCanvas)
	displayLabel = Listbox(displayCanvas,bg="white" ,font=("Courier", 15), justify="left")#, yscrollcommand = scrollbar.set, xscrollcommand = xscrollbar.set)
	displayLabel.place(relx=0.01, rely=0.02, relwidth=0.945, relheight=0.96)
	scrollbar.pack(side=RIGHT, fill=Y)
	#xscrollbar.pack(side=BOTTOM, fill=X)
	scrollbar.config(command=displayLabel.xview)
	scrollbar.config(command=displayLabel.yview)
	inputCanvas = Canvas(root, bg=BORDER)
	inputCanvas.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
	txtBox = Entry(inputCanvas, font=("Courier", 18))
	txtBox.place(relx=0.05, rely=0.10, relwidth=0.6, relheight=0.8)
	send = Button(inputCanvas, font=("Courier", 10), text="GET INFO!", command=lambda:elements.getInfo(txtBox.get(), displayLabel))
	send.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.9)
	root.mainloop() 


if __name__ == '__main__':
	main()