"""
Main program
"""

#!pip install --force-reinstall langchain==0.0.343
#!pip install --force-reinstall openai==1.3.6
#!pip install streamlit

import os
import sys


from response import ResponseService


import streamlit as st # All streamlit commands will be available through the "st" alias

import streaming_lib as glib  # reference to local lib script
import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler
from langchain.callbacks.streamlit.streamlit_callback_handler import (
    LLMThoughtLabeler as LLMThoughtLabeler,
)

from langchain.chains import ConversationChain
from langchain.llms import OpenAI


#
# ---> BEGIN: To modify the default behaviour of the LLMThoughtLabeler class
#
from typing import NamedTuple

CHECKMARK_EMOJI = "✅"
THINKING_EMOJI = ":thinking_face:"
HISTORY_EMOJI = ":books:"
EXCEPTION_EMOJI = "⚠️"

class ToolRecord(NamedTuple):
    """The tool record as a NamedTuple."""

    name: str
    input_str: str


class MyLLMThoughtLabeler(LLMThoughtLabeler):
    """
    Generates markdown labels for LLMThought containers. Pass a custom
    subclass of this to StreamlitCallbackHandler to override its default
    labeling logic.
    """

    def get_initial_label(self) -> str:
        """Return the markdown label for a new LLMThought that doesn't have
        an associated tool yet.
        """
        return f"{CHECKMARK_EMOJI} **On Line!**"

# ---> END: To modify the default behaviour of the LLMThoughtLabeler class

if __name__ == "__main__":
    # Remove the CWD from sys.path while we load stuff.
    # This is added back by InteractiveShellApp.init_path()
    if sys.path[0] == "":
        del sys.path[0]

    # print(sys.path)
    # To avoid numpy np.ndarray error when taking libraries
    # It was taking -> python -c "import site; print(site.USER_SITE)" -> the USER_SITE -> instead of where it was really installed -> python -c "import numpy as np; print(np.__file__); print(np.ndarray)"
    sys.path.insert(1, 'c:\\Users\\mchamochin\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages')
    # print(os.getcwd())

    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(find_dotenv())

    OpenAI.api_key=os.getenv("OPENAI_API_KEY")

    # Create the services
    response_service = ResponseService()

    #
    # Create the streamlit page
    #
    st.set_page_config(page_title="AI Law Query") #HTML title
    st.title("AI Law Query") #page title

    # display a multiline text box with no label
    input_text = st.text_area("Input text", label_visibility="collapsed")
    go_button = st.button("Go", type="primary")  # display a primary button

    if go_button:  # code in this if block will be run when the button is clicked
        # Use an empty container for streaming output
        c = st.container()
        with c:
            st_callback = StreamlitCallbackHandler(c, thought_labeler=MyLLMThoughtLabeler())
            streaming_response = response_service.generate_response(query=input_text, streaming_callback=st_callback)

        



