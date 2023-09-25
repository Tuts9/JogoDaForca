# Jogo da Forca em Python com Interface Gráfica

Este é um script Python que implementa o clássico jogo da forca em uma interface gráfica usando a biblioteca Tkinter. O jogo permite que o jogador insira seu nome, escolha um nível de dificuldade e adivinhe uma palavra oculta a partir de dicas fornecidas. O objetivo é adivinhar a palavra antes de cometer seis erros, desenhando parte por parte de um boneco enforcado.

## Pré-requisitos

- Python 3.x
- Biblioteca Tkinter (normalmente incluída na instalação padrão do Python)
- Biblioteca `customtkinter` (é necessário instalá-la)

## Como usar

1. Certifique-se de que os pré-requisitos estejam instalados.

2. Clone o repositório ou copie o código-fonte em um arquivo Python (.py).

3. Execute o arquivo Python.

4. O jogo será iniciado em uma janela gráfica.

5. Insira seu nome no campo de entrada de texto.

6. Escolha o nível de dificuldade no menu suspenso.

7. Clique no botão "Iniciar Jogo" para começar a partida.

8. Uma dica relacionada à palavra será exibida.

9. Digite uma letra no campo de entrada e clique no botão "Inserir letra" para adivinhar a palavra.

10. Continue adivinhando letras até adivinhar a palavra ou cometer seis erros.

11. O jogo terminará com uma mensagem de vitória ou derrota.

12. Você pode reiniciar o jogo clicando no botão "Iniciar Jogo" novamente.

## Estrutura do código

- O código é estruturado em classes e métodos para facilitar a manutenção e a compreensão.

- A classe `JogoDaForca` é a principal e contém toda a lógica do jogo e a interface gráfica.

- O jogo usa um dicionário de palavras e dicas relacionadas, com diferentes níveis de dificuldade.

- A interface gráfica é criada usando a biblioteca Tkinter, com elementos como rótulos, campos de entrada, botões e um canvas para desenhar o boneco enforcado.

- O jogo permite que o jogador insira letras e fornece feedback sobre letras já adivinhadas e erros cometidos.

- O jogo termina quando o jogador adivinha corretamente a palavra ou comete seis erros.

## Personalização

Você pode personalizar o jogo adicionando mais palavras e dicas ao dicionário `self.dict` na classe `JogoDaForca`. Basta seguir o formato existente.

## Licença

Este código é disponibilizado sob a licença [MIT](https://opensource.org/licenses/MIT), o que significa que você é livre para usá-lo, modificá-lo e distribuí-lo da maneira que desejar, desde que mantenha o aviso de direitos autorais original e não responsabilize os autores por qualquer dano ou perda relacionada ao uso deste código.
