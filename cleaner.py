def clean_data(data):
    result = []

    for row in data[1:]:
        result.append(float(row))

    return result