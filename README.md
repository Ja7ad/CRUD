# CRUD
a (Create, Retrieve, Update and Delete) api implementation


### Endpoints:
| #  | url                             | method | description                   | authorization |
|----|---------------------------------|--------|-------------------------------|---------------|
| 1  | /api                            | GET    | api's root                    | YES           |
| 2  | /api/accounts/signup            | POST   | signup with api               | NO            |
| 3  | /api/accounts/signin            | POST   | obtain your Token             | NO            |
| 4  | /api/ads                        | GET    | list of ads                   | YES           |
| 5  | /api/ads                        | POST   | create new ads                | YES           |
| 6  | /api/ad/{ad_id}                 | GET    | get ad by given ad_id         | YES           |
| 7  | /api/ad/{ad_id}                 | PUT    | update ad by given ad_id      | YES           |
| 8  | /api/ad/{ad_id}                 | DELETE | delete ad by given ad_id      | YES           |
| 9  | /api/categories                 | GET    | list of categories            | YES           |
| 10 | /api/category/{category_id}/ads | GET    | find ads by given category_id | YES           |
| 11 | /api/users                      | GET    | list of users                 | YES           |
| 12 | /api/user/{user_id}/ads         | GET    | find ads by given user_id     | YES           |


### Authorization:

##### curl
    curl {URL} -H 'Authorization: Token {YOUR_TOKEN}'
##### httpie
    http {URL} 'Authorization: Token {YOUR_TOKEN}'
##### python's requests module
```python
import requests

url = {URL}
headers = {'Authorization': 'Token {YOUR_TOKEN}'}
r = requests.get(url, headers=headers)
```
