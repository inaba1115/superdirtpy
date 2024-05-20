import unittest
from datetime import timedelta

from superdirtpy.temporal_context import TemporalContext


class TestTemporalContext(unittest.TestCase):
    def test_elapsed_time(self):
        tctx = TemporalContext(dryrun=True)
        tctx.sleep(timedelta(seconds=0.3))
        self.assertEqual(tctx.elapsed_time(), timedelta(seconds=0.3))

    def test_sleep(self):
        tctx = TemporalContext(dryrun=True)
        tctx.sleep(timedelta(seconds=0.3))
        self.assertEqual(tctx.elapsed_time(), timedelta(seconds=0.3))
        tctx.sleep(timedelta(seconds=0.3))
        self.assertEqual(tctx.elapsed_time(), timedelta(seconds=0.6))

    def test_sleep_until(self):
        tctx = TemporalContext(dryrun=True)
        now = tctx.now()
        tctx.sleep(timedelta(seconds=0.3))
        self.assertEqual(tctx.elapsed_time(), timedelta(seconds=0.3))
        tctx.sleep_until(now + timedelta(seconds=0.6))
        self.assertEqual(tctx.elapsed_time(), timedelta(seconds=0.6))
