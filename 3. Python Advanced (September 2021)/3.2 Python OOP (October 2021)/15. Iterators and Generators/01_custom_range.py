# Submit this is judge for 100/100/100
# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.end:
#             raise StopIteration
#
#         start = self.start
#         self.start += 1
#         return start

# Variant 2
# class custom_range_iterator:
#     def __init__(self, custom_range):
#         self.custom_range = custom_range
#         self.current_number = self.custom_range.start
#
#     def __next__(self):
#         if self.current_number > self.custom_range.end:
#             raise StopIteration
#
#         start = self.current_number
#         self.current_number += 1
#         return start
#
#
# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return custom_range_iterator(self)


# Variant 3
class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for i in range(self.start, self.end + 1):
            yield i


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
