def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # 입력받기: 예시 "946859 2"
    input_data = input().split()
    phone_number = input_data[0]
    added_digit = input_data[1]
    
    # 새 전화번호 생성
    new_phone_number = int(added_digit + phone_number)
    
    # 소수 판별 후 결과 출력
    if is_prime(int(phone_number)) and is_prime(new_phone_number):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
