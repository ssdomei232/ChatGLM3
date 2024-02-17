# ChatGLM3

<p align="center">
🤗 <a href="https://huggingface.co/THUDM/chatglm3-6b" target="_blank">HF Repo</a> • 🤖 <a href="https://modelscope.cn/models/ZhipuAI/chatglm3-6b" target="_blank">ModelScope</a> • 🤖 <a href="https://www.wisemodel.cn/models/ZhipuAI/chatglm3-6b" target="_blank">WiseModel</a> • 🐦 <a href="https://twitter.com/thukeg" target="_blank">Twitter</a> • 📃 <a href="https://arxiv.org/abs/2103.10360" target="_blank">[GLM@ACL 22]</a> <a href="https://github.com/THUDM/GLM" target="_blank">[GitHub]</a> • 📃 <a href="https://arxiv.org/abs/2210.02414" target="_blank">[GLM-130B@ICLR 23]</a> <a href="https://github.com/THUDM/GLM-130B" target="_blank">[GitHub]</a> <br>
</p>
<p align="center">
    👋 加入我们的 <a href="https://join.slack.com/t/chatglm/shared_invite/zt-25ti5uohv-A_hs~am_D3Q8XPZMpj7wwQ" target="_blank">Slack</a> 和 <a href="resources/WECHAT.md" target="_blank">微信</a>
</p>
<p align="center">
📍在 <a href="https://www.chatglm.cn">chatglm.cn</a> 体验更大规模的 ChatGLM 模型。
</p>

[Read this in English.](./README_en.md)

📔 关于`ChatGLM3-6B`
更为详细的使用信息，可以参考
+ [ChatGLM3 开放技术文档](https://lslfd0slxc.feishu.cn/wiki/WvQbwIJ9tiPAxGk8ywDck6yfnof?from=from_copylink)
+ [Bilibili video](https://www.bilibili.com/video/BV1uC4y1J7yA)
+ [YouTube video](https://www.youtube.com/watch?v=Pw9PB6R7ORA)

## ChatGLM3 介绍

**ChatGLM3** 是智谱AI和清华大学 KEG 实验室联合发布的对话预训练模型。ChatGLM3-6B 是 ChatGLM3
系列中的开源模型，在保留了前两代模型对话流畅、部署门槛低等众多优秀特性的基础上，ChatGLM3-6B 引入了如下特性：

1. **更强大的基础模型：** ChatGLM3-6B 的基础模型 ChatGLM3-6B-Base
   采用了更多样的训练数据、更充分的训练步数和更合理的训练策略。在语义、数学、推理、代码、知识等不同角度的数据集上测评显示，*
   *ChatGLM3-6B-Base 具有在 10B 以下的基础模型中最强的性能**。
2. **更完整的功能支持：** ChatGLM3-6B 采用了全新设计的 Prompt 格式
   ，除正常的多轮对话外。同时原生支持工具调用（Function Call）、代码执行（Code Interpreter）和
   Agent 任务等复杂场景。
3. **更全面的开源序列：** 除了对话模型 [ChatGLM3-6B](https://huggingface.co/THUDM/chatglm3-6b)
   外，还开源了基础模型 [ChatGLM3-6B-Base](https://huggingface.co/THUDM/chatglm3-6b-base)
   、长文本对话模型 [ChatGLM3-6B-32K](https://huggingface.co/THUDM/chatglm3-6b-32k)。以上所有权重对学术研究**完全开放**
   ，在填写 [问卷](https://open.bigmodel.cn/mla/form) 进行登记后**亦允许免费商业使用**。

-----

ChatGLM3 开源模型旨在与开源社区一起推动大模型技术发展，恳请开发者和大家遵守 [开源协议](MODEL_LICENSE)
，勿将开源模型和代码及基于开源项目产生的衍生物用于任何可能给国家和社会带来危害的用途以及用于任何未经过安全评估和备案的服务。目前，本项目团队未基于
**ChatGLM3 开源模型**开发任何应用，包括网页端、安卓、苹果 iOS 及 Windows App 等应用。

尽管模型在训练的各个阶段都尽力确保数据的合规性和准确性，但由于 ChatGLM3-6B
模型规模较小，且模型受概率随机性因素影响，无法保证输出内容的准确。同时模型的输出容易被用户的输入误导。*
*本项目不承担开源模型和代码导致的数据安全、舆情风险或发生任何模型被误导、滥用、传播、不当利用而产生的风险和责任。**

## 模型列表

|      Model       | Seq Length |                                                                                                   Download                                                                                                   
|:----------------:|:----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:
|   ChatGLM3-6B    |     8k     |        [HuggingFace](https://huggingface.co/THUDM/chatglm3-6b) \| [ModelScope](https://modelscope.cn/models/ZhipuAI/chatglm3-6b) \| [WiseModel](https://www.wisemodel.cn/models/ZhipuAI/chatglm3-6b)         
| ChatGLM3-6B-Base |     8k     | [HuggingFace](https://huggingface.co/THUDM/chatglm3-6b-base) \| [ModelScope](https://modelscope.cn/models/ZhipuAI/chatglm3-6b-base) \| [WiseModel](https://www.wisemodel.cn/models/ZhipuAI/chatglm3-6b-base) 
| ChatGLM3-6B-32K  |    32k     |  [HuggingFace](https://huggingface.co/THUDM/chatglm3-6b-32k) \| [ModelScope](https://modelscope.cn/models/ZhipuAI/chatglm3-6b-32k) \| [WiseModel](https://www.wisemodel.cn/models/ZhipuAI/chatglm3-6b-32k)   

请注意，所有模型的最新更新都会在 Huggingface 率先发布。 ModelScope 和 WiseModel 由于没有与 Huggingface 同步，需要开发人员手动更新，可能会在
Huggingface 更新后一段时间内同步更新。

