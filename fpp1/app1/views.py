from .models import Stage, Answer
from django.http import JsonResponse
import hashlib


def GetAllStages(request):
    if request.method == 'GET':
        stage_list = []
        stages = Stage.objects.filter(other_model__isnull=True)
        for i in stages:
            stage = {}
            stage_id = i.id
            substages = Stage.objects.filter(other_model=stage_id)
            substages_list = []
            stage['id'] = stage_id
            stage['title'] = i.title
            if substages:
                for j in substages:
                    substage = {}
                    substage['id'] = j.id
                    substage['title'] = j.title
                    substages_list.append(substage)
            stage['substages'] = substages_list
            stage_list.append(stage)
        return JsonResponse({'stage_list': stage_list}, status=200)
    else:
        JsonResponse({'error': 'Method not allowed'}, status=405)


def GetQuestionsByStage(request, pk):
    if request.method == 'GET':
        try:
            stage = Stage.objects.get(id=pk)
            answers = Answer.objects.filter(stage= stage)
        except BaseException:
            return JsonResponse({'error': 'This stage not exist or has no answers'}, status=400)
        ans_list = []
        for i in answers:
            print('PIPIPUPU')
            print('hash:' + i.answer_hash)
            ans_list.append(i.answer_hash)
        stage_data = {
            'id': pk,
            'guestion': stage.question,
            'answers': ans_list
        }
        return JsonResponse(stage_data, status=200)
    else:
        JsonResponse({'error': 'Method not allowed'}, status=405)

# Create your views here.
