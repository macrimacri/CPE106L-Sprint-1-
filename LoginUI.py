import tkinter as tk
import Login
class UI():
    def __init__(self):
        #window creation
        self.window = tk.Tk(className= 'Netflix Titles')
        self.window.resizable(width=False, height=False) 
        #frame creation
        self.frame1 = tk.Frame(master=self.window, width=800, height=500, bg="light green")
        self.frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand = False)
        self.frame1.pack_propagate(False) 
        #Welcome text creation
        self.welcome_Text = tk.Label(self.frame1, text="WELCOME TO NETFLIX TITLES", font=("Bahnschrift Light SemiCondensed", 30), bg= "Light green")
        self.welcome_Text.place(relx = 0.5, rely = 0.20, anchor ='center') 
        #Username, textbox creation and input
        self.name = tk.StringVar()
        self.userName_label = tk.Label(self.frame1, text="Username:",font= ("Bahnschrift Light SemiCondensed", 15), bg="light green")
        self.userName_textbox = tk.Entry(self.frame1, width= 15, font="Arial", textvariable= self.name)

        self.userName_label.place(relx = 0.35, rely = 0.40, anchor= 'center')
        self.userName_textbox.place(relx = 0.55, rely = 0.40, anchor ='center') 
        #Upassword, textbox creation and input
        self.password = tk.StringVar()
        self.password_label = tk.Label(self.frame1, text="Password:",font= ("Bahnschrift Light SemiCondensed", 15), bg="light green")
        self.password_textbox = tk.Entry(self.frame1, width= 15, font="Arial", textvariable=self.password, show = '*') 

        self.password_label.place(relx = 0.35, rely = 0.50, anchor= 'center')
        self.password_textbox.place(relx = 0.55, rely = 0.50, anchor ='center') 
    #button
        self.button = tk.Button(self.frame1, text = "Login Here!", font = ("Bahnschrift Light SemiCondensed", 15), command = lambda : self.login_button())
        self.button.place(relx = 0.50, rely = 0.70, anchor ='center') 
        self.window.mainloop()

    def login_button(self):
        person = Login.User()
        person.set_username(self.userName_textbox.get())
        person.set_password(self.password_textbox.get())

        self.result1_label = tk.Label(self.frame1, text="Login Sucessful", font= ("Bahnschrift Light SemiCondensed", 15), bg="light green")
        #self.result2_label = tk.Label(self.frame1, text="Login Failed", font= ("Bahnschrift Light SemiCondensed", 15), bg="light green")

        if(person.verifyLogin() == True):
            self.result1_label = tk.Label(self.frame1, text="Login Sucessful", font= ("Bahnschrift Light SemiCondensed", 15), bg="light green")
            self.result1_label.place(relx = 0.50, rely = 0.90, anchor ='center')
        else:

            self.result1_label.configure(text= "  Login Failed   ")
            self.result1_label.place(relx = 0.50, rely = 0.90, anchor ='center')
            
app = UI()


