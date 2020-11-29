import requests
from bs4 import BeautifulSoup
import re
import sys
sys.path.append('./')
import ownersleague_cards_list
import time

print('\n')
time.sleep(1)

players_npb = []
count_team_all = 0

def players_team(link, team_name):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    players = soup.find_all(href=re.compile('/bis/players/'))
    count_team = 0
    print(team_name)
    for player in players:
        player_modified = ((player.getText()).replace('　', '').replace('個人年度別成績', ''))
        players_npb.append(player_modified)
        if player_modified in ownersleague_cards_list.cardlist:
            print(player_modified)
            count_team += 1
            global count_team_all
            count_team_all += 1
    print('オーナーズリーグに収録された現役選手：' + str(count_team) + '人\n')
    time.sleep(1)

players_team('http://npb.jp/bis/teams/rst_b.html', 'オリックス・バファローズ')
players_team('http://npb.jp/bis/teams/rst_l.html', '埼玉西武ライオンズ')
players_team('http://npb.jp/bis/teams/rst_m.html', '千葉ロッテマリーンズ')
players_team('http://npb.jp/bis/teams/rst_d.html', '中日ドラゴンズ')
players_team('http://npb.jp/bis/teams/rst_s.html', '東京ヤクルトスワローズ')
players_team('http://npb.jp/bis/teams/rst_e.html', '東北楽天ゴールデンイーグルス')
players_team('http://npb.jp/bis/teams/rst_t.html', '阪神タイガース')
players_team('http://npb.jp/bis/teams/rst_c.html', '広島東洋カープ')
players_team('http://npb.jp/bis/teams/rst_h.html', '福岡ソフトバンクホークス')
players_team('http://npb.jp/bis/teams/rst_f.html', '北海道日本ハムファイターズ')
players_team('http://npb.jp/bis/teams/rst_db.html', '横浜DeNAベイスターズ')
players_team('http://npb.jp/bis/teams/rst_g.html', '読売ジャイアンツ')

print('オーナーズリーグに収録された現役選手の合計：' + str(count_team_all) + '人\n')

count_vol_all = 0
def players_vol(name, cards):
    count_vol = 0
    print(name)
    for name in cards:
        if name in players_npb:
            print(name)
            count_vol += 1
            global count_vol_all
            count_vol_all += 1
    print('現役選手のカード：' + str(count_vol) + '種類\n')
    if count_vol > 0:
        time.sleep(1)

players_vol('OL01', ownersleague_cards_list.OL01)
players_vol('OL02', ownersleague_cards_list.OL02)
players_vol('OL03', ownersleague_cards_list.OL03)
players_vol('OL04', ownersleague_cards_list.OL04)
players_vol('OL05', ownersleague_cards_list.OL05)
players_vol('OL06', ownersleague_cards_list.OL06)
players_vol('OL07', ownersleague_cards_list.OL07)
players_vol('OL08', ownersleague_cards_list.OL08)
players_vol('OL09', ownersleague_cards_list.OL09)
players_vol('OL10', ownersleague_cards_list.OL10)
players_vol('OL11', ownersleague_cards_list.OL11)
players_vol('OL12', ownersleague_cards_list.OL12)
players_vol('OL13', ownersleague_cards_list.OL13)
players_vol('OL14', ownersleague_cards_list.OL14)
players_vol('OL15', ownersleague_cards_list.OL15)
players_vol('OL16', ownersleague_cards_list.OL16)
players_vol('OL17', ownersleague_cards_list.OL17)
players_vol('OL18', ownersleague_cards_list.OL18)
players_vol('OL19', ownersleague_cards_list.OL19)
players_vol('OL20', ownersleague_cards_list.OL20)
players_vol('OL21', ownersleague_cards_list.OL21)
players_vol('OL22', ownersleague_cards_list.OL22)
players_vol('OL23', ownersleague_cards_list.OL23)
players_vol('OL24', ownersleague_cards_list.OL24)

'''
OB選手のみが収録されているため実行しない
players_vol('OLM01', ownersleague_cards_list.OLM01)
players_vol('OLM02', ownersleague_cards_list.OLM02)
players_vol('OLM03', ownersleague_cards_list.OLM03)
'''

players_vol('OLS01', ownersleague_cards_list.OLS01)

players_vol('OLP01', ownersleague_cards_list.OLP01)
players_vol('OLP02', ownersleague_cards_list.OLP02)
players_vol('OLP03', ownersleague_cards_list.OLP03)
players_vol('OLP04', ownersleague_cards_list.OLP04)
players_vol('OLP05', ownersleague_cards_list.OLP05)
players_vol('OLP06', ownersleague_cards_list.OLP06)
players_vol('OLP07', ownersleague_cards_list.OLP07)
players_vol('OLP08', ownersleague_cards_list.OLP08)
players_vol('OLP09', ownersleague_cards_list.OLP09)
players_vol('OLP10', ownersleague_cards_list.OLP10)
players_vol('OLP11', ownersleague_cards_list.OLP11)
players_vol('OLP12', ownersleague_cards_list.OLP12)
players_vol('OLP13', ownersleague_cards_list.OLP13)
players_vol('OLP14', ownersleague_cards_list.OLP14)
players_vol('OLP15', ownersleague_cards_list.OLP15)
players_vol('OLP16', ownersleague_cards_list.OLP16)
players_vol('OLP17', ownersleague_cards_list.OLP17)
players_vol('OLP18', ownersleague_cards_list.OLP18)
players_vol('OLP19', ownersleague_cards_list.OLP19)
players_vol('OLP20', ownersleague_cards_list.OLP20)
players_vol('OLP21', ownersleague_cards_list.OLP21)
players_vol('OLP22', ownersleague_cards_list.OLP22)
players_vol('OLP23', ownersleague_cards_list.OLP23)
players_vol('OLP24', ownersleague_cards_list.OLP24)
players_vol('OLP25', ownersleague_cards_list.OLP25)
players_vol('OLP26', ownersleague_cards_list.OLP26)
players_vol('OLP27', ownersleague_cards_list.OLP27)
players_vol('OLP28', ownersleague_cards_list.OLP28)

players_vol('OLB01', ownersleague_cards_list.OLB01)
players_vol('OLB02', ownersleague_cards_list.OLB02)
players_vol('OLB03', ownersleague_cards_list.OLB03)
players_vol('OLB04', ownersleague_cards_list.OLB04)
players_vol('OLB05', ownersleague_cards_list.OLB05)
players_vol('OLB06', ownersleague_cards_list.OLB06)
players_vol('OLB07', ownersleague_cards_list.OLB07)
players_vol('OLB08', ownersleague_cards_list.OLB08)
players_vol('OLB09', ownersleague_cards_list.OLB09)
players_vol('OLB10', ownersleague_cards_list.OLB10)
players_vol('OLB11', ownersleague_cards_list.OLB11)
players_vol('OLB12', ownersleague_cards_list.OLB12)
players_vol('OLB13', ownersleague_cards_list.OLB13)
players_vol('OLB14', ownersleague_cards_list.OLB14)
players_vol('OLB15', ownersleague_cards_list.OLB15)

players_vol('OLE01', ownersleague_cards_list.OLE01)
players_vol('OLE02', ownersleague_cards_list.OLE02)
players_vol('OLE03', ownersleague_cards_list.OLE03)
players_vol('OLE04', ownersleague_cards_list.OLE04)

print('現役選手のカードの合計：' + str(count_vol_all) + '種類\n')

print('同じ登録名の別の選手が含まれることがあります。\nまた使用しているリストの誤字等により表示される情報が正確でない場合があります。')
