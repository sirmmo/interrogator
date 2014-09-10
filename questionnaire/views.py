from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import *

@login_required
def index(request):
	return render(request, "index.html", {"q":Questionnaire.objects.all()})

@login_required
def questionnaire(request, id=None):
	"""questionnaire"""
	if id is None:
		return render(request, "questionnaire_editor.html")
	else:
		return render(request, "questionnaire_editor.html", {"questionnaire":Questionnaire.objects.get(id=id)})



def respond(request, id, rid=None):
	"""responding form"""
	if rid is None:
		#caching
		return render(request, "questionnaire.html", {"questionnaire":Questionnaire.objects.get(id=id)})
	else:
		return render(request, "response.html", {"done":Done.objects.get(id=rid)})


@csrf_exempt
def store(request, id):
	d = Done()
	d.questionnaire = Questionnaire.objects.get(id=id)
	d.save()

	for response in json.loads(request.REQUEST.get("response")).get("data"):
		da = DoneAnswer()
		da.done = d
		da.question = response.get("q")
		da.answer = response.get("a")
		da.save()

	d.close()

	return HttpResponse(json.dumps("OK"))
