class RocketError:
    """Base type for Rocket errors."""

    template = "Error in %(file)s on line %(line)i: %(reason)s"
    
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

    template = "Syntax Error in %(file)s on line %(line)i: Invalid symbol"

