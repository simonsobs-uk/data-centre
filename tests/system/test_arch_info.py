from __future__ import annotations

from souk.system.arch_info import System


def test_System():
    """Just test that round-trip is identical.
    I.e. whatever written can be re-created from the written data.
    """
    s = System()
    s2 = System.from_dict(s.data)
    assert s.to_yaml() == s2.to_yaml()
