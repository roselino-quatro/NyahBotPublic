# NyahBot

<p style="text-align:center">(=^-ω-^=)</p>
  
NyahBot é um chat-bot feito em Python 3 para o Telegram que pode ser adcionado em seu grupo de amigos de graça! Você pode conversar com ele (assumindo que você possui Telegram instalado) clicando [aqui](https://t.me/NyahBot).

## Adcionando o bot no grupo
Para adcionar bot em seu grupo siga os passos:
<details>
  <summary> Tutorial aqui </summary>
  
1- Entre no grupo que você quer adcionar o bot 

<img src="https://i.imgur.com/aDgiqot.jpg" width="300" height="640" alt="Imagem tutorial 1"/>

2-  Entre em membros e clique em Adcionar membros

<img src="https://i.imgur.com/Lth6zaQ.jpg" width="300" height="640" alt="Imagem tutorial 2"/>

3-  Escreva na barra de pesquisa o nome do bot (@NyahBot)

<img src="https://i.imgur.com/2wCfHW3.jpg" width="300" height="640" alt="Imagem tutorial 3"/>

4- Clique no simbolo de adcionar e confirme

<img src="https://imgur.com/4wM9eMC.jpg" width="300" height="640" alt="Imagem tutorial 4"/>

5- Pronto!

<img src="https://i.imgur.com/SShvWGl.jpg" width="300" height="640" alt="Imagem tutorial 5"/>

</details>

## Hosting do Bot na sua máquina

Para clonar o repositorio na sua máquina utilize
```
git clone https://github.com/roselino-quatro/NyahBotPublic.git
cd NyahBotPublic
pip install -r requirements.txt
```
Esse repositorio não possui as keys do NyahBot inclusas, isso significa que para rodar uma versão sua será necessario conversar com o @BotFather no Telegram e gerar as chaves do seu bot e gerar um arquivo em src/conf/ chamado .env com a seguinte linha:

```
TELEGRAM_TOKEN= SEU_TOKEN_AQUI
```

Apos isso é só executar o core.py

```
python core.py
```

## Comandos

O bot atualmente possui os seguintes comandos, porém você pode clona-lo e adcionar os seus próprios
| Nome | Função | Leva Argumentos? |
|:---- |:------ |:----------------:|
| /carentena | Envia uma imagem aleatoria | Não |
| /fofometro | Descubra seu nivel de fofura! Chuta um valor cada vez mais alto toda vez que erra | Não |
| /start     | Oi!!! | Não |
| /parabains | Envia Parabéns, yay | Não |
| /paises | precisa de um país aleatorio? Ta na mão | Não |
| /libgen | busca o livro passado como argumento na libgen | Sim |
