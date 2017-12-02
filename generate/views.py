
from django.http import HttpResponse
import markovify

# Get raw text as string.
with open("markovify.txt", "r", encoding="utf-8") as f:
    text = f.read()

text.encode("utf-8");
    
# Build the model.
text_model = markovify.Text(text)

str = ""

# Print five randomly-generated sentences
for i in range(5):
    str += text_model.make_sentence()

def index(request):
    return HttpResponse(str)
