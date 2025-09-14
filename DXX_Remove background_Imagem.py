''' Projeto OneCodeOneDay
Programa em Python que remove o background (fundo) de uma imagem
Dia XX - 03.ago.2025

Obs.: Precisa da instalação das bibliotecas rembg e pillow
> pip install rembg pillow

@utor: @pythonclcoding '''

# Importando as bibliotecas
from rembg import remove
from PIL import Image

# Entrada/Input de dados
input_path = 'Imagens/foto.jpg'
output_path = 'Imagens/saida1.png' # Use .png para preservar a transparência

# Abre a imagem de entrada
img = Image.open(input_path)

# Remove o fundo
output = remove(img)

# Salva a imagem com o fundo (background) removido (formato PNG é recomendado)
output.save(output_path)

# Abre a imagem resultado (opcional: para exibição ou verificação)
img_result = Image.open(output_path)
img_result.show()

# EOF
# source code --> clcoding.com