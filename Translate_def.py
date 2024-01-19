# import openai

# openai.api_key = "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"
# model_engine = "text-davinci-003"
# completion = openai.Completion.create(engine = model_engine, 
#                                       prompt = '請將下列對話翻譯成正體中文:' + "いえいつもブロデューサーさんにはお世話になってますから", 
#                                       max_tokens = 1024,
#                                       temperature = 0)

# print(completion.choices[0].text)

from googletrans import Translator

def translate_text(text, language):
    translator = Translator()
    translation = translator.translate(text, dest=language)
    return translation.text

# Example usage
# text_to_translate = "いえいつもブロデューサーさんにはお世話になってますから"
# destination_language = "zh-TW" 

# translated_text = translate_text(text_to_translate, destination_language)
# print(translated_text)
