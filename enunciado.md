# Robótica Computacional 2022.1


## Avaliação Intermediária (P1)


**Indique seu nome e as questões que escolheu fazer logo abaixo. Você deve escolher 4 questões, senão o avaliador o fará por você.**


Nome:_______________


Questões que fez:____________


**Observações de avaliações nesta disciplina:**

* Clone o repositório da prova dentro de `~/catkin_ws/src` se estiver trabalhando no Linux.
* Você poderá dar quantos `git push` quiser no repositório, apenas o último será considerado.
* Antes de finalizar a prova verifique que os arquivos enviados ao github estão na sua última versão. É sua responsabilidade garantir isso.
* Inicie a prova no Blackboard para a ferramenta de Proctoring iniciar.
* Só finalize a prova no Blackboard após enviar a prova via Github classroom.
* Durante esta prova vamos registrar somente a tela, não a câmera nem microfone
* Ponha o nome no enunciado da prova no Github
* Tenha os repositórios https://github.com/Insper/robot22.1/ ,  https://github.com/arnaldojr/my_simulation e https://github.com/arnaldojr/mybot_description.git  atualizados em seu `catkin_ws/src`.
* Você pode consultar a internet ou qualquer material, mas não pode se comunicar com pessoas ou colegas a respeito da prova
* Todos os códigos fornecidos adicionalmente aos scripts em que as questões serão desenvolvidas foram testados em outro contexto, e são apenas um compilado. Não é obrigatório usar. Fique à vontade para modificar esse código e trazer outros arquivos que achar melhor. 
* Teste sempre seu código
* Entregue código que executa - código com erro que impede de executar implica em zero na questào
* Faça commits e pushes frequentes no seu repositório (tem dicas [no final deste arquivo](./instrucoes_setup.md))
* Permite-se consultar qualquer material online ou próprio. Não se pode compartilhar informações com colegas durante a prova.
* Faça commits frequentes. Em caso de disputa sobre plágio, o primeiro a enviar alguma ideia será considerado autor original.
* A responsabilidade por ter o *setup* funcionando é de cada estudante.
* Questões de esclarecimento geral podem ser perguntadas no chat do Teams.
* É proibido colaborar ou pedir ajuda a colegas ou qualquer pessoa que conheça os assuntos avaliados nesta prova.
* Os exercícios admitem diversas estratégias de resolução. A prova de cada aluno é única. Atenha-se apenas à rubrica de cada questão.

Existe algumas dicas de referência rápida de setup [instrucoes_setup.md](instrucoes_setup.md)

**Integridade Intelectual**

