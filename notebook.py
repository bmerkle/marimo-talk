import marimo

__generated_with = "0.15.2"
app = marimo.App(layout_file="layouts/notebook.slides.json")


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

            # A New Era of Python Notebooks <br>for Explorers and Engineers
            """
        ),

        mo.image(src="public/marimo-logo-v2.png", width=110).style(
            padding_top="3rem"
        ),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## marimo: a next-generation Python notebook

    Unlike traditional notebooks, marimo notebooks are  
    - **maintainable** Python programs  
    - with **reproducible** execution semantics  
    - that can be **reused** as:

    1. ::lucide:circle-play:: a reactive notebook, with interactive elements <br> built-in; caching, lazy execution, and parallelization for expensive notebooks
    3. ::lucide:file-code-2:: a Python script, importable as a module, tight integration with uv for package management
    4. ::lucide:mouse-pointer-click:: an interactive web app, deployable on a server or shareable as HTML with WASM

    Built **entirely from scratch** — no dependencies on Jupyter or IPython.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Movitating a new kind of notebook

    ~~Software~~ eats the world (Marc Andreessen)

    **Data** eats the world (raise of AI)


    Number of GitHub repos with Jupyter notbooks **doubled** in 2024  

    AI/data work vs software engineering

    1. Data scientist vs Software Engineer
    2. evaluate datasets, models, algorithm
    3. interatively transform and visualize 
    4. data from CSV, DB, datasets, hold objects in memory

    Notebooks enable this workflow

    Python and Jupyter are dominant (vs. Pluto/Julia, Observable/JS, R)
    """
    )
    return


@app.cell
def _(mo):
    (
        mo.md("## reactive notebook to analyze embeddings"),

        mo.video(src="public/embedding.mp4", autoplay=True, loop=True )
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
        mo.md("maintainable, reproducible, reusable"),
        mo.md("interactive UI elements"),
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
    mo.md(r"""# Notebooks have problems""")
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

    * $\approx 33\%$ have invalid execution history
    * $\approx 95\%$ in Python2 or Python3, $\approx 5\%$ in R, Julia, etc
    * $\approx 95\%$ notebooks have < 465 LOC


    [^1]: with `ipykernel`
    [^2]: _A Large-scale Study about Quality and Reproducibility of Jupyter Notebooks_, Pimental et al, 2019.
    [^3]: https://blog.jetbrains.com/datalore/2020/12/17/we-downloaded-10-000-000-jupyter-notebooks-from-github-this-is-what-we-learned/
    """
    )
    return


@app.cell
def _(mo):
    (
        mo.md("## Reproducibility"),
        mo.image("public/memes.png")
    )
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
def _(mo):
    mo.md(
        r"""
    ## jupyter git diff problems  

    ### workarounds
    - nbstripout: https://github.com/kynan/nbstripout
    - Jupyter nbdime https://github.com/jupyter/nbdime
    - JupyterLab Git extension https://github.com/jupyterlab/jupyterlab-git

    ### remaining issues
    - only pre commit hook (local)
    - everybody has to stick to this rule
    - view diff on GitHub / GitLab server ?!?
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Marimo fixed notebook shortcomings""")
    return


@app.cell
def _(mo):
    (
        mo.md("## reactive notebook"),

        mo.video(src="public/reactive.webm", autoplay=True, loop=True )
    )
    return


@app.cell
def _(mo):
    (
        mo.md("## reactive notebook, no hidden state"),

         mo.video(src="public/delete.webm", autoplay=True, loop=True)
    )
    return


@app.cell
def _(mo):
    (
        mo.md("## reactive notebook, without callbacks"),

        mo.video(src="public/reactive-2.webm", autoplay=True, loop=True)
    )
    return


@app.cell
def _(mo):
    (
        mo.md("## Interactive dataframes."),
        mo.md("Page through, search, filter, and sort millions of rows blazingly fast, no code required."),

         mo.video(src="public/docs-df.mp4", autoplay=True, loop=True)
    )
    return


@app.cell
def _(mo):
    (
        mo.md("## Query data with SQL"),
        mo.md("SQL parser+highlight, query against dataframes, databases, lakehouses, CSVs, Google Sheets."),

        mo.image("public/readme-sql-cell.png")
    )
    return


@app.cell
def _(mo):
    (
    mo.md("## An intermediate representation as a dataflow graph"),

    mo.md("1. **Python cells:** a marimo \"program\" is composed of blocks of Python code."),
    mo.md("2. **Dataflow graph:** marimo wires a dataflow graph on cells, based on variables."),
    mo.md("3. **Runtimes:** marimo lets users run the graph interactively (notebook), as a script, or as a web app."),

    mo.image(src="public/compiler-v2.png", width="75%")   
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## No tracking of (runtime) mutations

    marimo does **not** track mutations

    it makes the dataflow structure **easy for developers to understand**

    it’s possible to implement with 100% **correctness**

    tracking mutations (e.g. list.append()) would require semantic knowledge about mutations and require significant analysis effort


    ## Tracking of package dependencies

    marimo edit --sandbox notebook.py

    creates an isolated environment (a virtual environment) to run the notebook

    dependencies tracked and installed automatically.

    dependencies tracked in the notebook file via inline script metadata, following PEP 723
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


@app.cell
def _(mo):
    mo.md(r"""# Marimo dataflow graph implementation aspects""")
    return


@app.cell
def _(mo):
    (
        mo.md("## Inspiration"),

        mo.center(
            mo.hstack([
                mo.image("public/pluto.png", width=150),
                mo.image("public/observable.png", width=100),
                mo.image("public/jupyter.png", width=100),
                mo.image("public/excel.png", width=150),
            ], gap=3)
        )
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Representation as a dataflow graph

    1. Each cell is a node
    2. an edge u -> v means cell v refers to a variable defined in cell u
    3. Definitions and references are **statically** inferred
    4. No runtime tracking of mutations
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
    ## Constraints and Conventions

    ###Constraints

    The dataflow graph must be a DAG  
    1. No cycles  
    2. No variable redefinitions across cells     
    3. No deleting another cell's variable

    ###Conventions

    Conventions in marimo python  
    1. Local variables start with `_`  
    2. Functions and classes are defined in their own cells  
    3. Cells that define functions or classes should not have side effects
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Implementation

    1. **Parsing**: code -> AST (abstract syntax tree)
    2. **Static analysis**: AST -> DFG (dataflow graph)
        - AST variable definitions and references
        - Scope resolution
        - Graph wiring
        - Constraints checking
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Summary""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Marimo Values 

    1. Embrace Python
    2. Embrace constraints
    3. Simple is better than complex
    4. Easy-to-understand contract between user and marimo
        - short description of constraints
        - unambiguous semantics
        - clear articulation of tradeoffs and value
    5. Design for extensibility
    6. Prefer simplicity
    7. Readability counts
    8. A culture of correctness
    9. Errors should never pass silently
    10. There should be one -- and preferably only one -- obvious way to do it
    """
    )
    return


@app.cell
def _(mo):
    (
        mo.md("## Next Generation Python Notebooks <br>for Explorers and Engineers"),

        mo.video(src="public/marimo.mp4", autoplay=True)
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Sources

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
