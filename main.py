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
				lst = list(self.content)
			else:
				lst = self.content[atom]
				display.inser(END, "    Name : {}\n".format(atom))
			for info in lst:
				if atom == "List":
					display.insert(END, "    {}".format(info))
				else:
					display.insert(END,"    {} : {}\n".format(info, self.content[atom][info]))

def main():
	elements = API("elements.json")
	root = Tk()
	root.title("Atom Gui")
	initial = Canvas(root,height=HEIGHT, width=WIDTH)
	initial.pack()
	bgimage = PhotoImage(file="atoms.png")
	background = Label(initial, image=bgimage)
	background.place(relx=0, rely=0, relwidth=1, relheight=1)
	displayFrame = Frame(root, bg=BORDER)
	displayFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)
	displayLabel = Listbox(displayFrame,bg="white" ,font=("Courier", 15), justify="left")
	displayLabel.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)
	scrollbar = Scrollbar(displayLabel)
	scrollbar.pack(side=RIGHT, fill=Y)
	scrollbar.config(command=displayLabel.yview)
	inputFrame = Frame(root, bg=BORDER)
	inputFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
	txtBox = Entry(inputFrame, font=("Courier", 18))
	txtBox.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.9)
	send = Button(inputFrame, font=("Courier", 10), text="GET INFO!", command=lambda:elements.getInfo(txtBox.get(), displayLabel))
	send.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.9)
	root.mainloop()


if __name__ == '__main__':
	main()