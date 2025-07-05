import pandas as pd
import numpy as np

# 读取s2-3.csv数据
df = pd.read_csv('s2-3.csv')

print("原始数据信息：")
print(f"数据形状: {df.shape}")
print(f"列名: {df.columns.tolist()}")
print("\n前5行数据:")
print(df.head())

# s2-3.csv已经是透视表格式，我们需要重新整理数据
# 设置产品线为索引，性别为行，保留总计和数量的城市列
df_filtered = df[df['产品线'] != 'All'].copy()  # 排除汇总行

# 创建新的透视表：以性别为行索引，产品线和城市为列
# 先分离总计列和数量列
total_cols = [col for col in df.columns if col.startswith('总计_')]
quantity_cols = [col for col in df.columns if col.startswith('数量_')]

# 创建总计数据的透视表
total_pivot = df_filtered.pivot_table(
    index=['性别'],
    columns=['产品线'],
    values=total_cols,
    aggfunc='sum',
    fill_value=0
)

# 创建数量数据的透视表
quantity_pivot = df_filtered.pivot_table(
    index=['性别'],
    columns=['产品线'],
    values=quantity_cols,
    aggfunc='sum',
    fill_value=0
)

# 合并两个透视表
result_pivot = pd.concat([total_pivot, quantity_pivot], axis=1, keys=['总计', '数量'])

# 添加汇总行
result_pivot.loc['All'] = result_pivot.sum()

print("\n透视表分析结果：")
print(result_pivot)

# 保存为s2-4.csv，保留行索引信息
result_pivot.to_csv('s2-4.csv', index=True, encoding='utf-8-sig')

print("\n分析完成！结果已保存为s2-4.csv")
print(f"透视表形状: {result_pivot.shape}")