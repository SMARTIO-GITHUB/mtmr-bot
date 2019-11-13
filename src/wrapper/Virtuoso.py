import requests


class Virtuoso:

    def __init__(self):
        pass

    def __get(self, uri, param):
        url = "https://qiita.com" + uri
        params = param
        response = requests.get(url, params=params)
        return response

    def __post(self):
        pass


    def _users(self, page, per_page):
        param = {"page": str(page), "per_page": str(per_page)}
        response = self.__get("/api/v2/users", param)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def users(self, page, per_page):
        json_data = self._v2_users(page, per_page)
        print(json_data)
        for user in json_data:
            print(user["name"])


    def comments_comment(self, comment_id):
        pass
    
    def _comments_comment(self, comment_id):
        pass

    def items_item_comments(self, item_id):
        pass

    def _items_item_comments(self, item_id):
        pass

    def _items(self, page, per_page, query):
        param = {"page": str(page), "per_page": str(per_page), "query": str(query)}
        response = self.__get("/api/v2/items", param=param)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def items(self, query):
        json_data = self._items(1, 100, query)
        print(json_data)


def main():
    v = Virtuoso()
    v.items("python")  

if __name__ == '__main__':
    main()
