class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Problema: dati un elenco di interi nums e un intero target,
        # restituire gli indici di due elementi la cui somma è target.
        # I due indici devono essere diversi: lo stesso elemento non può
        # essere usato due volte. L'ordine dei due indici è indifferente.
        # Esempio: nums = [2, 7, 11], target = 9 -> [0, 1].

        prevMap={} # Valore già visitato -> indice nel vettore.

        for i , n in enumerate(nums):
            # Questo è il valore che, sommato a n, produce il target.
            diff= target-n
            if diff in prevMap:
                return [prevMap[diff], i]
            # Inseriamo n dopo la ricerca per non usare due volte lo stesso indice.
            # In caso di valori ripetuti basta conservare l'ultimo indice visto.
            prevMap[n] = i
        # Se non esiste una coppia valida, il metodo restituisce None.
        return


# Logica: per ogni numero n cerchiamo il complemento target - n tra i
# numeri già visitati. Il dizionario associa ciascun valore al suo indice.
# Complessità temporale: O(n) attesa, con n = len(nums), grazie a ricerche
# e inserimenti O(1) in media nel dizionario. Le collisioni hash possono
# peggiorare questo limite.
# Complessità spaziale ausiliaria: O(n) per il dizionario degli indici.
