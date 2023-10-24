#install these two libraries
# pip install pyautogen
# pip install xgboost

from autogen import AssistantAgent, UserProxyAgent

# config_list = [
#     {
#         'model': 'gpt-4-0613',
#         'api_key': 'YOUR OPENAI API KEY: NOT REQUIRED'
#     }
# ]

config_list = [{
    "api_type" : "open_ai",
    "api_base" : "http://localhost:1234/v1",
    "api_key" : "NULL"
}
]

llm_config = {'config_list': config_list}

#create an instance of AssistanAgent
assistant = AssistantAgent(
    name = "assistant",
    llm_config=llm_config,
)

#create an instance of UserProxyAgent
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=100,

)


# user_proxy.initiate_chat(
#     assistant,
#     message = """Write me a python function to print the number 1 though 30"""
# )

user_proxy.initiate_chat(
    assistant,
    message = """Write me a python function to check for prime number and the check for the number 79"""
)


# user_proxy.initiate_chat(
#     assistant,
#     message = """Write a python code for a snake game"""

# )