from django.db import models

class Questionnaire(models.Model):
	name = models.CharField(max_length=1000)
	description = models.TextField(default="")
	header_template = models.TextField(default="")

	closed = models.BooleanField(default=False)
	
	def csv(self, writer):
		cn = []
		for col in self.questions.all():
			cn.append(col.id)
		writer.writerow(cn)
		for row in self.answers.all():
			writer.writerow(row.csvrow())

	def __str__(self):
		return self.name

class Question(models.Model):
	questionnaire = models.ForeignKey(Questionnaire, related_name="questions")
	question = models.TextField()
	order = models.IntegerField(default=1)

	class Meta:
		ordering = ("order",)


	def __str__(self):
		return str(self.questionnaire) + " -> " + self.question

class Option(models.Model):
	question = models.ForeignKey(Question, related_name="options")
	text = models.CharField(max_length=1000)
	value = models.IntegerField()
	order = models.IntegerField(default=1)

	class Meta:
		ordering = ("order",)

	def __str__(self):
		return str(self.question.questionnaire) + " -> " + str(self.question.question) + " -> " + self.text

class Response(models.Model):
	questionnaire = models.ForeignKey(Questionnaire, related_name="responses")
	min_points = models.IntegerField(default=0)
	max_points = models.IntegerField(default=100)

	text = models.TextField()

class Done(models.Model):
	questionnaire = models.ForeignKey(Questionnaire, related_name="answers")
	response = models.ForeignKey(Response, null=True, blank=True)

	def csvrow(self):
		ret = []
		for answer in self.answers.all():
			ret.append(answer.answer.id)

	def close(self):
		val = 0
		for answer in self.answers.all():
			val += answer.answer.value
		self.response = Response.objects.filter(min_points__lte=val, max_points__gte=val).first()
		self.save()

class DoneAnswer(models.Model):
	done = models.ForeignKey(Done, related_name="answers")
	question = models.ForeignKey(Question)
	answer = models.ForeignKey(Option)

	class Meta:
		ordering=("question__order",)


