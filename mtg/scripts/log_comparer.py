from mtg.ml.utils import load_model
from mtg.ml.display import draft_log_ai
import pickle

draft_model, attrs = load_model("Trained Models/SNC_Draft_May11_1/attrs.pkl")
# build_model, cards = load_model("path/to/build_model", extra_pickle="cards.pkl")
expansion = pickle.load(open("17Lands Data/SNC_Preprocess_May11.pkl", "rb"))

log = 'https://www.17lands.com/draft/9dbd9ccf208e40d185d8be7f40872cff'
token = '6af853a6c24242fab7e9b925895c3a7b'
# log_url[0] will be a link to a 17lands draft log
# log_url[1] will be a link to a sealeddeck.tech deckbuild
log_url = draft_log_ai(
    log,
    draft_model,
    expansion=expansion,
    token=token,
    #build_model=build_model,
)

def main():
    print(log_url)

if __name__ == "__main__":
    main()