import requests


class ConfluenceClient(object):
    def __init__(self, base_url, user, password, **kwargs):
        """
        param base_url: http://ホスト:ポート/コンテキストパス を記述。
        param user: ユーザ名を記述
        param password: パスワードを記述
        """

        self._base_url = base_url
        self._credential = (user, password)


    _GET_GROUP_MEMBERS_PATH="/rest/api/group/{}/member"
    def get_group_members(self, group_name):
        """
        特定のグループに所属するメンバーを取得
        """

        request_path = self._base_url + self._GET_GROUP_MEMBERS_PATH.format(group_name)

        response = requests.get(url=request_path, auth=self._credential)

        print(str(response))

        return response.json()
