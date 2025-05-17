# 📥 YouTube Video Downloader Pro

<div align="left">
    <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python Version" />
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License" />
    <img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build Status" />
    <img src="https://img.shields.io/badge/code%20style-black-000000" alt="Code Style" />
</div>

<br>

Um aplicativo CLI avançado em Python para download de vídeos do YouTube com controle total sobre qualidade, formatos e processamento de mídia. Oferece separação e mesclagem inteligente de streams de áudio e vídeo usando FFmpeg, com tratamento robusto de erros e validações.

## 🌟 Recursos Principais

- ⚡ **Download de alta performance** com progresso em tempo real
- 🎚 **Controle total de resolução** (144p até 4K quando disponível)
- 🔊 **Extração de áudio** em qualidade original
- 🎥 **Download de vídeo sem áudio** para edição profissional
- 🔀 **Mesclagem automática** de streams de áudio e vídeo
- 🛡 **Validação de URL** robusta
- 📁 **Gerenciamento de arquivos** automático com nomes seguros
- ♻ **Limpeza de temporários** após processamento

## 🛠 Tecnologias Utilizadas

| Tecnologia | Descrição | Versão |
|------------|-----------|--------|
| ![pytubefix](https://img.shields.io/badge/pytubefix-API-red) | Biblioteca para interação com a API do YouTube | 8.13.1 |
| ![FFmpeg](https://img.shields.io/badge/FFmpeg-Media%20Processing-green) | Ferramenta para processamento de mídia | Latest |
| ![python-slugify](https://img.shields.io/badge/slugify-Filename%20Safety-orange) | Geração de nomes de arquivo seguros | 8.0.4 |
| ![platformdirs](https://img.shields.io/badge/platformdirs-OS%20Paths-blue) | Localização de diretórios do sistema | 4.3.8 |

## 🏗 Arquitetura do Projeto

```bash
├── .gitignore
├── README.md
├── main.py                # Ponto de entrada principal
├── requirements.txt       # Dependências do projeto
└── src                    # Código fonte principal
    ├── __init__.py        # Exportação de módulos
    ├── downloader         # Módulo de download
    │   ├── __init__.py
    │   ├── download_audio_stream.py  # Especializado em áudio
    │   ├── download_video_stream.py  # Especializado em vídeo
    │   └── downloader.py  # Classe base abstrata
    └── utils              # Utilitários
        ├── __init__.py
        ├── error.py       # Tratamento de erros
        ├── menu.py        # Interface de seleção
        ├── midia.py       # Processamento de mídia
        └── url_validator.py # Validação de URLs
```

## 📦 Pré-requisitos

- Python 3.8+
- FFmpeg instalado e no PATH
- Dependências do projeto:

```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

### Instalação do FFmpeg

- **Windows**: Baixe do [site oficial](https://ffmpeg.org/download.html) e adicione ao PATH
- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```

### Executando o Aplicativo

```bash
python main.py
```

## 🖥 Exemplos de Uso

### 1. Download de Áudio

```bash
Digite a URL do vídeo (0 para sair):
>> https://www.youtube.com/watch?v=exemplo

Opções disponíveis:
1. Somente áudio
2. Somente vídeo 
3. Vídeo com áudio
0. Sair

>> 1

✅ Áudio salvo em: /caminho/para/nome-do-video-audio.mp3
```

### 2. Download de Vídeo em Resolução Específica

```bash
Digite a URL do vídeo (0 para sair):
>> https://www.youtube.com/watch?v=exemplo

Opções disponíveis:
1. Somente áudio
2. Somente vídeo 
3. Vídeo com áudio
0. Sair

>> 3

Resoluções disponíveis:
1. 2160p (4K)
2. 1440p (2K)
3. 1080p (Full HD)
4. 720p (HD)
5. 480p (SD)
6. 360p
7. 144p

>> 3

✅ Vídeo salvo em: /caminho/para/nome-do-video-1080p.mp4
```

## 🛠 Funcionalidades Avançadas

### 1. Validação de URL

O sistema verifica rigorosamente se a URL fornecida corresponde aos padrões do YouTube antes de processar:

```python
YOUTUBE_URL_PATTERN = re.compile(
    r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
)
```

### 2. Sistema de Download

Implementação baseada em classes abstratas para extensibilidade:

```python
class DownloadStream(ABC):
    @abstractmethod
    def select_stream(self): ...
    
    @abstractmethod 
    def file_name(self): ...
    
    def download(self) -> Path: ...
```

### 3. Processamento de Mídia

Mesclagem eficiente usando FFmpeg com validação de saída:

```python
command = [
    "ffmpeg",
    "-i", str(video_path),
    "-i", str(audio_path), 
    "-c:v", "copy",
    "-c:a", "aac",
    str(output_file)
]
```

## 📌 Notas Importantes

1. Este projeto é para fins educacionais
2. Verifique as políticas de uso do YouTube
3. Downloads podem estar sujeitos a restrições regionais

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
