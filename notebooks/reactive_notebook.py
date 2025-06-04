

import marimo

__generated_with = "0.13.2"
app = marimo.App()


@app.cell
def _():
    x = 0
    x
    return (x,)


@app.cell
def _(x):
    y = x + 1
    y
    return (y,)


@app.cell
def _(y):
    z = y + 1
    z
    return


if __name__ == "__main__":
    app.run()
