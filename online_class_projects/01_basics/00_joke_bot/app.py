import pyjokes as pj

PROMPT = "What do you want?"
SORRY = "Sorry, I only tell jokes."

def main():
    user_input = input("Write 'joke' for a joke: ").strip().lower()
    if "joke" in user_input:
        joke = pj.get_joke()
        print(joke)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
