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

__version__ = "1.0.0"

__author__ = "Gavin M. Roy"
__email__ = "gavinr@aweber.com"

__maintainer__ = "Alberto Vara"
__maintainer_email__ = "a.vara.1986@gmail.com"

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
