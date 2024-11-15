# import pandas as pd
#
# def read_students(filename):
#     try:
#         df = pd.read_csv(filename)
#         return df
#     except FileNotFoundError:
#         print(f'File {filename} not found')
#         return None
#
# def calculate_gender_ratio(df):
#     if df.empty:
#         print("empty dataframe!")
#         return None
#     #统计每个性别的人数
#     gender_counts = df['性别'].value_counts()
#     # total = df.shape[0]
#     # print(total)
#     total = len(df)
#     print(total)
#
#     male_counts = gender_counts.get("男", 0)
#     female_counts = gender_counts.get("女", 0)
#     male_ratio = male_counts / total
#     female_ratio = female_counts / total
#     return male_ratio, female_ratio
#
# if __name__ == '__main__':
#     df = read_students("student_data.csv")
#     if df is None:
#         print("data is not available")
#         exit(1)
#     male_ratio, female_ratio = calculate_gender_ratio(df)
#     print(f"male_ratio: {male_ratio:.2f}")
#     print(f"female_ratio: {female_ratio:.2f}")

import csv


def read_student_info(filename):
    """读取学生信息CSV文件并返回一个列表，每个元素是一个学生的字典"""
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 假设文件中的列名为 '学号', '姓名', '班级', '性别'
                students.append({
                    '学号': row['学号'],
                    '姓名': row['姓名'],
                    '班级': row['班级'],
                    '性别': row['性别']
                })
    except FileNotFoundError:
        print(f"文件 {filename} 未找到！")
    return students


def calculate_gender_ratio(students):
    """计算男女生比例"""
    male_count = 0
    female_count = 0

    for student in students:
        if student['性别'] == '男':
            male_count += 1
        elif student['性别'] == '女':
            female_count += 1

    total_students = male_count + female_count
    if total_students == 0:
        return "没有学生数据"

    male_ratio = male_count / total_students * 100
    female_ratio = female_count / total_students * 100

    return male_ratio, female_ratio


def main():
    # 读取学生信息
    students = read_student_info('student_data.csv')

    if not students:
        print("没有可用的学生信息")
        return

    # 计算男女比例
    male_ratio, female_ratio = calculate_gender_ratio(students)

    print(f"男生比例: {male_ratio:.2f}%")
    print(f"女生比例: {female_ratio:.2f}%")


if __name__ == '__main__':
    main()


