from mitmproxy import proxy
from mitmproxy import master
from mitmproxy.addons import state

from .. import tutils


class TestState:
    def test_duplicate_flow(self):
        s = state.State()
        fm = master.Master(None, proxy.DummyServer())
        fm.addons.add(s)
        f = tutils.tflow(resp=True)
        fm.load_flow(f)
        assert len(s.flows) == 1

        f2 = s.duplicate_flow(f)
        assert f2.response
        assert len(s.flows) == 2
        assert s.flows.index(f2) == 1
