from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def software(request):
    return HttpResponse ('''<h1><marquee> SOFTWARES </marquee><h1> \n
                         Software is a set of instructions, data or programs used
                         to operate computers and execute specific tasks. 
                         It is the opposite of hardware,
                         which describes the physical aspects of a computer.
                         Software is a generic term used to refer to applications, 
                         scripts and programs that run on a device. It can be thought
                         of as the variable part of a computer, while hardware is the 
                         invariable part. The two main categories of software are application software and system software.
                An application is software that fulfills a specific need or performs tasks. System software is designed
                to run a computer's hardware and provides 
                a platform for applications to run on top of.''')