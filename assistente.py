import speech_recognition as sr
from gtts import gTTS
import os
import time
import datetime
import webbrowser
import playsound
import pyaudio
import requests
import winshell
from pygame import mixer

api_key = os.environ.get('NEWSAPI_KEY')


def falar(text):
    tts = gTTS(text=text, lang='pt-BR')
    filename = "voice.mp3"

    # Libera o mixer antes de manipular o arquivo
    if mixer.get_init():
        mixer.quit()

    try:
        os.remove(filename)  # Remove o arquivo antigo, se existir
    except OSError:
        pass

    tts.save(filename)  # Salva o novo arquivo

    mixer.init()  # Inicializa o mixer novamente
    mixer.music.load(filename)  # Carrega o arquivo
    mixer.music.play()  # Reproduz o arquivo
    while mixer.music.get_busy():  # Aguarda até o áudio terminar
        time.sleep(0.1)
    mixer.quit()  # Fecha o mixer para liberar o arquivo


def ouvir_comando():
    """Usa a biblioteca speech_recognition para capturar um comando de voz."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Estou ouvindo... Fale algo!")
        try:
            audio = recognizer.listen(source, timeout=15, phrase_time_limit=15)
            comando = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("Não entendi o que você disse. Tente novamente.")
            return None
        except sr.RequestError:
            print("Erro no serviço de reconhecimento de voz.")
            return None


def buscar_por_palavra_chave(api_key, query):
    url = "https://newsapi.org/v2/everything"
    params = {
        'apiKey': api_key,
        'q': query,  # Palavra-chave para busca
        'language': 'pt',  # Idioma: pt para português
        'sortBy': 'relevance',  # Ordenação: relevância, popularidade, ou data
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        dados = response.json()
        for artigo in dados['articles']:
            print(f"Título: {artigo['title']}")
            print(f"Descrição: {artigo['description']}")
            print(f"Publicação: {artigo['publishedAt']}")
            print(f"Link: {artigo['url']}")
            print("-" * 40)
    else:
        print(f"Erro: {response.status_code} - {response.text}")


def executar_comando(comando):
    """Executa tarefas com base no comando reconhecido."""
    if "clima" in comando:
        falar("Por favor, diga o nome da cidade.")
        cidade = ouvir_comando()
        if cidade:
            falar(f"Buscando informações do clima para {cidade}.")
            webbrowser.open(f"https://www.google.com/search?q=clima+{cidade}")
        else:
            falar("Não consegui ouvir o nome da cidade.")
    elif "hora" in comando:
        agora = datetime.datetime.now()
        hora = agora.strftime("%H:%M")
        falar(f"Agora são {hora}.")
    elif "google" in comando:
        falar("O que você gostaria de pesquisar?")
        pesquisa = ouvir_comando()
        if pesquisa:
            falar(f"Pesquisando por {pesquisa}.")
            webbrowser.open(f"https://www.google.com/search?q={pesquisa}")
        else:
            falar("Não consegui ouvir o que você quer pesquisar.")
    elif "youtube" in comando:
        falar("O que você quer procurar no youtube?")
        pesquisa_yt = ouvir_comando()
        if pesquisa_yt:
            falar(f"pesquisando por {pesquisa_yt}.")
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={pesquisa_yt}")
        else:
            falar("Não consegui ouvir o que você quer pesquisar.")
    elif "notícias" in comando:
        falar("Quais notícias você quer procurar?")
        query = ouvir_comando()
        if query:
            falar(f"Buscando notícias sobre {query}")
            buscar_por_palavra_chave(api_key, query)
        else:
            falar("Não entendi sua palavra-chave. Tente novamente.")
    elif "sair" in comando:
        falar("Encerrando o assistente. Até mais!")
        exit()
    else:
        falar("Comando não reconhecido. Tente novamente.")


# Loop Principal
if __name__ == "__main__":
    falar("Olá, eu sou o seu assistente virtual. Como posso ajudar?")
    while True:
        comando = ouvir_comando()
        if comando:
            executar_comando(comando)
