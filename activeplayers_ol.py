import requests
from bs4 import BeautifulSoup
import re
import sys
sys.path.append("./")
import ownersleague_cards_list
import time

teams = {
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

count_all = 0
for team_name, team_url in teams.items():
    print(team_name)
    r = requests.get(team_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    players = soup.find_all(href=re.compile('/bis/players/'))
    count = 0
    for player in players:
        modified_player = (player.getText()).replace('　', '')
        if modified_player in ownersleague_cards_list.cardlist or modified_player == '金子弌大':
            print(modified_player)
            count_all += 1
            count += 1
    print('オーナーズリーグに収録された現役選手：' + str(count) + '人\n')
    time.sleep(1)
print('オーナーズリーグに収録された全チームの現役選手：' + str(count_all) + '人\n')
print('同じ登録名の別の選手が含まれることがあります。')
