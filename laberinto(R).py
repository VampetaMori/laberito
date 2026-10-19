N = 9
PUNTOS_MIN = 23

LABERINTO = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1],
]

INICIO = (N - 1, 0)
META = (0, 0)

MOVIMIENTOS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def valor(f, c):
    v = LABERINTO[f][c]
    return 1 if v in ('I', 'F') else v


def imprimir_laberinto(titulo="LABERINTO ORIGINAL"):
    print(f"\n{titulo}")
    print("    " + " ".join(f"{c:>2}" for c in range(N)))
    print("    " + "---" * N)

    for f in range(N):
        print(f"{f:>2} |" + " ".join(
            f"{str(LABERINTO[f][c]):>2}" for c in range(N)
        ))


def es_valido(f, c, visitado):
    return (
        0 <= f < N
        and 0 <= c < N
        and valor(f, c) != 0
        and not visitado[f][c]
    )


def resolver(f, c, puntos, visitado, camino):
    if not es_valido(f, c, visitado):
        return False

    puntos += valor(f, c)
    visitado[f][c] = True
    camino.append((f, c))

    if (f, c) == META:
        if puntos >= PUNTOS_MIN:
            return True
    else:
        for df, dc in MOVIMIENTOS:
            if resolver(f + df, c + dc, puntos, visitado, camino):
                return True

    camino.pop()
    visitado[f][c] = False
    return False


def matriz_solucion(camino):
    m = [['.'] * N for _ in range(N)]

    for paso, (f, c) in enumerate(camino, start=1):
        m[f][c] = paso

    return m


def imprimir_matriz(m, titulo):
    print(f"\n{titulo}")
    print("     " + " ".join(f"{c:>3}" for c in range(N)))
    print("     " + "----" * N)

    for f in range(N):
        print(f"{f:>2} | " + " ".join(
            f"{str(m[f][c]):>3}" for c in range(N)
        ))


def main():
    imprimir_laberinto()

    visitado = [[False] * N for _ in range(N)]
    camino = []
    exito = resolver(INICIO[0], INICIO[1], 0, visitado, camino)

    print("\n" + "=" * 60)

    if exito:
        total = sum(valor(f, c) for f, c in camino)

        print("¡EL RATÓN LOGRÓ SALIR DEL LABERINTO!")
        print(f"Puntos acumulados: {total} (mínimo requerido: {PUNTOS_MIN})")
        print(f"Pasos dados: {len(camino)}")

        imprimir_matriz(
            matriz_solucion(camino),
            "MATRIZ SOLUCIÓN (número = orden del paso, '.' = no usada)"
        )

        binaria = [[0] * N for _ in range(N)]

        for f, c in camino:
            binaria[f][c] = 1

        imprimir_matriz(binaria, "MATRIZ BINARIA DEL CAMINO (1 = ruta)")

        print("\nRecorrido (fila, columna):")
        print(" -> ".join(f"({f},{c})" for f, c in camino))

    else:
        print(
            "EL RATÓN NO LOGRÓ SALIR: no existe un camino que sume "
            f"{PUNTOS_MIN} o más puntos."
        )

        imprimir_matriz(
            matriz_solucion([]),
            "MATRIZ SOLUCIÓN (sin camino)"
        )

    print("=" * 60)


if __name__ == "__main__":
    main()