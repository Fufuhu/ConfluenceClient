import os
from module.confluence.client import ConfluenceClient

user=os.getenv('CONFLUENCE_USER') # JIRA/ConfluenceのユーザIDを記述します。
password=os.getenv('CONFLUENCE_PASSWORD')# パスワードを記入します。
host=os.getenv('CONFLUENCE_HOST')


client = ConfluenceClient(base_url=host, user=user, password=password)

response = client.get_group_members(group_name="jira-administrators")

# print(response)

results = response.get('results')

for result in results:
    username = result.get('username')
    display_name = result.get('displayName')

    print("{}\t{}".format(display_name, username))