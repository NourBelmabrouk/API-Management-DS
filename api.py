from simplexml import dumps
from flask import Flask, jsonify, request,make_response
from flask_restful import Api, Resource


def output_xml(data, code, headers=None):
    """Makes a Flask response with a XML encoded body"""
    resp = make_response(dumps({'response' :data}), code)
    resp.headers.extend(headers or {})
    return resp

app = Flask(__name__)
api = Api(app, default_mediatype='application/xml')
api.representations['application/xml'] = output_xml

week={
				"1":"Monday",
				"2":"Tuesday",
				"3":"Wednesday",
				"4":"Thursday",
				"5":"Friday",
				"6":"Saturday",
				"7":"Sunday",
		}
month={
	"1" : "January",
	"2" : "February",
	"3" : "March",
	"4" : "April",
	"5" : "May",
	"6" : "June",
	"7" : "July",
	"8" : "August",
	"9" : "September",
	"10" : "October",
	"11" : "November",
	"12" : "December",
}

class dayOfWeek(Resource):
    """
        # you need requests
        >>> from requests import get
        >>> get('http://localhost:5000/me').content # default_mediatype
        '<?xml version="1.0" ?><response><hello>me</hello></response>'
        >>> get('http://localhost:5000/me', headers={"accept":"application/json"}).content
        '{"hello": "me"}'
        >>> get('http://localhost:5000/me', headers={"accept":"application/xml"}).content
        '<?xml version="1.0" ?><response><hello>me</hello></response>'
    """
    def get(self, entry):
        if entry in week.keys():
        	return {'dayOfWeek': week[entry]}
		



class monthOfYear(Resource):
    def get(self, entry):
        if entry in month.keys():
            return {'monthOfYear': month[entry]}



api.add_resource(dayOfWeek, '/dayOfWeek/<string:entry>')
api.add_resource(monthOfYear, '/monthOfYear/<string:entry>')

if __name__ == '__main__':
    app.run(debug=True)