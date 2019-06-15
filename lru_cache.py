# In this Least Recently Used page replacement algorithm, page will be replaced which is least recently used.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def print_list(self):
        traverse = self.head
        while traverse:
            print(traverse.val)
            traverse = traverse.right


hash_arr = {}
llist = LinkedList()


def lru_cache(requests, page_size):
    cur_size = 0
    page_hits = 0
    page_faults = 0

    for req in requests:
        if req in hash_arr.keys():  # If the request is already present in the memory
            temp = hash_arr[req]
            if temp is llist.head:
                if llist.head.right is not None:
                    llist.head = llist.head.right
                    llist.head.left = None
                    llist.last.right = temp
                    temp.left = llist.last
                    llist.last = temp
                    llist.last.right = None
            elif temp is llist.last:
                pass
            else:
                prev = temp.left
                nextt = temp.right
                prev.right = temp.right
                nextt.left = temp.left
                llist.last.right = temp
                temp.left = llist.last
                llist.last = temp
                llist.last.right = None
            page_hits += 1

        else:  # If the request is not present in the memory
            if cur_size < page_size:
                if llist.head is None:
                    llist.head = Node(req)
                    llist.last = llist.head
                    hash_arr[req] = llist.head
                else:
                    temp = Node(req)
                    llist.last.right = temp
                    temp.left = llist.last
                    llist.last = temp
                    hash_arr[req] = llist.last
                cur_size += 1
            else:
                temp = Node(req)
                llist.last.right = temp
                temp.left = llist.last
                llist.last = temp
                hash_arr[req] = llist.last
                node_to_delete = llist.head
                llist.head = llist.head.right
                llist.head.left = None
                del hash_arr[node_to_delete.val]  # Deleting the node from the hash_arr after deleting from linked list
            page_faults += 1

    print("Page hits : {}".format(page_hits))
    print("Page faults : {}".format(page_faults))
    print("Final requests waiting in page frames(memory) are: ")
    llist.print_list()


# Size of the page limit
frame_size = int(input("Enter page size(page frames): "))

# providing input requests as a list
print("Enter requests as a list")
page_reference = list(map(int, input().split()))

lru_cache(page_reference, frame_size)