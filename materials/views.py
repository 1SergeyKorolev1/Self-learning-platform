from rest_framework.viewsets import ModelViewSet, generics
from materials.models import Course, Lesson, Test
from materials.serializers import (CourseSerializer, LessonSerializer,
                                   TestSerializer, AttemptAnswerSerializer)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def perform_create(self, serializer):
        test = serializer.save()
        test.owner = self.request.user
        test.save()


class AttemptAnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = AttemptAnswerSerializer

    def perform_create(self, serializer):
        attempt_answer = serializer.save()
        print(attempt_answer.answer)
        attempt_answer.owner = self.request.user
        attempt_answer.save()
        answer = attempt_answer.answer
        test_set = Test.objects.filter(pk=attempt_answer.test.pk)
        if test_set:
            if answer:
                for test in test_set:
                    if answer.lower() == test.correct_answer.lower():
                        attempt_answer.answer_bool = True
                    else:
                        attempt_answer.answer_bool = False
                    attempt_answer.save()

