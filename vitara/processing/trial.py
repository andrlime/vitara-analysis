"""
Wrapper for a single trial that contains all information about the trial
"""

from enum import Enum


class VerticalUnits(Enum):
    WAVELENGTH = 1
    WAVENUMBER = 2

    @staticmethod
    def to_string(units):
        """
        String format some units
        """
        match units:
            case VerticalUnits.WAVELENGTH:
                return "Wavelength (nm)"
            case VerticalUnits.WAVENUMBER:
                return "Frequency (cm$^{-1}$)"
            case _:
                return "**INVALID UNITS**"

    @staticmethod
    def convert_from_wavelength(units, x):
        """
        Convert x to the right units
        """
        match units:
            case VerticalUnits.WAVELENGTH:
                return x
            case VerticalUnits.WAVENUMBER:
                return 1 / (x * (10**-7))
            case _:
                return "**INVALID UNITS**"


class VitaraTrial:
    """
    VitaraTrial

    params
    ------
    folder_name: str
        Folder containing positions and spectrum files
    step_size: float
        How large each step is, in mm
    figure_x_label: str
        Figure x-axis label
    figure_title: str
        Figure title
    min_wavelength: float
        Wavelength at 0 pixels
    wavelength_per_n_pixels: [float, float]
        [0] This many nm per
        [1] This many pixels
    frequency_tick_rate: int
        One tick per X units of frequency (Hz, wavenumber, etc.)
    delay_tick_rate: int
        One tick per X fs delay
    cmap: str
        Colormap
    """

    def __init__(
        self,
        folder_names: str,
        step_size: float,
        figure_x_label: str,
        figure_title: str,
        min_wavelength: float,
        wavelength_per_n_pixels: tuple[float, float],
        x_tick_rate: int,
        y_tick_rate: int,
        vertical_units: VerticalUnits,
        cmap: str = "magma",
    ):
        self.folder_names = folder_names
        self.step_size = step_size
        self.figure_x_label = figure_x_label
        self.figure_title = figure_title
        self.min_wavelength = min_wavelength
        self.wavelength_per_n_pixels = wavelength_per_n_pixels
        self.x_tick_rate = x_tick_rate
        self.y_tick_rate = y_tick_rate
        self.vertical_units = vertical_units
        self.cmap = cmap
