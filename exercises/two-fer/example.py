def two_fer(name=""):
    if not name.strip():
        return "One for you, one for me."
    else:
        return "One for {}, one for me.".format(name)
