exercise_1_1_hint = """本练习中的评分函数正在寻找包含精确阿拉伯数字“1”、“2”和“3”的答案。
你通常只需通过提问就能让 Claude 做到你想要的。"""

exercise_1_2_hint = """本练习中的评分函数正在寻找包含“soo”或“giggles”的答案。
有很多方法可以解决这个问题，只需提问即可！"""

exercise_2_1_hint ="""本练习中的评分函数正在寻找任何包含“hola”一词的答案。
要求 Claude 像你与人交谈时那样用西班牙语回复。就这么简单！"""

exercise_2_2_hint = """本练习中的评分函数正在寻找精确的“Michael Jordan”。
你会如何要求另一个人这样做？不带其他词语地回复？只回复名字，不带其他内容？有几种方法可以解决这个问题。"""

exercise_2_3_hint = """此单元格中的评分函数正在寻找一个等于或大于 800 字的回复。
因为大型语言模型（LLM）还不擅长数词，你可能需要超出你的目标。"""

exercise_3_1_hint = """本练习中的评分函数正在寻找包含“incorrect”或“not correct”这些词的答案。
给 Claude 一个角色，这可能会让 Claude 更好地解决数学问题！"""

exercise_4_1_hint = """本练习中的评分函数正在寻找包含“haiku”和“pig”这些词的解决方案。
不要忘记在任何你希望替换主题的地方包含精确的短语“{TOPIC}”。改变“TOPIC”变量的值应该让 Claude 写一首关于不同主题的俳句。"""

exercise_4_2_hint = """本练习中的评分函数正在寻找包含“brown”一词的回复。
如果你用 XML 标签包围“{QUESTION}”，这会如何改变 Claude 的回复？"""

exercise_4_3_hint = """本练习中的评分函数正在寻找包含“brown”一词的回复。
尝试一次删除一个词或一段字符，从那些最不合逻辑的部分开始。每次删除一个词也能帮助你了解 Claude 能或不能解析和理解多少内容。"""

exercise_5_1_hint = """本练习的评分函数正在寻找包含“Warrior”一词的回复。
用 Claude 的语气写更多词语，以引导 Claude 按照你希望的方式行事。例如，与其写“斯蒂芬·库里是最好的，因为”，不如写“斯蒂芬·库里是最好的，原因有三。1：”"""

exercise_5_2_hint = """评分函数正在寻找一个长度超过 5 行且包含“cat”和“<haiku>”这些词的回复。
从简单开始。目前，提示要求 Claude 写一首俳句。你可以改变它，要求写两首（甚至更多）。然后，如果你遇到格式问题，在已经让 Claude 写出不止一首俳句之后，再修改你的提示来解决。"""

exercise_5_3_hint = """本练习中的评分函数正在寻找包含“tail”、“cat”和“<haiku>”这些词的回复。
将这个练习分解成几个步骤会很有帮助。
1. 修改初始提示模板，让 Claude 写两首诗。
2. 给 Claude 指示诗歌将是关于什么的，但不要直接写入主题（例如，狗、猫等），而是用关键词“{ANIMAL1}”和“{ANIMAL2}”替换这些主题。
3. 运行提示并确保带有变量替换的完整提示中所有词语都已正确替换。如果没有，请检查你的{括号}标签是否拼写正确，并用单个花括号正确格式化。"""

exercise_6_1_hint = """本练习中的评分函数正在寻找正确的分类字母 + 闭括号和类别名称的首字母，例如“C) B”或“B) B”等。
让我们一步一步地进行这个练习：
1. Claude 怎么会知道你想用什么类别？告诉它！将你想要的四个类别直接包含在提示中。务必包含括号内的字母以便于分类。随意使用 XML 标签来组织你的提示，并向 Claude 明确类别的开始和结束位置。
2. 尝试减少多余的文本，以便 Claude 立即只回答分类。有几种方法可以做到这一点，从替 Claude 说话（提供从句子开头到单个开括号的任何内容，以便 Claude 知道你希望括号内的字母作为答案的第一部分）到告诉 Claude 你只想要分类，跳过前言。
如果你想复习这些技巧，请参考第 2 章和第 5 章。
3. Claude 在回答时可能仍然错误分类或不包含类别名称。通过告诉 Claude 在回答中包含完整的类别名称来解决这个问题。
4. 确保你的提示模板中仍然有{email}，以便我们能够正确地替换电子邮件供 Claude 评估。"""

exercise_6_1_solution = """
USER TURN
请将此电子邮件分类到以下类别中：{email}

除了类别，不要包含任何额外的词语。

<categories>
(A) 售前问题
(B) 损坏或有缺陷的物品
(C) 账单问题
(D) 其他（请解释）
</categories>

ASSISTANT TURN
(
"""

exercise_6_2_hint = """本练习中的评分函数正在寻找仅包含在<answer>标签中的正确字母，例如“<answer>B</answer>”。正确的分类字母与上述练习中的相同。
有时最简单的方法是给 Claude 一个你希望其输出看起来的示例。只是不要忘记用<example></example>标签包裹你的示例！并且不要忘记，如果你用任何内容预填充 Claude 的回复，Claude 实际上不会将其作为回复的一部分输出。"""

