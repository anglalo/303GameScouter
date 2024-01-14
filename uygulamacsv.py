import tkinter as tk
import csv
from bs4 import BeautifulSoup
import requests
import json
import webbrowser

urlcoksatanlarindirim = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&category1=998&os=win&snr=1_7_7_2300_7&specials=1&filter=topsellers&infinite=1'
urlozelfirsatlar = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&category1=998&snr=1_7_7_2300_7&specials=1&infinite=1'
urlyenicikanlar = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=Released_DESC&category1=998&os=win&snr=1_7_7_popularnew_7&filter=popularnew&infinite=1'

urlactionadventure = 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&tags=19%2C21&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlactionadventure1 = 'https://store.steampowered.com/search/results/?query&start=100&count=150&dynamic_data=&sort_by=_ASC&tags=19%2C21&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlactionadventure2 = 'https://store.steampowered.com/search/results/?query&start=200&count=250&dynamic_data=&sort_by=_ASC&tags=19%2C21&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'

urlaction = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=19&snr=1_7_7_240_7&infinite=1'
urlaction1 = 'https://store.steampowered.com/search/results/?query&start=100&count=200&dynamic_data=&sort_by=_ASC&tags=19&snr=1_7_7_240_7&infinite=1'
urlaction2 = 'https://store.steampowered.com/search/results/?query&start=200&count=300&dynamic_data=&sort_by=_ASC&tags=19&snr=1_7_7_240_7&infinite=1'
urlaction3 = 'https://store.steampowered.com/search/results/?query&start=300&count=400&dynamic_data=&sort_by=_ASC&tags=19&snr=1_7_7_240_7&infinite=1'



urlrace = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=699&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlrace1 = 'https://store.steampowered.com/search/results/?query&start=100&count=150&dynamic_data=&sort_by=_ASC&tags=699&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlrace2 = 'https://store.steampowered.com/search/results/?query&start=200&count=250&dynamic_data=&sort_by=_ASC&tags=699&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'


urlbulmaca = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=1664&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlbulmaca1 = 'https://store.steampowered.com/search/results/?query&start=100&count=150&dynamic_data=&sort_by=_ASC&tags=1664&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlbulmaca2 = 'https://store.steampowered.com/search/results/?query&start=200&count=250&dynamic_data=&sort_by=_ASC&tags=1664&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'


urlrpg = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=122&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlrpg1 = 'https://store.steampowered.com/search/results/?query&start=100&count=150&dynamic_data=&sort_by=_ASC&tags=122&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlrpg2 = 'https://store.steampowered.com/search/results/?query&start=200&count=250&dynamic_data=&sort_by=_ASC&tags=122&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'


urldovus = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=1743&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urldovus1 = 'https://store.steampowered.com/search/results/?query&start=100&count=150&dynamic_data=&sort_by=_ASC&tags=1743&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urldovus2 = 'https://store.steampowered.com/search/results/?query&start=200&count=250&dynamic_data=&sort_by=_ASC&tags=1743&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'


urlmuzik = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=1621&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlmuzik1 = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=1621&snr=1_7_7_240_7&infinite=1'
urlmuzik2 = 'https://store.steampowered.com/search/results/?query&start=100&count=200&dynamic_data=&sort_by=_ASC&tags=1621&snr=1_7_7_240_7&infinite=1'



urlshooter = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=1774&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlshooter1 = 'https://store.steampowered.com/search/results/?query&start=100&count=150&dynamic_data=&sort_by=_ASC&tags=1774&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlshooter2 = 'https://store.steampowered.com/search/results/?query&start=2000&count=250&dynamic_data=&sort_by=_ASC&tags=1774&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'


urlplatformer = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=1625&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlplatformer1 = 'https://store.steampowered.com/search/results/?query&start=100&count=150&dynamic_data=&sort_by=_ASC&tags=1625&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlplatformer2 = 'https://store.steampowered.com/search/results/?query&start=200&count=250&dynamic_data=&sort_by=_ASC&tags=1625&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'


urlsimulasyon = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=599&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlsimulasyon1 = 'https://store.steampowered.com/search/results/?query&start=100&count=150&dynamic_data=&sort_by=_ASC&tags=599&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlsimulasyon2 = 'https://store.steampowered.com/search/results/?query&start=200&count=250&dynamic_data=&sort_by=_ASC&tags=599&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'

urlspor = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=701&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlspor1 = 'https://store.steampowered.com/search/results/?query&start=100&count=150&dynamic_data=&sort_by=_ASC&tags=701&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlspor2 = 'https://store.steampowered.com/search/results/?query&start=200&count=250&dynamic_data=&sort_by=_ASC&tags=701&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'

url90s = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=6691&snr=1_7_7_240_7&infinite=1'

urlfps = 'https://store.steampowered.com/search/results/?query&start=50&count=100&dynamic_data=&sort_by=_ASC&tags=1663&snr=1_7_7_240_7&infinite=1'
urlfps1 = 'https://store.steampowered.com/search/results/?query&start=100&count=200&dynamic_data=&sort_by=_ASC&tags=1663&snr=1_7_7_240_7&infinite=1'

urlstrategy = 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=9&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlstrategy1 = 'https://store.steampowered.com/search/results/?query&start=100&count=150&dynamic_data=&sort_by=_ASC&tags=9&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
urlstrategy2 = 'https://store.steampowered.com/search/results/?query&start=200&count=250&dynamic_data=&sort_by=_ASC&tags=9&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1'

