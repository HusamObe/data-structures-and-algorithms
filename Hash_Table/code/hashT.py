class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Hashtable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        hash_code = 0
        for char in key:
            hash_code = (hash_code + ord(char)) % self.size
        return hash_code

    def set(self, key, value):
        index = self.hash(key)
        if not self.table[index]:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self.hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key '{key}' not found in the hashtable.")

    def has(self, key):
        index = self.hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def keys(self):
        keys_list = []
        for node in self.table:
            current = node
            while current:
                keys_list.append(current.key)
                current = current.next
        return keys_list

def repeated_word(_str):
    _str = _str.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("-", "").replace("–", "")
    
    words = _str.split()
    word_hash = Hashtable()

    for word in words:
        if word_hash.has(word):
            return word
        word_hash.set(word, True)

    return None

print(repeated_word("Once upon a time, there was a brave princess who..."))
print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))

print("----------------------------------------------------------------------------------------------------")

hash_table = Hashtable()
hash_table.set("name", "Husam")
hash_table.set("age", 33)

print("Has 'name':", hash_table.has("name"))  
print("Has 'country':", hash_table.has("country")) 

print("Get 'name':", hash_table.get("name"))  
print("Get 'age':", hash_table.get("age"))  

print("Keys:", hash_table.keys()) 
