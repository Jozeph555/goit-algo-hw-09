"""
Модуль для розв'язання задачі видачі решти монетами різного номіналу.

Модуль надає дві реалізації алгоритму видачі решти:
1. Жадібний алгоритм (greedy algorithm)
2. Алгоритм динамічного програмування (dynamic programming)

Обидві реалізації працюють з фіксованим набором монет: [50, 25, 10, 5, 2, 1]
і повертають словник, що показує кількість монет кожного номіналу для видачі решти.
"""

from time import time
from typing import Dict

def find_coins_greedy(amount: int) -> Dict[int, int]:
    """
    Функція реалізує жадібний алгоритм для видачі решти.
    
    Алгоритм завжди вибирає найбільшу можливу монету на кожному кроці.
    
    Args:
        amount (int): Сума решти, яку потрібно видати
        
    Returns:
        Dict[int, int]: Словник, де ключі - номінали монет,
                        значення - кількість монет кожного номіналу
                        
    Raises:
        ValueError: Якщо сума менша за 0
        
    Example:
        >>> find_coins_greedy(113)
        {50: 2, 10: 1, 2: 1, 1: 1}
    """
    if amount < 0:
        raise ValueError("Сума решти не може бути від'ємною")
    
    # Список доступних номіналів монет
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    remaining = amount
    
    # Перебираємо всі номінали монет
    for coin in coins:
        # Якщо поточний номінал можна використати
        if remaining >= coin:
            # Визначаємо кількість монет цього номіналу
            count = remaining // coin
            # Додаємо в результат, якщо кількість більше 0
            if count > 0:
                result[coin] = count
            # Оновлюємо залишок для подальших обчислень
            remaining = remaining % coin
            
        if remaining == 0:
            break
            
    return result

def find_min_coins(amount: int) -> Dict[int, int]:
    """
    Функція реалізує алгоритм динамічного програмування для видачі решти.
    
    Алгоритм знаходить мінімальну кількість монет для видачі вказаної суми.
    
    Args:
        amount (int): Сума решти, яку потрібно видати
        
    Returns:
        Dict[int, int]: Словник, де ключі - номінали монет,
                        значення - кількість монет кожного номіналу
                        
    Raises:
        ValueError: Якщо сума менша за 0
        
    Example:
        >>> find_min_coins(113)
        {50: 2, 10: 1, 2: 1, 1: 1}
    """
    if amount < 0:
        raise ValueError("Сума решти не може бути від'ємною")
    
    coins = [50, 25, 10, 5, 2, 1]
    
    # Створюємо масив для зберігання мінімальної кількості монет
    # для кожної суми від 0 до amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # Зберігаємо останню використану монету для кожної суми
    last_coin = [0] * (amount + 1)
    
    # Для кожної суми від 1 до amount
    for i in range(1, amount + 1):
        # Перебираємо всі доступні монети
        for coin in coins:
            # Якщо поточна монета підходить
            if coin <= i:
                # Якщо використання поточної монети дає кращий результат
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    last_coin[i] = coin
    
    # Відновлюємо результат
    result = {}
    current_amount = amount
    
    # Поки є сума для розбиття
    while current_amount > 0:
        coin = last_coin[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin
        
    return result

def compare_algorithms(amount: int) -> tuple:
    """
    Функція для порівняння часу виконання обох алгоритмів.
    
    Args:
        amount (int): Сума для тестування
        
    Returns:
        tuple: (час жадібного алгоритму, час динамічного програмування)
    """
    # Заміряємо час виконання жадібного алгоритму
    start = time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time() - start
    
    # Заміряємо час виконання алгоритму динамічного програмування
    start = time()
    dp_result = find_min_coins(amount)
    dp_time = time() - start
    
    print(f"\nСума: {amount}")
    print(f"Жадібний алгоритм: {greedy_result}")
    print(f"Час виконання: {greedy_time:.6f} сек")
    print(f"Динамічне програмування: {dp_result}")
    print(f"Час виконання: {dp_time:.6f} сек")
    
    return greedy_time, dp_time

if __name__ == "__main__":
    # Тестування алгоритмів на різних сумах
    test_amounts = [113, 1500, 15000, 150000]
    
    print("Порівняння алгоритмів:")
    for amount in test_amounts:
        compare_algorithms(amount)