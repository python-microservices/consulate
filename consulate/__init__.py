"""
Consulate: A client library for Consul

"""
import logging
from logging import NullHandler

from consulate.client import Consul
from consulate.exceptions import (
    ACLDisabled,
    ClientError,
    ConsulateException,
    Forbidden,
    LockFailure,
    NotFound,
    RequestError,
    ServerError,
)

# Prevent undesired log output to the root logger
logging.getLogger("consulate").addHandler(NullHandler())

__all__ = [
    "Consul",
    "ConsulateException",
    "ClientError",
    "ServerError",
    "ACLDisabled",
    "Forbidden",
    "NotFound",
    "LockFailure",
    "RequestError",
]
