# Tutorial de como criar o jogo Pong

## 1 - Primeiramente, a criação da tela de fundo

```bash
Neste código abaixo, estamos primeiramente importando a pygame, definindo as cores, para então criar a tela com tamanho e nome
```
![tela1](./imagens/imagens_pong/tela1_codigo.png)1.1

```bash
Após isso, definimos que a tela só possa ser fechada, se o jogador fechar o programa
```
![tela2](./imagens/imagens_pong/tela2_codigo.png)1.2

### Este será o resultado
![tela3](./imagens/imagens_pong/tela_imagem.png)1.3

## 2 - Agora vamos fazer a raquete

```bash
Primeiro, vamos definir abaixo da criação da tela[1.1], as coordenadas da raquete com "rect", criar a raquete e já definir que ela não pode sair da tela
```
![raquete1](./imagens/imagens_pong/raquete1_codigo.png)2.1

```bash
Então mostraremos a raquete na tela
```
![raquete2](./imagens/imagens_pong/raquete2_codigo.png)2.2

### Este será o resultado
![raquete3](./imagens/imagens_pong/raquete_imagem.png)2.3

## 3 - Vamos criar a bola

```bash
Primeiramente, vamos criar coordenadas iniciais quaisquer para a bolinha
```
![bola1](./imagens/imagens_pong/bola1_codigo.png)3.1

```bash
Agora, vamos desenhar a bolinha na tela
```
![bola2](./imagens/imagens_pong/bola2_codigo.png)3.2

### Este será o resultado
![bola3](./imagens/imagens_pong/bola_imagem.png)3.3

## 4 - Vamos adicionar movimento à raquete

```bash
Começamos adicionando as coordenadas que alteraremos para movimentar a raquete
```
![mov_raquete](./imagens/imagens_pong/mov_raquete_2_codigo.png)4.1
 
 ```bash
Agora vamos adicionar movimento à raquete, fazendo com que as setas para direita e esquerda controlem a raquete
```
![mov_raquete2](./imagens/imagens_pong/mov_raquete_1_codigo.png)4.2

### Este será o resultado
![mov_raquete3](./imagens/imagens_pong/mov_raquete.png)4.3

## 5 - Agora adicionaremos movimento à bolinha

```bash
Começaremos adicionando as coordenadas que usaremos para dar movimento à bolinha
`````

![mov_bolinha1](./imagens/imagens_pong/mov_bola2_codigo.png)5.1

```bash
Agora iremos mudar as coordenadas da bolinha para dar movimento a ela, já estabelecendo os limites da tela
````

![mov_bolinha2](./imagens/imagens_pong/mov_bola1_codigo.png)5.2

### Este será o resultado
![mov_bolinha2](./imagens/imagens_pong/mov_bola_imagem.png)5.3


## 6 - Agora adicionaremos a biblioteca pygame para evitar erros no próximo passo

```bash
Primeiro vamos inicializar a biblioteca no começo do programa
````
![pygame1](./imagens/imagens_pong/pygame1.png)6.1s

```bash
Agora vamos fechar a biblioteca no final do programa
````
![pygame2](./imagens/imagens_pong/pygame2.png)6.2