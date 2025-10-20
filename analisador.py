"""
Analisador de vídeos do YouTube com IA

Este script baixa o áudio de um vídeo do YouTube, transcreve o conteúdo e gera um resumo em Markdown.
"""

import os
import subprocess
import yt_dlp
import whisper
from pathlib import Path

# Configurar o caminho do FFmpeg
FFMPEG_PATH = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'ffmpeg-6.0-full_build', 'bin', 'ffmpeg.exe')
FFMPEG_DIR = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'ffmpeg-6.0-full_build', 'bin')
os.environ["PATH"] = FFMPEG_DIR + os.pathsep + os.environ["PATH"]

# Função para baixar o áudio do vídeo do YouTube
def baixar_audio(url, output_path='audio.mp3'):
    try:
        ffmpeg_location = None
        possible_paths = [
            r'C:\Program Files\ffmpeg\bin\ffmpeg.exe',
            r'C:\ffmpeg\bin\ffmpeg.exe',
            os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'WinGet', 'Packages', 'Gyan.FFmpeg_8.0', 'ffmpeg.exe')
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                ffmpeg_location = os.path.dirname(path)
                break
        
        if not ffmpeg_location:
            print("AVISO: FFmpeg não encontrado nos caminhos padrão.")
            print("Baixando apenas o áudio sem conversão para MP3...")
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': output_path,
                'quiet': False
            }
        else:
            print(f"FFmpeg encontrado em: {ffmpeg_location}")
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': output_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'ffmpeg_location': ffmpeg_location,
                'quiet': False
            }

        print(f"Baixando áudio do vídeo: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Download concluído!")
        return output_path

    except Exception as e:
        print(f"Erro ao baixar o vídeo: {str(e)}")
        raise

# Função para transcrever o áudio usando Whisper
def transcrever_audio(audio_path):
    try:
        print("Iniciando transcrição do áudio...")
        
        if not os.path.exists(FFMPEG_PATH):
            raise Exception(f"FFmpeg não encontrado em {FFMPEG_PATH}")
        
        try:
            subprocess.run([FFMPEG_PATH, '-version'], capture_output=True, check=True)
            print(f"FFmpeg encontrado e funcionando em: {FFMPEG_PATH}")
        except Exception as e:
            raise Exception(f"FFmpeg encontrado mas não está funcionando: {e}")
        
        wav_path = os.path.splitext(audio_path)[0] + '.wav'
        print(f"Convertendo áudio para WAV: {wav_path}")
        
        subprocess.run([
            FFMPEG_PATH,
            '-i', audio_path,
            '-ar', '16000',
            '-ac', '1',
            '-c:a', 'pcm_s16le',
            wav_path
        ], capture_output=True, check=True)
        
        print("Carregando modelo Whisper...")
        model = whisper.load_model("base")
        
        print("Transcrevendo áudio...")
        result = model.transcribe(wav_path)
        
        os.remove(wav_path)
        
        print("Transcrição concluída!")
        return result["text"]
    except Exception as e:
        print(f"Erro durante a transcrição: {e}")
        import traceback
        print("Detalhes do erro:")
        print(traceback.format_exc())
        raise

# Função para resumir o texto (aqui retorna o texto completo como simulação)
def resumir_texto(texto):
    return texto

# Função principal
def analisar_video(url):
    audio_path = baixar_audio(url)
    texto = transcrever_audio(audio_path)

    if not texto:
        print("Erro: transcrição vazia ou falhou.")
        return

    # Formatar como Markdown
    markdown = "# Transcrição do Vídeo\n\n"
    markdown += "\n".join(texto.split(". "))  # Quebra por frases

    # Salvar como .md
    with open('resumo.md', 'w', encoding='utf-8') as f:
        f.write(markdown)

    print("Transcrição salva em formato Markdown no arquivo 'resumo.md'")

# Execução do programa
if __name__ == "__main__":
    url = input("Cole a URL do vídeo do YouTube: ")
    analisar_video(url)
