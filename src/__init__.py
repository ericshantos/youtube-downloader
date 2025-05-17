# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module for downloading and processing YouTube videos, including audio extraction 
and merging functionality.
"""

from .downloader import DownloadVideo, DownloadAudio
from .utils import MediaMerger, YoutubeURLValidator
from platformdirs import user_videos_dir
from pathlib import Path
import tempfile

class YoutubeDownloader:
    """
    Main class for handling YouTube video downloads with audio merging capability.

    Args:
        videos_path (Path): Path where the final videos will be saved. Defaults to 
        system's videos directory.
    """

    def __init__(self, videos_path: Path = Path(user_videos_dir())):
        self.videos_path = videos_path

    def run(self):
        """
        Execute the complete download and processing pipeline.
        
        Steps:
        1. Get YouTube URL from user input
        2. Validate the URL
        3. Download video and audio components
        4. Merge media components
        5. Notify user of successful completion
        """
        url = self._get_url()
        self._validate_url(url)

        with tempfile.TemporaryDirectory() as temp_dir:
            video = self._download_video(url, temp_dir)
            audio = self._download_audio(url, temp_dir)

            result = self._merge(video, audio)
        
        self._notify_success(result)

    def _get_url(self) -> str:
        """Prompt user for and return a YouTube URL."""
        return input("url: ").strip()

    def _validate_url(self, url: str) -> None:
        """Validate the provided URL as a valid YouTube URL.
        
        Raises:
            ValueError: If the URL is not a valid YouTube URL.
        """
        if not YoutubeURLValidator.is_valid(url):
            raise ValueError("Invalid URL for YouTube.")

    def _download_video(self, url: str, output: str):
        """Download video component from YouTube.
        
        Args:
            url: YouTube video URL
            output: Temporary directory path for download
            
        Returns:
            Path to the downloaded video file
        """
        downloader = DownloadVideo(url, output=output)
        video, _ = downloader.download()
        return video

    def _download_audio(self, url: str, output: str):
        """Download audio component from YouTube.
        
        Args:
            url: YouTube video URL
            output: Temporary directory path for download
            
        Returns:
            Path to the downloaded audio file
        """
        downloader = DownloadAudio(url, output=output)
        return downloader.download()

    def _merge(self, video: str, audio: str) -> str:
        """Merge video and audio components into final video file.
        
        Args:
            video: Path to video file
            audio: Path to audio file
            
        Returns:
            Path to the merged output file
        """
        return MediaMerger.merge(video, audio, self.videos_path)

    def _notify_success(self, result: str) -> None:
        """Notify user of successful download and processing.
        
        Args:
            result: Path to the final output file
        """
        print(f"Download completed. Video saved at: {result}")

__author__ = "Eric Santos <https://www.github.com/ericshantos>"

__all__ = ["YoutubeDownloader"]
