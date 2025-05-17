# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module for downloading audio streams from YouTube videos.
"""

from .downloader import DownloadStream
from pytubefix import Stream
from pathlib import Path

class DownloadAudio(DownloadStream):
    """
    Handles the downloading of audio streams from YouTube videos.
    
    Inherits from DownloadStream and specializes in audio stream selection
    and download operations.
    """

    def select_stream(self) -> Stream:
        """
        Selects the highest quality audio stream available.
        
        Returns:
            Stream: The selected audio stream with the highest bitrate.
        """
        stream = self.yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        self.stream = stream
        return stream

    def file_name(self) -> str:
        """
        Generates the output filename for the audio download.
        
        Uses the video title and stream extension to create a consistent
        filename format: '{title}-audio.{extension}'
        
        Returns:
            str: The generated filename with appropriate extension.
        """
        ext = getattr(self, 'stream', None)
        extension = ext.subtype if ext else 'webm'
        return f"{self.title}-audio.{extension}"

    def download(self) -> Path:
        """
        Executes the audio download process.
        
        Returns:
            Path: The filesystem path where the audio file was saved.
        """
        return super().download()
    