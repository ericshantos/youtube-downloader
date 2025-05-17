# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
YouTube URL validation and error handling module.
"""

import sys
from typing import NoReturn

class ErrorHandler:
    """Centralized error handling system with customizable exit behaviors.
    
    Features:
    - Pre-formatted error messages with visual indicators
    - Categorized error types
    - Customizable exit codes
    - Type-annotated methods
    
    Usage Examples:
        >>> ErrorHandler.exit_with_error("Connection failed")
    """

    ERROR_ICON = "❌"

    @staticmethod
    def exit_with_error(error_msg: str, exit_code: int = 1) -> NoReturn:
        """Terminate program with formatted error message.
        
        Args:
            error_msg: Description of the error condition
            exit_code: System exit code (default: 1)
            
        Raises:
            SystemExit: Always raises this exception to terminate program
            
        Example:
            >>> ErrorHandler.exit_with_error("Database connection timeout", 3)
            ❌ Database connection timeout.
        """
        print(f"\n{ErrorHandler.ERROR_ICON} {error_msg}.\n")
        sys.exit(exit_code)