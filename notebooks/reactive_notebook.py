import marimo

__generated_with = "0.15.2"
app = marimo.App()


@app.cell
def _():
    x = 1
    return (x,)


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


    return


@app.cell
def _():
    import marimo as mo
    import math
    return math, mo


@app.cell
def _(mo):
    v = mo.ui.slider(1, 20)
    v
    return (v,)


@app.cell
def _(math, mo, v):
    mo.md(f"""$e^{v.value} = {math.exp(v.value):0.3f}$""")
    return


if __name__ == "__main__":
    app.run()
