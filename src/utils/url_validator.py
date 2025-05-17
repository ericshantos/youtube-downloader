# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
YouTube URL validation module.

Provides functionality to validate YouTube URLs using regular expressions.
Ensures URLs conform to standard YouTube patterns before processing.
"""

import re

class YoutubeURLValidator:
    """
    Validates YouTube URLs using regular expression patterns.
    
    This class provides static methods to check if a given URL
    matches standard YouTube URL formats.
    """
    
    YOUTUBE_URL_PATTERN = re.compile(
        r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$'
    )

    @staticmethod
    def is_valid(url: str) -> bool:
        """
        Check if a URL is a valid YouTube URL.
        
        Args:
            url (str): The URL to validate
            
        Returns:
            bool: True if the URL matches YouTube patterns, False otherwise
            
        Examples:
            >>> YoutubeURLValidator.is_valid("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            True
            >>> YoutubeURLValidator.is_valid("https://invalid.com/video")
            False
        """
        return bool(YoutubeURLValidator.YOUTUBE_URL_PATTERN.match(url))
