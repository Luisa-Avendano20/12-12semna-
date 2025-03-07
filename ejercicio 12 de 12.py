#Crear una matriz 3D para almacenar datos de temperatura
#Primera dimensiòn: Ciudades ( 4 ciudades )
#Segunda  dimensiòn: semanas ( 4 semanas )
#Tercera dimensiòn: dias de la semana ( 7 dias )
temperaturas = [
    [   # Ciudad LA
        [   # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 25.19},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 24.80},
            {"day": "Domingo", "temp": 24.24}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp":25},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 25.91},
            {"day": "Sábado", "temp": 26.19},
            {"day": "Domingo", "temp":25.63 }
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 24.21},
            {"day": "Martes", "temp": 25.91},
            {"day": "Miércoles", "temp": 24.3},
            {"day": "Jueves", "temp": 24.59},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 24.81},
            {"day": "Domingo", "temp": 24.39}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 15.19},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 58},
            {"day": "Sábado", "temp": 98},
            {"day": "Domingo", "temp": 102}
        ],
        [  # Ciudad E
            [  # Semana 1
                {"day": "Lunes", "temp": 23.40},
                {"day": "Martes", "temp": 22.19},
                {"day": "Miércoles", "temp": 23.59},
                {"day": "Jueves", "temp": 23.91},
                {"day": "Viernes", "temp": 23},
                {"day": "Sábado", "temp": 22.80},
                {"day": "Domingo", "temp": 24}
            ],
            [  # Semana 2
                {"day": "Lunes", "temp": 42.8},
                {"day": "Martes", "temp": 24.81},
                {"day": "Miércoles", "temp": 23.91},
                {"day": "Jueves", "temp": 27.9},
                {"day": "Viernes", "temp": 25.19},
                {"day": "Sábado", "temp": 24.39},
                {"day": "Domingo", "temp": 23.51}
            ],
            [  # Semana 3
                {"day": "Lunes", "temp": 40},
                {"day": "Martes", "temp": 25},
                {"day": "Miércoles", "temp": 30},
                {"day": "Jueves", "temp": 59},
                {"day": "Viernes", "temp": 22},
                {"day": "Sábado", "temp": 81},
                {"day": "Domingo", "temp": 43}
            ],
            [  # Semana 4
                {"day": "Lunes", "temp": 19},
                {"day": "Martes", "temp": 26},
                {"day": "Miércoles", "temp": 82},
                {"day": "Jueves", "temp": 97},
                {"day": "Viernes", "temp": 84},
                {"day": "Sábado", "temp": 78},
                {"day": "Domingo", "temp": 12}
            ],
            [  # Ciudad K
                [  # Semana 1
                    {"day": "Lunes", "temp": 29},
                    {"day": "Martes", "temp": 25},
                    {"day": "Miércoles", "temp": 33},
                    {"day": "Jueves", "temp": 62},
                    {"day": "Viernes", "temp": 49},
                    {"day": "Sábado", "temp": 89},
                    {"day": "Domingo", "temp": 44}
                ],
                [  # Semana 2
                    {"day": "Lunes", "temp": 66},
                    {"day": "Martes", "temp": 86},
                    {"day": "Miércoles", "temp": 55},
                    {"day": "Jueves", "temp":70},
                    {"day": "Viernes", "temp": 91},
                    {"day": "Sábado", "temp": 13},
                    {"day": "Domingo", "temp": 14}
                ],
                [  # Semana 3
                    {"day": "Lunes", "temp": 87},
                    {"day": "Martes", "temp": 100},
                    {"day": "Miércoles", "temp": 24},
                    {"day": "Jueves", "temp": 30},
                    {"day": "Viernes", "temp": 22},
                    {"day": "Sábado", "temp": 98},
                    {"day": "Domingo", "temp": 99}
                ],
                [  # Semana 4
                    {"day": "Lunes", "temp": 19},
                    {"day": "Martes", "temp": 86},
                    {"day": "Miércoles", "temp": 22},
                    {"day": "Jueves", "temp": 49},
                    {"day": "Viernes", "temp": 84},
                    {"day": "Sábado", "temp": 78},
                    {"day": "Domingo", "temp": 32}
                ],
     ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad LA", "Ciudad E", "Ciudad K"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
