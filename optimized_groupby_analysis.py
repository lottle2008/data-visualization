import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional
import logging
from pathlib import Path

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataAnalyzer:
    """数据分析器类，提供多字段分组和透视表分析功能"""
    
    def __init__(self, file_path: str):
        """初始化数据分析器
        
        Args:
            file_path: 数据文件路径
        """
        self.file_path = Path(file_path)
        self.df = None
        self._validate_file()
        
    def _validate_file(self) -> None:
        """验证文件是否存在"""
        if not self.file_path.exists():
            raise FileNotFoundError(f"文件不存在: {self.file_path}")
        logger.info(f"文件验证成功: {self.file_path}")
    
    def load_data(self, encoding: str = 'utf-8') -> pd.DataFrame:
        """加载数据文件
        
        Args:
            encoding: 文件编码格式
            
        Returns:
            加载的DataFrame
        """
        try:
            self.df = pd.read_csv(self.file_path, encoding=encoding)
            logger.info(f"数据加载成功，形状: {self.df.shape}")
            return self.df
        except Exception as e:
            logger.error(f"数据加载失败: {e}")
            raise
    
    def data_summary(self) -> Dict[str, Any]:
        """获取数据摘要信息"""
        if self.df is None:
            raise ValueError("请先加载数据")
            
        summary = {
            'shape': self.df.shape,
            'columns': self.df.columns.tolist(),
            'dtypes': self.df.dtypes.to_dict(),
            'missing_values': self.df.isnull().sum().to_dict(),
            'memory_usage': self.df.memory_usage(deep=True).sum()
        }
        
        logger.info(f"数据摘要生成完成")
        return summary
    
    def optimized_groupby(
        self, 
        group_cols: List[str], 
        agg_dict: Dict[str, str], 
        filter_conditions: Optional[Dict[str, Any]] = None
    ) -> pd.DataFrame:
        """优化的分组聚合操作
        
        Args:
            group_cols: 分组列名列表
            agg_dict: 聚合字典 {列名: 聚合函数}
            filter_conditions: 过滤条件字典
            
        Returns:
            分组聚合结果
        """
        if self.df is None:
            raise ValueError("请先加载数据")
        
        # 验证列名是否存在
        missing_cols = set(group_cols + list(agg_dict.keys())) - set(self.df.columns)
        if missing_cols:
            raise ValueError(f"以下列不存在: {missing_cols}")
        
        # 应用过滤条件
        df_filtered = self.df.copy()
        if filter_conditions:
            for col, condition in filter_conditions.items():
                if isinstance(condition, list):
                    df_filtered = df_filtered[df_filtered[col].isin(condition)]
                else:
                    df_filtered = df_filtered[df_filtered[col] == condition]
        
        # 执行分组聚合
        try:
            result = df_filtered.groupby(group_cols).agg(agg_dict).round(2)
            logger.info(f"分组聚合完成，结果形状: {result.shape}")
            return result
        except Exception as e:
            logger.error(f"分组聚合失败: {e}")
            raise
    
    def advanced_pivot_table(
        self,
        index: List[str],
        columns: List[str],
        values: List[str],
        aggfunc: Dict[str, str],
        margins: bool = True,
        fill_value: Any = 0
    ) -> pd.DataFrame:
        """高级透视表分析
        
        Args:
            index: 行索引列
            columns: 列索引列
            values: 值列
            aggfunc: 聚合函数字典
            margins: 是否添加边际总计
            fill_value: 填充值
            
        Returns:
            透视表结果
        """
        if self.df is None:
            raise ValueError("请先加载数据")
        
        try:
            pivot_result = pd.pivot_table(
                self.df,
                index=index,
                columns=columns,
                values=values,
                aggfunc=aggfunc,
                margins=margins,
                fill_value=fill_value
            ).round(2)
            
            logger.info(f"透视表创建完成，形状: {pivot_result.shape}")
            return pivot_result
        except Exception as e:
            logger.error(f"透视表创建失败: {e}")
            raise
    
    def multi_level_groupby(
        self,
        level1_cols: List[str],
        level2_cols: List[str],
        agg_dict: Dict[str, str]
    ) -> Dict[str, pd.DataFrame]:
        """多层级分组分析
        
        Args:
            level1_cols: 第一层分组列
            level2_cols: 第二层分组列
            agg_dict: 聚合字典
            
        Returns:
            多层级分组结果字典
        """
        if self.df is None:
            raise ValueError("请先加载数据")
        
        results = {}
        
        # 第一层分组
        level1_result = self.optimized_groupby(level1_cols, agg_dict)
        results['level1'] = level1_result
        
        # 第二层分组
        level2_result = self.optimized_groupby(level2_cols, agg_dict)
        results['level2'] = level2_result
        
        # 组合分组
        combined_cols = level1_cols + level2_cols
        combined_result = self.optimized_groupby(combined_cols, agg_dict)
        results['combined'] = combined_result
        
        logger.info("多层级分组分析完成")
        return results
    
    def save_results(
        self,
        data: pd.DataFrame,
        output_path: str,
        include_index: bool = True,
        encoding: str = 'utf-8-sig'
    ) -> None:
        """保存分析结果
        
        Args:
            data: 要保存的数据
            output_path: 输出文件路径
            include_index: 是否包含索引
            encoding: 编码格式
        """
        try:
            data.to_csv(output_path, index=include_index, encoding=encoding)
            logger.info(f"结果已保存到: {output_path}")
        except Exception as e:
            logger.error(f"保存失败: {e}")
            raise

