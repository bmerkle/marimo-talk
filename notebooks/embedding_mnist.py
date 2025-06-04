import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""# Embedding MNIST""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    Here's an **embedding of MNIST**: each point represents a digit,
    with similar digits close to each other.
    """
    )
    return


@app.cell
def _(mo):
    quadratic = mo.ui.switch(value=False, label="Spectral embedding?")
    quadratic
    return (quadratic,)


@app.cell
def _(args, compute_embedding, constraint, embedding_dimension, mo):
    with mo.persistent_cache("embedding"):
        embedding = compute_embedding(embedding_dimension, constraint, args.quadratic)
    return (embedding,)


@app.cell
def _(alt, df, mo):
    alt_chart = (
        alt.Chart(df)
        .mark_circle(size=4)
        .encode(
            x=alt.X("x:Q").scale(domain=(-2.5, 2.5)),
            y=alt.Y("y:Q").scale(domain=(-2.5, 2.5)),
            color=alt.Color("digit:N"),
        )
        .properties(width=500, height=500)
    )

    chart = mo.ui.altair_chart(
        alt_chart,
        chart_selection="interval",
    )
    chart
    return alt_chart, chart


@app.cell
def _(alt_chart):
    alt_chart.save("embedding.html")
    return


@app.cell
def _(chart, mo):
    table = mo.ui.table(chart.value)
    return (table,)


@app.cell
def _(chart, mo, show_images, table):
    # mo.stop() prevents this cell from running if the chart has
    # no selection
    mo.stop(not len(chart.value))

    # show 10 images: either the first 10 from the selection, or the first ten
    # selected in the table
    selected_images = (
        show_images(list(chart.value["index"]))
        if not len(table.value)
        else show_images(list(table.value["index"]))
    )

    mo.md(
        f"""
        **Here's a preview of the images you've selected**:

        {mo.as_html(selected_images)}

        Here's all the data you've selected.

        {table}
        """
    )
    return


@app.cell
def _(pymde):
    embedding_dimension = 2
    constraint = pymde.Standardized()
    return constraint, embedding_dimension


@app.cell
def _(embedding, mnist, pd, torch):
    indices = torch.randperm(mnist.data.shape[0])[:20000].numpy()
    embedding_sampled = embedding.numpy()[indices]

    df = pd.DataFrame(
        {
            "index": indices,
            "x": embedding_sampled[:, 0],
            "y": embedding_sampled[:, 1],
            "digit": mnist.attributes["digits"][indices],
        }
    )
    return (df,)


@app.cell
def _(mnist, mo, pymde, torch):
    def compute_embedding(embedding_dim, constraint, quadratic=False):
        mo.output.append(
            mo.md("Your embedding is being computed ... hang tight!").callout(
                kind="warn"
            )
        )

        mde = pymde.preserve_neighbors(
            mnist.data,
            attractive_penalty=pymde.penalties.Log1p
            if not quadratic
            else pymde.penalties.Quadratic,
            repulsive_penalty=pymde.penalties.Log if not quadratic else None,
            embedding_dim=embedding_dim,
            constraint=constraint,
            device="cuda" if torch.cuda.is_available() else "cpu",
            verbose=True,
        )
        X = mde.embed(verbose=True)
        mo.output.clear()
        return X
    return (compute_embedding,)


@app.cell
def _(pymde):
    mnist = pymde.datasets.MNIST()
    return (mnist,)


@app.cell
def _(mnist, plt):
    def show_images(indices, max_images=10):
        indices = indices[:max_images]
        images = mnist.data.reshape((-1, 28, 28))[indices]
        fig, axes = plt.subplots(1, len(indices))
        fig.set_size_inches(12.5, 1.5)
        if len(indices) > 1:
            for im, ax in zip(images, axes.flat):
                ax.imshow(im, cmap="gray")
                ax.set_yticks([])
                ax.set_xticks([])
        else:
            axes.imshow(images[0], cmap="gray")
            axes.set_yticks([])
            axes.set_xticks([])
        plt.tight_layout()
        return fig
    return (show_images,)


@app.cell
def _(quadratic):
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-q", "--quadratic", action="store_true", default=quadratic.value
    )
    args = parser.parse_args()
    return (args,)


@app.cell
def _():
    import functools

    import matplotlib.pyplot as plt
    import pymde
    import torch
    return plt, pymde, torch


@app.cell
def _():
    import altair as alt
    return (alt,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    CACHE = __file__
    return


@app.cell
def _():
    import os

    CACHE_NAME = os.path.splitext(os.path.basename(__file__))[0]
    return


if __name__ == "__main__":
    app.run()
