import random


# json 파일 만들기 - 3개 만들어야 함(대분류, 소분류, 상품)
import json
from collections import OrderedDict

file = OrderedDict()

username_list = []


small_cate_list = [['감자', '당근', '양파', '대파', '오이', '콩나물', '버섯'],
                   ['사과', '샤인머스캣', '바나나', '방울토마토', '파인애플'],
                   ['오징어•낙지•문어', '전복•조개류', '새우•게•랍스터', '생선류'],
                   ['소고기', '돼지고기', '닭•오리고기', '소시지•베이컨•하몽', '계란'],
                   ['국•탕•찌개', '밑반찬', '김치•젓갈•장류', '두부•어묵•부침개'],
                   ['생수', '탄산수', '주스', '커피'],
                   ['초콜릿', '젤리', '캔디', '쿠키', '과자'],
                   ['우유', '두유', '요거트', '치즈', '아이스크림']]

major_cate_list = ['채소', '과일', '해산•건어물', '정육•가공육•계란', '국•반찬•메인요리', '생수•음료•커피', '간식', '유제품']
N = 39
idx = 0
# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = '/Users/sumtuckyi/web crawling/s_cate_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    for i in range(len(major_cate_list)):
        for j in range(len(small_cate_list[i])):
            file["model"] = "products.SmallCategory"
            file["pk"] = idx+1
            file["fields"] = {
                'name' : small_cate_list[i][j],
                'upper_cate' : i+1
            }

            json.dump(file, f, ensure_ascii=False, indent="\t")
            if idx != N-1:
                f.write(',')
                idx += 1
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')