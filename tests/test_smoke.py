# NOTE: This test is intentionally minimal.
#
# farfarfun's top-level package has an empty __init__.py and no
# submodules; this smoke test only verifies that the package imports
# cleanly.
import farfarfun


def test_import_farfarfun():
    assert farfarfun is not None
