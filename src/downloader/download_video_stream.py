# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module for downloading video streams from YouTube with resolution selection.

Provides functionality to select and download video streams from YouTube videos
with user-selected resolution options and save them to the local filesystem.
"""

from . import ResolutionSelector
from .downloader import DownloadStream
from pytubefix import Stream
from pathlib import Path
from typing import Optional, Tuple

class DownloadVideo(DownloadStream):
    """
    Handles the downloading of video streams from YouTube videos with resolution selection.
    
    Inherits from DownloadStream and provides specialized video stream selection
    and download operations with resolution menu support.
    """

    def select_stream(self) -> Stream:
        """
        Selects a video stream based on user's resolution choice.
        
        Filters available adaptive video streams and presents a resolution menu
        for user selection.
        
        Returns:
            Stream: The selected video stream with the chosen resolution.
            
        Raises:
            RuntimeError: If no video streams are available or if the selected
                        resolution isn't found.
        """
        video_streams = self.yt.streams.filter(
            adaptive=True, only_video=True
        ).order_by('resolution').desc()

        if not video_streams:
            raise RuntimeError("No video streams available!")

        selector = ResolutionSelector(video_streams)
        self.resolution_chosen = selector.select_resolution()

        stream = next((s for s in video_streams if s.resolution == self.resolution_chosen), None)

        if stream is None:
            raise RuntimeError(f"No stream found for resolution {selector}!")

        self.stream = stream
        return stream

    def file_name(self) -> str:
        """
        Generates the output filename for the video download.
        
        Uses the video title and stream extension to create a consistent
        filename format: '{title}-video.{extension}'
        
        Returns:
            str: The generated filename with appropriate extension.
        """
        ext = getattr(self, 'stream', None)
        extension = ext.subtype if ext else 'mp4'
        return f"{self.title}-video.{extension}"

    def download(self) -> Tuple[Optional[Path], str]:
        """
        Executes the video download process.
        
        Returns:
            Tuple[Optional[Path], str]: A tuple containing:
                - Path: The filesystem path where the video file was saved
                - str: The chosen resolution of the downloaded video
        """
        return super().download(), self.resolution_chosen
    