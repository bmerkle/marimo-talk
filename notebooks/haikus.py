# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.15.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(NUMBER_OF_EXAMPLES, mo):
    get_index, set_index = mo.state(0)


    def increment_index():
        set_index(lambda v: min(v + 1, NUMBER_OF_EXAMPLES - 1))


    def decrement_index() -> int:
        set_index(lambda v: max(0, v - 1))


    next_button = mo.ui.button(label="next", on_change=lambda _: increment_index())
    previous_button = mo.ui.button(
        label="previous", on_change=lambda _: decrement_index()
    )
    return get_index, set_index


@app.cell(hide_code=True)
def _(NUMBER_OF_EXAMPLES, get_index, mo, set_index):
    index = mo.ui.number(
        0,
        NUMBER_OF_EXAMPLES - 1,
        value=get_index(),
        step=1,
        debounce=True,
        label="example number",
        on_change=set_index,
    )
    return (index,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(f"""_Which haiku do you prefer?_""")
    return


@app.cell
def _(mo, num_a_preferred, num_b_preferred):
    mo.md(
        f"""
    Model A: {num_a_preferred * "🍃"}

    Model B: {num_b_preferred * "🍃"}
    """
    )
    return


@app.cell
def _(index):
    index.center()
    return


@app.cell(hide_code=True)
def _(CHOICES_PATH, get_choices, index, mo, write_choices):
    preference = get_choices()[index.value]
    mo.stop(preference is None, mo.md("**Choose the better model**.").center())
    write_choices(get_choices(), CHOICES_PATH)
    mo.md(f"You prefer **model {preference}**.").center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.hstack(
        [
            mo.md("**Model A**"),
            mo.md("**Model B**"),
        ],
        justify="space-around",
    )
    return


@app.cell
def _(CHOICES_PATH, HAIKU_PAIRS, load_choices, mo):
    get_choices, set_choices = mo.state(
        load_choices(CHOICES_PATH, len(HAIKU_PAIRS))
    )
    return get_choices, set_choices


@app.cell(hide_code=True)
def _(index, mo, set_choices):
    model_A = mo.ui.button(
        label="Model A",
        on_change=lambda _: set_choices(
            lambda v: v[: index.value] + ["A"] + v[index.value + 1 :]
        ),
    )

    model_B = mo.ui.button(
        label="Model B",
        on_change=lambda _: set_choices(
            lambda v: v[: index.value] + ["B"] + v[index.value + 1 :]
        ),
    )
    mo.hstack([model_A, model_B], justify="space-around")
    return


@app.cell(hide_code=True)
def _(HAIKU_PAIRS, index, mo):
    model_A_prediction = mo.md(HAIKU_PAIRS[index.value][0])
    model_B_prediction = mo.md(HAIKU_PAIRS[index.value][1])
    return model_A_prediction, model_B_prediction


@app.cell
def _(mo, model_A_prediction, model_B_prediction):
    mo.hstack(
        [model_A_prediction, model_B_prediction], gap=2, justify="space-around"
    )
    return


@app.cell
def _(get_choices):
    num_a_preferred = sum(1 for c in get_choices() if c == "A")
    num_b_preferred = sum(1 for c in get_choices() if c == "B")
    return num_a_preferred, num_b_preferred


@app.cell
def _():
    CHOICES_PATH = "choices.json"
    return (CHOICES_PATH,)


@app.cell
def _(json, os):
    def load_choices(path, number_of_examples):
        # HACK don't preserve to disk for demo
        if not os.path.exists(path) or True:
            return [None for _ in range(number_of_examples)]

        with open(path, "r") as f:
            choices = json.loads(f.read())
        assert len(choices) == number_of_examples
        return choices


    def write_choices(choices, path):
        # Trunacate notes
        with open(path, "w") as f:
            f.write(json.dumps(choices))
    return load_choices, write_choices


@app.cell
def _(random):
    import itertools as it

    haikus = [
        """Code slithers along

    Debugging takes far too long

    My patience is gone""",

        """Indentation woes

    How many spaces? Who knows?

    My anger just grows""",
        """Python's easy, right?

    Until your code doesnt bite

    Up all through the night""",
        """Import this and that

    My program is getting too fat

    Like my neighbor's cat""",
        """Functions call and wait

    Return values come in late

    Debugging is fate""",
        """Lists and dictionaries

    Causing coding injuries

    Solving mysteries""",
        """Object-oriented

    Gets too complicated

    Brain dehydrated""",
        """Exception thrown wide

    Try and except on your side

    Errors can't hide""",
        """Anaconda's might

    Packages install all night

    Code runs? What a sight""",
        """Pythonic and clean

    The most elegant I've seen

    Makes coders keen""",
    ]

    HAIKU_PAIRS = [(h1, h2) for h1, h2 in it.combinations(haikus, 2)]

    random.shuffle(HAIKU_PAIRS)
    random.shuffle(HAIKU_PAIRS)
    return (HAIKU_PAIRS,)


@app.cell
def _(HAIKU_PAIRS):
    NUMBER_OF_EXAMPLES = len(HAIKU_PAIRS)
    return (NUMBER_OF_EXAMPLES,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import json
    import os
    import random
    import textwrap
    import urllib
    return json, os, random


if __name__ == "__main__":
    app.run()
