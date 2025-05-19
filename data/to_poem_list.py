import csv


def to_poem_list(file_path,debug=False):
    poems = []

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            content = row["内容"].strip().replace(" ", "")  # 去除空格
            if not content:
                continue
            # 按中文句号分句
            for part in content.split("。"):
                part = part.strip()
                if len(part) >= 9:  # 避免短语/乱码  至少为单句七绝
                    poems.append(part + "。")  # 补回句号


    if debug:
        print(f"共提取单句：{len(poems)} 条")
        print("示例：", poems[:10])
        print(len(poems[0]))

    return poems



if __name__=="__main__":
    to_poem_list("Poetry/宋_1.csv",True)