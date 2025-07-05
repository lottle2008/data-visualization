import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('s1.csv')

# 定义英文到中文的列名映射
column_mapping = {
    'Invoice ID': '发票编号',
    'Branch': '分店',
    'City': '城市',
    'Customer type': '客户类型',
    'Gender': '性别',
    'Product line': '产品线',
    'Unit price': '单价',
    'Quantity': '数量',
    'Tax 5%': '税费5%',
    'Total': '总计',
    'Date': '日期',
    'Time': '时间',
    'Payment': '支付方式',
    'cogs': '销售成本',
    'gross margin percentage': '毛利率百分比',
    'gross income': '毛利润',
    'Rating': '评分'
}

# 重命名列名
df_chinese = df.rename(columns=column_mapping)

# 翻译数据内容中的英文值
# 翻译客户类型
df_chinese['客户类型'] = df_chinese['客户类型'].replace({
    'Member': '会员',
    'Normal': '普通客户'
})

# 翻译性别
df_chinese['性别'] = df_chinese['性别'].replace({
    'Male': '男',
    'Female': '女'
})

# 翻译产品线
df_chinese['产品线'] = df_chinese['产品线'].replace({
    'Health and beauty': '健康美容',
    'Electronic accessories': '电子配件',
    'Home and lifestyle': '家居生活',
    'Sports and travel': '运动旅行',
    'Food and beverages': '食品饮料',
    'Fashion accessories': '时尚配饰'
})

# 翻译支付方式
df_chinese['支付方式'] = df_chinese['支付方式'].replace({
    'Ewallet': '电子钱包',
    'Cash': '现金',
    'Credit card': '信用卡'
})

# 保存为新的CSV文件
df_chinese.to_csv('s2.csv', index=False, encoding='utf-8-sig')

print("翻译完成！已保存为 s2.csv")
print(f"原始数据形状: {df.shape}")
print(f"翻译后数据形状: {df_chinese.shape}")
print("\n翻译后的前5行数据:")
print(df_chinese.head())
print("\n列名对照:")
for eng, chn in column_mapping.items():
    print(f"{eng} -> {chn}")