"""
YouTube Media Downloader Package

This package provides functionality for downloading audio and video streams from YouTube.
It includes specialized classes for handling different media types with various options.

@Author: Eric Santos <https://www.github.com/ericshantos>
"""

from ..utils import ErrorHandler, ResolutionSelector
from .download_audio_stream import DownloadAudio
from .download_video_stream import DownloadVideo

__all__ = ["DownloadAudio", "DownloadVideo"]
__author__ = "Eric Santos <https://www.github.com/ericshantos>"