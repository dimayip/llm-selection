#!/usr/bin/env python3
"""
LLM 成本估算工具
根据调用量预估不同模型的月成本，支持国际模型（USD）和国内模型（CNY）。
"""

import sys

# 模型价格表（参考价，截至 2026-05，以官网为准）
# unit: "per_1m" = 每百万tokens, "per_1k" = 每千tokens
PRICING = {
    # 国际模型 (USD per 1M tokens)
    "gpt-4o":           {"input": 2.50,  "output": 10.00, "unit": "per_1m", "currency": "USD", "name": "GPT-4o"},
    "gpt-o3":           {"input": 10.00, "output": 40.00, "unit": "per_1m", "currency": "USD", "name": "GPT-o3"},
    "gpt-4o-mini":      {"input": 0.15,  "output": 0.60,  "unit": "per_1m", "currency": "USD", "name": "GPT-4o mini"},
    "claude-4-sonnet":  {"input": 5.00,  "output": 25.00, "unit": "per_1m", "currency": "USD", "name": "Claude 4 Sonnet"},
    "claude-3.7-sonnet":{"input": 3.00,  "output": 15.00, "unit": "per_1m", "currency": "USD", "name": "Claude 3.7 Sonnet"},
    "gemini-2.5-pro":   {"input": 1.25,  "output": 10.00, "unit": "per_1m", "currency": "USD", "name": "Gemini 2.5 Pro"},
    "gemini-2.5-flash": {"input": 0.15,  "output": 0.60,  "unit": "per_1m", "currency": "USD", "name": "Gemini 2.5 Flash"},
    "deepseek-v3":      {"input": 0.27,  "output": 1.10,  "unit": "per_1m", "currency": "USD", "name": "DeepSeek V3"},
    "deepseek-r1":      {"input": 0.55,  "output": 2.19,  "unit": "per_1m", "currency": "USD", "name": "DeepSeek R1"},

    # 国内模型 (CNY per 1K tokens)
    "hunyuan-turbo":    {"input": 0.03,  "output": 0.10,  "unit": "per_1k", "currency": "CNY", "name": "混元 Turbo"},
    "hunyuan-t1":       {"input": 0.10,  "output": 0.30,  "unit": "per_1k", "currency": "CNY", "name": "混元 T1"},
    "qwen-max":         {"input": 0.04,  "output": 0.12,  "unit": "per_1k", "currency": "CNY", "name": "通义千问 Max"},
    "qwen-plus":        {"input": 0.004, "output": 0.012, "unit": "per_1k", "currency": "CNY", "name": "通义千问 Plus"},
    "qwen-vl-plus":     {"input": 0.008, "output": 0.008, "unit": "per_1k", "currency": "CNY", "name": "通义千问 VL Plus"},
    "ernie-4.0-turbo": {"input": 0.03,  "output": 0.10,  "unit": "per_1k", "currency": "CNY", "name": "文心 4.0 Turbo"},
    "ernie-4.5":        {"input": 0.05,  "output": 0.15,  "unit": "per_1k", "currency": "CNY", "name": "文心 4.5"},
    "glm-4-plus":       {"input": 0.05,  "output": 0.05,  "unit": "per_1k", "currency": "CNY", "name": "GLM-4 Plus"},
    "kimi-k1.5":       {"input": 0.06,  "output": 0.06,  "unit": "per_1k", "currency": "CNY", "name": "Kimi K1.5"},
    "doubao-1.5-pro":   {"input": 0.005, "output": 0.009, "unit": "per_1k", "currency": "CNY", "name": "豆包 1.5 Pro"},
    "spark-4.0":        {"input": 0.02,  "output": 0.02,  "unit": "per_1k", "currency": "CNY", "name": "讯飞星火 4.0"},
}

# 自部署 GPU 成本参考（每台每月，人民币）
GPU_PRICES = {
    "A100_40GB": 10000,
    "A100_80GB": 16000,
    "H100": 25000,
    "RTX_4090": 3000,
}


def estimate_api_cost(model_key, daily_calls, avg_input_tokens, avg_output_tokens, days=30):
    """估算单个模型的 API 月成本。"""
    if model_key not in PRICING:
        return {"cost": -1, "currency": "UNK", "model_name": model_key, "error": "未知模型"}

    p = PRICING[model_key]
    currency = p["currency"]

    # 统一转换为 per_1m 单价
    if p["unit"] == "per_1k":
        input_unit = p["input"] * 1000
        output_unit = p["output"] * 1000
    else:
        input_unit = p["input"]
        output_unit = p["output"]

    input_cost = (avg_input_tokens / 1_000_000) * input_unit * daily_calls * days
    output_cost = (avg_output_tokens / 1_000_000) * output_unit * daily_calls * days
    total = input_cost + output_cost

    return {
        "cost": round(total, 2),
        "currency": currency,
        "model_name": p["name"],
        "model_key": model_key,
        "input_cost": round(input_cost, 2),
        "output_cost": round(output_cost, 2),
    }


