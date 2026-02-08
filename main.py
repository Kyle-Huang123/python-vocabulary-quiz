import random

file_name = "word.txt"
word_en = []
word_ch = []
proficiency_list = []
low_proficiency_test = True
threshold = 3
MCQ = True
MCQ_options = 6
mode_list = ["en_ch", "ch_en", "mixed"]

def read_file(file_name, word_en, word_ch, proficiency_list, threshold):
    with open(file_name, "r", encoding="utf-8") as file:
        words = file.read().split("\n")
        for word in words:
            word_en.append(word.split(" ")[0])
            word_ch.append(word.split(" ")[1])
            if(len(word.split(" ")) > 2):
                proficiency_list.append(word.split(" ")[2])
                threshold += int(word.split(" ")[2])
            else:
                proficiency_list.append("0")
        threshold = threshold / len(proficiency_list) + 2

def mode_ask():
    global test_times, test_mode, MCQ_options, MCQ, low_proficiency_test, threshold
    test_times = int(input("Test times: "))
    try:
        ask = input("Test mode (0: English, 1: Chinese, 2: Mixed): ")
        for i in range(len(ask.split(" "))):
            if(ask.split(" ")[i] == "-O"):
                MCQ_options = int(ask.split(" ")[i + 1])
            if(ask.split(" ")[i] == "-M"):
                MCQ = ask.split(" ")[i + 1] == "True"
            if(ask.split(" ")[i] == "-L"):
                low_proficiency_test = ask.split(" ")[i + 1] == "True"
            if(ask.split(" ")[i] == "-H"):
                threshold = int(ask.split(" ")[i + 1])
        test_mode = mode_list[int(ask.split(" ")[0])]
    except:
        test_mode = "mixed"

def NONE_MCQ(word_en, word_ch, proficiency_list, threshold, test_times, test_mode):
    for i in range(test_times):
        if(low_proficiency_test):
            try:
                index = random.choice([i for i, x in enumerate(proficiency_list) if int(x) < threshold])
            except:
                break
        else:
            index = random.randint(0, len(word_en) - 1)
        if(test_mode == "en_ch"):
            print("Question: " + word_en[index])
            answer = input("Answer: ")
            if(answer == word_ch[index]):
                print("\033[32m"+"Correct!"+"\033[37m")
                proficiency_list[index] = str(int(proficiency_list[index]) + 1)
            else:
                print("\033[31m"+"Wrong! The answer is "+"\033[37m" + word_ch[index])
                proficiency_list[index] = str(int(proficiency_list[index]) - 1)
        elif(test_mode == "ch_en"):
            print("Question: " + word_ch[index])
            answer = input("Answer: ")
            if(answer == word_en[index]):
                print("\033[32m"+"Correct!"+"\033[37m")
                proficiency_list[index] = str(int(proficiency_list[index]) + 1)
            else:
                print("\033[31m"+"Wrong! The answer is "+"\033[37m" + word_en[index])
                proficiency_list[index] = str(int(proficiency_list[index]) - 1)
        elif(test_mode == "mixed"):
            if(random.randint(0, 1) == 0):
                print("Question: " + word_en[index])
                answer = input("Answer: ")
                if(answer == word_ch[index]):
                    print("\033[32m"+"Correct!"+"\033[37m")
                    proficiency_list[index] = str(int(proficiency_list[index]) + 1)
                else:
                    print("\033[31m"+"Wrong! The answer is "+"\033[37m" + word_ch[index])
                    proficiency_list[index] = str(int(proficiency_list[index]) - 1)
            else:
                print("Question: " + word_ch[index])
                answer = input("Answer: ")
                if(answer == word_en[index]):
                    print("\033[32m"+"Correct!"+"\033[37m")
                    proficiency_list[index] = str(int(proficiency_list[index]) + 1)
                else:
                    print("\033[31m"+"Wrong! The answer is "+"\033[37m" + word_en[index])
                    proficiency_list[index] = str(int(proficiency_list[index]) - 1)

