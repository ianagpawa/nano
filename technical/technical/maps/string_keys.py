"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        hash_val = self.calculate_hash_value(string)
        if hash_val != -1:
            if self.table[hash_val] != None:
                self.table[hash_val].append(string)
            else:
                self.table[hash_val] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_val = self.calculate_hash_value(string)
        if hash_val != -1:
            if self.table[hash_val]:
                if string in self.table[hash_val]:
                    return hash_val
        return -1

    def calculate_hash_value(self, string):
        first = ord(string[0]) * 100
        second = ord(string[1])
        value = first + second
        return value


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
#print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
#print hash_table.lookup('UDACITY')


# Test store
hash_table.store('UDACITY')


# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')

print hash_table.table