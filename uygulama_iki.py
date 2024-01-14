import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import webbrowser
import uygulamacsv
import csv
class ScrollableFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        #Canvas and Scrolls
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.hsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)


        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)


        self.scrollable_frame = tk.Frame(self.canvas, background="#ffffff")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")


        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.scrollable_frame, width=event.width)
class SteamGameApp:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, background="#000235")
        self.frame.pack(side=tk.LEFT, padx=10)









        self.urls = {
            "Top Sellers - Discounts": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&category1=998&os=win&snr=1_7_7_2300_7&specials=1&filter=topsellers&infinite=1',
            "Special Offers": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&category1=998&snr=1_7_7_2300_7&specials=1&infinite=1',
            "New Releases": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=Released_DESC&category1=998&os=win&snr=1_7_7_popularnew_7&filter=popularnew&infinite=1',
            "Action & Adventure": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&tags=19%2C21&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',
            "Racing":'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&tags=699&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',
            "Puzzle": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&tags=1664&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',
            "Rpg": 'https://store.steampowered.com/search/results/?query&start=0&count=100&dynamic_data=&sort_by=_ASC&tags=122&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',
            "Fighting": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&tags=1743&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',
            "Music": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&tags=1621&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',
            "Shooter": 'https://store.steampowered.com/search/results/?query&start=0&count=200&dynamic_data=&sort_by=_ASC&tags=1774&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',
            "Platformer": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&tags=1625&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',
            "Simulation": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&tags=599&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',
            "Sports": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&tags=701&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',
            "Strategy": 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&tags=9&category1=998&os=win&snr=1_7_7_7000_7&filter=topsellers&infinite=1',


        }

        self.scrollable_frame = ScrollableFrame(self.frame)
        self.scrollable_frame.grid(row=2, column=0, pady=5, columnspan=2, sticky='w')


        self.url_label = tk.Label(self.frame, text="Steam Games:", font=("Helvetica", 14), anchor="w", padx=10)

        self.url_combobox = ttk.Combobox(self.frame, values=list(self.urls.keys()))
        self.url_combobox.set("Top Sellers - Discounts")

        self.fetch_button = tk.Button(self.frame, text="List Steam Games", command=self.take_data)


        self.url_label.grid(row=0, column=0, pady=10, sticky='w')

        self.url_combobox.grid(row=0, column=1, pady=10,sticky="w")
        self.fetch_button.grid(row=1, column=0, columnspan=1, pady=10,sticky="w")


    def get_exchange_rate(self):

        url = 'https://open.er-api.com/v6/latest/USD'
        response = requests.get(url)
        data = response.json()
        exchange_rate = data['rates']['TRY']
        return exchange_rate

    def convert_to_tl(self, price_in_dollars, exchange_rate):
        try:
            price_in_dollars = float(price_in_dollars.replace('$', '').strip())
            price_in_lira = price_in_dollars * exchange_rate
            return f'{price_in_lira:.2f} TL'
        except ValueError:
            return ' '

    def get_response(self, url):
        response = requests.get(url)
        data = dict(response.json())
        return data['results_html']

    def print_data(self, data, exchange_rate):
        for widget in self.scrollable_frame.scrollable_frame.winfo_children():
            widget.destroy()

        soup = BeautifulSoup(data, 'html.parser')
        game_elements = soup.find_all('a')
        for idx, game in enumerate(game_elements):
            game_names = game.find('span', {'class': 'title'}).text
            game_price_e = game.find('div', {'class': 'discount_final_price'})
            free_games = game.find('div', {'class': 'discount_final_price free'})
            game_links = game['href']
            if game_price_e:
                game_prices = self.convert_to_tl(game_price_e.text.strip(), exchange_rate)
            else:
                game_prices = 'Ücretsiz '
            if free_games:
                game_prices = free_games.text.strip()


            tk.Label(self.scrollable_frame.scrollable_frame, text=f"{game_names}: {game_prices}",font=("Helvetica",14)).grid(row=idx, column=0, pady=5,sticky='w')
            link_button = tk.Button(self.scrollable_frame.scrollable_frame, text="Store Link",command=lambda url=game_links: self.open_link(url))
            link_button.grid(row=idx, column=1, pady=5, sticky='e')
        self.scrollable_frame.on_frame_configure(None)
    def take_data(self):
        selected_url = self.urls[self.url_combobox.get()]
        exchange_rate = self.get_exchange_rate()
        response = self.get_response(selected_url)
        self.print_data(response, exchange_rate)

    def open_link(self, url):
        webbrowser.open(url)