urldepo = 'https://store.steampowered.com/search/results/?query&start=250&count=300&dynamic_data=&sort_by=_ASC&os=win&snr=1_7_7_globaltopsellers_7&filter=globaltopsellers&infinite=1'
urldepo1 = 'https://store.steampowered.com/search/results/?query&start=300&count=400&dynamic_data=&sort_by=_ASC&os=win&snr=1_7_7_globaltopsellers_7&filter=globaltopsellers&infinite=1'
urldepo2 = 'https://store.steampowered.com/search/results/?query&start=400&count=500&dynamic_data=&sort_by=_ASC&os=win&snr=1_7_7_globaltopsellers_7&filter=globaltopsellers&infinite=1'
urldepo3 = 'https://store.steampowered.com/search/results/?query&start=500&count=600&dynamic_data=&sort_by=_ASC&os=win&snr=1_7_7_globaltopsellers_7&filter=globaltopsellers&infinite=1'
urldepo4 = 'https://store.steampowered.com/search/results/?query&start=600&count=700&dynamic_data=&sort_by=_ASC&os=win&snr=1_7_7_globaltopsellers_7&filter=globaltopsellers&infinite=1'
urldepo5 = 'https://store.steampowered.com/search/results/?query&start=700&count=800&dynamic_data=&sort_by=_ASC&os=win&snr=1_7_7_globaltopsellers_7&filter=globaltopsellers&infinite=1'
arrurl = [url90s,urlfps,urlfps1,urlaction,urlaction1,urlaction2,urlaction3,urldepo,urldepo1,urldepo3,urldepo4,urldepo5,urlspor,urlspor1,urlspor2,urlstrategy,urlstrategy1,urlstrategy2,urlplatformer,urlplatformer1,urlplatformer2,urlrpg,urlrpg1,urlrpg2,urlsimulasyon,urlsimulasyon1,urlsimulasyon2,urlshooter,urlshooter1,urlshooter2,urlactionadventure,urlactionadventure1,urlactionadventure2,urlrace,urlrace1,urlrace2,urlbulmaca,urlbulmaca1,urlbulmaca2,urlmuzik,urlmuzik1,urlmuzik2,urldovus,urldovus1,urldovus2]


def get_exchangerate():
    url = 'https://open.er-api.com/v6/latest/USD'
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['rates']['TRY']
    return exchange_rate


def convert_totl(price_in_dollars, exchange_rate):
    try:
        price_in_dollars = float(price_in_dollars.replace('$', '').strip())
        price_in_lira = price_in_dollars * exchange_rate
        return f'{price_in_lira:.2f} TL'
    except ValueError:
        return ' '


def get_resp(url):
    response = requests.get(url)
    data = dict(response.json())
    return data['results_html']


def writedata(data, exchange_rate, unique_games):
    soup = BeautifulSoup(data, 'html.parser')
    game_elements = soup.find_all('a')

    games_data = []

    for game in game_elements:
        game_names = game.find('span', {'class': 'title'}).text
        game_link = game['href']

        if game_names not in unique_games:
            game_price_e = game.find('div', {'class': 'discount_final_price'})
            free_games = game.find('div', {'class': 'discount_final_price free'})

            if game_price_e:
                game_prices = convert_totl(game_price_e.text.strip(), exchange_rate)
            else:
                game_prices = 'Ücretsiz'

            if free_games:
                game_prices = free_games.text.strip()

            games_data.append([game_names, game_prices,game_link])
            unique_games.add(game_names)

    return games_data


def write_tocsv(file_path, data, header):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


exchange_rate = get_exchangerate()

all_games_data = []
unique_games = set()

for url in arrurl:
    response = get_resp(url)
    games_data = writedata(response, exchange_rate, unique_games)
    all_games_data.extend(games_data)


csv_file_path = 'games_data.csv'
csv_header = ['Game Name', 'Price (TL)','Store Link']

write_tocsv(csv_file_path, all_games_data, csv_header)

print(f'CSV file created: {csv_file_path}')

class GameSearchApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Game Search App')
        #self.master.configure(bg='#000235')

        self.create_widgets()
        self.load_data()
    def create_widgets(self):
        self.search_label = tk.Label(self.master, text='Search Game:')
        self.search_entry = tk.Entry(self.master)
        self.search_button = tk.Button(self.master, text='Search', command=self.search_game)

        self.canvas = tk.Canvas(self.master, width=500, height=300, borderwidth=2, relief='groove')
        self.canvas.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.result_frame = tk.Frame(self.canvas)
        self.result_frame.pack()

        self.search_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)
    def load_data(self):
        self.data = []
        with open('games_data.csv', mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                self.data.append(row)
    def search_game(self):
        search_term = self.search_entry.get().lower()


        for widget in self.result_frame.winfo_children():
            widget.destroy()

        for row in self.data:
            if search_term in row[0].lower():
                game_name_label = tk.Label(self.result_frame, text=f'Game Name: {row[0]}',font=("Helvetica",12))
                game_price_label = tk.Label(self.result_frame, text=f'Price (TL): {row[1]}', font=("Helvetica",12))

                store_link_button = tk.Button(self.result_frame, text='Store Link', command=lambda r=row[2]: self.open_link(r))

                game_name_label.pack(anchor='w', padx=5, pady=5)
                game_price_label.pack(anchor='w', padx=5, pady=5)
                store_link_button.pack(anchor='w', padx=5, pady=5)

    def open_link(self, link):
        if link != 'Ücretsiz':
            webbrowser.open(link)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameSearchApp(root)
    root.mainloop()