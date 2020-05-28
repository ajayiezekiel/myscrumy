from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse 
from  .models import GoalStatus, ScrumyGoals, ScrumyHistory
# import datetime
from random import randint
# from django.core.exceptions import *

def get_grading_parameters(request) :
      goals2 = ScrumyGoals.objects.filter(goal_name="Learn Django")
      return HttpResponse(goals2) 


def move_goal(request, goal_id):
    dictionary = {"error":"A record with that goal id does not exist"}
    try:
        obj = ScrumyGoals.objects.get(goal_id = goal_id)
    except ObjectDoesNotExist:
        return render(request, 'benpelumiscrumy/exception.html', dictionary)
    else:
        return HttpResponse(obj.goal_name)


def add_goal(request):
    weekly = GoalStatus.objects.get(status_name="Weekly Goal")
    user = User.objects.get(username="louis")
    new_list = ScrumyGoals.objects.all()
    id_dict = {goal.goal_id:goal.goal_name for goal in new_list}
    number = randint(1000,9999)
    if number not in id_dict:
        goal = ScrumyGoals.objects.create(goal_name="Keep Learning Django",
                                    goal_id=number,
                                    created_by="Louis",
                                    moved_by="Louis",
                                    owner="Louis",
                                    goal_status=weekly,
                                    user=user
                                )
        return HttpResponse(goal)

# def move_goal(request, goal_id):
#     #obj1 = get_object_or_404(ScrumyGoals, pk=goal_id)
#         dic = ({ 'error' : "A record with that goal id does not exist"})
#         dictionary = {'dict1' : dic}
#         try:
#             display = ScrumyGoals.objects.get(pk = goal_id)
#         except Exception as e:
#             return render (request, '404.html', dictionary)
    
#         else:
#             return HttpResponse(display.goal_name)           

# def move_goal(request, goal_id):
#       try:
#             display = ScrumyGoals.objects.get(goal_id = goal_id)
#       except  ScrumyGoals.DoesNotExist:
#             raise Http404('error = A record with that goal id does not exist' )
#       return HttpResponse(display.goal_name)

# def add_goal(request):            
#       goalId = randint(1000, 9999)
#       goalStatus = GoalStatus.objects.last()
#       addGoalUser = User.objects.get(username = 'louis')
#       addGoal = ScrumyGoals.objects.create(goal_name = 'keep learning django', goal_id = goalId, created_by = 'Louis' , moved_by = 'Louis', owner = 'Louis' , goal_status = goalStatus ,user = addGoalUser ) 
#       return HttpResponse(addGoal)

def home (request):
      # return HttpResponse("This is a Scrum Application")
      goal = ScrumyGoals.objects.get(goal_name ="Learn Django")
      # goals = ScrumyGoals.objects.filter(goal_id = 1)
      # return HttpResponse(goals)
      #goals = "learn django"
      #learnDjangoUser = User.objects.get(username = 'louis')
      scrumyValues = {'goal_name': goal.goal_name , 
                      'goal_id' : goal.goal_id ,
                      'user' : goal.user.username}

      return render(request, 'benpelumiscrumy/home.html', scrumyValues )

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


# def learningDjango(request) :
     

 


# get_grading_parameters"Welcome to Django"