import marimo

__generated_with = "0.15.2"
app = marimo.App()


@app.cell
def _(x):
    y = x + 5
    y
    return (y,)


@app.cell
def _(y):
    z = y + 1
    z
    return


@app.cell
def _():
    x = 42
    x
    return (x,)


if __name__ == "__main__":
    app.run()
