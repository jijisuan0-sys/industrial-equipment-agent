工业设备运维智能 Agent
基于 LangGraph 实现 ReAct 智能体，面向工业设备故障诊断场景Demo。
✨ 功能特性
1. RAG知识库：读取设备PDF手册，检索故障处理方案
2. 工具调用：集成 Tavily 搜索，查询公开行业标准、设备参数
3. 人工审批节点：高危操作建议强制人工复核，贴合工业安全管控需求
4. 全流程日志记录，操作可追溯
 🛠 技术栈
Python | LangGraph | LangChain | Tavily API | RAG

📌 核心原理
采用 ReAct（Reason + Act）循环：思考 → 调用工具 → 观察结果，循环推理。
区别于普通RAG问答，Agent可以自主判断：什么时候查本地手册、什么时候联网检索资料。

🚀 快速启动
1. 安装依赖
```bash
pip install -r requirements.txt
