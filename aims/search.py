def search_by_title(items, title):
     # Hotfix: Improve search matching logic.
    results = []
    for item in items:
        # Tìm kiếm không phân biệt hoa thường
        if title.lower() in item.title.lower():
            results.append(item)
    return results