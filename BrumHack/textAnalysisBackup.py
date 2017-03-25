from aylienapiclient import textapi

client = textapi.Client("1e8b470d", "2f8abc90c72a0dffd38238410356aa58")

classifications = client.Classify({"text": "Caught up with 2 old friends this week - US Army test pilot and an Mi-17. Last time I was in one of these was just after Soyuz landing."})

for category in classifications['categories']:
  print category