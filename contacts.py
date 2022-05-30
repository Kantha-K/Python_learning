contacts={
    "number":3,
    "vegfru":[{"name":"carrot","value":1},
    {"name":"apple","value":2},
    {"name":"cucumber","value":3}
    ]
}

for vegfru in contacts["vegfru"]:
    print(vegfru)

for vegfru in contacts["vegfru"]:
    print(vegfru["value"])