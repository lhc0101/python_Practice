import numpy as np
data = np.dtype({
    'names': ['name','chinese','english','math'],
    'formats': ['S32','i','i','i']
    # 'names': ['name', 'chinese', 'english', 'math'],
    # 'formats': ['S32', 'i', 'i', 'i']
})


students = np.array(
    [
        ("ZhangFei", 66, 65, 30),
        ("GuanYu", 95, 85, 98),
        ("ZhaoYun", 93, 92, 96),
        ("HuangZhong", 90, 88, 77),
        ("DianWei", 80, 90, 90)
    ],dtype=data
)

name = students[:]['name']
chinese = students[:]['chinese']
english = students[:]['english']
math = students[:]['math']

def show(name,cj):
    print('{} | {} | {} | {} | {} | {} '
          .format(name,np.mean(cj),np.min(cj),np.max(cj),np.var(cj),np.std(cj)))

print("科目 | 平均成绩 | 最小成绩 | 最大成绩 | 方差 | 标准差")
show("语文", chinese)
show("英语", english)
show("数学", math)

# print("排名:")
# #用sorted函数进行排序
# ranking = sorted(students,key=lambda x:x[1]+x[2]+x[3], reverse=True)
# print(ranking)

