import time
from datetime import datetime, timedelta


class TemporalContext:
    """Context for controlling time.

    TemporalContext holds virtual time and issues sleep.

    Attributes:
        init_vtime (datetime): initial virtual time
        vtime (datetime): current virtual time
        dryrun (bool): whether sleep or communication to server is actually performed
    """

    def __init__(self, dryrun: bool = False) -> None:
        """Initialize TemporalContext.

        Args:
            dryrun: whether sleep or communication to server is actually performed
        """
        init_vtime = datetime.now()
        self.__init_vtime = init_vtime
        self.__vtime = init_vtime
        self.__dryrun = dryrun

    def elapsed_time(self) -> timedelta:
        """Elapsed time from the beginning."""
        return self.__vtime - self.__init_vtime

    def now(self) -> datetime:
        """Current virtual time."""
        return self.__vtime

    def __sleep(self) -> None:
        if self.is_dryrun():
            return
        delta_sec = (self.__vtime - datetime.now()).total_seconds()
        if delta_sec > 0:
            time.sleep(delta_sec)

    def sleep(self, delta: timedelta) -> None:
        """Sleep delta time.

        Args:
            delta: sleep delta
        """
        self.__vtime += delta
        self.__sleep()

    def sleep_until(self, until: datetime) -> None:
        """Sleep until target datetime.

        Args:
            until: target datetime
        """
        self.__vtime = until
        self.__sleep()

    def is_dryrun(self) -> bool:
        """Returns dryrun or not"""
        return self.__dryrun
