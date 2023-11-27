from urllib import request


def connectionTest():
    try:
        request.urlopen('http://google.com', timeout=1)
    except Exception:
        import warnings

        warnings.warn(
            "Seems like there's no internet connection."
            " 'http://google.com' cannot be pinged."
            " App will continue to run without connection, but some functions may be missing.",
        )

connectionTest()
