from .models import Stage, Answer, Question
from django.http import JsonResponse


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
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def GetQuestionsByStage(request, pk):
    if request.method == 'GET':
        try:
            stage = Stage.objects.get(id=pk)
        except BaseException:
            return JsonResponse({'error': 'This stage not exist'}, status=400)
        questions = Question.objects.filter(stage=stage)
        if not questions:
            return JsonResponse({'error': 'No questions found for this stage'}, status=400)
        questions_list = []
        for i in questions:
            ans_list = []
            question = {
                'question_text': i.question_text
            }
            answers = Answer.objects.filter(question=i)
            if answers:
                for j in answers:
                    ans_list.append(j.answer_hash)
            question['answers'] = ans_list
            questions_list.append(question)
        stage_data = {
            'id': pk,
            'title': stage.title,
            'guestions': questions_list,
        }
        return JsonResponse(stage_data, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

