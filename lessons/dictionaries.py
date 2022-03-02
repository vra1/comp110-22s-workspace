"""Demonstrations of dictionary capabilities."""

# declaring the type of dictionary
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()

# set a key value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# print a dictionary literal representation
print(schools)

# access a value by its key -- lookup
print(f"UNC has {schools['UNC']} students")

# remove a key value pair froma dictionary
# by its key
schools.pop("Duke")

# Test for the existence of a key

is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")


# update/reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200

print(schools)

# demonstration of dictionary literals
schools = {}  # same as dict()

# alternatively, initialize key value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}

# print(schools["UNCC"])

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")