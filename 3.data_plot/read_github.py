import requests
# from plotly.graph_objs import bar
from plotly import offline


class Repository_Info:
    def __init__(self, url) -> None:
        self.url = url
        self.links = []
        self.stars = []
        self.labels = []

    def get_repo_info(self):
        headers = {'Accept': 'application/vnd.github.v3+json'}

        r = requests.get(self.url, headers=headers)
        # print(type(r))
        # # print(r.status_code)

        r_json = r.json()
        # print(r_json.keys())
        # print("total_count:", r_json['total_count'])
        # print("incomplete_results:", r_json['incomplete_results'])

        items = r_json['items']
        # print("items number:", len(items))

        # print("\nItems summary:\n")
        for item in items:
            name = item['name']
            url = item['html_url']
            link = f"<a href='{url}'>{name}</a>"
            self.links.append(link)

            self.stars.append(item['stargazers_count'])

            owner = item['owner']['login']
            description = item['description']
            label = f"{owner}<br />{description}"
            self.labels.append(label)

            # print("item_0 keys number:", len(item.keys()))
            # print("item_0 keys:", item_0.keys())
            # print(f"name: {item['name']}")
            # print(f"owner: {item['owner']['login']}")
            # print(f"stars: {item['stargazers_count']}")
            # print(f"description:{item['description']}\n")

        return self

    def get_rate_limit_info(self):
        url = 'https://api.github.com/rate_limit'
        headers = {'Accept': 'application/vnd.github.v3+json'}

        r = requests.get(url, headers=headers)
        print(r.status_code)
        print(r.json())


def draw():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    repo = Repository_Info(url)
    info = repo.get_repo_info()

    data = [{
        'type': 'bar',
        'x': info.links,
        'y': info.stars,
        'hovertext': info.labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    layout = {
        'title': 'Github',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14}
            },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14}
            },
    }

    fig = {'data': data, 'layout': layout}
    offline.plot(fig, filename="github.html")


draw()
