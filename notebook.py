import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import os
    return (os,)


@app.cell
def _(os):
    import pandas
    import pyarrow as pa
    import pyarrow.compute as pc
    import pyarrow.parquet as pq

    from pyiceberg.catalog.rest import RestCatalog
    from pyiceberg.exceptions import NamespaceAlreadyExistsError

    # Define catalog connection details (replace variables)
    WAREHOUSE = os.getenv("WAREHOUSE")
    TOKEN = os.getenv("TOKEN")
    CATALOG_URI = os.getenv("CATALOG_URI")

    # Connect to R2 Data Catalog
    catalog = RestCatalog(
        name="my_catalog",
        warehouse=WAREHOUSE,
        uri=CATALOG_URI,
        token=TOKEN,
    )
    return NamespaceAlreadyExistsError, catalog, pa


@app.cell
def _(NamespaceAlreadyExistsError, catalog):
    # Create default namespace if needed
    try:
        catalog.create_namespace("default")
    except NamespaceAlreadyExistsError:
        pass
    return


@app.cell
def _(pa):
    # Create simple PyArrow table
    df = pa.table(
        {
            "id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
            "score": [80.0, 92.5, 88.0],
        }
    )
    return (df,)


@app.cell
def _(mo):
    create_or_load_table = mo.ui.run_button(label="create or load table")
    create_or_load_table
    return (create_or_load_table,)


@app.cell
def _(catalog, create_or_load_table, df):
    # Create or load Iceberg table
    table = None

    if create_or_load_table.value:
        test_table = ("default", "people")
        if not catalog.table_exists(test_table):
            print(f"Creating table: {test_table}")
            table = catalog.create_table(
                test_table,
                schema=df.schema,
            )
        else:
            table = catalog.load_table(test_table)
    return table, test_table


@app.cell
def _(mo):
    append_table = mo.ui.run_button(label="Append table")
    append_table
    return (append_table,)


@app.cell
def _(append_table, df, mo, table):
    mo.stop(table is None)

    # Append data
    if append_table.value:
        table.append(df)

    scanned = table.scan().to_arrow()
    scanned
    return


@app.cell
def _(mo):
    drop_table = mo.ui.run_button(label="Drop table")
    drop_table
    return (drop_table,)


@app.cell
def _(catalog, drop_table, test_table):
    # Optional cleanup. To run uncomment and run cell
    if drop_table.value:
        print(f"Deleting table: {test_table}")
        catalog.drop_table(test_table)
        print("Table dropped.")
    return


if __name__ == "__main__":
    app.run()
