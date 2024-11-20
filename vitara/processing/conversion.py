"""
Takes care of converting units from length to time, pixels to wavelength, etc.
"""


def linear_map(
    value: float, old_min: float, old_max: float, new_min: float, new_max: float
):
    """
    For some x in [old_min, old_max], maps proportionally to [new_min, new_max]

    args
    ----
    value: float in [old_min, old_max]
        Value to linearly map from one domain to another
    old_min, old_max: [float, float]
        Original domain
    new_min, new_max: [float, float]
        New domain

    returns
    -------
    mapped_value (float)
    """
    if value < old_min or value > old_max:
        raise ValueError(
            f"Cannot map value {value}; not in range ([{old_min}, {old_max}])"
        )

    mapped_value = (value - old_min) * (new_max - new_min) / (
        old_max - old_min
    ) + new_min
    return mapped_value


def posn_to_time(position_number: int, length_of_position: float):
    """
    Takes a single position and returns the time offset in fs

    args
    ----
    position_number: unsigned int, unitless
    length_of_position: unsigned float, mm

    returns
    -------
    time_offset: float, fs
    """
    if position_number < 0:
        raise ValueError("Cannot convert negative position to time")

    # Every position corresponds to an offset of 2*length_of_position
    # because the stage includes the offset twice
    offset_length = 2 * length_of_position * position_number

    # Convert length to speed of light
    # speed of light = 3 mm / 1e4 fs
    speed_of_light_conversion = 10000 / 3
    return offset_length * speed_of_light_conversion


def map_wavelength(
    pixel_number: float,
    min_wavelength: float,
    wavelength_per_n_pixels: tuple[float, float],
):
    """
    Wraps the linear_map() function to take a pixel number, and maps it onto
    the range [min_wavelength, infinity) at a rate of nanometers_per_x_pixels
    nm per x pixels

    args
    ----
    pixel_number: unsigned float
        Which pixel are we mapping?
    min_wavelength: float
        The wavelength for pixel zero
    wavelength_per_n_pixels: [float, float]
        [0] Rate at which wavelength increases...
        [1] per this many pixels

    returns
    -------
    Wavelength (λ, nm): float
    """

    return min_wavelength + (
        pixel_number * wavelength_per_n_pixels[0] / wavelength_per_n_pixels[1]
    )
