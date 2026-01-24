def split_and_join(line):
    ans = line.split(" ")
    ans = "-".join(ans)
    return ans

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
