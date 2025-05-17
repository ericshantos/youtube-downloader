[🇧🇷] [Lê em português](README.pt.md)

# 📥 YouTube Video Downloader Pro

<div align="left">
    <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python Version" />
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License" />
    <img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build Status" />
    <img src="https://img.shields.io/badge/code%20style-black-000000" alt="Code Style" />
</div>

<br>

An advanced Python CLI application for downloading YouTube videos with complete control over quality, formats, and media processing. Offers intelligent separation and merging of audio and video streams using FFmpeg, with robust error handling and validations.

## 🌟 Key Features

- ⚡ **High-performance downloading** with real-time progress
- 🎚 **Full resolution control** (from 144p up to 4K when available)
- 🔊 **Audio extraction** in original quality
- 🎥 **Video-only download** for professional editing
- 🔀 **Automatic merging** of audio and video streams
- 🛡 **Robust URL validation**
- 📁 **Automatic file management** with safe filenames
- ♻ **Temporary files cleanup** after processing

## 🛠 Technologies Used

| Technology | Description | Version |
|------------|-----------|--------|
| ![pytubefix](https://img.shields.io/badge/pytubefix-API-red) | Library for YouTube API interaction | 8.13.1 |
| ![FFmpeg](https://img.shields.io/badge/FFmpeg-Media%20Processing-green) | Media processing tool | Latest |
| ![python-slugify](https://img.shields.io/badge/slugify-Filename%20Safety-orange) | Safe filename generation | 8.0.4 |
| ![platformdirs](https://img.shields.io/badge/platformdirs-OS%20Paths-blue) | System directory locations | 4.3.8 |

## 🏗 Project Architecture

```bash
├── .gitignore
├── README.md
├── main.py                # Main entry point
├── requirements.txt       # Project dependencies
└── src                    # Core source code
    ├── __init__.py        # Module exports
    ├── downloader         # Download module
    │   ├── __init__.py
    │   ├── download_audio_stream.py  # Audio specialization
    │   ├── download_video_stream.py  # Video specialization
    │   └── downloader.py  # Abstract base class
    └── utils              # Utilities
        ├── __init__.py
        ├── error.py       # Error handling
        ├── menu.py        # Selection interface
        ├── midia.py       # Media processing
        └── url_validator.py # URL validation
```

## 📦 Prerequisites

- Python 3.8+
- FFmpeg installed and in PATH
- Project dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 How to Use

### FFmpeg Installation

- **Windows**: Download from [official site](https://ffmpeg.org/download.html) and add to PATH
- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```

### Running the Application

```bash
python main.py
```

## 🖥 Usage Examples

### 1. Audio Download

```bash
Enter video URL (0 to exit):
>> https://www.youtube.com/watch?v=example

Available options:
1. Audio only
2. Video only
3. Video with audio
0. Exit

>> 1

✅ Audio saved at: /path/to/video-name-audio.mp3
```

### 2. Specific Resolution Video Download

```bash
Enter video URL (0 to exit):
>> https://www.youtube.com/watch?v=example

Available options:
1. Audio only
2. Video only
3. Video with audio
0. Exit

>> 3

Available resolutions:
1. 2160p (4K)
2. 1440p (2K)
3. 1080p (Full HD)
4. 720p (HD)
5. 480p (SD)
6. 360p
7. 144p

>> 3

✅ Video saved at: /path/to/video-name-1080p.mp4
```

## 🛠 Advanced Features

### 1. URL Validation

The system rigorously checks if the provided URL matches YouTube patterns before processing:

```python
YOUTUBE_URL_PATTERN = re.compile(
    r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
)
```

### 2. Download System

Abstract class-based implementation for extensibility:

```python
class DownloadStream(ABC):
    @abstractmethod
    def select_stream(self): ...
    
    @abstractmethod 
    def file_name(self): ...
    
    def download(self) -> Path: ...
```

### 3. Media Processing

Efficient merging using FFmpeg with output validation:

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

## 📌 Important Notes

1. This project is for educational purposes
2. Check YouTube's usage policies
3. Downloads may be subject to regional restrictions

## 🤝 Contribution

Contributions are welcome! Follow these steps:

1. Fork the project
2. Create a branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
