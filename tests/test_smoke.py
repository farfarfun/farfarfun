# 注意：此测试保持最小化。
#
# farfarfun 顶层包只有空的 __init__.py，没有子模块；此冒烟测试只验证
# 包能够正常导入。
import farfarfun


def test_import_farfarfun():
    assert farfarfun is not None
