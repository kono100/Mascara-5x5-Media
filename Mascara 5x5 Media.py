import cv2
import numpy as np

def filtro_suavizacao_media(imagem):
    # Criar a máscara de convolução 3x3 para suavização por média
    mascara = np.ones((5, 5), np.float32) / 25

    # Aplicar o filtro de convolução na imagem
    imagem_suavizada = cv2.filter2D(imagem, -1, mascara)

    return imagem_suavizada

# Carregar a imagem
imagem = cv2.imread('C:/Users/User/Downloads/Original.jpg')

# Aplicar o filtro de suavização por média local
imagem_suavizada = filtro_suavizacao_media(imagem)

# Exibir a imagem original e a imagem suavizada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Suavizada', imagem_suavizada)
cv2.waitKey(0)
cv2.destroyAllWindows()

