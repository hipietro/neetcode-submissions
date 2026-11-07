class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Problema: dato un elenco di stringhe strs, raggruppare le parole
        # che sono anagrammi, cioè hanno gli stessi caratteri con le stesse
        # frequenze. Restituire una lista di gruppi che contenga ogni parola
        # dell'elenco iniziale, comprese eventuali ripetizioni.
        # L'ordine dei gruppi e delle parole al loro interno è indifferente.
        # Esempio: ["eat", "tea", "bat"] -> [["eat", "tea"], ["bat"]].

        d = {}
        for word in strs:
            # Ad esempio, "eat" e "tea" diventano entrambe "aet".
            key = "".join(sorted(word))
            if key not in d:
                # La prima parola con questa chiave crea un nuovo gruppo.
                d[key] = []
            # Le parole successive con la stessa chiave si uniscono al gruppo.
            d[key].append(word)
        # Le chiavi servono solo per raggruppare: restituiamo le liste di parole.
        return list(d.values())


# Logica: usiamo come chiave la parola con i caratteri ordinati.
# Gli anagrammi producono la stessa chiave e finiscono nello stesso gruppo.
# Siano n il numero di parole e k la lunghezza massima di una parola.
# Complessità temporale attesa: O(n * k * log k) per k >= 2, poiché ogni
# parola viene ordinata; costruzione e hashing della chiave sono lineari
# nella sua lunghezza. Le operazioni sul dizionario sono O(1) in media,
# escluso il costo dell'hashing; le collisioni possono peggiorare il limite.
# Includendo parole vuote o di un carattere, il limite si può scrivere
# O(n * (1 + k * log(k + 1))).
# Complessità spaziale ausiliaria: O(n * (k + 1)) nel caso peggiore, per
# le chiavi e i riferimenti alle parole nei gruppi, più O(k) temporaneo
# per ordinare una parola. Le stringhe originali non vengono copiate
# nei gruppi. La lista restituita richiede inoltre O(g) riferimenti,
# dove g <= n è il numero di gruppi.
