from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from typing import TypedDict

search = TavilySearchResults(max_results=2)
tools = [search]
llm = ChatOpenAI(model="gpt-3.5-turbo")

class AgentState(TypedDict):
    question: str
    answer: str

def agent_node(state: AgentState):
    prompt = """你是工业设备运维工程师，不确定的参数、行业标准就调用搜索工具。"""
    res = llm.invoke(prompt + state["question"])
    return {"answer": res.content}

builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)
builder.set_entry_point("agent")
builder.add_edge("agent", END)
graph = builder.compile()

if __name__ == "__main__":
    result = graph.invoke({"question": "轴承温度过高告警怎么排查"})
    print(result["answer"])
