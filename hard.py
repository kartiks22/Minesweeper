from easy import Easy
from Tkinter import *
import tkMessageBox
import random


class Hard(Easy):
	def __init__(self,master):
		   #Takes image files from the folder
		self.tile_plain=PhotoImage(file="tile_plain.gif")
		self.tile_clicked=PhotoImage(file="tile_clicked.gif")
		self.tile_mine=PhotoImage(file="tile_mine.gif")
		self.tile_flag=PhotoImage(file="tile_flag.gif")
		self.tile_wrong=PhotoImage(file="tile_wrong.gif")
		self.tile_no=[]

		for x in range(1,9):
			self.tile_no.append(PhotoImage(file="tile_"+str(x)+".gif"))
		#creates a frame
		self.frame=Frame(master)
		self.frame.grid()
		

		self.Back_button=Button(self.frame,text="< Back",command=self.Back)
	        self.Back_button.grid(row=0,column=2,columnspan=4)
		
		self.Restart_button=Button(self.frame,text="restart",command=self.Res2)
		self.Restart_button.grid(row=0,column=6,columnspan=4)


		
		self.Quit_button=Button(self.frame,text="Quit >",command=self.Quit2)       #Displays Quit button.
	        self.Quit_button.grid(row=0,column=10,columnspan=4)
		

		
		self.flags=0
		self.correct_flags=0
		self.clicked=0

		self.buttons={}
		self.mines=0
		x_cord=1
		y_cord=0

		for x in range(256):
			mine=0
			image_p=self.tile_plain
			if (random.uniform(0,1)<0.15):     #computer chooses no.of mines randomly
				mine=1
				self.mines=self.mines+1
			#0:button
			#1:wether mine present(1:present,0:not present)
			#2:state(0:unclicked,1:clicked;2:flagged)
			#3:button number
			#4:coordinates
			#5:nearby mines
			self.buttons[x]=[Button(self.frame,image=image_p),mine,0,x,[x_cord,y_cord],0]
			self.buttons[x][0].bind("<Button-1>",self.lclick2(x))
			self.buttons[x][0].bind("<Button-3>",self.rclick2(x))

			y_cord=y_cord+1;
			if(y_cord==16):
				y_cord=0
				x_cord=x_cord+1

		for keys in self.buttons:
			self.buttons[keys][0].grid(row=self.buttons[keys][4][0],column=self.buttons[keys][4][1])
                
                #checks no.of mines near a tile
		for keys in self.buttons:
			x_crd=self.buttons[keys][4][0]
			y_crd=self.buttons[keys][4][1]
			self.near_mines=0
			if(keys==0):                 #Different for boundary tiles as no.of tiles surrounding it are different.
				if (self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+16)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+17)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(keys==15):
				if (self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+15)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+16)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(keys==240):
				if (self.check_mines(keys-16)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys-15)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(keys==255):
				if (self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys-16)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys-17)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(x_crd==1):
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+15)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+16)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+17)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(y_crd==0):
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-16)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-15)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+16)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+17)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(x_crd==16):
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-15)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-16)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-17)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(y_crd==15):
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+16)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+15)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-16)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-17)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			else:
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+15)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+16)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+17)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-15)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-16)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-17)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
                 #creates two labels which shows the the no.of mines in the game and no.of flags you can still plant.
		self.label2=Label(self.frame,text="Mines: "+str(self.mines))
		self.label2.grid(row=17,column=0,columnspan=8)
		self.label3=Label(self.frame,text="Flags: "+str(self.flags))
		self.label3.grid(row=17,column=8,columnspan=8)
	
	def Quit2(self):
	 	self.Quit()

	def Back(self):
		self.frame.grid_forget()
		self.__init__(self)
	
	def Res2(self):
		self.Restart2()



	def lclick2(self,keys):
		return lambda Button: self.l_click2(self.buttons[keys])
	
	def rclick2(self,keys):
		return lambda Button: self.r_click2(self.buttons[keys])
	#open the tile if we left click on it.
	def l_click2(self,button):
		if(button[1]==1):
			for keys in self.buttons:
				if (self.buttons[keys][1]!=1 and self.buttons[keys][2]==2):
					self.buttons[keys][0].configure(image=self.tile_wrong)
				if (self.buttons[keys][1]==1 and self.buttons[keys][2]!=2):
					self.buttons[keys][0].configure(image=self.tile_mine)
			self.end(2)
		else:
			if (button[5]==0):
				button[0].configure(image=self.tile_clicked)
				self.cln_emp_tile2(button[3])
			else:
				button[0].configure(image=self.tile_no[button[5]-1])
			if (button[2]!=1):
				button[2]=1
				self.clicked=self.clicked+1
			if (self.clicked==256-self.mines):
				self.win(2)
	#plants flag if once right clicked and removes it if clicked once again.
	def r_click2(self,button):
		if (button[2]==0):
			button[0].configure(image=self.tile_flag)
			button[2]=2
			button[0].unbind("<Button-1>")
			self.flags=self.flags+1
			self.update_flag()
		elif (button[2]==2):
			button[0].configure(image=self.tile_plain)
			button[2]=0
			button[0].bind("<Button-1>",self.lclick2(button[3]))
			self.flags=self.flags-1
			self.update_flag()
	
	#This function opens all the empty tiles near a tile.
	def cln_emp_tile2(self,button_num):
		button_list=[button_num]
		while (len(button_list)!=0):
			keys=button_list.pop()
			x_crd=self.buttons[keys][4][0]
			y_crd=self.buttons[keys][4][1]			
			if (keys==0):
				self.check(keys+1,button_list)
				self.check(keys+16,button_list)
				self.check(keys+17,button_list)				
			elif(keys==15):
				self.check(keys-1,button_list)
				self.check(keys+15,button_list)
				self.check(keys+16,button_list)
			elif(keys==240):
				self.check(keys-16,button_list)
				self.check(keys-15,button_list)
				self.check(keys+1,button_list)
			elif(keys==255):
				self.check(keys-17,button_list)
				self.check(keys-16,button_list)
				self.check(keys-1,button_list)
			elif(x_crd==1):
				self.check(keys-1,button_list)
				self.check(keys+1,button_list)
				self.check(keys+15,button_list)
				self.check(keys+16,button_list)
				self.check(keys+17,button_list)
			elif(y_crd==0):
				self.check(keys-16,button_list)
				self.check(keys-15,button_list)
				self.check(keys+1,button_list)
				self.check(keys+16,button_list)
				self.check(keys+17,button_list)
			elif(x_crd==16):
				self.check(keys-15,button_list)
				self.check(keys-16,button_list)
				self.check(keys-17,button_list)
				self.check(keys-1,button_list)
				self.check(keys+1,button_list)
			elif(y_crd==15):
				self.check(keys-16,button_list)
				self.check(keys-17,button_list)
				self.check(keys-1,button_list)
				self.check(keys+16,button_list)
				self.check(keys+15,button_list)
			else:
				self.check(keys-15,button_list)
				self.check(keys-16,button_list)
				self.check(keys-17,button_list)
				self.check(keys-1,button_list)
				self.check(keys+1,button_list)
				self.check(keys+15,button_list)
				self.check(keys+16,button_list)
				self.check(keys+17,button_list)
	
