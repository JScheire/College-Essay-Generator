
from django.http import HttpResponse
import markovify
import random
from django.shortcuts import render

# Get raw text as string.
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

text.encode("utf-8");
    
# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
#for i in range(5):
#    str += (text_model.make_sentence() + " ")

def index(request):
    content = ""
    for i in range(random.randint(4,6)):
        for j in range(random.randint(6,12)):  
            content += (text_model.make_sentence() + " ")
        content += "\n\n"
    #content = content.encode("utf-8")
    return render(request, "template.html", {"content" : content})
