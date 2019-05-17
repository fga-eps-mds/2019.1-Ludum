# Tutorial Jogo Snake 

# 1 - fazendo imports  
## 1.1 imports
<p  align="justify">&emsp;&emsp;O primeiro passo para criar o jogo e fazermos os imports das bibliotecas necessárias, que nesse caso é a PyGame e a Random. Portanto, em código temos:</p>
<html>
<ul>
<li>  import pygame, sys</li>
<li>  from pygame.locals import *</li>
<li>  from random import randint </li>
</ul>
</html>

## 1.2 escolhendo cores

<p  align="justify">&emsp;&emsp;Nessa parte, definir as cores do jogo, que serão: Preto (<i>Black</i>), Azul (<i>Blue</i>) e Cinza (<i>Gray</i>), em código fica:</p>
<html>
<ul>
<li>  BLACK = (0,0,0)</li>
<li>  BLUE = (0,0,255)</li>
<li>  GRAY = (200,200,200)</li>
</ul>
</html>

## 1.3 escolhendo as direções

<p  align="justify">&emsp;&emsp;Nessa parte, definir as direções de controle do jogo, que serão: Cima (<i>Up</i>), Baixo (<i>Down</i>), Esquerda (<i>Left</i>) e Direita (<i>Right</i>) em código fica:</p>
<html>
<ul>
<li>  UP = 8</li>
<li>  DOWN = 2</li>
<li>  LEFT = 4</li>
<li>  RIGHT = 6</li>
</ul>
</html>

# 2 - Criando Classes do jogo

## 2.1 - Classe para inicializar o jogo

<p  align="justify">&emsp;&emsp;Nessa parte, vamos iniciar o nosso jogo. Para isso, vamos criar a <i>class game</i> em código temos:</p>
<p align="justify">class Game():</p>
    <p align="justify">"""Initialize pygame, window, background, font,...</p>
    """</p>

### 2.1.1 - função para iniciar o jogo
<p  align="justify">&emsp;&emsp;Nessa parte, vamos criar a função para inciar o jogo dentro da <i>class game</i></p>

<p align="justify">def __init__(self,width,height,fps):</p>
<p align="justify">&emsp;pygame.init()</p>
<p align="justify">&emsp;#Janela</p>
<p align="justify">&emsp;pygame.display.set_caption('Snake')</p>
<p align="justify">&emsp;self.width=width</p>
<p align="justify">&emsp;self.height=height</p>
<p align="justify">&emsp;self.screen=pygame.display.set_mode((self.width,self.height))</p>
<p align="justify">&emsp;#Criando fundo</p>
<p align="justify">&emsp;self.background=pygame.Surface(self.screen.get_size())</p>
<p align="justify">&emsp;#Pintar de Preto</p>
<p align="justify">&emsp;self.background.fill(BLACK)</p>
<p align="justify">&emsp;#Converter superficie</p>
<p align="justify">&emsp;self.background.convert()</p>
<p align="justify">&emsp;self.scorecard=pygame.draw.rect(self.background,BLUE,Rect([10,10],[self.width-20,100]),1)</p>
<p align="justify">&emsp;#Game area</p>
<p align="justify">&emsp;self.gamearea=pygame.draw.rect(self.background,BLUE,Rect([10,120],[self.width-20,380]),1)</p>
<p align="justify">&emsp;self.points=0</p>
<p align="justify">&emsp;#Score</p>
<p align="justify">&emsp;self.font=pygame.font.Font(None,36)</p>
<p align="justify">&emsp;self.mainClock=pygame.time.Clock()</p>
<p align="justify">&emsp;self.fps=fps</p>
<p align="justify">&emsp;self.snake=Snake()</p>
<p align="justify">&emsp;self.food=Food(self.snake)</p>
</p>

### 2.1.2 - função run
<p align="justify">Agora, vamos criar a função para o jogo funcionar:</p>

