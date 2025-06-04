import marimo

__generated_with = "0.13.7"
app = marimo.App()


@app.cell
def _():
    value = False
    return (value,)


@app.cell
def _(args, mo):
    with mo.persistent_cache("cache_bug"):
        output = args.value

    output
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(value):
    class Unhashable:
        def __eq__(self, other):
            return isinstance(other, Unhashable)

        __hash__ = None  # Makes instances unhashable


    args = Unhashable()
    args.value = value
    return (args,)


@app.cell
def _(args):
    args.value
    return


if __name__ == "__main__":
    app.run()
