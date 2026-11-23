"""A client library for accessing HISinOne REST-Webservices"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
