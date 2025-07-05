import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 读取CSV文件，跳过多层标题行，正确设置列名
df = pd.read_csv('s5.csv', header=[0, 1], index_col=0)

# 重新整理数据结构，使其更适合可视化
# 将多层列标题展平
df.columns = ['总销售额', '平均订单额', '订单数', '最大订单', '最小订单']

# 重置索引，使产品线成为一个普通列
df_reset = df.reset_index()
df_reset.columns.name = None  # 移除列名的名称

print("数据结构预览:")
print(df_reset.head())
print(f"\n数据形状: {df_reset.shape}")
print(f"列名: {df_reset.columns.tolist()}")

# 创建子图
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('销售数据可视化分析', fontsize=16, fontweight='bold')

# 1. 平均订单额折线图
axes[0, 0].plot(df_reset['产品线'], df_reset['平均订单额'], 
                marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)
axes[0, 0].set_title('各产品线平均订单额', fontsize=12)
axes[0, 0].set_xlabel('产品线')
axes[0, 0].set_ylabel('平均订单额 (元)')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. 总销售额柱状图
axes[0, 1].bar(df_reset['产品线'], df_reset['总销售额'], 
               color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'])
axes[0, 1].set_title('各产品线总销售额', fontsize=12)
axes[0, 1].set_xlabel('产品线')
axes[0, 1].set_ylabel('总销售额 (元)')
axes[0, 1].tick_params(axis='x', rotation=45)

# 3. 订单数量对比
axes[1, 0].bar(df_reset['产品线'], df_reset['订单数'], 
               color=['#FF9F43', '#10AC84', '#5F27CD', '#00D2D3', '#FF6348', '#2E86AB'])
axes[1, 0].set_title('各产品线订单数量', fontsize=12)
axes[1, 0].set_xlabel('产品线')
axes[1, 0].set_ylabel('订单数量')
axes[1, 0].tick_params(axis='x', rotation=45)

# 4. 最大订单与最小订单对比
width = 0.35
x_pos = range(len(df_reset['产品线']))
axes[1, 1].bar([p - width/2 for p in x_pos], df_reset['最大订单'], 
               width, label='最大订单', color='lightcoral', alpha=0.8)
axes[1, 1].bar([p + width/2 for p in x_pos], df_reset['最小订单'], 
               width, label='最小订单', color='lightblue', alpha=0.8)
axes[1, 1].set_title('各产品线订单金额范围', fontsize=12)
axes[1, 1].set_xlabel('产品线')
axes[1, 1].set_ylabel('订单金额 (元)')
axes[1, 1].set_xticks(x_pos)
axes[1, 1].set_xticklabels(df_reset['产品线'], rotation=45)
axes[1, 1].legend()

# 调整布局
plt.tight_layout()

# 保存图表
plt.savefig('销售数据可视化分析.png', dpi=300, bbox_inches='tight')
print("\n图表已保存为: 销售数据可视化分析.png")

# 显示图表
plt.show()

# # 输出数据统计摘要
print("\n=== 数据统计摘要 ===")
print(f"平均订单额最高的产品线: {df_reset.loc[df_reset['平均订单额'].idxmax(), '产品线']} ({df_reset['平均订单额'].max():.2f}元)")
print(f"总销售额最高的产品线: {df_reset.loc[df_reset['总销售额'].idxmax(), '产品线']} ({df_reset['总销售额'].max():.2f}元)")
print(f"订单数最多的产品线: {df_reset.loc[df_reset['订单数'].idxmax(), '产品线']} ({df_reset['订单数'].max()}个订单)")
print(f"单笔最大订单: {df_reset['最大订单'].max():.2f}元")
print(f"单笔最小订单: {df_reset['最小订单'].min():.2f}元")