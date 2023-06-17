from django.shortcuts import render
from gpt4free import you


def get_gpt_response(answer):
    prompt = "Tu es une IA spécialisée en programmation et tu parles bien le français. tu es ici pour nous aider avec nos questions et problèmes liés au code. Que ce soit pour discuter des langages de programmation, des concepts d'algorithmes, des bonnes pratiques de développement ou même pour nous aider à résoudre des bugs"
    # simple request with links and details
    if(answer != ""):
        prompt = answer

        
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
        return render(request, 'gpt/_home.html', context)
    else:
        response = get_gpt_response("")
        context = {'response': response}
        return render(request, 'gpt/_home.html',context)