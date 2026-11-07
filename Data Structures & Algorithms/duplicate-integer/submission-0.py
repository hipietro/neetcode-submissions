class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Problema: dato un elenco di interi nums, restituire True se almeno
        # un valore compare più di una volta; restituire False se tutti
        # i valori sono distinti.
        # Esempi: [1, 2, 1] -> True; [1, 2, 3] -> False.

        hashset = set()
        for n in nums:
            # Il set contiene solo i valori visitati nelle iterazioni precedenti.
            if n in hashset:
                return True
            
            # Registriamo il valore per riconoscerne eventuali ripetizioni.
            hashset.add(n)
        # Abbiamo visitato tutti i numeri senza incontrare duplicati.
        return False


# Logica: memorizziamo i numeri già incontrati in un set. Se un numero è
# già presente, abbiamo trovato un duplicato e possiamo fermarci subito.
# Complessità temporale: O(n) attesa nel caso peggiore della scansione,
# con n = len(nums), perché ricerca e inserimento nel set costano O(1)
# in media. Le collisioni hash possono peggiorare questo limite.
# Complessità spaziale ausiliaria: O(n), se tutti i numeri sono distinti.
