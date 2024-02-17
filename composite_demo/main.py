import streamlit as st
st.set_page_config(
    page_title="ChatGLM3 Demo",
    page_icon=":robot:",
    layout='centered',
    initial_sidebar_state='expanded',
)


import demo_chat, demo_ci, demo_tool
from enum import Enum

DEFAULT_SYSTEM_PROMPT = '''
你是 ChatGLM3，一个由 Zhipu.AI 训练的大型语言模型。请仔细按照用户的说明进行操作。使用 Markdown 进行响应。在响应时,你应该使用中文,而不是英文。
'''.strip()

# Set the title of the demo
st.title("ChatGLM3 Demo")

# Add your custom text here, with smaller font size
st.markdown(
    "<sub>智谱AI 公开在线技术文档: https://lslfd0slxc.feishu.cn/wiki/WvQbwIJ9tiPAxGk8ywDck6yfnof </sub> \n\n <sub> 更多 ChatGLM3-6B 的使用方法请参考文档。</sub>",
    unsafe_allow_html=True)


class Mode(str, Enum):
    CHAT, TOOL, CI = '💬 Chat', '🛠️ Tool', '🧑‍💻 Code Interpreter'


with st.sidebar:
    top_p = st.slider(
        'top_p(生成文本多样性)', 0.0, 1.0, 0.8, step=0.01
    )
    temperature = st.slider(
        'temperature(生成文本的随机性和多样性,过高可使模型发癫)', 0.0, 1.5, 0.95, step=0.01
    )
    repetition_penalty = st.slider(
        'repetition_penalty(重复惩罚)', 0.0, 2.0, 1.1, step=0.01
    )
    max_new_token = st.slider(
        'Output length(生成的token的最大长度)', 5, 32000, 256, step=1
    )

    cols = st.columns(2)
    export_btn = cols[0]
    clear_history = cols[1].button("清除历史", use_container_width=True)
    retry = export_btn.button("重试", use_container_width=True)

    system_prompt = st.text_area(
        label="系统提示 (仅限对话模式)",
        height=300,
        value=DEFAULT_SYSTEM_PROMPT,
    )

prompt_text = st.chat_input(
    'Chat with ChatGLM3!',
    key='chat_input',
)

tab = st.radio(
    'Mode',
    [mode.value for mode in Mode],
    horizontal=True,
    label_visibility='hidden',
)

if clear_history or retry:
    prompt_text = ""

match tab:
    case Mode.CHAT:
        demo_chat.main(
            retry=retry,
            top_p=top_p,
            temperature=temperature,
            prompt_text=prompt_text,
            system_prompt=system_prompt,
            repetition_penalty=repetition_penalty,
            max_new_tokens=max_new_token
        )
    case Mode.TOOL:
        demo_tool.main(
            retry=retry,
            top_p=top_p,
            temperature=temperature,
            prompt_text=prompt_text,
            repetition_penalty=repetition_penalty,
            max_new_tokens=max_new_token,
            truncate_length=1024)
    case Mode.CI:
        demo_ci.main(
            retry=retry,
            top_p=top_p,
            temperature=temperature,
            prompt_text=prompt_text,
            repetition_penalty=repetition_penalty,
            max_new_tokens=max_new_token,
            truncate_length=1024)
    case _:
        st.error(f'Unexpected tab: {tab}')
