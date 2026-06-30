"""QuickBG package exports."""

__all__ = ["__version__", "batch_process", "process_image"]


def __getattr__(name):
    if name in __all__:
        from . import __main__

        return getattr(__main__, name)
    raise AttributeError(f"module 'quickbg' has no attribute {name!r}")
