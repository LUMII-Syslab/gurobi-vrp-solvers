from typing import List, Tuple

import folium
from IPython.display import display


def map_a_tour(
    tour: List[int],
    addresses: List[Tuple[float, float]]
) -> None:
    lithuania_map = folium.Map(location=[55, 24], zoom_start=8)

    # Get a list of addresses respective to the locations in the tour
    points = [addresses[location] for location in tour]

    # Add the locations on the folium map
    folium.PolyLine(points).add_to(lithuania_map)

    # Display the map to the Jupyter Notebook
    display(lithuania_map)
