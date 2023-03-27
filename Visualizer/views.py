from django.shortcuts import render
from django.http import JsonResponse
import json
import Module3.Module3 as Module3
# Create your views here.


def index(request):
    return render(request, 'home.html')

def miserables(request):
    data = json.load(
            open('/home/jaden/projects/socialMediaAnalytics/Visualizer/data.json', 'r'))
    # searchTerms = ["fit","lif"]
    # if searchTerms is not None:
    #     data = json.load(
    #         open('/home/jaden/projects/socialMediaAnalytics/Visualizer/data.json', 'r'))
    #     m = Module3.Module3()
    #     for searchTerm in searchTerms:
    #         entries = m.search(searchTerm)
    #         entries = entries.T
    #         jsonData = json.loads(entries.to_json())
    #         #{"source": 1, "target": 0, "value": 1}
    #         jsonResp = {
    #             "nodes": [
    #                 {"name": searchTerm, "group": 1}
    #                 ],
    #             "links": [
                    
    #             ]}
    #         linkId = 1
    #         for entry in jsonData:
    #             print(jsonData[entry])
    #             jsonResp['nodes'].append({"name":jsonData[entry]['post_id'],"group":1})
    #             jsonResp['links'].append({"source":0,"target":linkId,"value":1})
    #             linkId+=1
    return JsonResponse(data)

def draggable(request):
    searchTerm = request.GET.get('search', '')
    if searchTerm is not None:
        data = json.load(
            open('/home/jaden/projects/socialMediaAnalytics/Visualizer/data.json', 'r'))
        m = Module3.Module3()
        entries = m.search(searchTerm)
        entries = entries.T
        jsonData = json.loads(entries.to_json())
        print(jsonData)
        modifiedData = []
        for entry in jsonData:
            modifiedData.append(jsonData[entry])
        print(modifiedData)
        return render(request, "drag.html",{'data':modifiedData,'search_term':searchTerm})
    else:
        return JsonResponse({"data":"error occurred"})

def clustering(request):
    searchTerm = request.GET.get('search', '')
    if searchTerm is not None:
        m = Module3.Module3()
        entries = m.search(searchTerm)
        entries = entries.T
        jsonData = json.loads(entries.to_json())
        print(jsonData)
        modifiedData = []
        for entry in jsonData:
            modifiedData.append(jsonData[entry])
        print(modifiedData)
        return render(request, "clustering.html",{'data':modifiedData,'search_term':searchTerm})
    else:
        return JsonResponse({"data":"error occurred"})