def search_by_category(items, category):
    """Tìm kiếm đĩa DVD trong danh sách theo thể loại."""
    return [dvd for dvd in items if dvd.category and category.lower() in dvd.category.lower()]
def search_by_title(items, title):
    results = []
    for item in items:
        # Tìm kiếm không phân biệt hoa thường
        if title.lower() in item.title.lower():
            results.append(item)
    return results