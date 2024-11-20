"""
Takes care of reading spectrogram data from files into DataFrames
"""

import polars as pl
import numpy as np


def read_spectrum_into_np(filename: str, separator: str = "\t"):
    """
    Reads a spectrum into a Numpy array, with one column for each position.

    The format of the file is one row / position, so there must be a transpose.

    args
    ----
    filename: str
        Filename containing the spectrum data
    separator: str (optional)
        Override tab separator for data sheets to something else, e.g. comma

    returns
    -------
    Polars DataFrame with one unnamed column for each position
    """
    f = open(filename, "r", encoding="utf-8")
    contents = f.read()
    f.close()

    file_as_lines = contents.split("\n")
    lines_with_columns = np.array(
        [row.split(separator) for row in file_as_lines if row != ""]
    )
    casted_to_float = lines_with_columns.astype(float)
    return casted_to_float.T


def read_dataframe(folder_name: str, separator: str = "\t"):
    """
    Reads the positions and spectrum inside `folder_name` into a DataFrame

    args
    ----
    folder_name: str
        Folder containing positions/spectrum as tab separated values sheets
    separator: str (optional)
        Override tab separator for data sheets to something else, e.g. comma

    returns
    -------
    DataFrame[float] with columns for each position
    """
    positions = pl.read_csv(f"{folder_name}/positions", separator=separator)
    spectrum_np_array = read_spectrum_into_np(
        f"{folder_name}/spectrum", separator=separator
    )
    spectrum_np_array /= np.max(spectrum_np_array)
    spectrum = pl.from_numpy(spectrum_np_array)
    spectrum = spectrum.rename(
        {old: new for old, new in zip(spectrum.columns, positions.columns)}
    )

    return spectrum
