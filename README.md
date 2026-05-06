# LLM Selection Skill

A comprehensive decision-making framework for selecting the most suitable Large Language Model (LLM) based on your specific use cases, budget constraints, and compliance requirements.

## 🌟 Features

| Capability | Description |
|------------|-------------|
| **Scenario Analysis** | 10+ scenario types (chat, coding, creative writing, reasoning, multimodal, etc.) |
| **Global & Chinese Models** | OpenAI/Claude/Gemini + Hunyuan/Qwen/ERNIE/DeepSeek/GLM/Kimi/Doubao |
| **Hard Constraint Filtering** | Data compliance, context length, deployment mode, multimodal support |
| **Scoring Matrix** | Reasoning 30% + Multimodal 25% + Context 20% + Speed 15% + Cost 10% |
| **Cost Estimation** | Automatically calculate monthly costs based on usage volume |
| **Implementation Guide** | Canary testing plan + Fallback strategy |

## 📁 File Structure

```
llm-selection/
├── SKILL.md                    ← Skill entry point
├── references/
│   ├── model_zoo.md           ← 30+ mainstream model comparisons
│   └── selection_framework.md ← Selection framework, scoring matrix, scenario cheat sheet
└── scripts/
    └── cost_estimator.py      ← Cost estimation script
```

## 🚀 Installation

Run the following command to install the skill:

```bash
npx skills add https://github.com/dimayip/llm-selection.git
```

## 💡 Usage

Trigger the skill by using keywords in your CodeBuddy conversation:

- "Help me choose a model"
- "Which model for [scenario]"
- "Compare Model A and Model B"
- "LLM selection"
- "Cost estimation"

The skill will automatically启动 a 5-step selection process:

### Step 1: Requirement Collection
- Ask about: use case, budget, data compliance requirements
- Optional: context length, QPS, deployment preference, multimodal needs

### Step 2: Hard Constraint Filtering
- Data compliance → Only Chinese models for domestic business
- Context length → Filter out models that don't meet requirements
- Deployment mode → API / Can be local / Must be local

### Step 3: Scoring & Ranking
Weighted scoring:
- Task match 40% + Cost 30% + Latency 15% + Stability 10% + Usability 5%

### Step 4: Selection Report
Output includes:
- Top 3 recommendations (Primary / Alternative / Best Value)
- Cost comparison table
- Implementation suggestions (canary testing + fallback strategy)

### Step 5: Cost Estimation
Run the cost estimator:
```bash
python3 scripts/cost_estimator.py
```

## 🌐 Supported Models

### International Models
- **OpenAI**: GPT-4o, GPT-4o-mini, o1, o3
- **Anthropic**: Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Sonnet
- **Google**: Gemini 2.0 Flash, Gemini 2.5 Pro

### Chinese Models
- **Tencent Hunyuan**: Hunyuan-Turbo, Hunyuan-Pro, Hunyuan-T1
- **Alibaba Qwen**: Qwen-Max, Qwen-Plus, Qwen-Turbo, Qwen3-235B
- **Baidu ERNIE**: ERNIE-4.5-Turbo, ERNIE-Spark
- **DeepSeek**: DeepSeek-V3, DeepSeek-R1
- **Zhipu GLM**: GLM-4-Plus, GLM-4-Air
- **Moonshot Kimi**: Moonshot-v1-128k
- **ByteDance Doubao**: Doubao-Pro-32k

## 📊 Cost Estimation

The `scripts/cost_estimator.py` script helps you estimate monthly costs:

```bash
python3 scripts/cost_estimator.py [daily_calls] [avg_input_tokens] [avg_output_tokens]
```

Example:
```bash
python3 scripts/cost_estimator.py 10000 500 300
```

This will output a comparison table with estimated monthly costs for all supported models.

## 🔍 Selection Framework

For detailed information about the selection framework, scoring matrix, and scenario-specific recommendations, see:

- **[Model Zoo](references/model_zoo.md)** - Detailed comparison data for 30+ mainstream models
- **[Selection Framework](references/selection_framework.md)** - Scoring matrix, scenario cheat sheet, and implementation guide

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

- GitHub Issues: [https://github.com/dimayip/llm-selection/issues](https://github.com/dimayip/llm-selection/issues)
- Author: bellchen

---

⭐ If you find this skill useful, please consider giving it a star on GitHub!
