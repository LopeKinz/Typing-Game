import time
import enchant

def calculate_speed(words, time_taken):
    speed = (words / time_taken) * 60
    return speed

def get_paragraphs():
    paragraphs = ["The quick brown fox jumps over the lazy dog",
                  "The five boxing wizards jump quickly",
                  "Sphinx of black quartz, judge my vow",
                  "Jaded zombies acted quaintly but kept driving their oxen forward",
                  "Pack my box with five dozen liquor jugs"]
    return paragraphs

def typing_challenge():
    print("Welcome to the typing challenge!")
    print("You will have to type multiple paragraphs as fast as you can.")
    num_of_paragraphs = int(input("How many paragraphs would you like to type? "))
    paragraphs = get_paragraphs()
    start_time = time.time()
    typing_results = []
    en_dict = enchant.Dict("en_US")
    for i in range(num_of_paragraphs):
        print("Type the following paragraph as fast as you can:")
        print(paragraphs[i])
        user_input = input()
        # Rechtschreibprüfung
        misspelled_words = [word for word in user_input.split() if not en_dict.check(word)]
        if misspelled_words:
            print("Misspelled words:", misspelled_words)
        end_time = time.time()
        time_taken = end_time - start_time
        words = len(user_input.split())
        speed = calculate_speed(words, time_taken)
        result = {"paragraph": paragraphs[i], "words": words, "time": round(time_taken, 2), "speed": round(speed, 2)}
        typing_results.append(result)
        start_time = end_time
    print("Results:")
    for i in range(num_of_paragraphs):
        print("Paragraph", i+1, ":", typing_results[i]["paragraph"])
        print("You typed", typing_results[i]["words"], "words in", typing_results[i]["time"], "seconds.")
        print("Your typing speed is", typing_results[i]["speed"], "words per minute.")
    save_results(typing_results)

def save_results(typing_results):
    file_name = input("Enter file name to save results: ")
    with open(file_name, 'w') as f:
        for result in typing_results:
            f.write(f'Paragraph: {result["paragraph"]}\n')
            f.write(f'Words: {result["words"]}\n')
            f.write(f'Time: {result["time"]} seconds\n')
            f.write(f'Speed: {result["speed"]} words per minute\n\n')
    print("Results saved successfully.")

typing_challenge()
