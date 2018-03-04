"""
given

    4
A-----B
|   / |
2| 1/  |1
| /   |
|/    |
C------D
   3

expected

A     B
|   / |
2| 1/  |1
| /   |
|/    |
C      D
"""
simple_mst = {
    'edges': {
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('C', 'B', 1),
        ('B', 'D', 1),
        ('C', 'D', 3),
    },
    'expected': {
        ('B', 'D', 1),
        ('C', 'B', 1),
        ('A', 'C', 2),
    }
}

# https://www.maplesoft.com/applications/view.aspx?SID=5087&view=html
cost_mst = {
    'edges': {
        (1, 2, 5), (1, 3, 9), (1, 4, 20), (1, 5, 4), (1, 8, 14), (1, 9, 15),
        (2, 1, 5), (2, 3, 6), (3, 1, 9), (3, 2, 6), (3, 4, 15), (3, 5, 10),
        (4, 1, 20), (4, 3, 15), (4, 5, 20), (4, 6, 7), (4, 7, 12), (5, 1, 4),
        (5, 3, 10), (5, 4, 20), (5, 6, 3), (5, 7, 5), (5, 8, 13), (5, 9, 6),
        (6, 4, 7), (6, 5, 3), (7, 4, 12), (7, 5, 5), (7, 8, 7), (8, 1, 14),
        (8, 5, 13), (8, 7, 7), (8, 9, 5), (9, 1, 15), (9, 5, 6), (9, 8, 5)
    },
    'expected': {
        (2, 1, 5), (3, 2, 6), (5, 1, 4), (6, 4, 7),
        (6, 5, 3), (7, 5, 5), (9, 5, 6), (9, 8, 5),
    }
}

# https://www.maplesoft.com/applications/view.aspx?SID=5087&view=html
cities_mst = {
    'edges': {
        ("Omaha", "Chicago", 5),
        ("Omaha", "St Louis", 6),
        ("St Louis", "Chicago", 5),
        ("St Louis", "Cincinatti", 6),
        ("Chicago", "Boston", 11),
        ("Chicago", "New York", 9),
        ("Chicago", "Pittsburgh", 7),
        ("Chicago", "Cincinatti", 5),
        ("Chicago", "Memphis", 6),
        ("Boston", "New York", 3),
        ("New York", "Pittsburgh", 5),
        ("New York", "Washington DC", 5),
        ("Pittsburgh", "Washington DC", 5),
        ("Pittsburgh", "Atlanta", 7),
        ("Pittsburgh", "Cincinatti", 4),
        ("Washington DC", "Cincinatti", 6),
        ("Washington DC", "Atlanta", 4),
        ("Washington DC", "Miami", 8),
        ("Cincinatti", "Atlanta", 6),
        ("Cincinatti", "Memphis", 6),
        ("Memphis", "Atlanta", 7),
        ("Memphis", "New Orleans", 4),
        ("New Orleans", "Atlanta", 6),
        ("Atlanta", "Miami", 6)
    },
    'expected': {
        ('Omaha', 'Chicago', 5),
        ('St Louis', 'Chicago', 5),
        ('Chicago', 'Cincinatti', 5),
        ('Boston', 'New York', 3),
        ('New York', 'Washington DC', 5),
        ('Pittsburgh', 'Washington DC', 5),
        ('Pittsburgh', 'Cincinatti', 4),
        ('Washington DC', 'Atlanta', 4),
        ('Memphis', 'New Orleans', 4),
        ('New Orleans', 'Atlanta', 6),
        ('Atlanta ', 'Miami', 6),
    }
}
