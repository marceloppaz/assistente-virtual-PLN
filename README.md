# Assistente Virtual em Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Um assistente virtual com controle por voz desenvolvido em Python, capaz de executar diversas tarefas através de comandos de voz.

## 🚀 Funcionalidades Principais

- **Interação por voz bidirecional**
- Consulta de hora atual
- Pesquisa no Google e YouTube
- Previsão do tempo por cidade
- Busca de notícias em tempo real
- Acesso a informações online
- Interface com microfone e alto-falante

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Microfone funcional
- Conexão com internet
- API Key do [NewsAPI](https://newsapi.org/)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/assistente-virtual.git
cd assistente-virtual
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure a API Key:
```bash
export NEWSAPI_KEY='sua_chave_aqui'  # Linux/Mac
set NEWSAPI_KEY='sua_chave_aqui'    # Windows
```

## 📝 Requisitos do Sistema

- SpeechRecognition
- PyAudio
- gTTS
- pygame
- requests
- webbrowser

## 🎮 Como Usar

1. Inicie o assistente:
```bash
python assistente.py
```

2. Comandos disponíveis:
- "Que horas são?" → Mostra a hora atual
- "Pesquisar no Google [termo]" → Realiza pesquisa web
- "Procurar no YouTube [termo]" → Busca vídeos
- "Clima em [cidade]" → Mostra previsão do tempo
- "Notícias sobre [tópico]" → Exibe notícias recentes
- "Sair" → Encerra o programa

## ⚙️ Estrutura do Código

- `falar()`: Gera e reproduz áudio usando gTTS
- `ouvir_comando()`: Captura e processa entrada de voz
- `executar_comando()`: Gerencia a lógica de comandos
- `buscar_por_palavra_chave()`: Integração com NewsAPI

## 🛠 Melhorias Futuras

- [ ] Adicionar autenticação por voz
- [ ] Implementar agenda de compromissos
- [ ] Integrar com serviços de e-mail
- [ ] Criar interface gráfica
- [ ] Adicionar controle de dispositivos IoT

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:
1. Faça um Fork do projeto
2. Crie sua Branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a Branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Distribuído sob licença MIT. Veja `LICENSE` para mais informações.

---

**Nota:** Este projeto é para fins educacionais. Requer configuração adequada de ambiente e chaves API válidas para funcionamento completo.
```
