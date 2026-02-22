def main():
    valid_scores = []
    
    while len(valid_scores) < 2:
        try:
            score = float(input())
            
            if 0 <= score <= 10:
                valid_scores.append(score)
            else:
                print("nota invalida")
        except EOFError:
            break

    average = sum(valid_scores) / 2
    print(f"media = {average:.2f}")

if __name__ == "__main__":
    main()