# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
YouTube Video Resolution Selection Module.

Provides a comprehensive interface for selecting video resolutions from available streams.
Includes input validation, user-friendly display, and error handling.
"""

class ResolutionSelector:
    """A class for handling video resolution selection from available streams.
    
    Attributes:
        streams (list): List of video stream objects.
        resolutions (list): Unique available resolutions.
    """
    
    def __init__(self, streams):
        """Initialize the ResolutionSelector with available video streams.
        
        Args:
            streams (list): List of video stream objects containing resolution information.
        """
        self.streams = streams
        self.resolutions = self._get_unique_resolutions()
    
    def _get_unique_resolutions(self):
        """Extract unique resolutions from the streams.
        
        Returns:
            list: Sorted list of unique resolution strings.
        """
        resolutions = set()
        for stream in self.streams:
            if stream.resolution:
                resolutions.add(stream.resolution)
        return sorted(resolutions, key=lambda x: int(x[:-1]) if x[:-1].isdigit() else 0)
    
    def display_menu(self):
        """Display the resolution selection menu to the user."""
        print("\nAvailable resolutions:")
        for i, res in enumerate(self.resolutions, 1):
            print(f"{i} - {res}")
    
    def get_user_choice(self):
        """Prompt user to select a resolution.
        
        Returns:
            int: User's menu choice (1-based index).
        
        Raises:
            ValueError: If input cannot be converted to integer.
        """
        try:
            return int(input("Enter the resolution number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            raise
    
    def select_resolution(self):
        """Main method to handle the resolution selection process.
        
        Returns:
            str: The selected resolution.
            
        Raises:
            IndexError: If selected option is out of range.
        """
        self.display_menu()
        choice = self.get_user_choice()
        return self.resolutions[choice - 1]