from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv


load_dotenv(override=True)
WORKING_DIR = os.getenv("WORKING_DIR")
final_txt = WORKING_DIR+"transcripcion_final.txt"

with open(final_txt, "r", encoding="utf-8") as file:
    text = file.read()

spanish_stopwords = {
    "el", "la", "los", "las", 'este',"de", "y", "en", "a", "que", "por", "con", "una", "un", "para", "es", "al", "como", "más", "lo", "esto", "su", "si", "esta", "del", "no", "se", "ya", "pero", "todos", "está", "me", "también", "o", "te", "cuando", "muy", "sus", "nos", "tu", "estoy", "ser", "estoy", "ella", "ha", "le", "estaba", "haber", "porque", "siempre", "todo", "nosotros", "entre", "él", "hasta", "algunos", "durante"
}

stopwords = STOPWORDS.union(spanish_stopwords)

def filter_text(text, stopwords):
    words = text.split()
    filtered_words = [word for word in words if len(word) > 3 and word.lower() not in stopwords]

    return " ".join(filtered_words)

filtered_text = filter_text(text, stopwords)

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(filtered_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # Ocultar ejes
plt.show()

wordcloud.to_file("nube_de_palabras.png")
