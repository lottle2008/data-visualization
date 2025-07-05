import pandas as pd

# 读取s2.csv文件
df = pd.read_csv('s2.csv')

print(f"原始数据总行数: {len(df)}")
print(f"原始数据列名: {list(df.columns)}")

# 筛选女性客户的数据
female_data = df[df['性别'] == '女']

print(f"女性客户数据行数: {len(female_data)}")

# 提取指定的列：产品线、总计、支付方式、毛利率百分比
selected_columns = ['产品线', '总计', '支付方式', '毛利率百分比']
female_selected = female_data[selected_columns]

print(f"提取的列: {selected_columns}")
print("\n前5行提取的数据:")
print(female_selected.head())

# 保存为s3.csv
female_selected.to_csv('s3.csv', index=False, encoding='utf-8-sig')

print(f"\n数据已保存到s3.csv")
print(f"保存的数据形状: {female_selected.shape}")
print(f"各产品线的女性客户数量:")
print(female_selected['产品线'].value_counts())
print(f"\n各支付方式的使用次数:")
print(female_selected['支付方式'].value_counts())
print(f"\n毛利率统计信息:")
print(female_selected['毛利率百分比'].describe())