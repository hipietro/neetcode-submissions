class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Problema: date due stringhe s e t, restituire True se sono
        # anagrammi, cioè se contengono gli stessi caratteri con le stesse
        # frequenze, anche in ordine diverso; altrimenti restituire False.
        # Esempi: "roma" e "amor" -> True; "casa" e "cassa" -> False.

        # Il confronto tra liste verifica sia i caratteri sia le loro ripetizioni.
        return sorted(s) == sorted(t)


# Logica: due stringhe sono anagrammi se contengono gli stessi caratteri
# con le stesse frequenze. Ordinandole otteniamo la stessa sequenza
# esattamente quando questa condizione è rispettata.
# Complessità temporale: O(n log n + m log m), con n = len(s) e m = len(t),
# per i due ordinamenti; il confronto finale è al più lineare.
# Complessità spaziale ausiliaria: O(n + m), perché sorted crea due liste
# di caratteri e l'ordinamento può usare ulteriore memoria lineare.
