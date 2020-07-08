class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.hashtable = [ None ] * capacity
        self.capacity = capacity



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hashtable)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # # of items / total # of slots
        return (len(self.hashtable) - self.hashtable.count(None)) / len(self.hashtable)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        offset = 14695981039346656037
        prime = 1099511628211
        hash_bytes = key.encode("utf-8")
        hash_int = offset
        # print(hash_bytes)
        for byte in hash_bytes:
            hash_int = hash_int ^ byte
            hash_int = hash_int * prime
        
        return hash_int

        


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        #make node
        newNode = HashTableEntry(key, value)

        def searchNodes(cur, key, value):
            
            if cur.key == key:
                # print(f"Editing existing node with key {key} and value {value}")
                cur.value = value #If not empty, search list for matching key
            elif cur.next == None: #if we're at the end of the list, add node and update linked list
                # print(f"Adding new node with key {key} and value {value}")
                if self.get_load_factor() / self.capacity > .7:
                    self.resize(self.capacity * 2)
                cur.next = newNode
            else:
                searchNodes(cur.next, key, value) #move on 


        #If empty slot, add node or update value
        index = self.hash_index(key)
        if self.hashtable[index] == None:

            # print(f"adding new node to blank slot using key {key} and value {value}")
            if self.get_load_factor() / self.capacity > .7:
                    self.resize(self.capacity * 2)
            self.hashtable[index] = newNode
        else:
            searchNodes(self.hashtable[index], key, value)
            
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        def printWarning():
            print("This is a warning")

        def searchNodes(cur, prev, key):
            if cur.key == key:
                deleteNode(cur, prev, key)
            elif cur.next == None:
                printWarning()
            else:
                searchNodes(cur.next, cur, key)

        def deleteNode(cur, prev, key):
                #if it's the head, make it the new head
                if prev == None:
                    self.hashtable[index] = cur.next
                #if it's the tail, make the prev the new tail
                elif cur.next == None:
                    prev.next = None
                #otherwise, update the references for prev and next
                else:
                    prev.next = cur.next
        

        #find index
        index = self.hash_index(key)

        if self.hashtable[index] == None: #if there is no linked list, print warning
            printWarning()
        else: #search the list and delete
            searchNodes(self.hashtable[index], None, key)

        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        def searchNodes(cur, key):
            if cur.key == key:
                print(cur.value)
                return cur.value
            elif cur.next == None:
                return None
            else:
                return searchNodes(cur.next, key)
        # Your code here
        index = self.hash_index(key)

        #if index is none, return None
        if self.hashtable[index] == None:
            return None
        #if linked list, search
        else:
            searchNodes(self.hashtable[index], key)

       


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        #save old hashlist 
        oldArray = self.hashtable

        #create a new array with double the capacity
        self.capacity = new_capacity
        self.hashtable = [None] * self.capacity


        #populate new array with old hashes

        def rehash_nodes(cur):
            
            #rehash node key/value and add to new array
            self.put(cur.key, cur.value)
            if cur.next != None:
                rehash_nodes(cur.next)

            
        for x in oldArray:
            if x != None:
                rehash_nodes(x)


        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
