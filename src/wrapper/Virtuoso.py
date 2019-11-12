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


    def _v2_users(self, page, per_page):
        param = {"page": str(page), "per_page": str(per_page)}
        response = self.__get("/api/v2/users", param)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def v2_users(self, page, per_page):
        json_data = self._v2_users(page, per_page)
        print(json_data)
        for user in json_data:
            print(user["name"])




def main():
    v = Virtuoso()
    v.v2_users(1,20)

    

if __name__ == '__main__':
    main()
