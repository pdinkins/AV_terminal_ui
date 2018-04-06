from ui.menu import *
from av_functions import *



def stock_market_menu():
    initialize_menu(stock_market_menu_dict, 'Stock Market Menu')

def forex_market_menu():
    initialize_menu(forex_market_menu_dict, 'Foreign Exchange Menu')

def cc_market_menu():
    initialize_menu(cc_market_menu_dict, 'Crypto Currency Menu')

def end():
    quit()


main_menu_dict = {
    'Stock Market': stock_market_menu,
    'Foreign Exchange Market': forex_market_menu,
    'Crypto Currencies': cc_market_menu,
    'Quit': end
}

stock_market_menu_dict = {
    "Real Time Sector Performance Graph": rt_sector_performance_graph,
    "Sector Performance Raw Data": sector_performance_raw_data,
    "Single Sector Raw Data": sp_one_sector,
    "Print All Sector Data": print_sd,
    "Single Stock Data": ts_stock_data_intput 
}

forex_market_menu_dict = {

}

cc_market_menu_dict = {
    'Crypto Currency Intradaily\n(Price, Volume, Market Cap)': cc_info
}
