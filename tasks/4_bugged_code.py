"""
1.Что значит ошибка list index out of range?
Ответ: выход за границы списка
2. Почему при первом запуске функция работает корректно, а при втором — нет?
Ответ: При первом запуске функция удаляет из списка последний элемент и
возвращает элемент списка с индексом <1>. Список - изменяемый объект, поэтому
функция "портит" дефолтный список.
При повторном вызове список еще раз уменьшается, и элемент с индексом <1>
уже не существует, что вызывает ошибку IndexError.
"""

DEFAULT_USER_COUNT = 3


def delete_and_return_last_user(region, default_list=['A100', 'A101', 'A102']):
    """
    Удаляет из списка default_list последнего пользователя
    и возвращает ID нового последнего пользователя.
    """
    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)
    return default_list[DEFAULT_USER_COUNT - 2]
    # return default_list[-1]


print(delete_and_return_last_user(1))
print(delete_and_return_last_user(1))
