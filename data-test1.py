import pandas as pd
import numpy as np

# 创建一个销售分析报表（类似Excel中常见的销售分析透视表）
df = pd.read_csv('s2.csv')
sales_analysis = pd.pivot_table(
    df,  # 使用数据框df
    index=['产品线', '性别'],  # 将'产品线'和'性别'作为行索引，分组分析
    columns=['城市'],  # 将'城市'作为列索引，展开不同城市
    values=['总计', '数量'],  # 要分析的值为'总计'和'数量'
    aggfunc={
        '总计': 'sum',  # 对'总计'列进行求和
        '数量': 'mean'  # 对'数量'列进行求平均，计算每个分组的平均购买数量
    },
    margins=True,  # 添加总计行和总计列，显示整体的汇总数据
    fill_value=0  # 将缺失值填充为0，避免数据为空
).round(2)  # 将结果四舍五入到小数点后两位

# 重命名列，使列名更易于阅读，使用f字符串格式
sales_analysis.columns = [f'{col[0]}_{col[1]}' for col in sales_analysis.columns]

print("销售分析报表：")  # 输出销售分析报表的标题
print(sales_analysis)  # 打印销售分析报表
# 保存为新的CSV文件
sales_analysis.to_csv('s2-3.csv', index=True, encoding='utf-8-sig')
