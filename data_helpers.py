import copy
import csv
import itertools
import math


def read_distance_matrix_csv(
    file_path: str = "data/distance_matrix.csv"
):
    # This function expects the data to be in a certain format, for example, for
    #   locations {A, B, ..., Z}:
    #   AA, AB, AC, ..., AZ, BA, BB, BC, ..., BZ, ..., ZA, ZB, ZC, ..., ZZ
    # Function assumes that the data has at least one location

    # Will hold all addresses in order
    # [(56.950559, 24.115600), ...]
    addresses = []
    # Holds all distance column values
    distances = []

    # Helps to record only unique addresses
    record_addresses = True

    with open(file_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        for row in reader:
            # Each row contains 5 values: starting point coordinates (latitude,
            #   longitude), ending point coordinates (latitude, longitude), distance in
            #   meters
            # Transform all list values from str to float, then unpack them into six
            #   variables
            source_lat, source_lon, dest_lat, dest_lon, distance = map(float, row)

            # Destination address as a tuple
            dest = (float(dest_lat), float(dest_lon))

            # Record addresses until we find the first address again, as we don't want
            #   duplicates
            if addresses != [] and addresses[0] == dest:
                record_addresses = False

            if record_addresses:
                addresses.append(dest)

            distances.append(distance)

    num_locations = len(addresses)

    # Dictionary with N * N items
    # {(0, 0): 0.0, (0, 1): 267.314, ...}
    distance_dict = {}

    for i in range(num_locations):
        for j in range(num_locations):
            flat_index = i * num_locations + j
            # Distances in meters as floats
            distance_dict[(i, j)] = distances[flat_index]

    return distance_dict, addresses


def read_customers_csv(file_path: str = "data/customers.csv"):
    customers = []
    with open(file_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        for row in reader:
            # Each row contains 3 values: latitude, longitude, volume
            latitude, longitude, volume = row

            # Let's cast the values from strings into more usable types
            # Latitude and longitude into floats
            latitude = float(latitude)
            longitude = float(longitude)
            # Volume as integer
            volume = int(volume)

            # Add this customer as a dictionary to the final list
            customers.append(
                {
                    "address": (latitude, longitude),
                    "volume": volume
                }
            )
    return customers


def convert_data_to_symmetric(data):
    new_data = copy.deepcopy(data)
    n = int(math.sqrt(len(data)))
    for i, j in itertools.combinations(range(n), 2):
        # This won't go through cases where i == j, but we don't need to change
        #   those, as they are zero
        max_distance = max(data[(i, j)], data[(j, i)])
        new_data[(i, j)] = max_distance
        new_data[(j, i)] = max_distance
    return new_data


def time_str_to_seconds(time_str):
    # Split the time string into three parts and convert them to integer
    hours, minutes, seconds = map(int, time_str.split(":"))
    return hours * 3600 + minutes * 60 + seconds
