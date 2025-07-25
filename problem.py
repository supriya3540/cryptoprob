def caesar_cipher(message, shift, mode='encode'):
    if mode == 'decode':
        shift = -shift
    result = ''
    for char in message:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result


def format_indian_currency(amount):
    num_str = f"{amount:.4f}".rstrip('0').rstrip('.')
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
    else:
        integer_part, decimal_part = num_str, ''

    rev_int = integer_part[::-1]
    parts = [rev_int[:3]]
    for i in range(3, len(rev_int), 2):
        parts.append(rev_int[i:i+2])

    formatted = ','.join(parts)[::-1]
    return formatted + ('.' + decimal_part if decimal_part else '')


def combine_lists(list1, list2):
    combined = sorted(list1 + list2, key=lambda x: x['positions'][0])
    result = []

    for item in combined:
        if not result:
            result.append(item)
            continue

        last = result[-1]
        l1, r1 = last['positions']
        l2, r2 = item['positions']

        overlap = min(r1, r2) - max(l1, l2)
        len_item = r2 - l2

        if overlap > len_item / 2:
            last['values'].extend(item['values'])
        else:
            result.append(item)

    return result


def minimize_loss_efficient(prices):
    year_price = {price: i for i, price in enumerate(prices)}
    sorted_prices = sorted(prices, reverse=True)

    min_loss = float('inf')
    buy_year = sell_year = -1

    for i in range(len(prices) - 1):
        higher = sorted_prices[i]
        lower = sorted_prices[i + 1]
        if year_price[lower] > year_price[higher]:
            loss = higher - lower
            if loss < min_loss:
                min_loss = loss
                buy_year = year_price[higher] + 1
                sell_year = year_price[lower] + 1

    return buy_year, sell_year, min_loss


print("=== Caesar Cipher ===")
msg = "Hello World!"
encoded = caesar_cipher(msg, 3)
decoded = caesar_cipher(encoded, 3, 'decode')
print("Original :", msg)
print("Encoded  :", encoded)
print("Decoded  :", decoded)

print("\n=== Indian Currency Format ===")
number = 123456.7891
formatted = format_indian_currency(number)
print(f"Input: {number} -> Output: {formatted}")

print("\n=== Combine Lists ===")
list1 = [{"positions": [0, 5], "values": [1, 2]}]
list2 = [{"positions": [3, 8], "values": [3, 4]}]
combined_result = combine_lists(list1, list2)
print("Combined Result:", combined_result)

print("\n=== Minimize Loss ===")
prices = [20, 15, 7, 2, 13]
buy_year, sell_year, loss = minimize_loss_efficient(prices)
print(f"Prices: {prices}")
print(f"Buy Year: {buy_year}, Sell Year: {sell_year}, Minimum Loss: {loss}")
