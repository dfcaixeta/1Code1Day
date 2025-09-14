''' Projeto OneCodeOneDay
Script em Python que envia notificação (mensagem)
Dia XX - 03.ago.2025

Obs.: Precisa da instalação das bibliotecas rembg e pillow
> pip install plyer

@utor: @pythonclcoding '''

# Importando a biblioteca
from plyer import notification

# Enviando a mensagem de notificação
notification.notify(
    title = 'Lembrete', # Titulo do Lembrete
    message = 'Faça uma pausa e alongue-se!', # Mensagem
    app_name = 'Notificador Python',
    timeout = 10 # Tempo de duração da mensagem.
)

# EOF
# source code --> clcoding.com