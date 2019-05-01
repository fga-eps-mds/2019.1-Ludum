[1. Introdução](#1-Introdução)   
[2. Uma Consistência Tosca é o Bicho-Papão das Pequenas Mentes](#2-uma-consistência-tosca-é-o-bicho-papão-das-Pequenas-Mentes)    
[3. Formatação do Código](#3-formatação-do-código)    
[4. Comentários](#4-comentários)    
[5. Docstrings](#5-docstrings)     
[6. Nomes e Identificadores](#6-nomes-e-identificadores)   
[7. Recomendações ao Programar](#7-recomendações-ao-programar)    


------------------------------------------------------------------------
## 1. Introdução
<p  align="justify">Este documento oferece convenções para o código Python compreendido pela biblioteca padrão que acompanha a distribuição. Há outro documento semelhante 1 que trata do estilo para o código em C usado na implementação do interpretador e nas extensões que compõe a biblioteca padrão.</p>

<p  align="justify">O conteúdo deste documento é uma adaptação do artigo original Python Style Guide, de GuidoVanRossum, com alguns acréscimos retirados do guia de estilo de Barry Warsaw. Onde houve conflitos, as regras de GvR foram mantidas.</p>

## 2. Uma Consistência Tosca é o Bicho-Papão das Pequenas Mentes
<p  align="justify">O propósito de um guia de estilo é manter a consistência. Consistência em relação a esse guia é importante. Consistência em relação a outros detalhes de um projeto é mais importante. Consistência em relação a um módulo ou função é ainda mais importante.</p>

<p  align="justify">Mais importante ainda: saiba quando ser inconsistente - algumas vezes, as regras deste guia simplesmente não se aplicam. Em caso de dúvida, use seu melhor julgamento. veja outros exemplos e decida o que fica melhor. E não hesite em perguntar!</p>

Duas boas razões para quebrar uma regra:

* <p  align="justify">Quando a adoção de uma regra irá tornar o código menos legível, mesmo para alguém acostumado com essas regras.</p>
* <p  align="justify">Quando deseja-se ser consistente com outro código que acompanhe aquele em desenvolvimento que também viola as regras - apesar dessa ser uma boa oportunidade para consertar a bagunça de alguém.</p> 

## 3. Formatação do Código
* Indentação

<p  align="justify">Use o padrão usado pelo "Python-mode" do Emacs: 4 espaços por nível de indentação. Para código realmente antigo que você não quer bagunçar, você pode continuar a usar 8 espaços. O Python-mode automaticamente detecta o nível de indentação predominante em um arquivo e segue este padrão.</p> 

**Não Recomendado:**
```py
# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

**Recomendado:**
```py
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```
A regra dos 4-espaços é opcional para continuação de linhas.

Opcional:
```py
# Hanging indents *may* be indented to other than 4 spaces.
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)
```
<p  align="justify">Quando a parte condicional de uma instrução if é longa o suficiente para exigir que seja escrita em várias linhas, vale a pena observar que a combinação de uma palavra-chave de dois caracteres (mais um espaço, mais um parêntese de abertura cria um travessão 4-espaço para as linhas subsequentes do condicional de várias linhas. Isso pode produzir um conflito visual com o conjunto de código indentado aninhado dentro da instrução if, que também seria naturalmente indentado em 4 espaços. Esse PEP não tem uma posição explícita sobre como (ou se) distinguir visualmente essas linhas condicionais do conjunto aninhado dentro da instrução if. Opções aceitáveis nesta situação incluem, mas não estão limitadas a:</p>

```py
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```
<p  align="justify">A chave de fechamento / colchete / parênteses em construções de múltiplas linhas pode se alinhar sob o primeiro caractere que não é espaço em branco da última linha da lista, como em:</p>

```py
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```
<p  align="justify">ou pode ser alinhados sob o primeiro caractere da linha que começa a construção de várias linhas, como em:</p>

```py
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

* Tabulações ou espaços

<p  align="justify">Nunca misture tabulações e espaços. A forma mais popular de indentar código em Python é somente com espaços. A segunda forma mais popular é somente com tabulações. Código com uma mistura dos dois deve ser convertido para usar somente espaços. (No Emacs, selecione o buffer inteiro e digite ESC-x untabify). Passando a opção -t para o interpretador Python, faz com que ele emita avisos sobre código que misture ilegalmente tabulações e espaços. Com -tt esses avisos se tornam erros. Essas opções são altamente recomendadas! Para projetos novos, recomenda-se usar somente espaços. Muitos editores têm opções para tornar isso mais fácil.</p>

* Comprimento máximo de linhas

<p  align="justify">Ainda há por aí muitos monitores limitados a linhas de 80 colunas (além disso, limitando as janelas a 80 caracteres, permite ter várias janelas abertas, lado a lado). As quebras de linha padrão nesses monitores é horrível, portante, limite todas as linhas a um máximo de 79 caracteres. (o Emacs quebra as linhas que têm exatamente 80 caracteres). Para longos blocos de texto (docstrings ou comentários), limitar o comprimento a 72 colunas é recomendado.</p>

<p  align="justify">A melhor maneira de continuar linhas longas é usando a continuação implícita, entre parênteses, colchetes e chaves. Se necessário, você pode adicionar um par extra de parênteses em volta de uma expressão, mas, às vezes, uma barra invertida fica melhor. Tome o cuidado de indentar a linha adequadamente. O Python-mode do Emacs faz isso automaticamente. Exemplo:</p> 

```py
    class Rectangle(Blob):

        def __init__(self, width, height,
                     color='black', emphasis=None, highlight=0):
            if width == 0 and height == 0 and \
               color == 'red' and emphasis == 'strong' or \
               highlight > 100:
                raise ValueError, "sorry, you lose"
            if width == 0 and height == 0 and (color == 'red' or
                                               emphasis is None):
                raise ValueError, "I don't think so"
            Blob.__init__(self, width, height,
                          color, emphasis, highlight)
```
* <p  align="justify">Se uma quebra de linha antes ou depois de um operador binário?</p> 

    <p  align="justify">Durante décadas, o estilo recomendado era quebrar depois dos operadores binários. Mas isso pode prejudicar a legibilidade de duas maneiras: os operadores tendem a se espalhar por colunas diferentes na tela, e cada operador é movido para longe de seu operando e para a linha anterior. Aqui, o olho tem que fazer um trabalho extra para dizer quais itens são adicionados e quais são subtraídos:</p>

    ```py
    # No: operators sit far away from their operands
    income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
    ```
    <p  align="justify">Para resolver esse problema de legibilidade, os matemáticos e seus editores seguem a convenção oposta. Donald Knuth explica a regra tradicional em sua série Computers and Typesetting: "Embora as fórmulas dentro de um parágrafo sempre quebre após as operações e relações binárias, as fórmulas exibidas sempre se quebram antes das operações binárias".</p>

    <p  align="justify">Seguir a tradição da matemática geralmente resulta em um código mais legível:</p>

    ```py
    # Yes: easy to match operators with operands
    income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
    ```
    <p  align="justify">No código Python, é permitido interromper antes ou depois de um operador binário, desde que a convenção seja consistente localmente. Para o novo código, o estilo de Knuth é sugerido.</p>

* Linhas em branco

    <p  align="justify">Separe funções e definições de classe com duas linhas em branco. Métodos dentro de uma classe devem ser separados com uma única linha em branco. Linhas extras podem ser usadas (esporadicamente) para separar grupos de funções relacionadas e podem ser omitidas entre grupos relacionados de linhas, como por exemplo, métodos que sejam sobrescritas em subclasses. Quando linhas em branco são usadas para separar métodos, deve haver também uma linha em branco entre a linha 'class' e o primeiro método da classe. Use linhas em branco para separar blocos lógicos dentro de métodos e funções. Python aceita o caractere control-L (^L) como espaço em branco; o Emacs (e algumas ferramentas de impressão) tratam esses caracteres como quebra de página, então você pode usá-los para separar páginas de seções relacionadas no seu arquivo.</p>

* Import

    <p  align="justify">Imports devem sempre ser feitos em linhas separadas, por exemplo:</p> 

**Não Recomendado**
```py
import sys, os
```

**Recomendado**
```py
import sys
import os
```
Mas não há problema algum em usar: 
```py
from types import StringType, ListType
```

* <p  align="justify">Imports devem ser sempre colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings, e antes de constantes ou globais. Eles devem ser agrupados seguindo a ordem:</p> 


1. <p  align="justify">módulos da biblioteca padrão</p> 
2. <p  align="justify">módulos grandes relacionados entre si (por exemplo, todos os módulos de e-mail usados pela aplicação)</p> 
3. <p  align="justify">módulos específicos da aplicação</p>  

    <p  align="justify">Você deve colocar uma linha em branco separando cada grupo de módulos.</p> 

* <p  align="justify">Quando importar uma classe de um módulo de mesmo nome, não há problemas em usar:</p> 

```py
from MyClass import MyClass
from foo.bar.YourClass import YourClass
```
No entanto, se isso causar conflitos com nomes, use: 
```py
import MyClass
import foo.bar.YourClass
```
e depois "MyClass.MyClass" e "foo.bar.YourClass.YourClass". 

* Espaços em expressões e instruções

    Guido odeia espaços nos seguintes lugares:
    * Imediatamente antes e após parêntese, colchete ou chave, como em: 
    ```py
    spam( ham[ 1 ], { eggs: 2 } )
    ```
    Sempre escreva assim: 
    ```py
    spam(ham[1], {eggs: 2})
    ```

* Logo antes de uma vírgula, ponto-e-vírgula ou dois-pontos: 
```py
if x == 4 : print x , y ; x , y = y , x
```
Sempre escreva assim: 
```py
if x == 4: print x, y; x, y = y, x
```

* Entre uma vírgula final e um parêntese de fechamento a seguir:
```py
bar = (0, )
```
Sempre escreva assim:
```py
foo = (0,)
```


* Logo antes do parêntese que abre a lista de argumentos de uma função, como em: 
```py
spam (1)
```
Sempre escreva: 
```py
spam(1)
```
Imediatamente antes da chave que abre um índice, como em: 
```py
dict ['key'] = list [index]
```
Sempre escreva: 
```py
dict['key'] = list[index]
```

* Mais do que um espaço em volta de algum operador, para alinhar os operandos: 
```py
x             = 1
y             = 2
long_variable = 3
```
Escreva: 
```py
x = 1
y = 2
long_variable = 3
```
* Outras recomendações:
    * <p  align="justify">Sempre circunde os seguintes operadores binários com um único espaço de cada lado: =, ==, <, >, !=, <>, <=, >=, in, not in, is, and, or, not;</p>

    * <p  align="justify">Use o seu julgamento na hora de inserir espaços entre operadores aritméticos. Exemplos:</p>

    ```py
    i = i+1
    submitted = submitted + 1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)
    c = (a + b) * (a - b)
    ```
* <p  align="justify">Não use espaços ao redor do sinal de igual (=) quando usado para indicar um valor padrão de um argumento. Faça assim, por exemplo:</p>

```py
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```

* Múltiplos comandos na mesma linha são desencorajados: 

    **Não Recomendado**
    ```py
    if foo == 'blah': do_blah_thing()
    do_one(); do_two(); do_three()
    ```
    **Recomendado**
    ```py
    if foo == 'blah':
        do_blah_thing()
    do_one()
    do_two()
    do_three()
    ```
    
## 4. Comentários
<p  align="justify">Comentários que contradizem o código são piores do que nenhum comentário. Sempre tenha como prioridade manter os comentários atualizados com as mudanças no código! Comentários devem sempre ser frases completas e sua primeira letra deve ser maiúscula, a menos que ele comece com um identificador que começa com uma letra minúscula.</p>

<p  align="justify">Se um comentário for curto, o ponto final deve ser omitido. Comentários grandes normalmente consistem de um ou mais parágrafos e sentenças completas, estas sim devem terminar com ponto.

<p  align="justify">Você deve usar dois espaços depois do ponto final de uma frase, permitindo que o Emacs ajuste a linha de maneira consistente.

<p  align="justify">Programadores de países que não têm o inglês como língua nativa: escrevam seus comentários em inglês, a menos que você tenha 120% de certeza de que o código jamais será lido por pessoas que não falam sua língua.

<p  align="justify">Comentários em bloco devem ser indentados no mesmo nível do código a que se referem. Cada linha deve começar com # e um espaço (a menos que o texto dentro do comentário seja indentado). Parágrafos dentro de um bloco devem ser separados por uma linha contendo uma única tralha #. O bloco inteiro deve ser separado por uma linha em branco no topo e embaixo.

<p  align="justify">Comentários na mesma linha devem ser usados esporadicamente. Devem ser separados do comando por pelo menos dois espaços. Como outros comentários, devem começar com uma tralha e um espaço. Não faça comentários em coisas óbvias. Eles distraem mais do que ajudam. 

## 5. Docstrings
<p  align="justify">Escreva docstrings para todo módulo, função, classe e método público. Elas não são necessárias para métodos "privados", mas é recomendável ter um comentário que explique o que ele faz. Este comentário deve estar logo após a declaração.

<p  align="justify">A PEP 257 descreve as convenções usadas para docstrings. As mais importantes a lembrar são que deve sempre usar aspas triplas (string multiline) mesmo que a dosctring ocupe apenas uma linha (facilita uma possível expansão posterior) e que as aspas triplas que finalizam uma dosctring em múltiplas linhas deve estar em uma linha separada.</p> 

```py
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
```

## 6. Nomes e Identificadores
<p  align="justify">As convenções usadas em nomes na biblioteca padrão são um pouco bagunçadas e díficilmente vamos conseguir torná-las consistentes. Mesmo assim, vamos a algumas regras.</p>
 
* Estilos de nomes 

    <p  align="justify">Há uma série de diferentes estilos usados para identificadores. É bom saber reconhecer qual estilo está sendo usado, independentemente do que está sendo feito. Os estilos mais comuns são:</p>

    * "minúsculas_separadas_com_underscore" 
    * "MAIÚSCULAS_SEPARADAS_COM_UNDERSCORE" 
    * "PalavrasComeçandoPorMaíusculas" 
    * "nome!ComeçandoPorMinúscula" 
    * "Palavras_Começando_Por_Maiúsculas_E_Underscore" (horrível!) 

    <p  align="justify">Há ainda o costume de usar um prefixo curto para agrupar nomes relacionados. Por exemplo, a função os.stat() retorna uma tupla cujos ítens têm nomes como st_mode, st_size, st_mtime e assim port diante. A biblioteca X11 usa um X como prefixo para todas suas funções públicas. Este estilo não é muito comum em Python, porque, geralmente, atributos e nomes de métodos já são prefixados por um objeto, e funções, por um módulo.</p>

    <p  align="justify">Adicionalmente, as seguintes formas de usar underscores antes ou depois do identificador são reconhecidas.</p>
    
    * <p  align="justify">_underscore_no_inicio: costuma indicar que o atributo é de uso interno. ("from M import *" não importa objetos cujos nomes comecem com _ )</p> 

    * <p  align="justify">underscore_no_fim_: usado para evitar conflitos com palavras-chave.por exemplo: "Tkinter.Toplevel(master, class_='ClassName')".</p> 

    * <p  align="justify">__dois_underscores_no_início: atributo privado da classe ( classe.__atributo é convertido para classe.__classe__atributo ).</p> 

    * __dois_underscores_no_início_e_no_fim__: atributos ou objetos especiais, como __init__ , __import__ ou __file__ . As vezes estes podem ser definidos pelo usuário para disparar alguma ação especial (sobrecarga de operadores, por exemplo). 

* Convenções para Nomes: 
    * <p  align="justify">Nomes a evitar Nunca use os caracteres 'l' (L minúsculo), 'O' (o maiúsculo) ou 'I' (i maiúsculo) sozinhos como nomes de variáveis. Em algumas fontes, esses caracteres são indistinguíveis dos números um e zero. Quando tentado a usar somente 'l', use 'L'.</p>
     
    * Nomes de Módulos 
    
        <p  align="justify">Módulos devem ter nomes ou em PalavrasComeçandoPorMaíusculas ou totalmente_em_minúsculas. Módulos que contenham uma única classe podem ter o mesmo nome da classe (como no módulo StringIO, por exemplo). Módulos que exportam apenas funções são normalmente nomeados em minúsculas. Como nomes de módulos são mapeados para nomes de arquivos, e alguns sistemas de arquivo não apenas desprezam maiúsculas e minúsculas como também reduzem o comprimento do nome, é importante que eles sejam escolhidos de forma a serem curtos e não entrar em conflito com outros módulos. Isso não é um problema em sistemas Unix ou Linux, mas pode ser um problema se o código for usado em Mac ou Windows.</p>

        <p  align="justify">Há uma convenção surgindo de que quando uma extensão escrita em C ou C++ tem um módulo em Python que ofereça uma interface de alto nível, este módulo deve ter o nome em PalavrasComeçandoPorMaiúsculas, enquanto o módulo em C/C++ deve ter o nome todo em minúsculas, começando por um underscore (_socket, por exemplo).</p> 

    * Nomes de Classes 

        <p  align="justify">Quase sem exceção, nomes de classe devem usar o padrão de PalavrasComeçandoPorMaiúscula, exceto no caso de classes para uso interno, que devem começar com um underscore.</p>
         
    * Nomes de Exceptions 

        <p  align="justify">Se um módulo define uma única exception usada para todos os tipos de erro, ela é geralmente chamada "error" ou "Error".</p> 

    * Nomes de Funções 
        
        <p  align="justify">Funções globais, exportadas por um módulo podem usar tanto o padrão PalavrasComeçandoPorMaiúscula, quanto totalmente em minúsculas ou minúsculas_separadas_por_underscore). Não há nenhuma preferência clara, mas o primeiro estilo costuma ser mais usado para funções que provêm mais funcionalidade, enquanto o segundo é usado por funções mais simples.</p> 

    * <p  align="justify">Variáveis Globais: Variáveis globais devem ser usadas somente dentro do módulo. As convenções são as mesmas para funções. Módulos que são projetados para ser usados com 'from M import *' devem ter suas globais com um underscore como prefixo, para evitar que sejam exportadas.</p> 

    * Nomes de Métodos 

        <p  align="justify">Vale o mesmo para as funções. Use dois underscores quando for importante que apenas a classe atual acesse um atributo. (mas tenha em mente que isso não torna o método realmente privado. Um usuário insistente ainda pode acessá-lo de diversas formas, através do atributo <b>dict</b> por exemplo).</p> 
         
    * Herança 
        
        <p  align="justify">Decida sempre se os métodos de uma classe e as variáveis de uma instância serão públicos ou não. Em geral, nunca torne variáveis públicas, a menos que você esteja implementando algum tipo de registro. Decida ainda se os atributos serão privados ou não. A diferença entre eles é que atributos privados são aqueles que jamais terão utilidade para uma subclasse, enquanto os públicos podem ter. É prudente projetar suas classes tendo a possibilidade de herança em mente.</p>  

<p  align="justify">Atributos privados devem ter dois underscores no começo e nenhum no fim. Atributos não-públicos devem ter um underscore no começo e nenhum no fim.</p>

<p  align="justify">Atributos públicos não devem ter underscores nem no começo, nem no fim, a menos que eles entrem em conflito com palavras reservadas, caso em que um único underscore no fim é preferível a um no começo, ou a uma pronúncia diferente, como class_ ao invés de klass.</p> 

## 7. Recomendações ao Programar
<p  align="justify">Comparações com singletons, como None, False e True devem sempre ser feitas com "is" ou "is not". Além disso, cuidado para não escrever "if x" quando o que você deseja é "if x is not None", como ao testar se uma variável ou argumento que tem um valor padrão de None, teve outro valor atribuído.</p>

<p  align="justify">Classes são sempre preferidas à strings, como em exceptions. Módulos ou pacotes devem definir sua própria classe-exception base, que deve ser uma subclasse da classe Exception. Sempre inclua uma docstring. Exemplo:</p>

```py
class MessageError(Exception):
    """Base class for errors in the email package."""
```
<p  align="justify">Use métodos do objeto string ao invés do módulo string, a menos que seja exigida compatibilidade com versões de Python anteriores à 2.0. Os métodos são muito mais rápidos e têm a mesma API de strings Unicode.</p>

<p  align="justify">Evite fatiar strings quando verificando prefixos ou sufixos. Use os métodos startswith() e endswith(), que são mais eficientes e menos sujeitos a erro. Por exemplo:</p>

**Não Recomendado:**
```py
if foo[:3] == 'bar':
```
**Recomendado:**
```py
if foo.startswith('bar'):
```
<p  align="justify">A exceção é se existir a necessidade do seu código de funcionar com versões de Python anteriores à 1.5.2.</p>

<p  align="justify">Comparações de tipo de objetos devem sempre usar isinstance() ao invés de comparar tipos diretamente. Exemplo:</p>

**Não Recomendado:**
```py
if type(obj) is type(1):
```
**Recomendado:**
```py
if isinstance(obj, int):
```
<p  align="justify">Com seqüências (strings, listas, tuples), tenha em mente o fato de que, quando vazias, elas são falsas em um contexto booleano, portanto, "if not seq" ou "if seq" são preferíveis a "if len(seq)" ou "if not len(seq)".</p>

<p  align="justify">Não use strings que dependam de uma quantia significativa de espaços no começo ou no fim. A quantidade desses espaços é visualmente indistinguível e alguns editores até mesmo a ajustam.</p>

Não compare valores booleanos com True e False usando == 
**Não Recomendado:**
```py
if greeting == True:
```
**Recomendado:**
```py
if greeting:
```




### REFERÊNCIAS
  * PEP 7, Style Guide for C Code, van Rossum

  * http://www.python.org/doc/essays/styleguide.html
    
  * PEP 257, Docstring Conventions, Goodger, van Rossum

  * http://www.wikipedia.com/wiki/CamelCase

  * Barry's GNU Mailman/mimelib style guide
  
  * https://www.python.org/dev/peps/pep-0008/