def print_comparison_table(daily_calls, avg_input, avg_output, model_keys=None, days=30):
    """打印多个模型的对比表。"""
    if model_keys is None:
        model_keys = list(PRICING.keys())

    results = []
    for key in model_keys:
        r = estimate_api_cost(key, daily_calls, avg_input, avg_output, days)
        if r.get("cost", 0) > 0:
            results.append(r)

    results.sort(key=lambda x: x["cost"])

    print(f"\n{'='*80}")
    print(f"  成本对比表（日调用 {daily_calls:,} 次，输入 {avg_input} tokens，输出 {avg_output} tokens，{days} 天）")
    print(f"{'='*80}\n")
    print(f"  {'排名':<4} {'模型':<22} {'月成本':<16} {'输入成本':<14} {'输出成本':<14} 币种")
    print("  " + "-" * 76)

    for i, r in enumerate(results, 1):
        symbol = "¥" if r["currency"] == "CNY" else "$"
        print(f"  {i:<4} {r['model_name']:<22} {symbol}{r['cost']:<15} "
              f"{symbol}{r['input_cost']:<13} {symbol}{r['output_cost']:<13} {r['currency']}")

    print(f"\n  提示：价格为参考价（截至 2026-05），以各平台官网为准。")
    print(f"  国内模型价格为每千 tokens，已自动换算为每百万 tokens 进行比较。\n")


def interactive_mode():
    """交互式成本估算。"""
    print("\n" + "=" * 50)
    print("  LLM 成本估算工具（交互模式）")
    print("=" * 50)

    try:
        daily_calls = int(input("\n  日均调用次数（次/天）: ") or "10000")
        avg_input = int(input("  平均输入 token 数: ") or "500")
        avg_output = int(input("  平均输出 token 数: ") or "300")
        days = int(input("  计算天数（默认 30 天）: ") or "30")

        print("\n  请选择要对比的模型类型：")
        print("    1. 全部模型")
        print("    2. 仅国际模型（OpenAI/Anthropic/Google/DeepSeek）")
        print("    3. 仅国内模型（混元/通义/文心/GLM/Kimi/豆包）")
        print("    4. 仅低成本模型（<¥1000/月 或 <$200/月）")
        choice = input("  请选择（1-4，默认 1）: ") or "1"

        if choice == "2":
            keys = [k for k in PRICING if PRICING[k]["currency"] == "USD"]
        elif choice == "3":
            keys = [k for k in PRICING if PRICING[k]["currency"] == "CNY"]
        elif choice == "4":
            all_results = []
            for k in PRICING:
                r = estimate_api_cost(k, daily_calls, avg_input, avg_output, days)
                if r.get("cost", 0) > 0:
                    all_results.append((k, r))
            keys = [k for k, r in all_results
                    if (r["currency"] == "CNY" and r["cost"] < 1000)
                    or (r["currency"] == "USD" and r["cost"] < 200)]
        else:
            keys = list(PRICING.keys())

        print_comparison_table(daily_calls, avg_input, avg_output, keys, days)

        show_self_host = input("\n  是否显示自部署成本对比？(y/N): ").lower() == 'y'
        if show_self_host:
            print(f"\n  自部署成本参考（GPU 租赁费，{days} 天）:")
            for gpu, price_per_month in GPU_PRICES.items():
                daily = price_per_month / 30
                total = daily * days
                print(f"    {gpu:<15}: ¥{daily:.0f}/天 → ¥{total:.0f}/{days}天")

            print("\n  适用场景建议：")
            print("    - Qwen 2.5 14B : 1×RTX 4090 (¥3,000/月)")
            print("    - Qwen 2.5 32B : 1×A100 40GB (¥10,000/月)")
            print("    - Qwen 2.5 72B : 2×A100 40GB (¥20,000/月)")
            print("    - DeepSeek R1 14B: 1×RTX 4090 (¥3,000/月)")

    except KeyboardInterrupt:
        print("\n\n已退出。")
    except Exception as e:
        print(f"\n  错误: {e}")


def main():
    if len(sys.argv) >= 4:
        daily_calls = int(sys.argv[1])
        avg_input = int(sys.argv[2])
        avg_output = int(sys.argv[3])
        model_keys = sys.argv[4:] if len(sys.argv) > 4 else None
        days = int(sys.argv[5]) if len(sys.argv) > 5 else 30
        print_comparison_table(daily_calls, avg_input, avg_output, model_keys, days)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
