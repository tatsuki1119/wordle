# 5文字だけを抽出

# with open("word_list_orig.txt", "r") as f:
#     word_list = f.read()

# with open("word_list_5.txt", "w") as f:
#     for i in word_list.split():
#         if len(i) == 5:
#             f.write(i+"\n")


with open("La.txt", "r") as f:
    words = list(f.read().split())

# 2:hit
# 1:blow
# 0:lost

inp = []
ans = []


def solve():

    hit_list = [[], [], [], [], []]
    blow_list = [[], [], [], [], []]
    lost_list = []

    # 入力からリストに変換する
    for inp_, ans_ in zip(inp, ans):
        if len(inp_) == 5:
            for j in range(5):
                if ans_[j] == "0":
                    lost_list.append(inp_[j])
                if ans_[j] == "1":
                    blow_list[j].append(inp_[j])
                if ans_[j] == "2":
                    hit_list[j].append(inp_[j])
                    hit_list[j] = list(set(hit_list[j]))

    output = []

    for w in words:  # 単語ごとにループ

        # lost_listの文字が含まれていたらスキップ
        flag = 0
        for l in lost_list:
            if l in w:
                flag = 1
        if flag:
            continue

        # hit_listと一致しなかったらスキップ
        flag = 0
        for i in range(5):
            if hit_list[i]:
                if hit_list[i][0] != w[i]:
                    flag = 1
        if flag:
            continue

        # blow_list
        flag = 0
        for i in range(5):
            for bi in blow_list[i]:
                # blow_listの文字を含まなかったらスキップ
                for b in bi:
                    if b not in w:
                        flag = 1
                        break
                # blow_listの文字を間違った位置に含んだらスキップ
                if w[i] in bi:
                    flag = 1
                    break
        if flag:
            continue

        output.append(w)

    print()
    print("入力情報:")
    for i, j in zip(inp, ans):
        print(i, j)
    print()
    print("hit :", hit_list)
    print("blow:", blow_list)
    print("lost:", lost_list)
    print()
    print(output)


def main():
    while 1:
        print("5文字の単語とその正解状況を入力")
        print("[単語] [結果]")
        _inp, _ans = input().split()
        if len(_inp) == 5 and len(_ans) == 5:
            inp.append(_inp)
            ans.append(_ans)
            solve()

        else:
            print("5文字で入力")


if __name__ == "__main__":
    main()
