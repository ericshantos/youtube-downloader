# 📥 YouTube Video Downloader com Python

Um script CLI em Python para download de vídeos do YouTube em alta qualidade, com seleção de resolução, separação e mesclagem de áudio e vídeo usando FFmpeg.

## 🧰 Tecnologias utilizadas
- [pytubefix](https://github.com/rohit-px/pytubefix) — para captura de streams de vídeo e áudio do YouTube
- [python-slugify](https://github.com/un33k/python-slugify) — para gerar nomes de arquivos seguros
- [FFmpeg](https://ffmpeg.org/) — para mesclar vídeo e áudio
- Python 3.8+

## ✨ Funcionalidades
- Entrada de URL via terminal
- Lista de resoluções de vídeo disponíveis para escolha
- Download separado de vídeo e áudio em MP4
- Combinação dos arquivos usando FFmpeg
- Nomeação automática dos arquivos com títulos seguros
- Exclusão automática dos arquivos temporários

## 📦 Como usar

1. Instale os requisitos:

pip install pytubefix python-slugify

2. Certifique-se de que o ffmpeg esteja instalado e acessível via terminal.

3. execulte o script:

python downloader.py
