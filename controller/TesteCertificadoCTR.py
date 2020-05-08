import os
from os import getcwd
from sys import path, platform
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

path.extend(['/'.join(getcwd().split('/')[0:-4])])

from controller.CertificadoCTR import CertificadoCTR


#corrigindo o contra barra do path
#path.extend(['/'.join(getcwd().split('/')[0:-4])])

win_width = 800
win_height = 600
'''def gps_open():
    tk.messagebox.showinfo("Mosquito", "Gps Open")
'''
class LendoCertificado (tk.Tk):

    def __init__(self, master=None):
        #inicializa os objetos na tela
        tk.Tk.__init__(self, master)
        self.master = master
        self.initialize()

    def initialize(self):
        #path = 'C:/Users/0327470/Documents/Yan/Reg_Cert/'
        #load = Image.open(path + "logo.jpg")
       # render = ImageTk.PhotoImage(load)
        #img = tk.Label(self, image=render)
        #img.image = render
       # img.place(x=300, y=200)
        # Criação do menu de opções
        top = self.winfo_toplevel()
        self.menuBar = tk.Menu(top)
        file = tk.Menu(self.menuBar, tearoff=0)
        file.add_command(label="Open", command=self.clicked)
        file.add_command(label="Exit", command=self.quit)
        self.menuBar.add_cascade(label="File", menu=file)
        top.config(menu=self.menuBar)
        # cliação do label para verificar o arquivo escolhido
        # cliar um grid para colocar os objetos
        self.grid()
        # Criando um botao para submeter o arquivo
        self.btn = tk.Button(self, text="Analisar ", command=self.run)
        self.btn.configure(width=10, height=1, font=("calibri", 10, "bold"))
        # self.btn.map( foreground = [('active', '! disabled', 'green')], background = [('active', 'black')])
        # self.btn.grid(column=0,row=1,padx=20)
        self.btn.grid(column=0, row=1, padx=20,pady=10)

        # Gps button
        '''self.gpsbutton = tk.Button(self, text="Open gps", command=gps_open)
        self.gpsbutton.configure(width=10, height=1, font=("calibri", 10, "bold"))
        # self.gpsbutton.grid(column=1,row=1, pady=5)
        self.gpsbutton.grid(column=0, row=2, pady=20,padx=20)
'''
    #função para enviar o path do arquivo formato xlsx
    def clicked(self): 
        
         # app.withdraw()
        filename = tk.filedialog.askdirectory(title='Select Folder')
        #variavel que armazena o diretorio do arquivo para ser enviado
        self.data = filename
        #print(self.data)
        self.label_file = tk.Label(self, wraplength=win_width,text=filename)
        self.label_file.configure(relief="ridge", font="Arial 10 bold", border=1, background="white")
        self.label_file.grid(column=0, row=0)
        self.label_file["text"] = filename


    def run(self):
        # escrever codigo para ver a existencia do video
        #try:
        print(self.data)
        is_exists = os.path.exists(self.data)
        print(is_exists)
        if os.path.exists(self.data):
             
            
            cl1 = CertificadoCTR(str(self.data)+'/','sonopique5') 
            cl1.dicio()
            

if __name__ == "__main__":
    app = LendoCertificado(None)
    app.title("Registro Certificado")
    app.geometry("{}x{}".format(win_width,win_height))
    app.mainloop()