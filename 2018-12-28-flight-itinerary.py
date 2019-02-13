# This problem was asked by Facebook.

# Given an unordered list of flights taken by someone, each represented as
# (origin, destination) pairs, and a starting airport, compute the person's
# itinerary. If no such itinerary exists, return null. If there are multiple
# possible itineraries, return the lexicographically smallest one. All flights
# must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'),
# ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return
# the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting
# airport 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
# and starting airport 'A', you should return the list
# ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a
# valid itinerary. However, the first one is lexicographically smaller.

from collections import defaultdict


def itinerary(flights, start):
    flight_bank = defaultdict(set)

    for flight in flights:
        flight_bank[flight[0]].add(flight[1])

    valid_itineraries = []

    def recursive_helper(itinerary, available_flight_bank):
        if not itinerary:
            return
        city = itinerary[-1]
        if not available_flight_bank.get(city):
            if len(itinerary) == len(flights) + 1:
                valid_itineraries.append(itinerary)

            recursive_helper(itinerary[:-1], available_flight_bank)
            return

        for destination in available_flight_bank[city]:
            new_bank = dict(available_flight_bank)
            new_city_bank = set(new_bank[city])
            new_city_bank.remove(destination)
            new_bank[city] = new_city_bank
            recursive_helper(itinerary + [destination], new_bank)

    recursive_helper([start], flight_bank)

    return min(valid_itineraries) if valid_itineraries else None


if __name__ == '__main__':
    print(itinerary(
        [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')],
        'A'
    ))

    print(itinerary(
        [('SFO', 'COM'), ('COM', 'YYZ')],
        'COM'
    ))

    print(itinerary(
        [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')],
        'YUL'
    ))
