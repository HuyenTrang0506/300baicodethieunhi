def generate_gray_code(n):
    # Bắt đầu từ Gray code cho n = 1
    gray_code = ['0', '1']

    # Dùng phương pháp đệ quy để tạo Gray code cho n
    for i in range(2, n + 1):
        # Lấy bản sao ngược của gray_code hiện tại
        gray_code = gray_code + [x for x in reversed(gray_code)]

        # Thêm 0 vào đầu của các phần tử ban đầu
        for j in range(len(gray_code) // 2):
            gray_code[j] = '0' + gray_code[j]

        # Thêm 1 vào đầu của các phần tử sau khi đảo ngược
        for j in range(len(gray_code) // 2, len(gray_code)):
            gray_code[j] = '1' + gray_code[j]

    return gray_code


# Đọc đầu vào
n = int(input())

# Tạo Gray code cho n
gray_code = generate_gray_code(n)

# In kết quả
for code in gray_code:
    print(code)
