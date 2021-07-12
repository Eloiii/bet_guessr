import http.client
import json

connection = None
headers = {'X-Auth-Token': '8b5ac6f1ed9e4855ac4cc68ebd93f7fb'}


def call_api(option):
    connection.request('GET', option, None, headers)
    return json.loads(connection.getresponse().read().decode())


def get_match_data(team1, team2):
    matches = call_api('/v2/matches/')['matches']
    for match in matches:
        if (match['awayTeam']['name'] == team1 and match['homeTeam']['name'] == team2) or (match['awayTeam']['name'] == team2 and match['homeTeam']['name'] == team1):
            return match


if __name__ == '__main__':
    connection = http.client.HTTPConnection('api.football-data.org')
    print(json.dumps(get_match_data("England", "Italy"), indent=4, sort_keys=True))
