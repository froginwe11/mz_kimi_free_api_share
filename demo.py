from kimi import *

# 刷新kimi token
# {'error_type': 'auth.token.invalid', 'message': '您的授权已过期，请重新登录', 'detail': '该用户的授权已过期，请重新登录'}
kimi_token_refresh()

# 直接使用，会自动创建新对话
kimi_prompt("你好，我想了解唐僧是个什么样的人")

# 也可以主动创建新对话，然后传入对话id
chat_id = kimi_new_chat()
kimi_prompt("你怎么看上证指数两天时间从2700回归3000点？", chat_id=chat_id)
# 这样的化可以保持历史对话记录
answer = kimi_prompt("我刚才问了你什么内容？", chat_id=chat_id)
# 回答会作为返回值返回
print(answer)

chat_id = kimi_new_chat()
# 上传本地的测试文件，参数为文件路径以及当前对话的id
# 上传成功后会返回文件id
file_id = kimi_upload_file("测试上传.txt", chat_id=chat_id)
kimi_prompt("这篇文章说了什么内容？", refs=[file_id], chat_id=chat_id)
