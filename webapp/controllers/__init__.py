def get_or_None(request, param):
	if request.args.get(param):
		return request.args.get(param)
	else:
		return None 


def post_or_None(request, param):
	print(request.json, request.form)
	if request.json:
		if param in request.josn:
			return request.json[param]
		else:
			return None 
	elif request.form:
		if param in request.form:
			return request.form[param]
		else:
			return None 
	else:
		return None



@csrf.exempt
@ais.route('/inapi/1.0/users', methods=['GET'])
