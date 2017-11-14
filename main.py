
import argparse
import dataPretreatment
import model
from config import *

def defineArgs():
    parser = argparse.ArgumentParser(description = "poem.")
    parser.add_argument("-m", "--mode", help = "select mode by 'train' or test or head",
                        choices = ["train", "test"], default = "test")
    return parser.parse_args()

if __name__ == "__main__":
    X, Y, wordNum, wordToID, words = dataPretreatment.pretreatment(trainPoems)
    args = defineArgs()
    if args.mode == "train":
        print("training...")
        model.train(X, Y, wordNum)
    else:
        if args.mode == "test":
            print("genrating...")
            poems = model.test(wordNum, wordToID, words)