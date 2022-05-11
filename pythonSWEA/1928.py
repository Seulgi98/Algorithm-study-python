T = int(input())
decode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
          ]

for tc in range(1, 1 + T):
    word = list(input()) # 한글자씩 나누기 위해 list로 받아옴
    length = len(word)
    res = ''

    for q in range(length):
        num = decode.index(q) # 디코드 안의 q의 인덱스
        bin_num = str(bin(num)[2:])
        while len(bin_num) < 6: # 6자리수가 될때까지 0붙이기 반복
            bin_num = '0' + bin_num
        res += bin_num
    r = '' # 문제에서 구하고자 하는 원래 문장

    for w in range(len(res) // 8):
        e = int(res[w * 8:w * 8 + 8], 2)
        r += chr(e)

    print('#{} {}'.format(tc, r))