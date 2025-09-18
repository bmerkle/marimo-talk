import marimo

__generated_with = "0.15.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Outline""")
    return


@app.cell
def _(mo):
    (
        mo.md(
            """
            # Marimo Magic: 

            # A New Era of Python Notebooks for Explorers and Engineers
            """
        ),
        mo.md("next-gen reactive Python notebook"),
        mo.md("app-like interactivity"),
        mo.md("no reruns, instant updates"),
        mo.image(src="public/marimo-logo-v2.png", width=110).style(
            padding_top="3rem"
        ),
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# About me""")
    return


@app.cell
def _(mo):
    (
        mo.image(src="pictures-sick/sick-logo-and-me.png")
    )
    return


@app.cell
def _(mo):
    (
        mo.image(src="pictures-sick/sick-google-street-view-1.png")
    )
    return


@app.cell
def _(mo):
    (
        mo.image(src="pictures-sick/sick-google-street-view-2.png")
    )
    return


@app.cell
def _(mo):
    (
        mo.image(src="pictures-sick/sick-google-street-view-3.png")
    )
    return


@app.cell
def _(mo):
    (
        mo.image(src="pictures-sick/sick-airport-1.png")
    )
    return


@app.cell
def _(mo):
    (
        mo.image(src="pictures-sick/sick-airport-2.png")
    )
    return


@app.cell
def _(mo):
    (
        mo.image(src="pictures-sick/sick-airport-3.png")
    )
    return


@app.cell
def _(mo):
    (
        mo.image(src="pictures-sick/sick-airport-4.png")
    )
    return


@app.cell
def _(mo):
    (
        mo.image(src="pictures-sick/sick-airport-5.png")
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Marimo""")
    return


@app.cell(hide_code=True)
def _(mo):
    (
        mo.md(
            """
            # marimo: a next-generation Python notebook
            """
        ),
        mo.md("open source"),
        mo.md("stored as Python (version with Git!)"),
        mo.md("reproducible"),
        mo.md("share as apps"),
        mo.md("run as scripts"),
        mo.md("SQL built-in"),
        mo.md("connect to databases and catalogs"),
        mo.md("AI-native"),
        mo.image(src="public/marimo-logo-v2.png", width=110).style(
            padding_top="3rem"
        ),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## A new kind of Python notebook

    Unlike traditional notebooks, marimo notebooks are **maintainable** Python programs with **reproducible** execution semantics that can be **reused** as:

    1. ::lucide:circle-play:: a reactive notebook, with interactive elements built-in; caching, lazy execution, and parallelization for expensive notebooks
    2. ::lucide:file-code-2:: a Python script, importable as a module, tight integration with uv for package management
    3. ::lucide:mouse-pointer-click:: an interactive web app, deployable on a server or shareable as HTML with WASM

    Built **entirely from scratch** — no dependencies on Jupyter or IPython.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Reproducibility: Jupyter notebooks are usually broken

    Of ~1M Jupyter[^1] notebooks on GitHub[^2]:

    * $\approx 24\%$ notebooks were runnable
    * $\approx 4\%$  notebooks on GitHub were reproducible

    Of ~10M Jupyter[^1] notebooks on GitHub[^3]:

    * $\approx 95\%$ in Python2 or Python3, $\approx 5\%$ in R, Julia, etc
    * $\approx 95\%$ notebooks have < 465 LOC
    * $\approx 33\%$ have invalid execution history

    [^1]: with `ipykernel`
    [^2]: _A Large-scale Study about Quality and Reproducibility of Jupyter Notebooks_, Pimental et al, 2019.
    [^3]: https://blog.jetbrains.com/datalore/2020/12/17/we-downloaded-10-000-000-jupyter-notebooks-from-github-this-is-what-we-learned/
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Notebooks have problems""")
    return


@app.cell
def _(mo):
    mo.md(r"""mo.image("public/memes.png")""")
    return


@app.cell
def _(mo):
    (
        mo.md("## Reproducibility"),
        mo.image("public/meme-2.png")
    )
    return


@app.cell
def _(mo):
    (
        mo.md("## Maintainability"),
        mo.image("public/meme-3.png")
    )
    return


@app.cell
def _(mo):
    (
        mo.md("## git diff problems"),
        mo.image("public/meme-4.png")
    )
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""# Marimo fixed notebook shortcomings""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## Reactive runtime

    Each cell is keyed with a unique ID; running the cell registers its code with
    the graph

    **Runtime rule.** When run as a notebook, marimo uses the DAG to keep code and outputs in sync.
    > When a cell is run, all other cells that reference its definitions (its descendants) are also run.

    **State pruning.** When a cell is deleted (or modified), its definitions are removed from kernel memory and its descendants are run.

    **Lazy execution.** Descendants marked as stale instead of run.

    **Control flow.** A runtime function `mo.stop()` that halts execution of the cell (and descendants).

    **Granular re-runs for imports.** Statically determine the set of modules imported by a cell; descendants of "import-only" filtered to unseen imports.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## A social contract

    **The agreement.** 

    marimo notebooks are dataflow graphs on cells, based on statically parsed variable definitions and references.

    marimo imposes a few constraints on your code to ensure that your notebook is a directed acyclic graph (DAG).



    1. No variable redefinitions across cells.
    2. No cycles

    Small learning curve

    Scales for notebooks (LOC)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## A social contract


    **In return, you get a notebook that is:**

    - 🚀 **batteries-included:** replaces `jupyter`, `streamlit`, `jupytext`, `ipywidgets`, `papermill`, and more
    - ⚡️ **reactive**: run a cell, and marimo reactively [runs all dependent cells](https://docs.marimo.io/guides/reactivity.html) or <a href="#expensive-notebooks">marks them as stale</a>
    - 🖐️ **interactive:** [bind sliders, tables, plots, and more](https://docs.marimo.io/guides/interactivity.html) to Python — no callbacks required
    - 🐍 **git-friendly:** stored as `.py` files
    - 🛢️ **designed for data**: query dataframes, databases, warehouses, or lakehouses [with SQL](https://docs.marimo.io/guides/working_with_data/sql.html), filter and search [dataframes](https://docs.marimo.io/guides/working_with_data/dataframes.html)
    - 🔬 **reproducible:** [no hidden state](https://docs.marimo.io/guides/reactivity.html#no-hidden-state), deterministic execution, [built-in package management](https://docs.marimo.io/guides/package_management/)
    - 🏃 **executable:** [execute as a Python script](https://docs.marimo.io/guides/scripts.html), parameterized by CLI args
    - 🛜 **shareable**: [deploy as an interactive web app](https://docs.marimo.io/guides/apps.html) or [slides](https://docs.marimo.io/guides/apps.html#slides-layout), [run in the browser via WASM](https://docs.marimo.io/guides/wasm.html)
    - 🧩 **reusable:** [import functions and classes](https://docs.marimo.io/guides/reusing_functions/) from one notebook to another
    - 🧪 **testable:** [run pytest](https://docs.marimo.io/guides/testing/) on notebooks
    - ⌨️ **a modern editor**: [GitHub Copilot](https://docs.marimo.io/guides/editor_features/ai_completion.html#github-copilot), [AI assistants](https://docs.marimo.io/guides/editor_features/ai_completion.html#using-ollama), vim keybindings, variable explorer, and [more](https://docs.marimo.io/guides/editor_features/index.html)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Marimo usage""")
    return


@app.cell
def _(mo):
    mo.image("public/star-history-2025426.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack(
        [
            mo.md(
                r"""
        ## People use marimo

        1. Data science
        2. Data engineering
        3. Machine learning
        4. Scientific experimentation
        5. Simulation
        6. Prompting LLMs
        7. Runbooks
        8. Threat hunting
        9. Internal tools
        10. Dashboards
        11. Tutorials
        12. Interactive API docs (with WASM)
        13. Presentations
        """
            ),
            mo.hstack(
                [
                    # mo.image(
                    #    "public/blackrock.jpg",
                    #    height=140,
                    #    style={"filter": "grayscale(1)"},
                    # ),
                    mo.image(
                        "public/mozilla.jpg",
                        height=140,
                        style={"filter": "grayscale(1)"},
                    ),
                    mo.image(
                        "public/huggingface.png",
                        height=100,
                        style={"filter": "grayscale(1)"},
                    ),
                    mo.image(
                        "public/cloudflare.png",
                        height=200,
                        style={"filter": "grayscale(1)"},
                    ),
                    mo.image(
                        "public/stanford.png",
                        height=100,
                        style={"filter": "grayscale(1)"},
                    ),
                    mo.image(
                        "public/berkeley.png",
                        height=100,
                        style={"filter": "grayscale(1)"},
                    ),
                ],
                align="center",
                gap=2,
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [mo.md("## People like marimo"), mo.image("public/testimonials.png")]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Marimo features""")
    return


@app.cell
def _(mo):
    leaves = mo.ui.slider(1, 10)
    return (leaves,)


@app.cell(hide_code=True)
def _(leaves, mo):
    mo.md(
        f"""
    ## Interactive elements

    Binding UI elements to global variables connects them to marimo's runtime.

    {leaves}

    {"🍃" * leaves.value}


    > **An interaction rule.** Interacting with a UI element marks for execution all cells that refer to its bound variable but *don't define it*.

    * Each UI element is given a unique ID by the runtime, shared with the frontend.
    * On interaction, runtime searches `globals` for matching `UIElement` objects.
    """
    )
    return


@app.cell
def _():
    from mohtml.components import terminal
    return (terminal,)


@app.cell(hide_code=True)
def _(mo, terminal):
    mo.md(
        f"""
    ## ::lucide:file-code-2:: A Python script

    #### Script execution


    {terminal("python my_notebook.py --batch_size=4096")}


    executes the cells in a topologically sorted order, optionally
    with CLI args.

    #### Reuse as a module

    ```python
    from my_notebook import my_function, my_class
    ```

    #### Other properties

    Each cell is saved as a function mapping referred variables to
    definitions.

    1. Version with Git
    2. Test with pytest
    3. Inline script metadata and configuration
    4. Edit as plaintext files
    """
    )
    return


@app.cell
def _():
    from notebooks.haikus import app as model_comparison
    return (model_comparison,)


@app.cell
async def _(model_comparison):
    model_comparison_result = await model_comparison.embed()
    return (model_comparison_result,)


@app.cell
def _(mo, model_comparison_result):
    mo.vstack(
        [
            mo.md("## ::lucide:mouse-pointer-click:: An interactive web app"),
            model_comparison_result.output,
        ],
        gap=2,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    ## SQL embedding

    SQL supported through an embedding in Python:

    * We parse a dataflow graph on SQL, analagous to Python, by specializing
      Python AST visitor's analysis of `Call` nodes.
    * Python and SQL graphs joined based on return value and referenced variables

    {mo.image("public/sql_cell.png")}

    \[
    \Updownarrow
    \]

    ```python
    mo.sql(
    f'''
    SELECT * FROM df WHERE b < {{max_b_value}}
    '''
    )
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    ## An intermediate representation as a dataflow graph

    1. **Python cells:** a marimo "program" is composed of blocks of Python code.
    2. **Dataflow graph:** marimo wires a dataflow graph on cells, based on variables.
    3. **Runtimes:** marimo lets users run the graph interactively (notebook), as a script, or as a web app.

    {mo.image("public/compiler-v2.png", width="75%")}
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Sources

    [^1]: Marimo team youtube channel: https://www.youtube.com/@marimo-team

    [^2]: Marimo team github repo: https://github.com/marimo-team/marimo

    [^3]: Akshay Agrawal: Marimo Presentation https://github.com/akshayka/marimo-talk

    [^4]: Python notebooks as dataflow graphs: reactive, reproducible, and reusable https://marimo.io/blog/dataflow

    [^5]: _A Large-scale Study about Quality and Reproducibility of Jupyter Notebooks_, Pimental et al, 2019.

    [^6]: https://blog.jetbrains.com/datalore/2020/12/17/we-downloaded-10-000-000-jupyter-notebooks-from-github-this-is-what-we-learned/

    [^7]: https://sick.com

    [^8]: https://maps.google.com
    """
    )
    return


@app.cell
def _(mo):
    (
        mo.md(
            text="""
    ## https://github.com/marimo-team/marimo
    """
        ),
        mo.image("public/marimo-logo-v2.png", width=80).style(padding_top="3rem"),
    )
    return


if __name__ == "__main__":
    app.run()
