# session 1 problems
"""
The sequence is dictated by a 0-indexed string arrival_pattern of length n,
consisting of the characters 'I' meaning the next guest should have a higher
status than the previous one, and 'D' meaning the next guest should have a lower
status than the previous one.

You need to create a 0-indexed string guest_order of
length n + 1 that satisfies the following conditions:

guest_order consists of the digits '1' to '9', where each digit represents
the guest's status and is used at most once.

If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
"""
"""
U: need to arrange people in order of "status", done using the I and D characters
P: 
I: 
"""

def arrange_guest_arrival_order(arrival_pattern):
  pass
