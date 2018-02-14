from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls

from api.views import home, welcome, echo_username

routes = [
    Route('/', 'GET', home),
    Route('/welcome', 'GET', welcome),
    Route('/{user_id}/', 'GET', echo_username),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
