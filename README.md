此FORK适用于只希望简单体验ChatGLM3的人,所以删除了很多对于这类人来说不必要的目录和文件 </br>
此FORK默认使用4bit量化,从本地加载模型.模型文件请放在`basic_demo`或`composite_demo`目录的`chatglm3-6b`目录下 </br>
如果你使用windows或带有桌面的linux,更推荐你使用`composite_demo`,如果你使用命令行的linux,请使用`basic_demo`体验 </br>
如果你的GPU显存小于13G,那么可以直接克隆此仓库到本地使用,不需要做额外的修改代码操作 </br>
如果你的GPU显存大于13G,且又喜欢折腾,请离开此仓库,以免浪费时间

## 模型列表

|      Model       | Seq Length |                                                                                                   Download                                                                                                   
|:----------------:|:----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:
|   ChatGLM3-6B    |     8k     |        [HuggingFace](https://huggingface.co/THUDM/chatglm3-6b) \| [ModelScope](https://modelscope.cn/models/ZhipuAI/chatglm3-6b) \| [WiseModel](https://www.wisemodel.cn/models/ZhipuAI/chatglm3-6b)         
| ChatGLM3-6B-Base |     8k     | [HuggingFace](https://huggingface.co/THUDM/chatglm3-6b-base) \| [ModelScope](https://modelscope.cn/models/ZhipuAI/chatglm3-6b-base) \| [WiseModel](https://www.wisemodel.cn/models/ZhipuAI/chatglm3-6b-base) 
| ChatGLM3-6B-32K  |    32k     |  [HuggingFace](https://huggingface.co/THUDM/chatglm3-6b-32k) \| [ModelScope](https://modelscope.cn/models/ZhipuAI/chatglm3-6b-32k) \| [WiseModel](https://www.wisemodel.cn/models/ZhipuAI/chatglm3-6b-32k)   


