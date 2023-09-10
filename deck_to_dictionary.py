from ankipandas import Collection
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv('.env')

user = os.environ.get("ANKI_USER_PROFILE")
deck_name = os.environ.get("ANKI_DECK_NAME")

col = Collection(user=user)
cards = col.cards
review_cards = cards[(cards.cdeck == deck_name)]
review_cards_with_notes = review_cards.merge_notes()

japanese_fields = review_cards_with_notes["nflds"].apply(lambda x: x[0])
english_fields = review_cards_with_notes["nflds"].apply(lambda x: x[1])

dictionary = pd.DataFrame({"kanji": japanese_fields, "meaning": english_fields}) 
print(dictionary.head())
dictionary.to_csv("dictionary.csv", index=False)
