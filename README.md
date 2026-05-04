# LLM Selection Skill

大模型选型指南 Skill —— 根据使用场景、预算、合规要求等条件，系统化推荐最合适的大语言模型。

## 功能特性

| 能力 | 说明 |
|------|------|
| 场景分析 | 聊天/代码/创作/推理/多模态等 10+ 场景类型 |
| 国内外覆盖 | OpenAI/Claude/Gemini + 混元/通义/文心/DeepSeek/GLM 等 |
| 硬约束筛选 | 数据合规、上下文长度、部署方式、多模态能力 |
| 评分矩阵 | 推理30% + 多模态25% + 上下文20% + 速度15% + 成本10% |
| 成本估算 | 根据调用量自动计算各模型月成本 |
| 落地建议 | 小流量验证方案 + Fallback 策略 |

## 文件结构

```
llm-selection/
├── SKILL.md                    ← Skill 主入口
├── references/
│   ├── model_zoo.md           ← 30+ 主流模型详细对比数据
│   └── selection_framework.md ← 选型框架、评分矩阵、场景速查表
└── scripts/
    └── cost_estimator.py      ← 成本估算脚本
```

## 安装

将本仓库内容放入 CodeBuddy `.codebuddy/skills/llm-selection/` 目录，然后在 CodeBuddy 中加载 skill。

## 触发关键词

- "帮我选型"、"该选哪个模型"
- "XX场景用什么模型"、"对比一下XX和XX"
- "大模型选型"、"成本预估"

## 使用方法

在 CodeBuddy 对话中输入触发关键词，Skill 将自动启动 5 步选型流程：

1. **收集需求** — 询问使用场景、预算、数据合规要求
2. **硬约束初筛** — 根据合规/上下文/部署方式过滤模型
3. **评分排序** — 多维度打分，输出 Top 推荐
4. **输出选型报告** — Top3 推荐 + 成本对比表 + 落地建议
5. **成本估算** — 运行 `scripts/cost_estimator.py` 计算月成本

## 支持的模型

### 国际模型
- OpenAI: GPT-4o, GPT-4o-mini, o1, o3
- Anthropic: Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Sonnet
- Google: Gemini 2.0 Flash, Gemini 2.5 Pro

### 国内模型
- 腾讯混元: Hunyuan-Turbo, Hunyuan-Pro, Hunyuan-T1
- 阿里通义: Qwen-Max, Qwen-Plus, Qwen-Turbo, Qwen3-235B
- 百度文心: ERNIE-4.5-Turbo, ERNIE-Spark
- DeepSeek: DeepSeek-V3, DeepSeek-R1
- 智谱 GLM: GLM-4-Plus, GLM-4-Air
- 月之暗面 Kimi: Moonshot-v1-128k
- 字节豆包: Doubao-Pro-32k

## 许可证

MIT License
