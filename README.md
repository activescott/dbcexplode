# dbc explode

dbcexplode unpacks the source files contained in the notebooks of a Databricks .dbc archive file. Databricks' .dbc archive files can be saved from the Databricks application by exporting a notebook file or folder. You can explode the dbc file directly or unzip the notebooks out of the dbc file explode individual notebooks into readable and immediately usable source files from inside the notebooks.

## Usage
Unpack a dbc archive file directly (potentially containing multiple notebooks):

    python dbcexplode.py ./dbcdir/exported.dbc

Unpack a single notebook file from inside a dbc:

    python dbcexplode.py ./dbcdir/notebook.python

Unpack a folder of notebook files:

    python dbcexplode.py ./dbcdir/


## TODO
- <strike>Unpack the dbc zip archive file directly from the compressed archive.</strike> 
