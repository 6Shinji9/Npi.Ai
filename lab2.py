def format_phone_numbers(phone_numbers):
    formatted_numbers = []
    for number in phone_numbers:
        formatted_numbers.append(f"+7 ({number[1:4]}) {number[4:7]}-{number[7:10]}-{number[10:]}")
    return formatted_numbers

# Примеры номеров
phone_numbers = ["79261234567", "79161122334", "79012345678"]
formatted_numbers = format_phone_numbers(phone_numbers)
print(formatted_numbers)
