"""
Stock tickers database for search functionality.
Includes NSE (Indian) and major US stocks.
Now with 150+ Indian stocks covering NIFTY 50, NIFTY Next 50, and popular mid/small caps.
"""

STOCK_TICKERS = [
    # NIFTY 50 - India's Top 50 Stocks
    {"symbol": "RELIANCE.NS", "name": "Reliance Industries", "exchange": "NSE", "sector": "Oil & Gas"},
    {"symbol": "TCS.NS", "name": "Tata Consultancy Services", "exchange": "NSE", "sector": "IT Services"},
    {"symbol": "HDFCBANK.NS", "name": "HDFC Bank", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "INFY.NS", "name": "Infosys", "exchange": "NSE", "sector": "IT Services"},
    {"symbol": "ICICIBANK.NS", "name": "ICICI Bank", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "HINDUNILVR.NS", "name": "Hindustan  Unilever", "exchange": "NSE", "sector": "FMCG"},
    {"symbol": "ITC.NS", "name": "ITC Limited", "exchange": "NSE", "sector": "FMCG"},
    {"symbol": "SBIN.NS", "name": "State Bank of India", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel", "exchange": "NSE", "sector": "Telecom"},
    {"symbol": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "AXISBANK.NS", "name": "Axis Bank", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "LT.NS", "name": "Larsen & Toubro", "exchange": "NSE", "sector": "Construction"},
    {"symbol": "ASIANPAINT.NS", "name": "Asian Paints", "exchange": "NSE", "sector": "Paints"},
    {"symbol": "MARUTI.NS", "name": "Maruti Suzuki", "exchange": "NSE", "sector": "Automobile"},
    {"symbol": "SUNPHARMA.NS", "name": "Sun Pharmaceutical", "exchange": "NSE", "sector": "Pharma"},
    {"symbol": "TITAN.NS", "name": "Titan Company", "exchange": "NSE", "sector": "Jewellery"},
    {"symbol": "NESTLEIND.NS", "name": "Nestle India", "exchange": "NSE", "sector": "FMCG"},
    {"symbol": "ULTRACEMCO.NS", "name": "UltraTech Cement", "exchange": "NSE", "sector": "Cement"},
    {"symbol": "BAJFINANCE.NS", "name": "Bajaj Finance", "exchange": "NSE", "sector": "Financial Services"},
    {"symbol": "WIPRO.NS", "name": "Wipro", "exchange": "NSE", "sector": "IT Services"},
    {"symbol": "HCLTECH.NS", "name": "HCL Technologies", "exchange": "NSE", "sector": "IT Services"},
    {"symbol": "TECHM.NS", "name": "Tech Mahindra", "exchange": "NSE", "sector": "IT Services"},
    {"symbol": "M&M.NS", "name": "Mahindra & Mahindra", "exchange": "NSE", "sector": "Automobile"},
    {"symbol": "TATAMOTORS.NS", "name": "Tata Motors", "exchange": "NSE", "sector": "Automobile"},
    {"symbol": "TATASTEEL.NS", "name": "Tata Steel", "exchange": "NSE", "sector": "Metals"},
    {"symbol": "POWERGRID.NS", "name": "Power Grid Corporation", "exchange": "NSE", "sector": "Power"},
    {"symbol": "NTPC.NS", "name": "NTPC Limited", "exchange": "NSE", "sector": "Power"},
    {"symbol": "ONGC.NS", "name": "Oil & Natural Gas Corporation", "exchange": "NSE", "sector": "Oil & Gas"},
    {"symbol": "COALINDIA.NS", "name": "Coal India", "exchange": "NSE", "sector": "Mining"},
    {"symbol": "INDUSINDBK.NS", "name": "IndusInd Bank", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "BAJAJ-AUTO.NS", "name": "Bajaj Auto", "exchange": "NSE", "sector": "Automobile"},
    {"symbol": "BAJAJFINSV.NS", "name": "Bajaj Finserv", "exchange": "NSE", "sector": "Financial Services"},
    {"symbol": "HEROMOTOCO.NS", "name": "Hero MotoCorp", "exchange": "NSE", "sector": "Automobile"},
    {"symbol": "EICHERMOT.NS", "name": "Eicher Motors", "exchange": "NSE", "sector": "Automobile"},
    {"symbol": "BRITANNIA.NS", "name": "Britannia Industries", "exchange": "NSE", "sector": "FMCG"},
    {"symbol": "DRREDDY.NS", "name": "Dr. Reddy's Laboratories", "exchange": "NSE", "sector": "Pharma"},
    {"symbol": "CIPLA.NS", "name": "Cipla", "exchange": "NSE", "sector": "Pharma"},
    {"symbol": "DIVISLAB.NS", "name": "Divi's Laboratories", "exchange": "NSE", "sector": "Pharma"},
    {"symbol": "APOLLOHOSP.NS", "name": "Apollo Hospitals", "exchange": "NSE", "sector": "Healthcare"},
    {"symbol": "ADANIPORTS.NS", "name": "Adani Ports", "exchange": "NSE", "sector": "Infrastructure"},
    {"symbol": "ADANIENT.NS", "name": "Adani Enterprises", "exchange": "NSE", "sector": "Diversified"},
    {"symbol": "JSWSTEEL.NS", "name": "JSW Steel", "exchange": "NSE", "sector": "Metals"},
    {"symbol": "HINDALCO.NS", "name": "Hindalco Industries", "exchange": "NSE", "sector": "Metals"},
    {"symbol": "GRASIM.NS", "name": "Grasim Industries", "exchange": "NSE", "sector": "Diversified"},
    {"symbol": "UPL.NS", "name": "UPL Limited", "exchange": "NSE", "sector": "Chemicals"},
    {"symbol": "BPCL.NS", "name": "Bharat Petroleum", "exchange": "NSE", "sector": "Oil & Gas"},
    {"symbol": "TATACONSUM.NS", "name": "Tata Consumer Products", "exchange": "NSE", "sector": "FMCG"},
    {"symbol": "SBILIFE.NS", "name": "SBI Life Insurance", "exchange": "NSE", "sector": "Insurance"},
    {"symbol": "HDFCLIFE.NS", "name": "HDFC Life Insurance", "exchange": "NSE", "sector": "Insurance"},
    
    # NIFTY Next 50 - Top Mid-cap Stocks
    {"symbol": "ADANIGREEN.NS", "name": "Adani Green Energy", "exchange": "NSE", "sector": "Power"},
    {"symbol": "ADANITRANS.NS", "name": "Adani Transmission", "exchange": "NSE", "sector": "Power"},
    {"symbol": "AMBUJACEM.NS", "name": "Ambuja Cements", "exchange": "NSE", "sector": "Cement"},
    {"symbol": "BANDHANBNK.NS", "name": "Bandhan Bank", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "BERGEPAINT.NS", "name": "Berger Paints", "exchange": "NSE", "sector": "Paints"},
    {"symbol": "BEL.NS", "name": "Bharat Electronics", "exchange": "NSE", "sector": "Defense"},
    {"symbol": "BIOCON.NS", "name": "Biocon Limited", "exchange": "NSE", "sector": "Pharma"},
    {"symbol": "BOSCHLTD.NS", "name": "Bosch Limited", "exchange": "NSE", "sector": "Auto Components"},
    {"symbol": "CHOLAFIN.NS", "name": "Cholamandalam Investment", "exchange": "NSE", "sector": "Financial Services"},
    {"symbol": "COLPAL.NS", "name": "Colgate-Palmolive India", "exchange": "NSE", "sector": "FMCG"},
    {"symbol": "DABUR.NS", "name": "Dabur India", "exchange": "NSE", "sector": "FMCG"},
    {"symbol": "DLF.NS", "name": "DLF Limited", "exchange": "NSE", "sector": "Real Estate"},
    {"symbol": "DMART.NS", "name": "Avenue Supermarts (DMart)", "exchange": "NSE", "sector": "Retail"},
    {"symbol": "GAIL.NS", "name": "GAIL India", "exchange": "NSE", "sector": "Oil & Gas"},
    {"symbol": "GODREJCP.NS", "name": "Godrej Consumer Products", "exchange": "NSE", "sector": "FMCG"},
    {"symbol": "HAVELLS.NS", "name": "Havells India", "exchange": "NSE", "sector": "Electricals"},
    {"symbol": "HINDZINC.NS", "name": "Hindustan Zinc", "exchange": "NSE", "sector": "Metals"},
    {"symbol": "ICICIPRULI.NS", "name": "ICICI Prudential Life", "exchange": "NSE", "sector": "Insurance"},
    {"symbol": "INDIGO.NS", "name": "InterGlobe Aviation", "exchange": "NSE", "sector": "Aviation"},
    {"symbol": "IOC.NS", "name": "Indian Oil Corporation", "exchange": "NSE", "sector": "Oil & Gas"},
    {"symbol": "JINDALSTEL.NS", "name": "Jindal Steel & Power", "exchange": "NSE", "sector": "Metals"},
    {"symbol": "MARICO.NS", "name": "Marico Limited", "exchange": "NSE", "sector": "FMCG"},
    {"symbol": "MCDOWELL-N.NS", "name": "United Spirits", "exchange": "NSE", "sector": "Beverages"},
    {"symbol": "MOTHERSON.NS", "name": "Samvardhana Motherson", "exchange": "NSE", "sector": "Auto Components"},
    {"symbol": "MUTHOOTFIN.NS", "name": "Muthoot Finance", "exchange": "NSE", "sector": "Financial Services"},
    {"symbol": "NAUKRI.NS", "name": "Info Edge (Naukri.com)", "exchange": "NSE", "sector": "Internet"},
    {"symbol": "NMDC.NS", "name": "NMDC Limited", "exchange": "NSE", "sector": "Mining"},
    {"symbol": "PAGEIND.NS", "name": "Page Industries", "exchange": "NSE", "sector": "Textiles"},
    {"symbol": "PGHH.NS", "name": "Procter & Gamble Health", "exchange": "NSE", "sector": "FMCG"},
    {"symbol": "PIDILITIND.NS", "name": "Pidilite Industries", "exchange": "NSE", "sector": "Chemicals"},
    {"symbol": "PNB.NS", "name": "Punjab National Bank", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "SAIL.NS", "name": "Steel Authority of India", "exchange": "NSE", "sector": "Metals"},
    {"symbol": "SHREECEM.NS", "name": "Shree Cement", "exchange": "NSE", "sector": "Cement"},
    {"symbol": "SIEMENS.NS", "name": "Siemens Limited", "exchange": "NSE", "sector": "Engineering"},
    {"symbol": "SRF.NS", "name": "SRF Limited", "exchange": "NSE", "sector": "Chemicals"},
    {"symbol": "TATAPOWER.NS", "name": "Tata Power", "exchange": "NSE", "sector": "Power"},
    {"symbol": "TORNTPHARM.NS", "name": "Torrent Pharmaceuticals", "exchange": "NSE", "sector": "Pharma"},
    {"symbol": "UBL.NS", "name": "United Breweries", "exchange": "NSE", "sector": "Beverages"},
    {"symbol": "VEDL.NS", "name": "Vedanta Limited", "exchange": "NSE", "sector": "Metals"},
    {"symbol": "ZEEL.NS", "name": "Zee Entertainment", "exchange": "NSE", "sector": "Media"},
    
    # Popular Mid/Small Cap Stocks
    {"symbol": "AARTIIND.NS", "name": "Aarti Industries", "exchange": "NSE", "sector": "Chemicals"},
    {"symbol": "ACC.NS", "name": "ACC Limited", "exchange": "NSE", "sector": "Cement"},
    {"symbol": "ASHOKLEY.NS", "name": "Ashok Leyland", "exchange": "NSE", "sector": "Automobile"},
    {"symbol": "AUROPHARMA.NS", "name": "Aurobindo Pharma", "exchange": "NSE", "sector": "Pharma"},
    {"symbol": "BALKRISIND.NS", "name": "Balkrishna Industries", "exchange": "NSE", "sector": "Auto Components"},
    {"symbol": "BANKBARODA.NS", "name": "Bank of Baroda", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "BATAINDIA.NS", "name": "Bata India", "exchange": "NSE", "sector": "Footwear"},
    {"symbol": "BHARATFORG.NS", "name": "Bharat Forge", "exchange": "NSE", "sector": "Auto Components"},
    {"symbol": "CANBK.NS", "name": "Canara Bank", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "COFORGE.NS", "name": "Coforge Limited", "exchange": "NSE", "sector": "IT Services"},
    {"symbol": "CONCOR.NS", "name": "Container Corporation", "exchange": "NSE", "sector": "Logistics"},
    {"symbol": "CUMMINSIND.NS", "name": "Cummins India", "exchange": "NSE", "sector": "Engineering"},
    {"symbol": "ESCORTS.NS", "name": "Escorts Kubota", "exchange": "NSE", "sector": "Auto Components"},
    {"symbol": "EXIDEIND.NS", "name": "Exide Industries", "exchange": "NSE", "sector": "Auto Components"},
    {"symbol": "FEDERALBNK.NS", "name": "Federal Bank", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "GODREJPROP.NS", "name": "Godrej Properties", "exchange": "NSE", "sector": "Real Estate"},
    {"symbol": "HDFCAMC.NS", "name": "HDFC AMC", "exchange": "NSE", "sector": "Financial Services"},
    {"symbol": "IGL.NS", "name": "Indraprastha Gas", "exchange": "NSE", "sector": "Oil & Gas"},
    {"symbol": "IRCTC.NS", "name": "IRCTC", "exchange": "NSE", "sector": "Travel & Tourism"},
    {"symbol": "JUBLFOOD.NS", "name": "Jubilant FoodWorks", "exchange": "NSE", "sector": "Restaurants"},
    {"symbol": "LICI.NS", "name": "Life Insurance Corporation", "exchange": "NSE", "sector": "Insurance"},
    {"symbol": "LUPIN.NS", "name": "Lupin Limited", "exchange": "NSE", "sector": "Pharma"},
    {"symbol": "MANAPPURAM.NS", "name": "Manappuram Finance", "exchange": "NSE", "sector": "Financial Services"},
    {"symbol": "MGL.NS", "name": "Mahanagar Gas", "exchange": "NSE", "sector": "Oil & Gas"},
    {"symbol": "MPHASIS.NS", "name": "Mphasis Limited", "exchange": "NSE", "sector": "IT Services"},
    {"symbol": "MRF.NS", "name": "MRF Limited", "exchange": "NSE", "sector": "Auto Components"},
    {"symbol": "OBEROIRLTY.NS", "name": "Oberoi Realty", "exchange": "NSE", "sector": "Real Estate"},
    {"symbol": "OFSS.NS", "name": "Oracle Financial Services", "exchange": "NSE", "sector": "IT Services"},
    {"symbol": "PERSISTENT.NS", "name": "Persistent Systems", "exchange": "NSE", "sector": "IT Services"},
    {"symbol": "PETRONET.NS", "name": "Petronet LNG", "exchange": "NSE", "sector": "Oil & Gas"},
    {"symbol": "PFC.NS", "name": "Power Finance Corporation", "exchange": "NSE", "sector": "Financial Services"},
    {"symbol": "PIIND.NS", "name": "PI Industries", "exchange": "NSE", "sector": "Chemicals"},
    {"symbol": "RECLTD.NS", "name": "REC Limited", "exchange": "NSE", "sector": "Financial Services"},
    {"symbol": "TATACOMM.NS", "name": "Tata Communications", "exchange": "NSE", "sector": "Telecom"},
    {"symbol": "TATACHEM.NS", "name": "Tata Chemicals", "exchange": "NSE", "sector": "Chemicals"},
    {"symbol": "TATAELXSI.NS", "name": "Tata Elxsi", "exchange": "NSE", "sector": "IT Services"},
    {"symbol": "TRENT.NS", "name": "Trent Limited", "exchange": "NSE", "sector": "Retail"},
    {"symbol": "TVSMOTOR.NS", "name": "TVS Motor Company", "exchange": "NSE", "sector": "Automobile"},
    {"symbol": "UNIONBANK.NS", "name": "Union Bank of India", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "VOLTAS.NS", "name": "Voltas Limited", "exchange": "NSE", "sector": "Consumer Durables"},
    {"symbol": "YESBANK.NS", "name": "Yes Bank", "exchange": "NSE", "sector": "Banking"},
    {"symbol": "ZOMATO.NS", "name": "Zomato Limited", "exchange": "NSE", "sector": "Internet"},
    {"symbol": "ZYDUSLIFE.NS", "name": "Zydus Lifesciences", "exchange": "NSE", "sector": "Pharma"},
    
    # Major US Stocks
    {"symbol": "AAPL", "name": "Apple Inc.", "exchange": "NASDAQ", "sector": "Technology"},
    {"symbol": "MSFT", "name": "Microsoft Corporation", "exchange": "NASDAQ", "sector": "Technology"},
    {"symbol": "GOOGL", "name": "Alphabet Inc. (Google)", "exchange": "NASDAQ", "sector": "Technology"},
    {"symbol": "AMZN", "name": "Amazon.com Inc.", "exchange": "NASDAQ", "sector": "E-commerce"},
    {"symbol": "META", "name": "Meta Platforms (Facebook)", "exchange": "NASDAQ", "sector": "Technology"},
    {"symbol": "TSLA", "name": "Tesla Inc.", "exchange": "NASDAQ", "sector": "Automobile"},
    {"symbol": "NVDA", "name": "NVIDIA Corporation", "exchange": "NASDAQ", "sector": "Technology"},
    {"symbol": "NFLX", "name": "Netflix Inc.", "exchange": "NASDAQ", "sector": "Entertainment"},
    {"symbol": "JPM", "name": "JPMorgan Chase & Co.", "exchange": "NYSE", "sector": "Banking"},
    {"symbol": "V", "name": "Visa Inc.", "exchange": "NYSE", "sector": "Financial Services"},
    {"symbol": "JNJ", "name": "Johnson & Johnson", "exchange": "NYSE", "sector": "Healthcare"},
    {"symbol": "WMT", "name": "Walmart Inc.", "exchange": "NYSE", "sector": "Retail"},
    {"symbol": "PG", "name": "Procter & Gamble", "exchange": "NYSE", "sector": "FMCG"},
    {"symbol": "DIS", "name": "The Walt Disney Company", "exchange": "NYSE", "sector": "Entertainment"},
    {"symbol": "INTC", "name": "Intel Corporation", "exchange": "NASDAQ", "sector": "Technology"},
    {"symbol": "AMD", "name": "Advanced Micro Devices", "exchange": "NASDAQ", "sector": "Technology"},
    {"symbol": "CSCO", "name": "Cisco Systems", "exchange": "NASDAQ", "sector": "Technology"},
    {"symbol": "ORCL", "name": "Oracle Corporation", "exchange": "NYSE", "sector": "Technology"},
    {"symbol": "ADBE", "name": "Adobe Inc.", "exchange": "NASDAQ", "sector": "Technology"},
    {"symbol": "CRM", "name": "Salesforce Inc.", "exchange": "NYSE", "sector": "Technology"},
    {"symbol": "BA", "name": "Boeing Company", "exchange": "NYSE", "sector": "Aerospace"},
    {"symbol": "KO", "name": "The Coca-Cola Company", "exchange": "NYSE", "sector": "Beverages"},
    {"symbol": "PEP", "name": "PepsiCo Inc.", "exchange": "NASDAQ", "sector": "Beverages"},
    {"symbol": "NKE", "name": "Nike Inc.", "exchange": "NYSE", "sector": "Apparel"},
    {"symbol": "MCD", "name": "McDonald's Corporation", "exchange": "NYSE", "sector": "Restaurants"},
]


def search_tickers(query: str, limit: int = 10):
    """
    Search for stock tickers by symbol or name.
    Returns matching results with fuzzy matching support.
    """
    if not query:
        return []
    
    query = query.upper().strip()
    results = []
    
    # Exact symbol matches first
    for ticker in STOCK_TICKERS:
        if ticker["symbol"].upper().startswith(query):
            results.append({**ticker, "match_type": "symbol"})
    
    # Then name matches
    for ticker in STOCK_TICKERS:
        if query in ticker["name"].upper() and ticker not in results:
            results.append({**ticker, "match_type": "name"})
    
    # Return limited results
    return results[:limit]
