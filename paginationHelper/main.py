"""
NOTE: INCOMPLETE. NEEDS REDO
"""

# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if self.item_count() != 0:
            return (self.item_count() // self.items_per_page) + 1
        else:
            return -1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > self.item_count()-1 < 0:
            return -1
        else:
            if page_index == self.page_count():
                return self.item_count() % self.items_per_page
            elif 0 <= page_index < self.page_count():
                return page_index

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        index_start = 0
        index_end = self.items_per_page-1
        index = 0
        if item_index <= 0 or item_index > self.item_count()-1:
            return -1
        for i in range(self.page_count()):
            if index_end >= item_index >= index_start:
                return index
            else:
                index_end += self.items_per_page
                index_start += self.items_per_page
            index += 1
        return index








test_collection = range(1, 11)
helper = PaginationHelper(test_collection, 9)
print(helper.item_count())
print(helper.page_count())
print(helper.page_item_count(2))
print(helper.page_index(1))

print("empty list")
helper = PaginationHelper([], 0)
print(helper.item_count())
print(helper.page_count())
print(helper.page_item_count(0))
