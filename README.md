# dbc explode

dbcexplode will unpack the source files from a Databricks .dbc archive file. Databricks' .dbc archive files can be saved from the Databricks application by exporting a notebook file or folder. Then unzip the dbc files as a zip file into a directory and use this utility to unpack the resulting notebook json files into readable source files that are contained inside each.

## Usage
Unpack a single dbc archive file:

    python dbcexplode.py ./dbcdir/somefile.python

Unpack a folder of dbc files:

    python dbcexplode.py ./dbcdir/


## TODO
- <strike>Unpack the dbc zip archive file directly from the compressed archive.</strike> 