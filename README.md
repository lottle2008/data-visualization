# 数据分析项目

## 项目简介

这是一个基于Python的数据分析项目，主要用于处理和分析销售数据，包含数据清洗、透视表分析、统计分析和数据可视化等功能。

## 项目结构

### 核心脚本
- `analyze_s2_3.py` - 数据透视表分析脚本
- `data-test1.py` - 基础数据处理和透视表生成
- `extract_female_data.py` - 女性客户数据提取分析
- `test5.py` - 高级统计分析（总计、平均值、计数、最大值、最小值）
- `可视化.py` - 数据可视化分析脚本
- `optimized_groupby_analysis.py` - 优化的分组分析工具类
- `translate_csv.py` - CSV数据翻译处理

### 数据文件
- `s2.csv` - 原始销售数据
- `s2-3.csv` - 透视表处理后的数据
- `s2-4.csv` - 最终分析结果
- `s3.csv` - 女性客户数据
- `s5.csv` - 高级统计分析结果
- `company_data.xlsx` - 公司数据
- `sales_data.csv` - 销售数据
- 其他支持数据文件

### 输出文件
- `销售数据可视化分析.png` - 数据可视化图表
- `s3.html` - HTML格式报告
- `optimized_group_result.csv` - 优化分组结果
- `optimized_pivot_result.csv` - 优化透视表结果

## 主要功能

### 1. 数据透视表分析
- 多维度数据透视
- 按产品线、性别、城市等维度分析
- 自动计算总计和数量统计

### 2. 统计分析
- 描述性统计（总和、平均值、计数、最大值、最小值）
- 分组统计分析
- 多字段聚合分析

### 3. 数据可视化
- 多子图布局设计
- 折线图：平均订单额趋势
- 柱状图：销售额和订单数对比
- 分组柱状图：订单金额范围分析
- 支持中文显示

### 4. 数据处理优化
- 面向对象的数据分析器
- 性能优化的分组操作
- 错误处理和日志记录
- 类型提示和代码规范

## 技术栈

- **Python 3.x**
- **pandas** - 数据处理和分析
- **matplotlib** - 数据可视化
- **numpy** - 数值计算

## 使用方法

### 基础数据分析
```bash
python data-test1.py
```

### 高级统计分析
```bash
python test5.py
```

### 数据可视化
```bash
python 可视化.py
```

### 优化分组分析
```bash
python optimized_groupby_analysis.py
```

## 分析结果示例

### 关键业务指标
- **平均订单额最高**: 家居生活 (336.64元)
- **总销售额最高**: 食品饮料 (56144.84元)
- **订单数最多**: 时尚配饰 (178个订单)
- **订单金额范围**: 10.68元 - 1042.65元

## 代码质量特性

- ✅ 错误处理和异常管理
- ✅ 类型提示和文档字符串
- ✅ 面向对象设计
- ✅ 性能优化
- ✅ 代码复用性
- ✅ 中文编码支持

## 环境要求

```
pandas>=1.3.0
matplotlib>=3.3.0
numpy>=1.20.0
```

## 作者

Jason - assist

## 许可证

MIT License
