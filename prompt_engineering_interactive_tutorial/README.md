# 欢迎来到Anthropic的提示工程互动教程

## 课程介绍与目标

本课程旨在为您提供关于如何在Claude中设计最优提示的全面分步理解。

**完成本课程后，您将能够**：

- 掌握良好提示的基本结构
- 识别常见的失败模式，并学习“80/20”技术来解决它们
- 理解Claude的优势和劣势
- 从零开始为常见用例构建强大的提示

## 课程结构与内容

本课程的结构旨在为您提供大量练习编写和排查提示的机会。课程分为**9个章节，并附带配套练习**，以及一个包含更高级方法的附录。建议您**按章节顺序学习本课程**。

**每节课底部都有一个“示例演练场”区域**，您可以在其中自由地尝试课程中的示例，亲身体验改变提示如何改变Claude的响应。此外，还有一个[答案](https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLye0Oh_hR_ZB75a47KX_E/edit?usp=sharing)。

注意：本教程使用的是我们最小、最快、最经济的模型——Claude 3 Haiku。Anthropic还有[另外两个模型](https://docs.anthropic.com/claude/docs/models-overview)，Claude 3 Sonnet和Claude 3 Opus，它们比Haiku更智能，其中Opus是智能程度最高的。

*本教程也存在于[使用Anthropic的Claude for Sheets扩展的Google Sheets](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing)上。我们建议使用该版本，因为它更用户友好。*

准备好开始时，请前往“`01_Basic Prompt Structure`”继续。

## 目录

每个章节都包含一节课和一套练习。

### 初级

- **第一章：** 基本提示结构

- **第二章：** 清晰直接

- **第三章：** 分配角色

### 中级

- **第四章：** 将数据与指令分离

- **第五章：** 格式化输出和为Claude发言

- **第六章：** 预认知（逐步思考）

- **第七章：** 使用示例

### 高级

- **第八章：** 避免幻觉

- **第九章：** 构建复杂提示（行业用例）
  - 从零开始构建复杂提示 - 聊天机器人
  - 法律服务的复杂提示
  - **练习：** 金融服务的复杂提示
  - **练习：** 编码的复杂提示
  - 祝贺与后续步骤

- **附录：** 超越标准提示
  - 链式提示
  - 工具使用
  - 搜索与检索

---

# Welcome to Anthropic's Prompt Engineering Interactive Tutorial

## Course introduction and goals

This course is intended to provide you with a comprehensive step-by-step understanding of how to engineer optimal prompts within Claude.

**After completing this course, you will be able to**:

- Master the basic structure of a good prompt
- Recognize common failure modes and learn the '80/20' techniques to address them
- Understand Claude's strengths and weaknesses
- Build strong prompts from scratch for common use cases

## Course structure and content

This course is structured to allow you many chances to practice writing and troubleshooting prompts yourself. The course is broken up into **9 chapters with accompanying exercises**, as well as an appendix of even more advanced methods. It is intended for you to **work through the course in chapter order**.

**Each lesson has an "Example Playground" area** at the bottom where you are free to experiment with the examples in the lesson and see for yourself how changing prompts can change Claude's responses. There is also an [answer key](https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit?usp=sharing).

Note: This tutorial uses our smallest, fastest, and cheapest model, Claude 3 Haiku. Anthropic has [two other models](https://docs.anthropic.com/claude/docs/models-overview), Claude 3 Sonnet and Claude 3 Opus, which are more intelligent than Haiku, with Opus being the most intelligent.

*This tutorial also exists on [Google Sheets using Anthropic's Claude for Sheets extension](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing). We recommend using that version as it is more user friendly.*

When you are ready to begin, go to `01_Basic Prompt Structure` to proceed.

## Table of Contents

Each chapter consists of a lesson and a set of exercises.

### Beginner

- **Chapter 1:** Basic Prompt Structure

- **Chapter 2:** Being Clear and Direct  

- **Chapter 3:** Assigning Roles

### Intermediate

- **Chapter 4:** Separating Data from Instructions

- **Chapter 5:** Formatting Output & Speaking for Claude

- **Chapter 6:** Precognition (Thinking Step by Step)

- **Chapter 7:** Using Examples

### Advanced

- **Chapter 8:** Avoiding Hallucinations

- **Chapter 9:** Building Complex Prompts (Industry Use Cases)
  - Complex Prompts from Scratch - Chatbot
  - Complex Prompts for Legal Services
  - **Exercise:** Complex Prompts for Financial Services
  - **Exercise:** Complex Prompts for Coding
  - Congratulations & Next Steps

- **Appendix:** Beyond Standard Prompting
  - Chaining Prompts
  - Tool Use
  - Search & Retrieval
