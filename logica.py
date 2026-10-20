def calcular_estadisticas_notas(notas):
    if len(notas) == 0:
        return {
            "total": 0,
            "promedio": 0.0,
            "aprobados": 0,
            "reprobados": 0,
            "nota_maxima": 0.0,
            "nota_minima": 0.0
        }

    total = len(notas)
    suma = 0
    aprobados = 0
    reprobados = 0
    for nota in notas:
        suma += nota
        if nota >= 3.0:
            aprobados += 1
        else:
            reprobados += 1

    return {
        "total": total,
        "promedio": round(suma / total, 2),
        "aprobados": aprobados,
        "reprobados": reprobados,
        "nota_maxima": max(notas),
        "nota_minima": min(notas)
    }
