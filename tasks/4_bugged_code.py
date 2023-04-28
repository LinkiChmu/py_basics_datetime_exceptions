"""
An example of not using lists as default function values.
Since the list is a mutable data structure, the first time the function is run
it removes the last element from the list.
When called again, the list is decremented again and
the element at the requested index doesn't exist, which raises an IndexError:
'list index out of range'.
"""

DEFAULT_USER_COUNT = 3


def delete_and_return_last_user(region, default_list=['A100', 'A101', 'A102']):
    """Removes the last user from the default_list
    and returns the ID of the new last user.
    """
    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)
    return default_list[DEFAULT_USER_COUNT - 2]


print(delete_and_return_last_user(1))
print(delete_and_return_last_user(1))
