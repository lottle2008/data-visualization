
import pandas as pd
import numpy as np

# 创建一个销售分析报表（类似Excel中常见的销售分析透视表）
df = pd.read_csv('s2.csv')# 使用 agg 方法进行复杂的分组统计

advanced_stats = df.groupby('产品线').agg({
    '总计': [  # 对 '订单金额' 列进行多种统计
        ('总销售额', 'sum'),  # 计算每个商品类别的订单金额总和，并重命名为 "总销售额"
        ('平均订单额', 'mean'),  # 计算每个商品类别的平均订单金额，并重命名为 "平均订单额"
        ('订单数', 'count'),  # 计算每个商品类别的订单数量，并重命名为 "订单数"
        ('最大订单', 'max'),  # 计算每个商品类别的最大订单金额，并重命名为 "最大订单"
        ('最小订单', 'min')  # 计算每个商品类别的最小订单金额，并重命名为 "最小订单"
    ]
}).round(2)  # 将结果四舍五入到小数点后两位

advanced_stats.to_csv('s5.csv', index=True, encoding='utf-8-sig')

print("\n=== 分析完成 ===")
print(f"高级统计结果形状: {advanced_stats.shape}")
print("\n统计结果预览:")
print(advanced_stats)