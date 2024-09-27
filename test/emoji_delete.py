# import re


# text = "🕓报修时间：2024.9.22\n📍报修地点: L134\n📝报修内容：店铺电路故障，请前往查看处理\n联系方式:电员 18602876540\n报修编号:JK002",
# # text = "这里是一些文本，包含 emoji 🕓 😊、📍🌍📝 和其他字符！🕓 还要去除\n的内容。JK002"

# # 要去除的内容（例如 emoji 和“去除的内容”）
# pattern = r'[\U0001F600-\U0001F64F|\U0001F300-\U0001F5FF|\U0001F680-\U0001F6FF|\U0001F700-\U0001F77F|\U0001F800-\U0001F8FF|\U0001F900-\U0001F9FF|\U0001FA00-\U0001FAFF]+|去除的内容'

# # 替换指定内容为空
# cleaned_text = re.sub(pattern, '', text)

# # 清理多余的空格
# cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

# print("清理后的文本：", cleaned_text)

import re

text = "🕓报修时间：2024.9.22\n📍报修地点: L134\n📝报修内容：店铺电路故障，请前往查看处理\n联系方式:电员 18602876540\n报修编号:JK002"

pattern = r'[\U0001F600-\U0001F64F|\U0001F300-\U0001F5FF|\U0001F680-\U0001F6FF|\U0001F700-\U0001F77F|\U0001F800-\U0001F8FF|\U0001F900-\U0001F9FF|\U0001FA00-\U0001FAFF]+|去除的内容'

cleaned_text = re.sub(pattern, '', text)

cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

print("清理后的文本：", cleaned_text)
