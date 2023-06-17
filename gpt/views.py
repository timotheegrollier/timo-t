from django.shortcuts import render
from gpt4free import you


def get_gpt_response(answer):
    # simple request with links and details
    preAnswer = "voici ma question:"
    if(answer != ""):
        answer = preAnswer + answer
    prompt = f"parles en francais {answer}"

        
    response = you.Completion.create(
        prompt=prompt,
        detailed=True,
        include_links=False)
    return response.text.encode().decode('unicode-escape')


def home(request):
    if request.method == 'POST':
        answer = request.POST.get('prompt')
        response = get_gpt_response(answer)
        context = {'response': response}
        return render(request, 'gpt/home.html', context)
    else:
        response = get_gpt_response("")
        context = {'response': response}
        return render(request, 'gpt/home.html',context)