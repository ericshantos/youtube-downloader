# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Abstract base class for downloading YouTube media streams.

Provides the core functionality for downloading both audio and video streams
from YouTube, including progress tracking and file handling.
"""

from . import ErrorHandler
from abc import ABC, abstractmethod
from pathlib import Path
from pytubefix import YouTube
from pytubefix.cli import on_progress
from slugify import slugify

class DownloadStream(ABC):
    """
    Abstract base class for YouTube media stream downloads.
    
    Implements common download functionality while requiring subclasses to
    implement stream selection and filename generation specifics.
    
    Args:
        url (str): YouTube video URL
        output (Path): Output directory for downloaded files
    """

    def __init__(self, url: str, output: Path):
        """
        Initialize the downloader with YouTube URL and output path.
        
        Args:
            url: YouTube video URL
            output: Directory where downloaded files will be saved
        """
        self.yt = YouTube(url, on_progress_callback=on_progress)
        self.title = slugify(self.yt.title)
        self.output = Path(output)

    @abstractmethod
    def select_stream(self):
        """
        Abstract method for selecting the appropriate media stream.
        
        Subclasses must implement this to choose specific stream types
        (audio/video) and qualities.
        """
        pass

    @abstractmethod
    def file_name(self):
        """
        Abstract method for generating output filenames.
        
        Subclasses must implement this to provide appropriate naming
        conventions for different media types.
        """
        pass

    def download(self) -> Path:
        """
        Execute the complete download process.
        
        Returns:
            Path: Full path to the downloaded file
            
        Raises:
            RuntimeError: If stream selection fails or download is incomplete
        """
        stream = self.select_stream()

        if not stream:
            raise RuntimeError("Stream not found!")
        
        file_name = self.file_name()
        path = self.output / file_name

        print(f"\nDownloading {file_name}...")
        stream.download(output_path=self.output, filename=file_name)

        if not path.exists() or path.stat().st_size == 0:
            ErrorHandler.exit_with_error(f"{file_name} was not downloaded correctly!")

        return path