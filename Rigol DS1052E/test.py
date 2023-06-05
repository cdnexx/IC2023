def get_prefix(value):
    pre_number = str(value).split("e")[0]
    number = "Error"
    if "1" in pre_number:
        number = "1"
    elif "2" in pre_number:
        number = "2"
    elif "5" in pre_number:
        number = "5"

    prefix = {
        5e+01: "0 ",
        2e+01: "0 ",
        1e+01: "0 ",
        5e+00: " ",
        2e+00: " ",
        1e+00: " ",
        5e-01: "00 m",
        2e-01: "00 m",
        1e-01: "00 m",
        5e-02: "0 m",
        2e-02: "0 m",
        1e-02: "0 m",
        5e-03: " m",
        2e-03: " m",
        1e-03: " m",
        5e-04: "00 u",
        2e-04: "00 u",
        1e-04: "00 u",
        5e-05: "0 u",
        2e-05: "0 u",
        1e-05: "0 u",
        5e-06: " u",
        2e-06: " u",
        1e-06: " u",
        5e-07: "00 n",
        2e-07: "00 n",
        1e-07: "00 n",
        5e-08: "0 n",
        2e-08: "0 n",
        1e-08: "0 n",
        5e-09: " n",
    }

    return f"{number}{prefix[value]}"


scale_value = {
    1: 5e+01,
    2: 2e+01,
    3: 1e+01,
    4: 5e+00,
    5: 2e+00,
    6: 1e+00,
    7: 5e-01,
    8: 2e-01,
    9: 1e-01,
    10: 5e-02,
    11: 2e-02,
    12: 1e-02,
    13: 5e-03,
    14: 2e-03,
    15: 1e-03,
    16: 5e-04,
    17: 2e-04,
    18: 1e-04,
    19: 5e-05,
    20: 2e-05,
    21: 1e-05,
    22: 5e-06,
    23: 2e-06,
    24: 1e-06,
    25: 5e-07,
    26: 2e-07,
    27: 1e-07,
    28: 5e-08,
    29: 2e-08,
    30: 1e-08,
    31: 5e-09
}

for i in range(1, 32):
    get_prefix(scale_value[i])
