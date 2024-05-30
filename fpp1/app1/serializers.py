from rest_framework import serializers
from .models import Stage, Question, Answer, Subtage



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_hash']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True, source='answer_set')

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'answers']

class SubStageDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, source='question_set')

    class Meta:
        model = Subtage
        fields = ['id', 'title', 'questions']

class SubStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subtage
        fields = ['id', 'title']

class StageSerializer(serializers.ModelSerializer):
    substages = SubStageSerializer(many=True, read_only=True, source='substage_set')

    class Meta:
        model = Stage
        fields = ['id', 'title', 'substages']