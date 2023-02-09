
"""This really needs a better name but I'm all out of ideas."""

import json
from urllib.request import urlopen

def coalesce_providers(member_id, strategy="average"):
    data = _get_data_from_providers(member_id)
    
    # Apply the chosen strategy
    if strategy == "average":
        return _coalesce_by_average(data)
    elif strategy == "majority-vote":
        return _coalesce_by_majority_vote(data)
    elif strategy == "minimum":
        return _coalesce_by_minimum(data)
    elif strategy == "maximum":
        return _coalesce_by_maximum(data)

def _get_data_from_providers(member_id):
    r1 = urlopen(f"http://localhost:8000/api1?member_id={member_id}")
    api1 = json.loads(r1.read().decode())
    
    r2 = urlopen(f"http://localhost:8000/api2?member_id={member_id}")
    api2 = json.loads(r2.read().decode())

    r3 = urlopen(f"http://localhost:8000/api3?member_id={member_id}")
    api3 = json.loads(r3.read().decode())

    return api1, api2, api3

def _coalesce_by_average(data):
    result = {}
    for category in data[0]:
        total = 0
        for row in data:
            total += row[category]
        
        result[category] = total / len(data)

    return result

def _coalesce_by_majority_vote(data):
    result = {}
    for category in data[0]:
        values = {}
        for row in data:
            value = row[category]
            if value in values:
                values[value] += 1
            else:
                values[value] = 1
        
        # Ties will go to the larger value
        majority_value = 0
        max_votes = 0

        for v in values:
            if values[v] > max_votes:
                majority_value = v
                max_votes = values[v]
            elif values[v] == max_votes and v > majority_value:
                majority_value = v

        result[category] = majority_value

    return result

def _coalesce_by_minimum(data):
    result = {}
    for category in data[0]:
        values = []
        for row in data:
            values.append(row[category])
        
        result[category] = min(values)

    return result

def _coalesce_by_maximum(data):
    result = {}
    for category in data[0]:
        values = []
        for row in data:
            values.append(row[category])
        
        result[category] = max(values)

    return result