class XboxGameApp:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame,background="#000235")
        self.frame.pack(side=tk.RIGHT, padx=10)

        self.url_label = tk.Label(self.frame, text="Xbox Games:",font=("Helvetica",14))
        self.url_label.grid(row=0, column=0, pady=10, sticky='w')


        self.url_dict = {
            'Action & Adventure': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Action+%26+adventure',
            'Racing & Flying': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Racing+%26+flying',
            'Puzzle': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Puzzle+%26+trivia',
            'RPG': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Role+playing',
            'Fighting': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Fighting',
            'Music': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Music',
            'Shooter': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Shooter',
            'Platformer': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Platformer',
            'Simulation': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Simulation',
            'Sport': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Sports',
            'Strategy': 'https://www.xbox.com/tr-TR/games/all-games/pc?PlayWith=PC&xr=shellnav&Genre=Strategy',
        }

        self.scrollable_frame = ScrollableFrame(self.frame)
        self.scrollable_frame.grid(row=2, column=0, pady=5, columnspan=2, sticky='ew')

        self.url_combobox = ttk.Combobox(self.frame, values=list(self.url_dict.keys()))
        self.url_combobox.set('Action & Adventure')

        self.scrape_button = tk.Button(self.frame, text="List Xbox Games", command=self.select_data)

        self.result_frame = tk.Frame(self.scrollable_frame.scrollable_frame)
        self.result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5,sticky='ew')


        self.url_combobox.grid(row=0, column=1, pady=10, sticky='w')
        self.scrape_button.grid(row=1, column=0, columnspan=1, pady=10, sticky='w')


    def getdata(self, url, num_clicks):
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        driver.implicitly_wait(10)

        page_sources = []

        for _ in range(num_clicks):
            load_more_buttons = driver.find_elements(By.XPATH, '//div[contains(text(), "Daha fazla yükle")]')
            if not load_more_buttons:
                break

            load_more_buttons[0].click()

            time.sleep(2)
            page_sources.append(driver.page_source)

        driver.quit()

        return page_sources
    def open_link(self, url):
        webbrowser.open(url)

    def get_game_info(self, page_sources):
        game_info = []

        for page_source in page_sources:
            soup = BeautifulSoup(page_source, 'html.parser')
            game_elements = soup.find_all('a', {'class': 'Button-module__basicBorderRadius___TaX9J'})

            for i in game_elements:
                game_name2 = i.find('span', {'class': 'ProductCard-module__singleLineTitle___32jUF'})
                if game_name2:
                    game_name_e2 = game_name2.text.strip()
                else:
                    game_name_e2 = "Bilgi Bulunamadı"

                game_name_element = i.find('span', {'class': 'ProductCard-module__title___nHGIp'})
                game_name = game_name_element.text.strip() if game_name_element else game_name_e2

                game_price_element = i.find('span', {'class': 'Price-module__boldText___vmNHu'})
                game_price = game_price_element.text.strip() if game_price_element else "Bilgi Bulunamadı"

                game_link = i['href'] if 'href' in i.attrs else "Bilgi Bulunamadı"

                game_info.append((game_name, game_price, game_link))

        return game_info
    def display_game_info(self, game_info):

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        if game_info:
            for idx, (name, price, link) in enumerate(game_info):
                tk.Label(self.result_frame, text=f"{name}: {price}",font=("Helvetica",14)).grid(row=idx, column=0, pady=5, sticky='w')
                link_button = tk.Button(self.result_frame, text="Store Link",command=lambda url=link: self.open_link(url))
                link_button.grid(row=idx, column=1, pady=5, padx=(0, 10), sticky='e')
        else:
            tk.Label(self.result_frame, text="No game information found.").grid(row=0, column=0, pady=5, sticky='w')
        self.scrollable_frame.on_frame_configure(None)
    def select_data(self):
        selected_genre = self.url_combobox.get()
        selected_url = self.url_dict.get(selected_genre)

        if selected_url:
            page_sources = self.getdata(selected_url, num_clicks=4)
            game_info = self.get_game_info(page_sources)
            self.display_game_info(game_info)
        else:
            print("Select another option")





def run_uygulama_csv():
    root = tk.Tk()
    app = uygulamacsv.GameSearchApp(root)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x600")
    root.title("Game Scouter")
    bg = tk.PhotoImage(file="arkplan1.png")
    bg1 = tk.PhotoImage(file="Steam-Logo.png")
    bg1 = bg1.subsample(3, 3)
    bg2 = tk.PhotoImage(file="xbox-logo2.png")







    # Show image using label
    label1 = tk.Label(root, image=bg)
    label1.place(x=0, y=0)
    label2 = tk.Label(root, image=bg1)
    label2.place(x=0, y=5)
    label3 = tk.Label(root, image=bg2)
    label3.place(x=790, y=5)
    app1 = SteamGameApp(root)
    app2 = XboxGameApp(root)
    run_uygulama_csv()
    root.mainloop()