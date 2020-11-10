"""
Consul API Endpoints

"""
from consulate.api.acl import ACL
from consulate.api.agent import Agent
from consulate.api.base import Response
from consulate.api.catalog import Catalog
from consulate.api.coordinate import Coordinate
from consulate.api.event import Event
from consulate.api.health import Health
from consulate.api.kv import KV
from consulate.api.lock import Lock
from consulate.api.session import Session
from consulate.api.status import Status

__all__ = ["ACL", "Agent", "Catalog", "Event", "Health", "KV", "Lock", "Session", "Status", "Response", "Coordinate"]
