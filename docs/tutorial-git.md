# Tutorial de como contribuir utilizando o Git

**Importante:** este tutorial utiliza linhas de comando no terminal do Linux/macOS ou prompt de comando do Windows. Há alternativas de interfaces gráficas para utilização git, mas não serão abordadas nesse tutorial.
1) Para clonar o repositório, utilize o seguinte comando no terminal do Linux/macOS ou prompt de comando do Windows dentro de uma pasta de sua preferência
```bash
git clone https://github.com/fga-eps-mds/2019.1-Grupo-8
```
Algo parecido com isto será apresentado no seu terminal caso processo de clone for bem sucedido:
![clone](https://i.imgur.com/DyUXnHH.png)

2) Ainda dentro do mesmo terminal, navegue até a pasta do repositório que você clonou utilizando o comando:
```bash
cd 2019.1-Grupo-8/
``` 

3) Utilizaremos o git flow, trabalhando com **branches**, portanto, após clonar o repositório, deve-se verificar em qual branch você está. Para isso, execute o comando:
```bash
git branch
```
![branch](https://i.imgur.com/uNb7vvp.png)
o asterisco representa em qual branch o seu repositório local está. Para visualizar todas as branches que há no repositório, deve-se executar o comando:
```bash
git branch --all
```
![branch--all](https://i.imgur.com/VB37TnT.png)
Para trocar de branch, deve-se utilizar o comando
```bash
git checkout nome-da-branch
```
![checkout](https://i.imgur.com/WnxhN2r.png)
Para CRIAR uma branch nova, deve-se executar o comando:
```bash
git checkout -b nome-da-nova-branch
```
![checkout-b](https://i.imgur.com/tgPR3EJ.png)

4) Para realizar as suas modificações, deve-se utilizar o editor de texto [Visual Studio Code](https://code.visualstudio.com/). Após baixar e instalar o software, pode-se abrir o diretório que o seu terminal está situado utilizando a seguinte linha de comando:
```bash 
code .
```
ou então pode-se abrir o diretório direto no Visual Studio Code da seguinte forma:

* Na barra superior do Visual Studio Code, navegue até a opção 'File'e depois até a opção 'Open'.]; 
![code1](https://i.imgur.com/hcDcSvN.png)

* Na janela que será aberta, selecione a pasta que você quer abrir no editor de texto (no nosso caso, será a pasta do projeto. 2019.1-Grupo-8):
![code2](https://i.imgur.com/RlmULgf.png)

* Na barra lateral aparecerá as pastas e arquivos do diretório aberto:
![code3](https://i.imgur.com/7sOakuv.png)

5) Após modificar os arquivos desejados, volte ao terminal anteriormente aberto na pasta do projeto e digite:
```bash
git status
```
no terminal, aparecerá os arquivos que você modificou:
![git-status](https://i.imgur.com/IGE9afJ.png)
no caso do exemplo da imagem, o arquivo contribuindo.md situado na pasta docs foi modificado. O próximo passo é adicionar os arquivos modificados ao seu index.

6) Para adicionar os arquivos, deve-se utilizar o seguinte comando no terminal:
```bash
git add nome-do-arquivo
```
no caso do exemplo utilizado neste tutorial, adicionaremos o arquivo docs/contribuindo.md:
```bash
git add docs/contribuindo.md
```
e em seguida daremos novamente o comando
```bash
git status
```
para conferir se o arquivo desejado foi adicionado corretamente:
![add](https://i.imgur.com/uVJIfUG.png)
como o arquivo apareceu na cor verde no terminal, significa que foi adicionado corretamente ao seu index local.

**Observação 1:** ao longo do projeto poderá ser realizadas várias mudanças em diferentes arquivos, então há um comando que adiciona todos os arquivos modificados de uma vez:
```bash
git add .
```

**Observação 2:** caso você tenha adicionado um arquivo por engano NESTE PASSO, basta executar o seguinte comando para remover o arquivo do index:
```bash
git reset nome-do-arquivo
```
![reset](https://i.imgur.com/SG2UUbO.png)

7) O próximo passo é enviar as mudanças para o repositório local utilizando o comando:
```bash
git commit -m "descrição do commit"
```
![commit](https://i.imgur.com/cKeB3bn.png)

8) O último passo é enviar o seu commit para o repositório remoto. Para isso, utilize o comando:
```bash 
git push
```

## Dicas Úteis:
* SEMPRE execute o comando 
```bash
git pull
```
em seus repositórios locais. Este comando pega as últimas mudanças que outros membros do time subiram no git e diminui a chance de haver conflitos nos arquivos. Por exemplo: você criou uma nova branch chamada 'bug/01' com base na branch 'development'. Enquanto você realizava a correção do bug, outro membro do time atualizou o conteúdo da branch 'development'. Então, para realizar um pull request com as suas modificações, você deve atualizar a branch 'bug/01' com as atualizações da branch 'development'. Para isso, execute o comando:
```bash
git pull origin development
``` 
e sua branch será atualizada. Caso os arquivos que você tiver mexido for os mesmos arquivos que a pessoa que atualizou a branch 'development' também mexeu, haverá um CONFLITO:
![conflito](https://i.imgur.com/WvhfgCI.png)
a imagem acima ilustra uma situação de conflito no arquivo README.md após tentar atualizar o conteúdio da nova branch com o conteúdo da branch 'master'. Para resolver este conflito, digite no terminal
```bash
code .
```
Será aberta uma janela com os arquivos do diretório no Visual Studio Code:
![merge](https://i.imgur.com/8Anog2f.png)
em que na barra lateral (onde a seta número 1 está apontando), na cor roxa, será representado o arquivo (ou arquivos) em que existe conflito. A seta número 2 representa as mudanças que VOCÊ fez, enquanto a seta 3 representa as mudanças que estão na branch em que você está tentando "puxar" a atualização.
No local que a seta 2 está apontando há três botões:
* **Accept Current Change:** aceita a mudança que você fez na sua branch;
* **Accept Incoming Change:** aceita a mudança que está na branch que você está "puxando as atualizações";
* **Accept Both Changes:** aceita as duas mudanças, colocando uma linha embaixo da outra;
* **Compare Changes:** coloca as duas linhas de conflito para serem comparadas.  

Após selecionar qual opção melhor te atende, deve-se proceder conforme o passo 5 do presente tutorial.