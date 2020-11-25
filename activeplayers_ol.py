import requests
from bs4 import BeautifulSoup
import re
import sys
sys.path.append("./")
import ownersleague_cards_list
import time

r = requests.get("http://npb.jp/bis/teams/rst_b.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_b = soup.find_all(href=re.compile('/bis/players/'))
players_b_formatted = []
for player in players_b:
    players_b_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('オリックス・バファローズ')
count_b = 0
for player in players_b_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_b += 1
print('オーナーズリーグに収録された現役選手：' + str(count_b) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_l.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_l = soup.find_all(href=re.compile('/bis/players/'))
players_l_formatted = []
for player in players_l:
    players_l_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('埼玉西武ライオンズ')
count_l = 0
for player in players_l_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_l += 1
print('オーナーズリーグに収録された現役選手：' + str(count_l) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_m.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_m = soup.find_all(href=re.compile('/bis/players/'))
players_m_formatted = []
for player in players_m:
    players_m_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('千葉ロッテマリーンズ')
count_m = 0
for player in players_m_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_m += 1
print('オーナーズリーグに収録された現役選手：' + str(count_m) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_d.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_d = soup.find_all(href=re.compile('/bis/players/'))
players_d_formatted = []
for player in players_d:
    players_d_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('中日ドラゴンズ')
count_d = 0
for player in players_d_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_d += 1
print('オーナーズリーグに収録された現役選手：' + str(count_d) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_s.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_s = soup.find_all(href=re.compile('/bis/players/'))
players_s_formatted = []
for player in players_s:
    players_s_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('東京ヤクルトスワローズ')
count_s = 0
for player in players_s_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_s += 1
print('オーナーズリーグに収録された現役選手：' + str(count_s) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_e.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_e = soup.find_all(href=re.compile('/bis/players/'))
players_e_formatted = []
for player in players_e:
    players_e_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('東北楽天ゴールデンイーグルス')
count_e = 0
for player in players_e_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_e += 1
print('オーナーズリーグに収録された現役選手：' + str(count_e) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_t.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_t = soup.find_all(href=re.compile('/bis/players/'))
players_t_formatted = []
for player in players_t:
    players_t_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('阪神タイガース')
count_t = 0
for player in players_t_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_t += 1
print('オーナーズリーグに収録された現役選手：' + str(count_t) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_c.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_c = soup.find_all(href=re.compile('/bis/players/'))
players_c_formatted = []
for player in players_c:
    players_c_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('広島東洋カープ')
count_c = 0
for player in players_c_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_c += 1
print('オーナーズリーグに収録された現役選手：' + str(count_c) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_h.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_h = soup.find_all(href=re.compile('/bis/players/'))
players_h_formatted = []
for player in players_h:
    players_h_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('福岡ソフトバンクホークス')
count_h = 0
for player in players_h_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_h += 1
print('オーナーズリーグに収録された現役選手：' + str(count_h) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_f.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_f = soup.find_all(href=re.compile('/bis/players/'))
players_f_formatted = []
for player in players_f:
    players_f_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('北海道日本ハムファイターズ')
count_f = 0
for player in players_f_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_f += 1
print('オーナーズリーグに収録された現役選手：' + str(count_f) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_db.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_db = soup.find_all(href=re.compile('/bis/players/'))
players_db_formatted = []
for player in players_db:
    players_db_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('横浜DeNAベイスターズ')
count_db = 0
for player in players_db_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_db += 1
print('オーナーズリーグに収録された現役選手：' + str(count_db) + '人\n')
time.sleep(1)

r = requests.get("http://npb.jp/bis/teams/rst_g.html")
soup = BeautifulSoup(r.content, 'html.parser')
players_g = soup.find_all(href=re.compile('/bis/players/'))
players_g_formatted = []
for player in players_g:
    players_g_formatted.append((player.getText()).replace('　', '').replace('個人年度別成績', ''))
print('読売ジャイアンツ')
count_g = 0
for player in players_g_formatted:
    if player in ownersleague_cards_list.cardlist:
        print(player)
        count_g += 1
print('オーナーズリーグに収録された現役選手：' + str(count_g) + '人\n')
time.sleep(1)

count_npb = count_b + count_l + count_m + count_d + count_s + count_e + count_t + count_c + count_h + count_f + count_db + count_g
print('オーナーズリーグに収録された全チームの現役選手：' + str(count_npb) + '人\n')

players_npb = players_b_formatted + players_l_formatted + players_m_formatted + players_d_formatted# + players_s_formatted + players_e_formatted + players_t_formatted + players_c_formatted + players_h_formatted + players_f_formatted + players_db_formatted + players_g_formatted

def players_vol(name, cards):
    count = 0
    print(name)
    for name in cards:
        if name in players_npb:
            print(name)
            count += 1
    print('収録された選手のうち現役選手：' + str(count) + '人\n')
    if count > 0:
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

"""
OB選手のみが収録されているため実行しない
players_vol('OLM01', ownersleague_cards_list.OLM01)
players_vol('OLM02', ownersleague_cards_list.OLM02)
players_vol('OLM03', ownersleague_cards_list.OLM03)
"""

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

print('同じ登録名の別の選手が含まれることがあります。\nまた使用しているリストの誤字等により表示される情報が正確でない場合があります。')
