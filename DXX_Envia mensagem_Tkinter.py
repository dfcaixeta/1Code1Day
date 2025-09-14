''' Projeto OneCodeOneDay
Script com GUI Tkinter em Python que envia notificação (mensagem)
Dia XX - 03.ago.2025

Obs.: Precisa da instalação das bibliotecas rembg e pillow
> pip install tkinter

@utor: @pythonclcoding '''

# Importando a biblioteca
import tkinter as tk

# Enviando a mensagem de notificação
root = tk.Tk()

# Insere o rótulo, o texto, a fonte e a cor do texto
tk.Label(root, text = 'Feliz aniversário!', font = ('Helvetica', 14), fg = 'green').pack()

# Inicia o loop principal da janela
root.mainloop()

# EOF
# source code --> clcoding.com