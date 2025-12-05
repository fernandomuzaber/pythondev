#Love calculator challenge


def calculate_love_score(name1, name2):
    true = "TRUE"
    love = "LOVE"
    total_words = (name1 + name2)
    count_true = 0
    count_love = 0
    
    for char in total_words:
        if char in true.lower():
            count_true +=1
        if char in love.lower():
            count_love +=1
    final_count = ""
    final_count = str(count_true) + str(count_love)
    print(final_count)
            
    
calculate_love_score("John", "Doe")
