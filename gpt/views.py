from django.shortcuts import render
from gpt4free import you



def get_gpt_response():
    # simple request with links and details
    response = you.Completion.create(
        prompt="Salut parle en français et présente toi comme un expert en code",
        detailed=True,
        include_links=False)
    return response.text.encode().decode('unicode-escape')


# Create your views here.
def home(request):
    response = get_gpt_response()
    context = {'response': response}
    return render(request, 'gpt/gpt.html',context)