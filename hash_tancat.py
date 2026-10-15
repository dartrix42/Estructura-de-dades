# Estats d'una posició de la taula (hash tancat). NO canvieu aquests valors.
LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"

class MyHashMap:
    """Taula de hash amb adreçament obert i sondeig lineal."""

    def __init__(self, cap=13):
        self._table = [[None, None, LLIURE] for _ in range(cap)]   # m posicions
        self._n = 0                  # nombre de claus desades

    def _hash_function(self, key):
        return key % len(self._table)          # h(x) = x % m

    def _resize(self, c: int):
        old_table = self._table
        self._table = [[None, None, LLIURE] for _ in range(c)]
        self._n = 0

        for slot in old_table:
            if slot[2] == OCUPAT:
                self.put(slot[0], slot[1])

    def put(self, key: int, value: int) -> None:
        m = len(self._table)
        h = self._hash_function(key)
        pos_lliure = None

        for i in range(m):
            idx = (h + i) % m
            slot = self._table[idx]

            # Si ja la tenim, actualitzem el valor
            if slot[2] == OCUPAT and slot[0] == key:
                slot[1] = value
                return

            # Guardem la primera posició disponible que trobem
            if slot[2] in (ESBORRAT, LLIURE) and pos_lliure is None:
                pos_lliure = idx

            # Si trobem una LLIURE, la clau no està més endavant
            if slot[2] == LLIURE:
                break

        # Inserim a la primera posició disponible trobada
        self._table[pos_lliure] = [key, value, OCUPAT]
        self._n += 1

        # Redimensionat si superem el factor de càrrega
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def _find(self, key: int):
        m = len(self._table)
        h = self._hash_function(key)

        for i in range(m):
            idx = (h + i) % m
            slot = self._table[idx]

            if slot[2] == OCUPAT and slot[0] == key:
                return idx
            if slot[2] == LLIURE:
                return None

        return None

    def get(self, key: int) -> int:
        pos = self._find(key)
        if pos is not None:
            return self._table[pos][1]
        return -1

    def remove(self, key: int) -> None:
        pos = self._find(key)
        if pos is not None:
            self._table[pos] = [None, None, ESBORRAT]
            self._n -= 1

    def __len__(self):
        return self._n
