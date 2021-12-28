class Trie:

    def __init__(self):
        self.store = {}

    def insert(self, word: str) -> None:
        self.inner_insert(word, self.store)

    def inner_insert(self, word: str, store: dict):
        l = len(word)

        if l == 1:
            store.setdefault(word, Node(True, {})).set_is_word(True)
            return

        if word[0] not in store:
            store[word[0]] = Node(False, {})
            self.inner_insert(word[1:], store[word[0]].get_store())
        else:
            self.inner_insert(word[1:], store[word[0]].get_store())

    def search(self, word: str) -> bool:
        return self.inner_search(word, self.store)

    def inner_search(self, word, store) -> bool:
        if len(word) == 1:
            return word in store and store[word].is_word()
        if word[0] not in store:
            return False
        return self.inner_search(word[1:], store[word[0]].get_store())

    def startsWith(self, prefix: str) -> bool:
        return self.inner_startsWith(prefix, self.store)

    def inner_startsWith(self, prefix: str, store) -> bool:
        if len(prefix) == 1:
            return prefix in store
        if prefix[0] not in store:
            return False
        return self.inner_startsWith(prefix[1:], store[prefix[0]].get_store())


class Node:
    def __init__(self, is_word, store):
        self._is_word = is_word
        self._store = store

    def get_store(self):
        return self._store

    def set_is_word(self, is_word):
        self._is_word = is_word

    def is_word(self):
        return self._is_word

trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))   # return True
print(trie.search("app"))    # return False
print(trie.startsWith("app")) # return True
print(trie.insert("app"))
print(trie.search("app"))
