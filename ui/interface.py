from customtkinter import *
from PIL import Image

class StudentTaskPlanner():
    def __init__(self):
        self.app = CTk()
        self.app.geometry("1024x900")
        self.app.title("Studente Task Planner")

        self.splash_screen=CTkFrame(self.app, fg_color="#ADD8E6")
        self.splash_screen.pack(fill="both", expand=True)

        img_logo = CTkImage(light_image=Image.open("logo.png"), dark_image=Image.open("logo.png"), 
                        size=(500, 500))
        
        logo_label = CTkLabel(self.splash_screen, text="", image=img_logo)
        logo_label.pack(expand=True)

        text_logo=CTkLabel(self.splash_screen,font=("Arial", 18, "bold"), text="A carregar todas dependencias...")
        text_logo.pack(pady=90)

        self.app.after(3000, self.pagina_principal)

    def criar_cabecalho(self, frame):
        self.frame_title=CTkFrame(frame, fg_color="transparent")
        self.frame_title.pack(fill="x")
        self.logo= CTkImage(light_image=Image.open("ui/logo.png"), size=(100, 100))
        self.logo_title =CTkLabel(self.frame_title, text="", image=self.logo)
        self.logo_title.grid(row=0, column=0)
        self.title=CTkLabel(self.frame_title, text="Student Task Planner",
                             font=("arial", 28, "bold"))
        self.title.grid(row=0, column=1)

    def pagina_principal(self):
        self.splash_screen.pack_forget()
        self.frame1=CTkFrame(self.app, fg_color="#ADD8E6")
        self.frame1.pack(fill="both", expand=True)

        self.criar_cabecalho(self.frame1)



        frame_content=CTkFrame(self.frame1, fg_color="transparent")
        frame_content.pack(fill="both", expand=True)

        btn1 = CTkButton(frame_content, )
        btn1.grid()

        








    def executar(self):
        self.app.mainloop()
