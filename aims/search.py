def search_by_title(items, title):
    results = []
    for item in items:
        # Tìm kiếm không phân biệt hoa thường
        if title.lower() in item.title.lower():
            results.append(item)
    return results