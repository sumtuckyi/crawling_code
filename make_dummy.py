import random


# json 파일 만들기 - 3개 만들어야 함(대분류, 소분류, 상품)
import json
from collections import OrderedDict

file = OrderedDict()

username_list = []




major_cate_list = ['채소', '과일', '해산•건어물', '정육•가공육•계란', '국•반찬•메인요리', '생수•음료•커피', '간식', '유제품']
N = len(major_cate_list)

# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = '/Users/sumtuckyi/web crawling/m_cate_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    for i in range(len(major_cate_list)):
        file["model"] = "products.MajorCategory"
        file["pk"] = i+1
        file["fields"] = {
            'name' : major_cate_list[i]
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')