# 使用示例和优化建议
def main():
    """主函数 - 演示优化的多字段分组操作"""
    
    # 1. 初始化分析器
    analyzer = DataAnalyzer('s2.csv')
    
    # 2. 加载数据
    df = analyzer.load_data()
    
    # 3. 数据摘要
    summary = analyzer.data_summary()
    print("=== 数据摘要 ===")
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    # 4. 优化的分组聚合示例
    print("\n=== 优化的分组聚合 ===")
    
    # 按产品线和性别分组，计算总计和数量的统计
    group_result = analyzer.optimized_groupby(
        group_cols=['产品线', '性别'],
        agg_dict={
            '总计': 'sum',
            '数量': 'mean',
            '毛利率百分比': 'mean'
        }
    )
    print(group_result)
    
    # 5. 高级透视表分析
    print("\n=== 高级透视表分析 ===")
    pivot_result = analyzer.advanced_pivot_table(
        index=['性别'],
        columns=['产品线'],
        values=['总计', '数量'],
        aggfunc={'总计': 'sum', '数量': 'mean'}
    )
    print(pivot_result)
    
    # 6. 多层级分组分析
    print("\n=== 多层级分组分析 ===")
    multi_results = analyzer.multi_level_groupby(
        level1_cols=['产品线'],
        level2_cols=['性别'],
        agg_dict={'总计': 'sum', '数量': 'count'}
    )
    
    for level, result in multi_results.items():
        print(f"\n{level} 分组结果:")
        print(result)
    
    # 7. 保存结果
    analyzer.save_results(pivot_result, 'optimized_pivot_result.csv')
    analyzer.save_results(group_result, 'optimized_group_result.csv')
    
    print("\n=== 分析完成 ===")


print("复杂分组统计：")  # 输出复杂分组统计的标题
print(advanced_stats)  # 打印复杂分组统计的结果




if __name__ == "__main__":
    main()

# 性能优化建议：
# 1. 使用 .query() 方法进行条件筛选，比布尔索引更快
# 2. 对于大数据集，考虑使用 .groupby().agg() 而不是 .pivot_table()
# 3. 使用 .memory_usage(deep=True) 监控内存使用
# 4. 对于重复操作，考虑缓存中间结果
# 5. 使用 .dtype 优化数据类型，减少内存占用

# 代码质量建议：
# 1. 添加类型提示提高代码可读性
# 2. 使用日志记录操作过程
# 3. 添加异常处理和数据验证
# 4. 将功能封装成类，提高代码复用性
# 5. 添加详细的文档字符串