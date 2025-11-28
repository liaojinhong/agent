from agents import function_tool

# 1. 定义核心工具：让智能体能够展示菜单
@function_tool
def show_order_menu():
    menu = '''
    1. 美式咖啡 ￥10
    2. 拿铁 ￥15
    3. 卡布奇诺 ￥15
    4. 摩卡 ￥20
    5. 热巧克力 ￥15
    6. 红茶 ￥10
    7. 松饼 ￥10
    8. 蛋糕 ￥15
    '''
    print(menu)  # 在后台打印菜单
    return menu  # 将菜单内容返回给智能体

# 2. 创建智能体，并赋予它工具和明确的指令
menu_agent = Agent(
    name="Menu_Agent",
    model="deepseek-v3-tool",  # 使用支持函数调用的模型
    instructions="你是一名餐厅服务助手，当顾客询问菜单时，你需要调用工具展示菜单，并根据菜单内容回答顾客的问题。",
    tools=[show_order_menu]  # 让智能体获得使用菜单工具的能力
)