from  transformers import pipeline

classifier=pipeline("sentiment-analysis")

result=classifier("Foreign institutional investors (FIIs) are staging a structural overhaul of their Indian equity portfolios by aggressively slashing their exposure to the country's multi-billion-dollar bluechip heavyweight stocks. Shareholding pattern data reveals that the top 10 stocks held by FIIs in March 2022, which once commanded a massive 40.9% of their entire India portfolio, saw that allocation nearly halved to just 21.3% by March 2026.")

print(result)
