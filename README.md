## Projeto Bimestral (Processamento Digital de Imagens - PDI )

Este repositório contém um projeto para aplicação de KMeans em imagens através da biblioteca OpenCV e Python. Após a aplicação do KMeans, é possível fazer a visualização de todos os centróides (clusters) gerados pelo KMeans, e compara-los com a imagem original, da mesma forma que escolher multiplas configurações de dimensões e centróides, para atingir o objetivo esperado.

## Sobre o trabalho:

* Disciplina: OP63I-CC8 - Processamento De Imagens E Reconhecimento De Padrões	
* Turma: 2023/2 - 8º Período
* Docente: Prof. Dr. Pedro Luiz de Paula Filho

## Recursos 
- **Escolha de Dimensões:** O usuário pode escolher a quantidade de dimensões que serão utilizadas pelo KMeans.
- **Escolha de Centróides:** O usuário pode escolher a quantidade de clusters que serão utilizadas pelo KMeans.
- **Aplicação do KMeans:** KMeans aplicado automáticamente na aplicação, apenas com as duas configurações necessárias anteriores.
- **Visualização de Centróides:** O usuário pode visualizar a imagem original ao lado de cada um dos centróides gerados pelo KMeans.

## Dependências
**Dependêndicas utilizadas:** Python 3, Numpy, OpenCV (cv2), PIL e TKInter.

### Para o Linux:  
`pip install numpy opencv-python tkinter pillow` 

### Para o Windows:
1. Python 3.11.5 ([Instalador 64-bit](https://www.python.org/downloads/windows/))
2. `pip install numpy opencv-python pillow` 

PS.: Não é necessário a instalação do TKinter no Windows, pois ele já vem incluso no Python.

## Como Utilizar
1. Clone o repositório do GitHub: `git clone https://github.com/thiagodalsanto/kmeans_app.git`
2. Instale as [dependências](#dependências) utilizadas
3. Execute o aplicativo em uma IDE, dentro da raiz do projeto, com o comando:
   1. Linux: `python3 main.py`
   2. Windows: `python main.py`

## Imagens da Aplicação
Imagem 1 - Imagem teste de um nadador, com aplicação do KMeans para 3 dimensões e 6 centróides. Com possibilidade de ver todos os centróides gerados.

<p align="center">
    <img src="https://i.imgur.com/I771txT.png" width="800">
</p>

Imagem 2 - Imagem com muitas cores, com aplicação da mesma configuração da imagem de teste, 3 dimensões e 6 centróides. Com possibilidade de ver todos os centróides gerados.
<p align="center">
    <img src="https://i.imgur.com/pZXfF8g.png" width="800">
</p>