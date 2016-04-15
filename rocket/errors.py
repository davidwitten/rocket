class ERROR:
    """Error templates."""

    LOCATION = "%(file)s on line %(line)i"
    
    ERROR = "Error in " + LOCATION + ":\n  %(reason)s"
    SYNTAX = "Syntax error in " + LOCATION + ":\n  Invalid symbol: %(char)s"


class RocketError:
    """Base type for Rocket errors."""

    template = ERROR.ERROR
    
    def __init__(self, file, line):
        """Initialize a new error."""
        self.file = file
        self.line = line

    def __getitem__(self, name):
        return getattr(self, name, None)

    def __str__(self):
        return self.template % self


class RocketSyntaxError(RocketError):
    """Generic syntax error that is raised by the parser."""

    template = ERROR.SYNTAX

    def __init__(self, file, line, char):
        """Initialize the syntax error."""

        super().__init__(file, line)
        self.char = char
        
