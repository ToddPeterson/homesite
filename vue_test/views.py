from django.shortcuts import render


def vue_view(request):
    return render(request, 'vue_test/vue-test.html')
