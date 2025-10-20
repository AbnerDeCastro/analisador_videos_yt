🎥 Analisador de Vídeos do YouTube com IA
Este projeto em Python permite baixar o áudio de um vídeo do YouTube, transcrevê-lo usando inteligência artificial (Whisper) e salvar a transcrição em formato Markdown. Ideal para estudar conteúdos longos como palestras, tutoriais e entrevistas.

🧠 Funcionalidades
✅ Baixa o áudio de vídeos do YouTube

✅ Converte o áudio para formato compatível com IA

✅ Transcreve o conteúdo usando o modelo Whisper

✅ Formata a transcrição em Markdown

✅ Salva o resultado em um arquivo .md

📦 Requisitos
Antes de executar o projeto, certifique-se de ter:

Python 3.8 ou superior

FFmpeg instalado localmente ou incluído na pasta do projeto

Ambiente virtual configurado (opcional, mas recomendado)

📚 Bibliotecas utilizadas
bash
pip install yt-dlp openai-whisper
O Whisper também instala automaticamente torch, necessário para rodar o modelo de IA.

🛠️ Estrutura do Projeto
Code
analisador_de_videos/
├── analisador.py
├── ffmpeg/
│   └── ffmpeg-6.0-full_build/
│       └── bin/
│           └── ffmpeg.exe
├── resumo.md
└── audio.mp3
🚀 Como Executar
Clone o repositório:

bash
git clone https://github.com/seu-usuario/analisador-de-videos.git
cd analisador-de-videos
(Opcional) Crie um ambiente virtual:

bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate      # Windows
Instale as dependências:

bash
pip install yt-dlp openai-whisper
Execute o script:

bash
python analisador.py
Cole a URL do vídeo do YouTube quando solicitado.

O arquivo resumo.md será gerado com a transcrição formatada.

📝 Exemplo de Uso
bash
Cole a URL do vídeo do YouTube: https://www.youtube.com/watch?v=abc123xyz
Resultado:

markdown
# Transcrição do Vídeo

Esta é a primeira frase.
Esta é a segunda frase.
...
📁 Saída
resumo.md: transcrição formatada em Markdown

audio.mp3: áudio extraído do vídeo

🧪 Testado com
Vídeos com legendas automáticas

Vídeos em português e inglês

Windows 10 com FFmpeg local

📌 Observações
O Whisper pode demorar alguns minutos dependendo do tamanho do vídeo e da capacidade do seu computador.

Certifique-se de que o vídeo tem áudio claro para melhor transcrição.

📚 Aprendizados
Este projeto foi desenvolvido como parte do meu portfólio de desenvolvedor júnior, com foco em:

Manipulação de arquivos e áudio

Integração com bibliotecas de IA

Automação de tarefas com Python

Formatação de texto e geração de arquivos Markdown
