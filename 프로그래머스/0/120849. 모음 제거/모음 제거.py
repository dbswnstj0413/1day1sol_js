def solution(my_string):
    answer = ''
    collection = ("aeiou")
    for i in my_string:
         if i not in collection:
            answer += i
    return answer

 
     
     