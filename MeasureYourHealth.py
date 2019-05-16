from tkinter import *


class Contact_manager (Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.configure(background='#41B77F')
        self.language ="French"
        self.title = "NUTRIFORMQ"
        self.Rentrer = "Rentrer!"
        self.pagelabel1 ="VOS DONNÉE PERSONNEL"
        self.pagelabel2="Comment voulez vous que je vous apelle ?"
        self.pagelabel3="Quel est votre âge ?"
        self.pagelabel4="Quel est votre taille (en cm) ?"
        self.pagelabel5="Quel est votre poids (en Kg) ?"
        self.pagelabel6="Je suis une/un : "
        self.pagelabel7="Quel est votre morphologie ?"
        self.pagelabel8="Valider !"
        self.pagelabel9="RÉSULTATS POUR"
        self.pagelabel10="IMC :"
        self.pagelabel11="poids idéal :"
        self.imc_var=0
        self.weight=0
        self.vHeight=0
        self.pin_var =0
        self.vAge =10
        self.sexe_var =0
        self.vName=""
        self.mg =0
        self.corpulence_var =1
        self.MR =0
        self.msg = "Chez NUTRIFORM nous voulons absolument être utile aux autres et accompagner les utilisateurs dans leur quête de bonne santé physique"
        self.parent = parent
        self.initUI()    

    def initUI(self):
        self.parent.title(self.title)
        self.parent.minsize(1080, 720)
        self.parent.maxsize(1080, 720)
        self.parent.iconbitmap("logo.ico")
        self.pack(fill=BOTH, expand=1)
        Label(self, text=self.title, font=("Times", 40),bg='#41B77F', fg='white').place(relx=.5, rely=.3, anchor="center")
        Label(self, text=self.msg, font=("Times", 13), bg='#41B77F', fg='white').place(relx=.5, rely=.4, anchor="center")
        variable = StringVar(self)
        variable.set(self.language) # default value
        LangOption = OptionMenu(self, variable, "English", "French", command=self.SelectLang)
        LangOption.config(bg = "#41B77F", fg='white')
        LangOption.place(relx=1, rely=.0, anchor="ne")
        bouton1 = Button(self, text=self.Rentrer, width=10, height=2,
                 font=("Times", 10), bg='white', fg='#41B77F',command=self.SecondPage).place(relx=.5, rely=.6, anchor="center")
        image1 = PhotoImage(file='logo.PNG').zoom(35).subsample(50)
        label = Label(self,image=image1) 
        label.image = image1 # keep a reference!
        label.place(relx=.5, rely=.8, anchor="center")
        pass
    def SelectLang(self,value):
        self.language = value
        if  self.language == "English":
            self.pagelabel2="How do you want me to call you?"
            self.title = "NUTRIFORMQ"
            self.pagelabel3="What is your age ?"
            self.pagelabel1 ="YOUR PERSONAL DATA"  
            self.pagelabel4="What is your height (in cm)?"
            self.pagelabel5="What is your weight (in Kg)?"
            self.pagelabel6="I am Man/ Women:"
            self.pagelabel7="What is your morphology?"
            self.pagelabel8="Validate!"
            self.Rentrer = "Come in!"
            self.pagelabel9="RESULTS FOR"
            self.pagelabel10="BMI :"
            self.pagelabel11="Ideal Weight :"
            self.msg = "At NUTRIFORM we absolutely want to be useful to others and support users in their quest for good physical health"
        else:
            self.title = "NUTRIFORMQ"
            self.pagelabel3="Quel est votre âge ?"
            self.pagelabel2="Comment voulez vous que je vous apelle ?"
            self.pagelabel1 ="VOS DONNÉE PERSONNEL"
            self.pagelabel6="Je suis une/un : "
            self.pagelabel7="Quel est votre morphologie ?"
            self.pagelabel8="Valider !"
            self.Rentrer = "Rentrer!"
            self.pagelabel9="RÉSULTATS POUR"
            self.pagelabel4="Quel est votre taille (en cm) ?"
            self.pagelabel5="Quel est votre poids (en Kg) ?"
            self.pagelabel10="IMC :"
            self.pagelabel11="Poids Idéal :"
            self.msg = "Chez NUTRIFORM nous voulons absolument être utile aux autres et accompagner les utilisateurs dans leur quête de bonne santé physique"
            pass
        self.ClearFrame()
        self.initUI()
        pass
    
    def ClearFrame(self):
            for child in self.winfo_children():
                child.destroy()
            pass
 
        
    def SecondPage(self):
            self.ClearFrame()  
            Label(self, text=self.pagelabel1, font=("Times", 40),bg='#41B77F', fg='white').place(relx=.5, rely=.1, anchor="center")
            image2 = PhotoImage(file='donne.PNG').zoom(35).subsample(50)
            label1 = Label(self,image=image2)
            label1.image = image2 # keep a reference!
            label1.place(relx=.5, rely=.2, anchor="center") 
            Label(self, text=self.pagelabel2,font=("Times", 12), bg='#41B77F', fg='white').place(relx=.5, rely=.3, anchor="e")
            self.vName = StringVar()
            Entry(self, textvariable=self.vName , width=30).place(relx=.5, rely=.3, anchor="w")
            Label(self, text=self.pagelabel3, font=("Times", 12), bg='#41B77F', fg='white').place(relx=.5, rely=.35, anchor="e")
            self.vAge = IntVar()
            self.vAge.set(10)
            Spinbox(self, from_=10, to=99, textvariable=self.vAge).place(relx=.5, rely=.35, anchor="w")
            Label(self, text=self.pagelabel4, font=("Times", 12), bg='#41B77F', fg='white').place(relx=.5, rely=.4, anchor="e")
            self.vHeight = IntVar()
            self.vHeight.set(10)
            Spinbox(self, from_=10, to=99, textvariable=self.vHeight).place(relx=.5, rely=.4, anchor="w")
            Label(self, text=self.pagelabel5,font=("Times", 12), bg='#41B77F', fg='white').place(relx=.5, rely=.45, anchor="e")
            self.weight = IntVar()
            Scale(self, variable= self.weight, from_=10, to=130,orient='horizontal', bg='#41B77F', fg='white').place(relx=.5, rely=.45, anchor="w")
            Label(self, text=self.pagelabel6, font=("Times", 12),bg='#41B77F', fg='white').place(relx=.5, rely=.5, anchor="e")
            self.sexe_var = IntVar()
            self.sexe_var.set(0)
            Radiobutton(self, text="Femme", variable= self.sexe_var, value=0,bg='#41B77F').place(relx=.5, rely=.5, anchor="w")
            Radiobutton(self, text="Homme", variable= self.sexe_var, value=1,bg='#41B77F').place(relx=.6, rely=.5, anchor="w")
           
            Label(self, text=self.pagelabel7,font=("Times", 12), bg='#41B77F', fg='white').place(relx=.5, rely=.55, anchor="e")
            self.corpulence_var = IntVar()
            self.corpulence_var.set(3)
            Radiobutton(self, text=" Fine  ", variable=self.corpulence_var,value=1, bg='#41B77F').place(relx=.5, rely=.55, anchor="w")
            Radiobutton(self, text="Normal ",variable=self.corpulence_var,value=2, bg='#41B77F').place(relx=.55, rely=.55, anchor="w")
            Radiobutton(self, text=" Large ",variable=self.corpulence_var,value=3, bg='#41B77F').place(relx=.6, rely=.55, anchor="w")
            Button(self, text=self.pagelabel8, width=10,height=2, font=("Times", 10), bg='white',
                 fg='#41B77F', command=self.ThirdPage).place(relx=.5, rely=.65, anchor="center")
            pass
    def ThirdPage(self):
        self.calculate_imc()
        self.ClearFrame()        
        if self.corpulence_var.get() == 1:
            self.pin = (self.vHeight.get() - 100 + self.vAge.get() / 10) * 0.9
            print("pin :"+ str(self.pin))  
            pin_var = IntVar()
            pin_var.set(self.pin)
            pass
        elif self.corpulence_var.get() == 3:  
            self.pin = (self.vHeight.get() - 100 + self.vAge.get() / 10) * 0.9 * 0.9
            pin_var = IntVar()
            pin_var.set(self.pin)           
            pass
        else:
            self.pin = (self.vHeight.get() - 100 + self.vAge.get() / 10) * 0.9
            pin_var = IntVar()
            pin_var.set(round(self.pin,2))
            pass
        Label(self, text=self.pagelabel9+" "+self.vName.get().upper(),font=("Times", 40), bg='#41B77F', fg='white').place(relx=.5, rely=.1, anchor="center")
#         You Ideal Weight
        pin_texte = Label(self, text=self.pagelabel11,font=("Times", 20), bg='#41B77F', fg='white').place(relx=.3, rely=.2, anchor="e")
        pin_texte2 = Label(self, textvariable=pin_var,font=("Times", 20), bg='#41B77F', fg='white').place(relx=.3, rely=.2, anchor="w")            
#         AMI
        imc = IntVar()
        imc.set(self.imc_var)
        Label(self, text=self.pagelabel10,font=("Times", 20), bg='#41B77F', fg='white').place(relx=.6, rely=.2, anchor="e")
        Label(self, textvariable=imc, font=("Times", 20), bg='#41B77F', fg='white').place(relx=.6, rely=.2, anchor="w")
#         MG (%) = (1.20 * BMI) + (0.23 * Age) - (10.8 * Sex) - 5.4
        self.mg =round((1.20 * self.imc_var) + (0.23 * self.vAge.get()) - (10.8 * int(self.sexe_var.get())) - 5.4,2)
        print(self.mg)
        mg = IntVar()
        mg.set(self.mg)
        Label(self, text="MG :",font=("Times", 20), bg='#41B77F', fg='white').place(relx=.3, rely=.3, anchor="e")
        Label(self, textvariable=mg, font=("Times", 20), bg='#41B77F', fg='white').place(relx=.3, rely=.3, anchor="w")
#         S = (Size ^ 0.725) * (Weight ^ 0.425) * 0.202) then MR = 24 = 35 * 40 * S 
        self.MR = (self.vHeight.get() ** 0.725) * ((self.weight.get() ** 0.425) * 0.202) * 37.5 * 24
        print(self.MR)
        mr = IntVar()
        mr.set(round(self.MR,2))
        Label(self, text="MR :",font=("Times", 20), bg='#41B77F', fg='white').place(relx=.6, rely=.3, anchor="e")
        Label(self, textvariable=mr, font=("Times", 20), bg='#41B77F', fg='white').place(relx=.6, rely=.3, anchor="w")
        Button(self, text="Back", width=10,height=2, font=("Times", 10), bg='white',
                 fg='#41B77F', command=self.SecondPage).place(relx=.1, rely=.8, anchor="w")
        

        pass
    def calculate_imc(self):
        print("Weight :"+ str(self.weight.get()))
        print("Height :"+ str(self.vHeight.get()))  
        print("vAge :"+ str(self.vAge.get()))  
        print("sexe_var :"+ str(self.sexe_var.get()))
        self.imc_var = round(self.weight.get() / ((self.vHeight.get() / 100)**2),2)
        print("imc_var :"+ str(self.imc_var)) 
        pass

def main():
    root = Tk()
    ex = Contact_manager(root)
    root.geometry('1080x720+400+150')
    root.mainloop()

if __name__ == '__main__':
    main()


# In[ ]:




