import requests
from bs4 import BeautifulSoup
import re
import sys
sys.path.append("./")
import ownersleague_cards_list
import time

npb_teams = {
    "オリックス・バファローズ" : "http://npb.jp/bis/teams/rst_b.html",
    "埼玉西武ライオンズ" : "http://npb.jp/bis/teams/rst_l.html",
    "千葉ロッテマリーンズ" : "http://npb.jp/bis/teams/rst_m.html",
    "中日ドラゴンズ" : "http://npb.jp/bis/teams/rst_d.html",
    "東京ヤクルトスワローズ" : "http://npb.jp/bis/teams/rst_s.html",
    "東北楽天ゴールデンイーグルス" : "http://npb.jp/bis/teams/rst_e.html",
    "阪神タイガース" : "http://npb.jp/bis/teams/rst_t.html",
    "広島東洋カープ" : "http://npb.jp/bis/teams/rst_c.html",
    "福岡ソフトバンクホークス" : "http://npb.jp/bis/teams/rst_h.html",
    "北海道日本ハムファイターズ" : "http://npb.jp/bis/teams/rst_f.html",
    "横浜DeNAベイスターズ" : "http://npb.jp/bis/teams/rst_db.html",
    "読売ジャイアンツ" : "http://npb.jp/bis/teams/rst_g.html"
}

npb_players = []
activeplayers_count_all = 0
for npb_team_name, npb_team_url in npb_teams.items():
    print(npb_team_name)
    r = requests.get(npb_team_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    npb_players = (soup.find_all(href=re.compile('/bis/players/')))
    activeplayers_count_team = 0
    for npb_player in npb_players:
        npb_player_modified = (npb_player.getText()).replace('　', '')
        if npb_player_modified in ownersleague_cards_list.cardlist or npb_player_modified == '金子弌大':
            print(npb_player_modified)
            activeplayers_count_all += 1
            activeplayers_count_team += 1
    print('オーナーズリーグに収録された現役選手：' + str(activeplayers_count_team) + '人\n')
    time.sleep(1)
print('オーナーズリーグに収録された全チームの現役選手：' + str(activeplayers_count_all) + '人\n')
print('同じ登録名の別の選手が含まれることがあります。')
