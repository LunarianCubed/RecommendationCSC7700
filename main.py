import sys
from get_movie import get_movie

def main(*args):
    args = sys.argv
    user_id = null

    if "-u" in  args:
        user_id = args[args.index("-u") + 1]

    if user_id == null:
        user_id = input("Enter the user_id you want to recommend to:")



if __name__ == "__main__":
    main()
