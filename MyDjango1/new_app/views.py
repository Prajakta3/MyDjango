from django.shortcuts import render

from models import paragraph


def firstpage(request):
    if request.method == "POST":
        form_data = request.POST

        data_update = paragraph(First_name=form_data['First_name'], Last_name=form_data['Last_name'],
                           Add_line1=form_data['Add_line1'], Add_line2=form_data['Add_line2'],
                           City=form_data['City'], State=form_data['State'], Zip=form_data['Zip'],
                           Email=form_data['Email'], Phone=form_data['Phone'])
        data_update.save()
        return render(request, 'page1.html', {'data': data_update})
    else:
        data1 = 'this is else'
        return render(request, 'page1.html', {'data1': data1})

def secondpage(request):
    data2 = paragraph.objects.all()
    return render(request,'page2.html',{'name': data2})