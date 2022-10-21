def words_sorting(*args):
    result = {}
    total_sum = 0
    final_result = ''

    for item in args:
        ascii_value = 0
        for ch in item:
            ascii_value += ord(ch)
        total_sum += ascii_value

        if item not in result:
            result[item] = ascii_value

    if total_sum % 2 == 0:
        result = sorted(result.items(), key=lambda x: x[0])
    else:
        result = sorted(result.items(), key=lambda x: -x[1])

    for item in result:
        name = item[0]
        final_result += f"{name} - "
        count = item[1]
        final_result += f"{count}\n"
    return final_result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

