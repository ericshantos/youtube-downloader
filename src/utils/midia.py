# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Media merging utility for combining audio and video streams.

Provides functionality to merge separate audio and video streams into a single media file
using FFmpeg. Handles error cases and validates output quality.
"""

import subprocess
from pathlib import Path
from .error import ErrorHandler

class MediaMerger:
    """
    A utility class for merging audio and video streams using FFmpeg.

    This class provides static methods to combine separate audio and video files
    into a single media container while preserving quality.
    """

    @staticmethod
    def merge(video_path: Path, audio_path: Path, output_dir: Path) -> Path:
        """
        Merges audio and video streams into a single MP4 file.

        Args:
            video_path: Path to the video stream file (without audio)
            audio_path: Path to the audio stream file
            output_dir: Directory where the merged file will be saved

        Returns:
            Path: The path to the successfully merged media file

        Raises:
            SystemExit: If any error occurs during the merge process,
                       including FFmpeg execution failures or output validation

        Example:
            >>> merged_file = MediaMerger.merge(
            ...     Path("video.mp4"),
            ...     Path("audio.mp3"),
            ...     Path("output/")
            ... )
            >>> print(merged_file)
            PosixPath('output/video.mp4')
        """
        output_file = output_dir / f"{video_path.stem}.mp4"

        command = [
            "ffmpeg",
            "-i", str(video_path),
            "-i", str(audio_path),
            "-c:v", "copy",
            "-c:a", "aac",
            str(output_file)
        ]

        try:
            print(f"\nMerging audio and video into {output_file.name}...")
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.returncode != 0:
                ErrorHandler.exit_with_error(
                    "Failed to merge audio and video:\n" + result.stderr.decode()
                )

            if not output_file.exists() or output_file.stat().st_size == 0:
                ErrorHandler.exit_with_error("Final output file was not created correctly.")

            print("Final media file created successfully.")
            return output_file

        except FileNotFoundError:
            ErrorHandler.exit_with_error("FFmpeg not found. Make sure it is installed and in your PATH.")
        except Exception as err:
            ErrorHandler.exit_with_error(f"An error occurred during merge: {err}")