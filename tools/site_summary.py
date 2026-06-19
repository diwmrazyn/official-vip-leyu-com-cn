import json
import textwrap
from datetime import datetime

# 内置站点资料
SITE_DATA = {
    "title": "乐鱼体育",
    "keywords": ["乐鱼体育", "体育赛事", "在线娱乐", "VIP服务", "体育投注"],
    "url": "https://official-vip-leyu.com.cn",
    "description": "乐鱼体育提供专业的体育赛事直播与投注服务，汇聚全球热门赛事，打造高端VIP体验平台。",
    "tags": ["体育平台", "赛事直播", "在线投注", "VIP会员", "体育资讯"],
    "version": "2.0.1",
    "last_updated": "2025-03-21"
}

def generate_summary(data: dict) -> str:
    """根据站点资料生成结构化摘要"""
    lines = []
    lines.append("=" * 50)
    lines.append("站点摘要报告")
    lines.append("=" * 50)

    # 基本信息
    lines.append(f"站点名称：{data.get('title', '未命名')}")
    lines.append(f"访问地址：{data.get('url', '无URL')}")
    lines.append(f"更新日期：{data.get('last_updated', '未知')}")
    lines.append(f"版本号：{data.get('version', 'N/A')}")

    # 关键词
    kw = data.get("keywords", [])
    if kw:
        lines.append(f"核心关键词：{', '.join(kw)}")
    else:
        lines.append("核心关键词：无")

    # 标签
    tags = data.get("tags", [])
    if tags:
        lines.append(f"相关标签：{', '.join(tags)}")
    else:
        lines.append("相关标签：无")

    # 描述（自动换行）
    desc = data.get("description", "暂无描述")
    wrapped_desc = textwrap.fill(desc, width=60, initial_indent="描述：", subsequent_indent="      ")
    lines.append(wrapped_desc)

    # 辅助统计
    lines.append(f"关键词数量：{len(kw)} 个")
    lines.append(f"标签数量：{len(tags)} 个")
    lines.append("-" * 50)
    lines.append(f"报告生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 50)

    return "\n".join(lines)


def export_json(data: dict) -> str:
    """将站点资料转换为JSON字符串（格式化输出）"""
    return json.dumps(data, ensure_ascii=False, indent=2)


def print_summary(data: dict = None) -> None:
    """打印完整摘要到控制台"""
    if data is None:
        data = SITE_DATA
    summary = generate_summary(data)
    print(summary)


def main():
    """主运行函数"""
    print("=== 乐鱼体育站点摘要 ===")
    print_summary(SITE_DATA)

    print("\n\n=== JSON 格式输出 ===")
    json_str = export_json(SITE_DATA)
    print(json_str)


if __name__ == "__main__":
    main()