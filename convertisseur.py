from tkinter import *
 
class Interface(Frame):
 
	def __init__(self, fenetre, **kwargs):
		Frame.__init__(self, fenetre, width=768, height=576,**kwargs)
		self.pack(fill=BOTH)
		self.nb_clic = 0
 
	
 
		self.label_choix_monnaie = Label(self, text="Choisissez le sens de conversion",fg='red')
		self.label_choix_monnaie.pack()
 
		self.sens = StringVar()
 
		self.s1 = Radiobutton(self, text='Euros -> Autre monnaie', variable=self.sens, value='s1')
		self.s1.pack()
 
		self.s2 = Radiobutton(self, text='Autre monnaie -> Euros', variable=self.sens, value='s2')
		self.s2.pack()
 
		self.label_choix_monnaie = Label(self, text="Choisissez l'autre monnaie",fg='blue')
		self.label_choix_monnaie.pack()
 
		self.monnaie = StringVar()
 
		self.m1 = Radiobutton(self, text='Dollars US', variable=self.monnaie, value='Dollars US')
		self.m1.pack()
 
		self.m2 = Radiobutton(self, text='Livres Sterling', variable=self.monnaie, value='Livres Sterling')
		self.m2.pack()

		self.m6 = Radiobutton(self, text='Dinars algeriens', variable=self.monnaie, value='Dinars ')
		self.m6.pack()
 
		self.labelentry = Label(self, text="Entrez la somme de départ",fg='blue')
		self.labelentry.pack()
 
		self.entry = Entry(self)
		self.entry.pack()
 
		self.bouton = Button(self, text="CONVERTIR", command=self.convert,fg='red')
		self.bouton.pack()
 
		self.output = StringVar()
		self.out = Label(self, textvariable=self.output,fg='yelow')
		self.out.pack()
 
		self.error = StringVar()
		self.err = Label(self, textvariable=self.error,fg='black')
		self.err.pack()
 
	def convert(self):
		ent=self.entry.get()
		if ent=='':
			ent=0
		else:
			ent=float(ent)
		a=1.24
		b=0.79
		c=146.04
		d=17.04
		e=655.62
		f=106.81
		g=58.22
		h=7.64
		i=77.04
		j=3.16
		if self.sens.get()=='s1':
			if self.monnaie.get()=='Dollars US':
				o=ent*a
				self.error.set('')
			elif self.monnaie.get()=='Livres Sterling':
				o=ent*b
				self.error.set('')
			
			elif self.monnaie.get()=='Dinars algeriens':
				o=ent*f
				self.error.set('')
			
			else:
				self.error.set('Veuillez entrer toutes les informations necessaires a* la conversion')
				print ('Probleme')
			monnaie_arrivee=self.monnaie.get()
		elif self.sens.get()=='s2':
			if self.monnaie.get()=='Dollars US':
				o=ent/(a+0.0)
				self.error.set('')
			elif self.monnaie.get()=='Livres Sterling':
				o=ent/(b+0.0)
				self.error.set('')
			
			elif self.monnaie.get()=='Dinars algeriens':
				o=ent/(f+0.0)
				self.error.set('')
			
			else:
				print ('probleme')
				self.error.set('Veuillez entrer toutes les informations necessaires à la conversion')
			monnaie_arrivee='Euros'
		else:
			self.error.set('Veuillez entrer toutes les informations necessaires à la conversion')
			print ('problème')
		self.output.set('Vous avez convertis'+str(o)+' '+monnaie_arrivee)
 
 
fenetre = Tk()
fenetre.title("Convertission en euros")
 
interface = Interface(fenetre)
 
bouton=Button(fenetre,text="Quitter",command=fenetre.destroy,fg="red")
bouton.pack()
 
interface.mainloop()
interface.destroy()


   
    