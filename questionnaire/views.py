import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import *
from django.views.decorators.clickjacking import xframe_options_exempt
import json


import redis

r = redis.Redis()
@login_required
def index(request):
	return render(request, "index.html", {"title":"Questionnaires", "questionnaires":Questionnaire.objects.all()})

@login_required
def questionnaire(request, id=None):
	"""questionnaire"""
	if id is None:
		return render(request, "questionnaire_editor.html")
	else:
		q = Questionnaire.objects.get(id=id)
		return render(request, "questionnaire_editor.html", {"questionnaire":q})

@xframe_options_exempt
def respond(request, id, rid=None):
	"""responding form"""

	if rid is None:
		cache = r.get("q:%s" % rid)
		if cache is not None:
			return HttpResponse(cache)
		else:
			q = Questionnaire.objects.get(id=id)
			if q.closed:
				t = loader.get_template('nope.html')
				c = RequestContext(request)
				return render(request, "nope.html")
			t = loader.get_template('questionnaire.html')
			c = RequestContext(request,{"title":q.name, "questionnaire":q})
			to_store = t.render(c)
			r.set("q:%s" % rid, to_store)
			return HttpResponse(to_store)
	else:
		d = Done.objects.get(id=rid)

		return HttpResponseRedirect("/response/%s" % d.response.id)
@xframe_options_exempt
def response(request, rid):
	cache = r.get("r:%s" % rid)
	if cache is not None:
		return HttpResponse(cache)
	res = Response.objects.get(id=rid)
	t = loader.get_template('response.html')
	c = RequestContext(request,{"response":res})
	to_store = t.render(c)
	r.set("r:%s" % rid, to_store)
	return HttpResponse(to_store)

def image(request, rid):
	img = Response.objects.get(id=rid).image
	response = HttpResponse(img.read(), content_type='image/%s' %img.path.split(".")[-1])
	response['Content-Disposition'] = 'attachment; filename="img.%s"' %img.path.split(".")[-1]
	return response


def header(request, id):
	img = Questionnaire.objects.get(id=id).image
	response = HttpResponse(img.read(), content_type='image/%s' %img.path.split(".")[-1])
	response['Content-Disposition'] = 'attachment; filename="img.%s"' %img.path.split(".")[-1]
	return response


@csrf_exempt
def store(request, id):
	d = Done()
	d.questionnaire = Questionnaire.objects.get(id=id)
	d.save()

	for response in json.loads(request.REQUEST.get("data")):
		da = DoneAnswer()
		da.done = d
		da.question = Question.objects.get(id=response.get("q"))
		try: 
			val = int(response.get("a"))
			da.answer = Option.objects.get(id=response.get("a"))
		except: 
			val = response.get("a")
			da.value = val
		da.save()

	d.close()

	return HttpResponse(json.dumps(d.id))

@login_required
def deactivate(reqeust, id):
	q = Questionnaire.objects.get(id=id)
	q.closed = True
	q.save()
	return HttpResponseRedirect("/")

@login_required
def activate(request, id):
	q = Questionnaire.objects.get(id=id)
	q.closed = False
	q.save()
	return HttpResponseRedirect("/")

import csv as csv_mod

@login_required
def csv(request, id):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

	q = Questionnaire.objects.get(id=id)

	writer = csv_mod.writer(response)
	titles = ["timestamp", "result"]
	for question in q.questions.all():
		titles.append(question.question)
	writer.writerow(titles)
	for resp in q.answers.all():
		rw = []
		if resp.datetime:
			rw.append(resp.datetime)
		if resp.response:
			rw.append(resp.response.title)
		else:
			rw.append("-")
		for answer in resp.answers.all():
			if answer.answer:
				rw.append(answer.answer.text)
			else:
				rw.append(answer.value)
		writer.writerow(rw)
	return response






