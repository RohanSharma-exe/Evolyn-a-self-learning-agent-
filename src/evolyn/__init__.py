"""Evolyn package bootstrap.

Load and normalize Evolyn configuration before importing any optional
infrastructure such as Cognee.
"""

from evolyn.config import settings
from evolyn.core.agent import Evolyn

__all__ = ["Evolyn", "settings"]
