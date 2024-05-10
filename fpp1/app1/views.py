from .models import Stage
from django.http import JsonResponse
import hashlib


def GetAllStages(request):
    if request.method == 'GET':
        stage_list = []
        stages = Stage.objects.filter(other_model__isnull=True)
        for i in stages:
            stage = {}
            stage_id = i.id
            substages = Stage.objects.filter(id=stage_id)
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
        except BaseException:
            return JsonResponse({'error': 'This stage not exist'}, status=400)
        if not stage.question:
            return JsonResponse({'error': 'No question'}, status=400)
        answer_string = stage.answer.encode('utf-8')
        hash_answer = hashlib.sha256(answer_string)
        stage_data = {
            'id': pk,
            'guestion': stage.question,
            'answer': hash_answer.hexdigest()
        }
        return JsonResponse(stage_data, status=200)
    else:
        JsonResponse({'error': 'Method not allowed'}, status=405)

# Create your views here.
