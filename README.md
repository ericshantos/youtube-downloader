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

1. Clone ou baixe este repositório.

2. Instale as dependências com pip: pip install pytubefix python-slugify

3. Certifique-se de que o FFmpeg está instalado e acessível no terminal (adicione ao PATH, se necessário).

Para instalar o FFmpeg no Windows: https://ffmpeg.org/download.html

No Linux (Debian/Ubuntu): sudo apt install ffmpeg

4.Execute o script via terminal: python downloader.py

## 📸 Exemplo de uso
**para baixar somente áudio:**

Digite a URL do vídeo: https://youtube.com/xyz123
Deseja baixar só o áudio? (s/n): s
...
✅ Áudio salvo em: C:\Users\seunome\Music\nome-do-video_audio.mp4

**Ou para baixar o vídeo com áudio:**

Digite a URL do vídeo: https://youtube.com/xyz123
Deseja baixar só o áudio? (s/n): n
Escolha a resolução:
1 - 1080p
2 - 720p
...
✅ Vídeo final salvo em: C:\Users\seunome\Videos\nome-do-video_1080p.mp4
