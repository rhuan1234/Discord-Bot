# 🤖 Discord Bot – Python  

Este é um **bot para Discord** desenvolvido em **Python**, com diversas funcionalidades, incluindo reprodução de músicas, gerenciamento de cargos, interações com mensagens e integração com APIs externas.  

---

## 🚀 Funcionalidades  
🎵 **Música**  
- Toca músicas **aleatórias sem direitos autorais** do YouTube a partir de uma lista de URLs.  
- Permite que o usuário toque **qualquer música** fornecendo uma **URL do YouTube**.  

⚙️ **Gerenciamento do Servidor**  
- **Adiciona cargos** aos usuários.  
- **Reage automaticamente** a mensagens específicas.  
- **Cria mensagens personalizadas** com **embeds**.  

🌐 **Integração com APIs**  
- Compara moedas em tempo real.  
- Obtém **imagens aleatórias**.  
- Realiza cálculos simples, como **soma de dois números**.  

🛡️ **Moderação e Segurança**  
- **Sistema de controle de chat**:  
  - Caso um usuário digite "porra", o bot **deleta a mensagem** e **emite um aviso** para evitar ofensas.  
  - Se um usuário **fizer spam**, o bot **baniu automaticamente** do servidor.  

---

## 🛠️ Tecnologias Utilizadas  
- **Python** – Linguagem principal  
- **discord.py** – Biblioteca para interagir com o Discord  
- **youtube-dl / yt-dlp** – Para tocar músicas do YouTube  
- **requests** – Para integração com APIs externas  

---
## 📌 Requisitos do Projeto  

Para rodar o bot corretamente, siga os passos abaixo:  

# 1️⃣ **Gerar Token do Bot**  
- No [Discord Developer Portal](https://discord.com/developers/applications), crie um bot e copie seu **TOKEN**.  
- No arquivo `bot.py`, vá até a **linha 31** e atribua o token à variável:  
  ```python
  TOKEN = "seu_token_aqui"
  
# 2️⃣ Instalar Dependências

No terminal, instale as bibliotecas necessárias:
pip install discord.py yt-dlp

# 3️⃣ Configurar Cargos no Servidor

No seu servidor do Discord, crie os seguintes cargos:
- 🥉 Bronze
- 🥈 Prata
- 🥇 Ouro
- 💎 Diamante
Depois, no arquivo commands/cargo.py, substitua os IDs dos cargos nas seguintes linhas:
Linhas 63, 65, 67 e 69 (para adicionar cargos).
Linhas 91, 93, 95 e 97 (para remover cargos).
Atenção! Não coloque os IDs entre aspas.
Agora, seu bot está pronto para ser executado! 🚀🎵
