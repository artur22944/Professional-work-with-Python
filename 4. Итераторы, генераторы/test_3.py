class FlatIterator:

    def __init__(self, list_of_list):

        self.list_of_list = list_of_list
        self.list_of_list_len = len(self.list_of_list)
        self.list_of_list_counter = -1
        self.temp_list = []

    def __iter__(self):

        return self

    def __next__(self):
        while True:
            if len(self.temp_list):
                return self.temp_list.pop(-1)
            else:
                self.list_of_list_counter += 1
                if self.list_of_list_counter >= self.list_of_list_len:
                    raise StopIteration
                i = self.list_of_list[self.list_of_list_counter]
                if isinstance(i, list):
                    if not len(i):
                        continue
                    self.temp_list = list(FlatIterator(i))
                    self.temp_list = self.temp_list[::-1]
                    return self.temp_list.pop(-1)
                return i


def test_3():

    list_of_lists_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_2),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"],
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
        "!",
    ]


if __name__ == "__main__":
    test_3()
