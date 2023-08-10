from django.core.exceptions import PermissionDenied, SuspiciousOperation


class InvalidSessionKey(SuspiciousOperation):
    """Invalid characters in session key"""

    pass


class SuspiciousSession(SuspiciousOperation):
    """The session may be tampered with"""

    pass


class SessionInterrupted(PermissionDenied):
    """The session was interrupted."""

    pass
