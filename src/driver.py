from passage.passage import get_esv_text
from config import ApiConfig
from Levenshtein import ratio
import random
from util import clean
import yaml
from yaml.loader import FullLoader

if __name__ == "__main__":

    with open("config.yml","r") as config_file:
        cfg = yaml.load(config_file,Loader=FullLoader)
        api_url = cfg['API_URL']
        api_key = cfg['API_KEY']

        api_config = ApiConfig(api_key,api_url)

        passage_name = input('Enter the passage you want to Memorize: ')

        passage = clean(get_esv_text(passage_name,api_config))

        passage_list = passage.split(' ')

        difficulty = input("Choose level of difficulty between 0-10: ")
        while difficulty.isnumeric() != True:
            difficulty = input("Re-Enter Level of difficulty between 0-10: ")
        
        difficulty = int(difficulty)
        
        if difficulty > 10:
            difficulty = 10
        if difficulty < 0:
            difficulty = 0

        remove = int(len(passage_list) * difficulty / 10)

        indices = random.sample(range(0,len(passage_list)-1),remove)

        for index in indices:
            passage_list[index] = "_" * len(passage_list[index])
        
        trick_passage = ""

        for word in passage_list:
            trick_passage = trick_passage + "%s " % word

        trick_passage = trick_passage[:-1]

        print(trick_passage)

        passage_in = input("Enter the Passage Above or Q to exit: ")

        accuracy = ratio(passage,passage_in)

        while accuracy < 1 and passage_in != 'Q':
            passage_in = input("Accuracy: %s.\nRe-Enter the Passage Above or P to print incomplete passage again or Q to exit: " % accuracy)
            if passage_in == 'P':
                print(trick_passage)
                passage_in = input("Enter the Passage Above or Q to exit: ")

            accuracy = ratio(passage,passage_in)