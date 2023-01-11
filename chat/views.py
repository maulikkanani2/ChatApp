from django.shortcuts import render
from django.views import View
from chat.models import Chat
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from chat.open_api import open_ai_completion


@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        question = request.POST.get('question', None)
        if question:
            response = open_ai_completion(question)
            answer = response['choices'][0]['text'].strip()
            chat = Chat.objects.create(question=question, user=request.user, answer=answer)
        return render(request, 'home.html', {"question": question,"answer": answer})