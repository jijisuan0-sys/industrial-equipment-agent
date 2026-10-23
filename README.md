 工业设备运维智能Agent
基于 LangGraph 实现 ReAct 智能体，面向工业设备故障诊断场景 Demo

 ✨ 功能特性
1. RAG知识库：读取设备PDF手册，检索故障处理方案
2. 联网搜索：集成 Tavily 工具，查询工业标准、设备资料
3. ReAct 智能体：思考-工具调用-回答闭环，自主排查设备问题

 🛠 技术栈
- Python
- LangChain / LangGraph
- Tavily Search
- PyPDF

 📦 环境安装
```bash
pip install -r requirements.txt