def MCQ_test(word_en, word_ch, proficiency_list, threshold, test_times, test_mode, MCQ_options):
    for i in range(test_times):
        if(low_proficiency_test):
            try:
                index = random.choice([i for i, x in enumerate(proficiency_list) if int(x) < threshold])
            except:
                break
        else:
            index = random.randint(0, len(word_en) - 1)
        if(test_mode == "en_ch"):
            print("Question: " + word_en[index])
            answer_list = [word_ch[index]]
            while(len(answer_list) < MCQ_options):
                new_answer = random.choice(word_ch)
                if(new_answer not in answer_list):
                    answer_list.append(new_answer)
            random.shuffle(answer_list)
            for j in range(MCQ_options):
                print(str(j) + ": " + answer_list[j])
            answer = int(input("Answer: "))
            if(answer_list[answer] == word_ch[index]):
                print("\033[32m"+"Correct!"+"\033[37m")
                proficiency_list[index] = str(int(proficiency_list[index]) + 1)
            else:
                print("\033[31m"+"Wrong! The answer is "+"\033[37m" + word_ch[index])
                proficiency_list[index] = str(int(proficiency_list[index]) - 1)
        elif(test_mode == "ch_en"):
            print("Question: " + word_ch[index])
            answer_list = [word_en[index]]
            while(len(answer_list) < MCQ_options):
                new_answer = random.choice(word_en)
                if(new_answer not in answer_list):
                    answer_list.append(new_answer)
            random.shuffle(answer_list)
            for j in range(MCQ_options):
                print(str(j) + ": " + answer_list[j])
            answer = int(input("Answer: "))
            if(answer_list[answer] == word_en[index]):
                print("\033[32m"+"Correct!"+"\033[37m")
                proficiency_list[index] = str(int(proficiency_list[index]) + 1)
            else:
                print("\033[31m"+"Wrong! The answer is "+"\033[37m" + word_en[index])
                proficiency_list[index] = str(int(proficiency_list[index]) - 1)
        elif(test_mode == "mixed"):
            md = random.randint(0, 1)
            if(md == 0):
                print("Question: " + word_en[index])
                answer_list = [word_ch[index]]
                while(len(answer_list) < MCQ_options):
                    new_answer = random.choice(word_ch)
                    if(new_answer not in answer_list):
                        answer_list.append(new_answer)
                random.shuffle(answer_list)
                for j in range(MCQ_options):
                    print(str(j) + ": " + answer_list[j])
                answer = int(input("Answer: "))
                if(answer_list[answer] == word_ch[index]):
                    print("\033[32m"+"Correct!"+"\033[37m")
                    proficiency_list[index] = str(int(proficiency_list[index]) + 1)
                else:
                    print("\033[31m"+"Wrong! The answer is "+"\033[37m" + word_ch[index])
                    proficiency_list[index] = str(int(proficiency_list[index]) - 1)
            else:
                print("Question: " + word_ch[index])
                answer_list = [word_en[index]]
                while(len(answer_list) < MCQ_options):
                    new_answer = random.choice(word_en)
                    if(new_answer not in answer_list):
                        answer_list.append(new_answer)
                random.shuffle(answer_list)
                for j in range(MCQ_options):
                    print(str(j) + ": " + answer_list[j])
                answer = int(input("Answer: "))
                if(answer_list[answer] == word_en[index]):
                    print("\033[32m"+"Correct!"+"\033[37m")
                    proficiency_list[index] = str(int(proficiency_list[index]) + 1)
                else:
                    print("\033[31m"+"Wrong! The answer is "+"\033[37m" + word_en[index])
                    proficiency_list[index] = str(int(proficiency_list[index]) - 1)

def write_file(file_name, word_en, word_ch, proficiency_list):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(len(word_en)):
            file.write(word_en[i] + " " + word_ch[i] + " " + proficiency_list[i] + "\n")
        #刪空行
        file.seek(file.tell()-2, 0)
        file.truncate()

if __name__ == "__main__":
    read_file(file_name, word_en, word_ch, proficiency_list, threshold)
    mode_ask()
    if(MCQ):
        MCQ_test(word_en, word_ch, proficiency_list, threshold, test_times, test_mode, MCQ_options)
    else:
        NONE_MCQ(word_en, word_ch, proficiency_list, threshold, test_times, test_mode)
    proficiency_list = [str(max(0, int(x))) for x in proficiency_list]
    write_file(file_name, word_en, word_ch, proficiency_list)