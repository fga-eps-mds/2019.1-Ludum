# Tutorial Jogo Snake 

# 1 - fazendo imports    

<p  align="justify">&emsp;&emsp;O primeiro passo para criar o jogo e fazermos os imports das bibliotecas necessárias, que nesse caso é a PyGame e a Random. Portanto, em código temos:</p>

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