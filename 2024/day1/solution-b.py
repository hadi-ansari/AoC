from reader import read_problem

def main():
    first_col, second_col = read_problem("input.txt")
    similarity_score = 0

    for number in first_col:
        similarity_score += (int(second_col.count(number)) * int(number))



    print("Similarity score => {}".format(similarity_score))
    
        

main()