def first(update, context):
    text = update.message.text
    nums_sum = sum(float(x) for x in text.split())
    print(nums_sum)
    update.message.reply_text(nums_sum)
# функция принимает значение из ТГ, считывает, выполняет сложение и отправляет итог в чат