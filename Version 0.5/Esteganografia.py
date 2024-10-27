import numpy as np
import cv2

# teste1 = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x06\x00\x00\x00\x06\x08\x02\x00\x00\x00o\xaex\x1f\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00\x00 IDAT\x18Wc\xf8\xff\xff?\x03\x03\n\t\x02\xe8\xa2\xe8|\x08@\x17E\xe7C\x00\x8a\xe8\xff\xff\x00\xfb\x115\xcb\x81\xeb\x14i\x00\x00\x00\x00IEND\xaeB`\x82'
# teste2 = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x02\x00\x00\x00\x02\x08\x02\x00\x00\x00\xfd\xd4\x9as\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00\x00\x11IDAT\x18Wc\x00\x82\xff\xff\xff\x831\x03\x03\x00)\xe4\x05\xfbnO\xf2\x7f\x00\x00\x00\x00IEND\xaeB`\x82'
# with open("teste.png","xb") as arq:
#   arq.write(teste1)

def esteganografar(imagem:str, texto:str, end=";"):
    '''Imagem = path da imagem no seu computador\n
    texto = texto que deseja esconder\n
    end = caracter q mostrará o final do texto'''

    try:
      # Lendo a Imagem
      img1 = cv2.imread(imagem)
      #print(img1)
      if img1 is None:
        raise FileNotFoundError("Não foi possível ler o arquivo. Verifique o caminho ou a integridade do arquivo.")

      # Formatando o Texto
      #texto = """Se você abre uma porta, você pode ou não entrar em uma nova sala. Você pode não entrar e ficar observando a vida. Mas se você vence a dúvida, o temor, e entra, dá um grande passo: nesta sala vive-se! Mas, também, tem um preço... São inúmeras outras portas que você descobre. Às vezes curte-se mil e uma. O grande segredo é saber quando e qual porta deve ser aberta. A vida não é rigorosa, ela propicia erros e acertos. Os erros podem ser transformados em acertos quando com eles se aprende. Não existe a segurança do acerto eterno.

      #A vida é generosa, a cada sala que se vive, descobre-se tantas outras portas. E a vida enriquece quem se arrisca a abrir novas portas. Ela privilegia quem descobre seus segredos e generosamente oferece afortunadas portas. Mas a vida também pode ser dura e severa. Se você não ultrapassar a porta, terá sempre a mesma porta pela frente. É a repetição perante a criação, é a monotonia monocromática perante a multiplicidade das cores, é a estagnação da vida... Para a vida, as portas não são obstáculos, mas diferentes passagens!"""
      texto += end

      # Pegando os Binarios do texto
      bina = []

      for i in texto.encode("utf-8"):
        bina.append(f"{i:08b}")
      #print(bina)

      # Pegando os Binarios da Imagem
      binarios = []
      for i in img1:
        for j in i:
          for num in j:
            binarios.append(f"{num:08b}")
      #print(binarios)

      # Separando os Binarios do Texto
      #print(bina)
      nbina = []
      for i in bina:
        for j in range(0,len(i),2):
          nbina.append(i[j]+i[j+1])
      #print(nbina)

      # Fazendo o Novo Código Binario da Imagem
      nbin = []
      num = 0
      for i in binarios:
        codigo = ""
        for j in range(0,len(i),2):
          if j>=6:
            try:
              codigo += nbina[num]
              num += 1
            except:
              codigo += i[j]+i[j+1]
          else:
            codigo += i[j]+i[j+1]
        nbin.append(codigo)
      #print(nbin)

      # Transformando em Imagem
      width = img1.shape[0]
      height = img1.shape[1]
      newBin = np.zeros((width, height, 3), np.uint8)
      cont = 0
      for i in range(width):
        for j in range(height):
          for l in range(3):
            newBin[i][j][l] = int(nbin[cont],2)
            cont += 1
      #print(newBin)
      ponto = imagem[::-1].find(".")+1
      nome_img = imagem[:len(imagem)-ponto]+"(1)"+imagem[len(imagem)-ponto:]
      #print(nome_img)
      cv2.imwrite(nome_img, newBin)
      return "Operação Concluida"
    except FileNotFoundError:
      return "","Arquivo não encontrado"
    except Exception:
      return "","Operação Falhou"
#esteganografar("tt_esteg.png","teste")

def desesteganografar(imagem, end=";"):
    # Ler a Imagem
    try:
      img1 = cv2.imread(imagem)

      if img1 is None:
        raise FileNotFoundError("Não foi possível ler o arquivo. Verifique o caminho ou a integridade do arquivo.")

      # Pegando os Binarios da Imagem
      binarios = []
      for i in img1:
        for j in i:
          for num in j:
            binarios.append(f"{num:08b}")
      #print(binarios)

      # Separando os Binarios da Imagem
      nbin = []
      #num = 0
      for i in binarios:
        codigo = ""
        for j in range(0,len(i),2):
          if j>=6:
            try:
              codigo += i[j]+i[j+1]
              #num += 1
            except:
              pass
        nbin.append(codigo)
      #print(nbin)

      # Juntando os Binarios Escondidos da Imagem
      bina = []
      codigo = ""
      cont = 0
      for i in nbin:
        if cont % 4 == 0:
          if codigo != "":bina.append(codigo)
          codigo = i
        else:
          codigo += i
        cont += 1
      #print(bina)

      # Tirando o texto da imagem
      texto = ""
      qtde = ""
      for i in bina:
        if chr(int(i,2)) == end:
          break
        texto += chr(int(i,2))
      return texto
    except FileNotFoundError:
      return "","Arquivo não encontrado"
    except Exception:
      return "","Operação Falhou"
