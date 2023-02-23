from time import sleep


# Function to write I love you
def main():
    i = 1
    kiss = "x"
    answer = ""
    
    while i < 20:
        answer += f"I love you {i * kiss}\n"
        i+=1

    return answer


if __name__ == "__main__":
    print(main())