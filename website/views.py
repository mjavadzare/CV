from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {
            "fullname":"Mohamad Javad Zare",
            "vocation":"Back-End Developer",
            "firstname":"Mohamad Javad",
            "content":"My nickname is Mikey. I was born in Quchan, a rather small city in Iran. My English language skills except for speaking are prrety good. As of now, i'm a Computer Science student in Bojnourd university. I've learned Python and Django well for Back-end Web Development. I've also learned about regex and a little bit Machine Learning in Python.",
            "skills":"Python, Django, MySQL, ML, Regex, HTML, CSS, C++",
            "educations":"Undergraduate Computer Science",
            "birthday":"28 March, 2002",
            "location":"Bojnourd, Iran",
            "languages":"Persian, English",
            "email":"mjz589.2018@gmail.com",
            "phone":"+989013023089",
            "ML_project":"https://github.com/mjz589/Machine-Learning-first-project",
            "first_site":"https://github.com/mjz589/My-First-Site",
            "personal_site":"https://github.com/mjz589/Personal-Site",
            "Agriculture_Dashboard":"https://github.com/mjz589/Agriculture-Dashboard",
            "django_42":"https://github.com/mjz589/First-Site-with-Django-4.2",
            }
    return render(request, 'index.html', context)