exercise_7_1_hint = """你将需要编写一些示例电子邮件并为 Claude 分类（使用你想要的精确格式）。有多种方法可以做到这一点。以下是一些指导方针。
1. 尝试至少有两个示例电子邮件。Claude 不需要所有类别的示例，并且示例不必很长。为你认为更棘手的类别提供示例会更有帮助（在第 6 章练习 1 的底部要求你思考过）。XML 标签将帮助你将示例与提示的其余部分分开，尽管这不是必需的。
2. 确保你的示例答案格式与你希望 Claude 使用的格式完全一致，这样 Claude 也能模仿该格式。这种格式应该使 Claude 的答案以类别字母结尾。无论你将{email}占位符放在哪里，请确保它的格式与你的示例电子邮件完全相同。
3. 确保你仍然在提示本身中列出了类别，否则 Claude 将不知道要引用哪些类别，以及{email}作为替换的占位符。"""

exercise_7_1_solution = """
USER TURN
请将电子邮件分类到以下类别中，并且不要包含解释：
<categories>
(A) 售前问题
(B) 损坏或有缺陷的物品
(C) 账单问题
(D) 其他（请解释）
</categories>

以下是一些正确答案格式的示例：
<examples>
Q: 购买 Mixmaster4000 需要多少钱？
A: 正确的类别是：A

Q: 我的 Mixmaster 打不开了。
A: 正确的类别是：B

Q: 请将我从您的邮件列表中移除。
A: 正确的类别是：D
</examples>

这是供你分类的电子邮件：{email}

ASSISTANT TURN
正确的类别是：
"""
exercise_8_1_hint = """本练习中的评分函数正在寻找包含短语“I do not”、“I don't”或“Unfortunately”的回复。
如果 Claude 不知道答案，它应该怎么做？"""

exercise_8_2_hint = """本练习中的评分函数正在寻找包含短语“49-fold”的回复。
让 Claude 首先通过提取相关引用并查看这些引用是否提供了足够的证据来展示其工作和思考过程。如果你想复习，请参考第 8 章课程。"""

exercise_9_1_solution = """
你是一位税务会计大师。你的任务是使用任何提供的参考文档来回答用户问题。

以下是你应该用来回答用户问题的材料：
<docs>
{TAX_CODE}
</docs>

以下是回复示例：
<example>
<question>
“合格”员工的定义是什么？
</question>
<answer>
<quotes>就本小节而言——
(A) 一般规定
“合格员工”一词指任何——
(i) 非被排除员工，且
(ii) 同意在本小节所作的选择中满足秘书确定的必要要求，以确保公司根据第 24 章对合格股票的预扣要求得到满足。</quotes>

<answer>根据提供的文档，“合格员工”被定义为符合以下条件的个人：

1. 不是文档中定义的“被排除员工”。
2. 同意满足秘书确定的必要要求，以确保公司根据第 24 章对合格股票的预扣要求得到满足。</answer>
</example>

首先，在<quotes></quotes>标签中收集与回答用户问题相关的引用。如果没有引用，则写“no relevant quotes found”。

然后，在<answer></answer>标签中回答用户问题之前插入两个段落分隔符。只有当你确信<quotes></quotes>标签中的引用支持你的答案时，才回答用户问题。如果不支持，请告诉用户你很抱歉没有足够的信息来回答用户的问题。

这是用户问题：{QUESTION}
"""

exercise_9_2_solution = """
你是 Codebot，一个乐于助人的 AI 助手，负责发现代码问题并提出可能的改进建议。

扮演一个苏格拉底式导师，帮助用户学习。

你将收到用户提供的一些代码。请执行以下操作：
1. 识别代码中的任何问题。将每个问题放入单独的<issues>标签中。
2. 邀请用户编写代码的修订版本来修复问题。

这是一个示例：

<example>
<code>
def calculate_circle_area(radius):
    return (3.14 * radius) ** 2
</code>
<issues>
<issue>
3.14 被平方了，而实际上应该只有半径被平方。
</issue>
<response>
这几乎是正确的，但有一个与运算顺序相关的问题。写出圆的公式，然后仔细查看代码中的括号可能会有所帮助。
</response>
</example>

这是你要分析的代码：

<code>
{CODE}
</code>

找出相关问题并编写苏格拉底式导师风格的回复。不要给用户太多帮助！相反，只给他们指导，让他们自己找到正确的解决方案。

将每个问题放入<issue>标签中，并将你的最终回复放入<response>标签中。
"""

exercise_10_2_1_solution = """system_prompt = system_prompt_tools_general_explanation + \"""以下是 JSONSchema 格式的可用函数：

<tools>

<tool_description>
<tool_name>get_user</tool_name>
<description>
根据用户 ID 从数据库中检索用户。
</description>
<parameters>
<parameter>
<name>user_id</name>
<type>int</type>
<description>要检索的用户 ID。</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>get_product</tool_name>
<description>
根据产品 ID 从数据库中检索产品。
</description>
<parameters>
<parameter>
<name>product_id</name>
<type>int</type>
<description>要检索的产品 ID。</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_user</tool_name>
<description>
向数据库添加新用户。
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>用户的姓名。</description>
</parameter>
<parameter>
<name>email</name>
<type>str</type>
<description>用户的电子邮件地址。</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_product</tool_name>
<description>
向数据库添加新产品。
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>产品的名称。</description>
</parameter>
<parameter>
<name>price</name>
<type>float</type>
<description>产品的价格。</description>
</parameter>
</parameters>
</tool_description>

</tools>
"""