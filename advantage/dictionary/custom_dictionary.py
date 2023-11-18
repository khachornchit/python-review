def create_dict(header_rows, body_rows):
    results = []
    for olympics in countries:
        result = dict(zip(headers, olympics))
        results.append(result)

    return results


if __name__ == '__main__':
    headers = ['Capital', 'Food', 'Year']
    countries = [
        ['New York', 'Hot Dog', '1932'],
        ['Sydney', 'Shrimp on the Barbie', '2000'],
        ['Moscow', 'Borscht', '1980'],
        ['London', 'Fish & Chips', '2012'],
        ['Beijing', 'Noodles', '2008'],
        ['Paris', 'Croissant', '2024'],
        ['Tokyo', 'Sushi', '2020'],
        ['Rome', 'Pizza', '1960'],
        ['Rio de Janeiro', 'Feijoada', '2016'],
        ['Berlin', 'Bratwurst', '1936'],
    ]

    results = create_dict(headers, countries)
    print(results)
