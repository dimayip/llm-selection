# 大模型选型 Skill

一个系统化的决策框架，用于根据您的具体使用场景、预算约束和合规要求，选择最合适的大语言模型（LLM）。

## 🌟 功能特性

| 能力 | 说明 |
|------|------|
| **场景分析** | 10+ 场景类型（聊天、代码、创作、推理、多模态等） |
| **国内外模型覆盖** | OpenAI/Claude/Gemini + 混元/通义/文心/DeepSeek/GLM/Kimi/豆包 |
| **硬约束筛选** | 数据合规、上下文长度、部署方式、多模态支持 |
| **评分矩阵** | 推理能力 30% + 多模态 25% + 上下文 20% + 速度 15% + 成本 10% |
| **成本估算** | 根据调用量自动计算各模型月成本 |
| **落地建议** | 小流量验证方案 + Fallback 策略 |

## 📁 文件结构

```
llm-selection/
├── SKILL.md                    ← Skill 主入口
├── references/
│   ├── model_zoo.md           ← 30+ 主流模型详细对比数据
│   └── selection_framework.md ← 选型框架、评分矩阵、场景速查表
└── scripts/
    └── cost_estimator.py      ← 成本估算脚本
```

## 🚀 安装方法

运行以下命令安装该 Skill：

```bash
npx skills add https://github.com/dimayip/llm-selection.git
```

## 💡 使用方法

在 CodeBuddy 对话中使用触发关键词：

- "帮我选型"
- "该选哪个模型"
- "XX场景用什么模型"
- "对比一下XX和XX"
- "大模型选型"
- "成本预估"

Skill 将自动启动 5 步选型流程：

### 步骤 1：收集需求
- 必问：使用场景、预算、数据合规要求
- 选问：上下文长度、QPS、部署偏好、多模态需求

### 步骤 2：硬约束初筛
- 数据合规 → 国内业务只能选国内模型
- 上下文长度 → 过滤不满足的模型
- 部署方式 → API / 可本地 / 必须本地

### 步骤 3：评分排序
加权评分：
- 任务匹配度 40% + 成本 30% + 延迟 15% + 稳定性 10% + 易用性 5%

### 步骤 4：输出选型报告
输出内容包括：
- Top 3 推荐（首选 / 备选 / 性价比之选）
- 成本对比表
- 落地建议（小流量验证 + Fallback 策略）

### 步骤 5：成本估算
运行成本估算脚本：
```bash
python3 scripts/cost_estimator.py
```

## 🌐 支持的模型

### 国际模型
- **OpenAI**: GPT-4o, GPT-4o-mini, o1, o3
- **Anthropic**: Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Sonnet
- **Google**: Gemini 2.0 Flash, Gemini 2.5 Pro

### 国内模型
- **腾讯混元**: Hunyuan-Turbo, Hunyuan-Pro, Hunyuan-T1
- **阿里通义**: Qwen-Max, Qwen-Plus, Qwen-Turbo, Qwen3-235B
- **百度文心**: ERNIE-4.5-Turbo, ERNIE-Spark
- **DeepSeek**: DeepSeek-V3, DeepSeek-R1
- **智谱 GLM**: GLM-4-Plus, GLM-4-Air
- **月之暗面 Kimi**: Moonshot-v1-128k
- **字节豆包**: Doubao-Pro-32k

## 📊 成本估算

`scripts/cost_estimator.py` 脚本可帮助估算月成本：

```bash
python3 scripts/cost_estimator.py [日均调用量] [平均输入token数] [平均输出token数]
```

示例：
```bash
python3 scripts/cost_estimator.py 10000 500 300
```

这将输出所有支持模型的估算月成本对比表。

## 🔍 选型框架

关于选型框架、评分矩阵和场景推荐的详细信息，请参阅：

- **[模型动物园](references/model_zoo.md)** - 30+ 主流模型详细对比数据
- **[选型框架](references/selection_framework.md)** - 评分矩阵、场景速查表和实施指南

## 📝 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

## 📧 联系我们

- GitHub Issues: [https://github.com/dimayip/llm-selection/issues](https://github.com/dimayip/llm-selection/issues)
- 作者: bellchen

---

⭐ 如果您觉得这个 skill 有用，请在 GitHub 上给我们一个星标！
