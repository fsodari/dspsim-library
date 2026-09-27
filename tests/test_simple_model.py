from dspsim.framework import (
    Clock,
    Context,
    Signal8,
    Signal32,
)
from dspsim_library._library import SimpleModel


def test_simple_model():
    """Test the SimpleModel creation and basic evaluation steps."""
    with Context() as ctx:
        ctx.log_level = "debug"
        with ctx.construct():
            clk = Clock("clk", 10)
            rst = Signal8("rst", 1)
            i = Signal32("i")
            o1 = Signal32("o1")
            o2 = Signal32("o2")

            a = SimpleModel("a")
            # a = SimpleModel("a")
            # b = SimpleModel("b")

        # # Trace functions be called after context timescale is set.
        # a.open_trace(Path("traces") / "a.trace")
        # b.open_trace(Path("traces") / "b.trace")

        # ctx.elaborate()

        # rst.d = 1
        # ctx.run(100)
        # rst.d = 0
        # ctx.run(10)

        # for iter in range(10):
        #     i.d = iter
        #     ctx.run(10)
        #     print(o1.q, o2.q)

        # # print(f"a id: {a.id}, b id: {b.id}")
        # for m in ctx.models:
        #     print(m)

    # dspsim.framework.reset_global_context_factory()
    # dspsim.library.reset_global_context_factory()