Se você tiver alguma evidência de fraude cometida nesta prova, [use este serviço de e-mail anônimo](https://www.guerrillamail.com/pt/compose)  para informar ao professor através do e-mail `antoniohps1@insper.edu.br`.



# Questões


## Questão 1  (2.50 pontos)


Nononononon

*Exemplo de situação onde o canhão acertou a nave*

Estado do jogo (imagem de entrada)
![](alien_exemplo.png)

Como deve ficar a tela (imagem de saída)
![](alien_exemplo_acertou.png)


#### Orientações

Trabalhe no arquivo `q1/q1.py`. Este exercício **não precisa** de ROS. Portanto pode ser feito até em Mac ou Windows

Você vai notar que este programa roda o vídeo `lasercannon.mp4`. Baixe o vídeo [neste endereço](https://drive.google.com/file/d/1n7JRLZzbN8YZDxTZS0tli8v_RpNzZUAc/view?usp=sharing), dentro da pasta `q1/`.


#### O que você deve fazer:


|Resultado| Conceito| 
|---|---|
| Não executa | zero |
| Segmenta ou filtra a imagem baseado em cores ou canais da imagem e produz output visual| 0.6|
| Identifica o ponto de confluência corretamente, com output bem claro OU identifica que a nave atinge a altura perigosa| 1.3|
| Identifica ambas as situações acima| 2.1 |
| Identifica as três situações pedidas no enunciado, mas não está perfeito | 2.8 |
| Resultados perfeitos | 3.33|


Casos intermediários ou omissos da rubrica serão decididos pelo professor.

## Questão 2  (2.50 pontos)

Nonononono


#### Orientações

Trabalhe no arquivo `q2/q2.py`. Este exercício **não precisa** de ROS. Portanto pode ser feito até em Mac ou Windows

Você vai notar que este programa roda o vídeo `dogtraining.mp4`. Baixe o vídeo [neste endereço](https://drive.google.com/file/d/10v0lrUtciTE7HNeO2WSE4ug9HafpQvHP/view?usp=sharing), dentro da pasta `q1/`.


#### O que você deve fazer:


|Resultado| Conceito| 
|---|---|
| Não executa | zero |
| Identifica o cachorro OU a bola, marcando claramente na imagem| 0.6|
| Identifica o cachorro E a bola, marcando claramente na imagem| 1.5|
| Identifica o cachorro E mede a distância percorrida| 1.5|
| Identifica o cachorro e a bola e mede a distância percorrida| 2.4 |
| Faz tudo o que se pede no enunciado, mas não está perfeito | 2.8 |
| Resultados perfeitos | 3.33|


Casos intermediários ou omissos da rubrica serão decididos pelo professor.

*Exemplo do que deve ser feito*

Exemplo de imagem de entrada
![](cao_exemplo.png)

Exemplo de imagem de saida
![](cao_exemplo_detecta.png)


## Questão 3  (2.50 pontos)

Nonononono


#### Orientações

Trabalhe no arquivo `q3/q3.py`. Este exercício **não precisa** de ROS. Portanto pode ser feito até em Mac ou Windows

Você vai notar que este programa roda o vídeo `dogtraining.mp4`. Baixe o vídeo [neste endereço](https://drive.google.com/file/d/10v0lrUtciTE7HNeO2WSE4ug9HafpQvHP/view?usp=sharing), dentro da pasta `q1/`.


#### O que você deve fazer:


|Resultado| Conceito| 
|---|---|
| Não executa | zero |
| Identifica o cachorro OU a bola, marcando claramente na imagem| 0.6|
| Identifica o cachorro E a bola, marcando claramente na imagem| 1.5|
| Identifica o cachorro E mede a distância percorrida| 1.5|
| Identifica o cachorro e a bola e mede a distância percorrida| 2.4 |
| Faz tudo o que se pede no enunciado, mas não está perfeito | 2.8 |
| Resultados perfeitos | 3.33|


Casos intermediários ou omissos da rubrica serão decididos pelo professor.

*Exemplo do que deve ser feito*

Exemplo de imagem de entrada
![](cao_exemplo.png)

Exemplo de imagem de saida
![](cao_exemplo_detecta.png)


## Questões de ROS

**Atenção: ** 

Para fazer estra questão você precisa ter o `my_simulation` e o `mybot_description` atualizado.

    cd ~/catkin_ws/src
    cd my_simulation
    git stash
    git pull

Ou então se ainda não tiver:

    cd ~/catkin_ws/src
    git clone https://github.com/arnaldojr/my_simulation.git

Para o mybot_description:

    cd ~/catkin_ws/src
    cd mybot_description
    git stash
    git pull

Ou então se ainda não tiver:

    cd ~/catkin_ws/src
    git clone https://github.com/arnaldojr/mybot_description



Em seguida faça o [catkin_make](./instrucoes_setup.md). 


## Questão 4 (2.50 pontos)

<img src="gaz_quarto.png" width=100%></img>

Seu robô está no cenário visível abaixo:

    roslaunch my_simulation quarto.launch


#### O que é para fazer

Faça o robô dar uma volta na pista abaixo, parando quando chegar próximo ao início (você pode descobrir isso usando a odometria). A distância do robô à posição inicial deve ser impressa no terminal. Dicas: 

1. Você pode centralizar o robô na pista tanto usando o ponto de fuga quanto o ponto de cruzamento da  reta central com a linha inferior da imagem.

2. Caso a pista apareça muito curva na imagem e não possa ser bem aproximada por uma reta, você pode usar apenas a porção inferior da mesma para encontrar retas melhores  

Para responder à questão você deverá trabalhar em `p1_221/scripts/q4.py`:

1. Preencher a função `gerar_ponto_referencia()` que deve retornar o ponto central da imagem, o ponto de referência para o controle do robô e a imagem com o ponto de referência desenhado usando um croshair

2. Usando as informações geradas pela função acima, preencha o loop de controle do robô para mantê-lo centralizado na pista

3. Preencher a função `distancia_origem()` para calcular e imprimir a distância do robô à origem


#### Detalhes de como rodar

O código para este exercício está em: `p1_221/scripts/q4.py`

Para rodar, recomendamos que faça:

    roslaunch my_simulation quarto.launch

Depois:

    rosrun p1_221 q4.py


|Resultado| Conceito| 
|---|---|
| Não executa | 0 |
| Segmenta a reta do centro ou as retas das laterais e fornece evidência visual | 0.7 |
| Encontra ao menos uma das retas e fornece evidência visual  | 1.2 |
| Encontra o ponto de referência para controle do robô | 1.8 |
| O robô consegue dar ao menos uma volta na pista | 2.2|
| O robô para após completar uma volta | 2.5|


Casos intermediários ou omissos da rubrica serão decididos pelo professor.

## Questão 5 (2.50 pontos)

![](gaz_cubos.png)

Seu robô está no cenário visível abaixo:

    roslaunch my_simulation cubos.launch


#### O que é para fazer

Gire o robô até encontrar o bloco com a figura assinalada (veja a tabela abaixo). Ao centralizar a figura, use o lidar para chegar próximo (30 cm) daquela figura. Depois, gire 180 graus e pare a 30 cm do bloco que está diametralmente oposto.

Quem cujo primeiro nome se inicia com as letras da tabela abaixo, deve inicialmente se aproximar da figura correspondente:

|Letra inicial do nome| Figura inicial| 
|---|---|
| A até C | Cachorro |
| D até H | Cavalo |
| I até P | Pássaro |
| Q até Z | XXX |

#### Detalhes de como rodar


O código para este exercício está em: `212_p1/scripts/q5.py`

Para rodar, recomendamos que faça:

    roslaunch my_simulation cubos.launch

Depois:

    rosrun p1_212 q5.py



|Resultado| Conceito| 
|---|---|
| Não executa | 0 |
| Faz o robô detectar a primeira figura apenas, e mostra evidências | 1.0 |
| Consegue centralizar na primeira figura | 1.50|
| Chega próximo à primeira figura | 2.00|
| Dá a volta e chega na segunda figura | 2.50|


Casos intermediários ou omissos da rubrica serão decididos pelo professor.

**Boa sorte!!**