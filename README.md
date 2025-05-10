# 📥 YouTube Video Downloader com Python

Um script CLI em Python para download de vídeos do YouTube em alta qualidade, com seleção de resolução, separação e mesclagem de áudio e vídeo usando FFmpeg.

## 🧰 Tecnologias utilizadas
- [pytubefix](https://github.com/rohit-px/pytubefix) — para captura de streams de vídeo e áudio do YouTube
- [python-slugify](https://github.com/un33k/python-slugify) — para gerar nomes de arquivos seguros (sem espaços ou caracteres inválidos)
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

**1.** Clone ou baixe este repositório.

**2.** Instale as dependências com pip: `pip install -r requirements.txt`

**3.** Certifique-se de que o FFmpeg está instalado e acessível no terminal (adicione ao PATH, se necessário).

  - Para instalar o FFmpeg no Windows: https://ffmpeg.org/download.html
  - No Linux (Debian/Ubuntu): sudo apt install ffmpeg

**4.** Execute o script via terminal: `python downloader.py`

## 📸 Exemplo de uso

### 1. baixar somente áudio
```
Digite a url conforme um dos modelos abaixo (0 para encerrar) :
  - https://www.youtube.com/watch?v=exemplo
  ou
  - https://youtu.be/exemplo

  >> https://www.youtube.com/watch?v=exemplo

Escolha uma das opções de download :
  1. somente áudio
  2. somente vídeo
  3. vídeo com áudio
  0. encerrar

  >> 1
...

✅ Áudio salvo em: C:\Users\usuario\Music\nome-do-video-audio.mp3
```

### 2. baixar somente vídeo
```
Digite a url conforme um dos modelos abaixo (0 para encerrar) :
  - https://www.youtube.com/watch?v=exemplo
  ou
  - https://youtu.be/exemplo

  >> https://www.youtube.com/watch?v=exemplo

Escolha uma das opções de download :
  1. somente áudio
  2. somente vídeo
  3. vídeo com áudio
  0. encerrar

  >> 2
...

✅ Áudio salvo em: C:\Users\usuario\Videos\nome-do-video-video.mp4
```

### 3. baixar vídeo com áudio
```
Digite a url conforme um dos modelos abaixo (0 para encerrar) :
  - https://www.youtube.com/watch?v=exemplo
  ou
  - https://youtu.be/exemplo

  >> https://www.youtube.com/watch?v=exemplo

Escolha uma das opções de download :
  1. somente áudio
  2. somente vídeo
  3. vídeo com áudio
  0. encerrar

  >> 3

Escolha uma resolução da lista abaixo :
  1. 1080p
  2. 720p
  3. 480p
  4. 360p
  5. 144p
  0. encerrar

  >> 1

...

✅ Áudio final salvo em: C:\Users\usuario\Videos\nome-do-video-1080p.mp4
```
