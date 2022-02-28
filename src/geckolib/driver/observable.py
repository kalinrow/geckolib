""" Observable class """

import logging

_LOGGER = logging.getLogger(__name__)


class Observable:
    """Class to manage observables"""

    def __init__(self):
        self._observers = []

    def watch(self, observer):
        """Add an observer to this observable class"""
        self._observers.append(observer)

    def unwatch(self, observer):
        """Remove an observer to this observable class"""
        self._observers.remove(observer)

    def _on_change(self, sender=None, old_value=None, new_value=None):
        """Trigger the change notification for all observers"""
        _LOGGER.debug(
            f"{self.__class__.__name__} {sender} changed from {old_value} to {new_value}"
        )
        for observer in self._observers:
            observer(sender, old_value, new_value)

    @property
    def has_observers(self):
        return self._observers

    def __repr__(self):
        return f"{self.__class__.__name__} watched by={self._observers!r}"
