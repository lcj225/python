#lab_2의 school함수만 임포트한다.
from lab_2 import school
from bs4 import BeautifulSoup as bs
import matplotlib
import json

table = {'a':1, 'b':2, 'c':3}
ka = set([1,2,3,4])
tu = (1,2,3)
colors = [1, 2, 3, 4, 5, 6, "4", float(4)]
k = "123456789"
x = ["1", "2", "3"]


with open("9_json_xml/json/ipa110106.XML", "r", encoding="utf8") as bf:
    bf.readlines()
    for l in bf:
        if l.strip("<"):
            if not "/" in l:
                st = l.replace("<", "")
                st = st.replace(">", "")




with open("9_json_xml/json/data.json", "r", encoding="utf8") as bf:
    bx = bf.read()
    j = json.loads(bx)
    j["Name"] = "lee"
    print(j)




# with open("9_json_xml/xml/books.xml", "r", encoding="utf8") as bf:
#     bx = bf.read()
#
# soup = bs(bx,"lxml")
#
# for bi in soup.find_all("author"):
#     print(bi)
#     print(bi.getText())
#
# with open("9_json_xml/xml/US08621662-20140107.XML", "r", encoding="utf8") as bf:
#     bx = bf.read()
#
# soup = bs(bx,"xml")
#
# for bi in soup.find_all("publication-reference"):
#     #print(bi)
#     b1 = bi.find("document-id").find("country")
#     print(b1.getText())
#
#
# re = m.t_converter()
# print(re)
# school(20)
#
#
#
# f1 = open("test.txt", 'a')
# a = ""
# while a != "끝":
#     a = input("입력 : ")
#     if a != "끝":
#         f1.write( a + "\n")
# f1.close()
#
# with open("test.txt", "r") as f:
#     print(f.read())
#
#
#
#
# # enumerate 인덱스,값 동시추출
#
# print(list(enumerate(k)))
#
# # zip 길이가 같은 리스트를 묶음
#
# for c in zip(tu,list(enumerate(k)), k):
#     print(c)
#
# # list comprehension
#
# lis = [i for i in range(10)]
# print(lis)
#
# #for a 안의 for b
# lis = [i+str(j) for i in k for j in colors if j == 6]
# print(lis)
#
# #for b 안의 for a + 이중배열로 됨
# lis = [[i+str(j) for i in k]for j in colors]
# print(lis)
#
# print("\n".join(k))
# assert True
# print(k)
# print(k.join(x))
# print(table)
# table['a'] = 6
# print(table['a'])
# print(table)
#
# ka.add(1)
# ka.add(5)
# print(ka)
#
# print(tu)
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [a, b]
#
# for i in colors:
#     print(i)
#
# for i in k:
#     print(i)
#
# k = 0
#
# while k < 10:
#     k += 1
#     if k == 5: continue
#     print(k)
# else:
#     print("end")
# for i in range(0, len(c)):
#     k += c[i][0]
#
# print( k )
#
# colors.extend( colors )
# print( colors )
#
# colors.append( 1 )
# print( colors )

# colors.sort(  )
# print( colors )
#
# colors.sort( reverse=True )
# print( colors )

# colors.insert( 1,4 )
# print( colors )

# not4 = []
#
# for i in colors:
#     if i != 4:
#         not4.append(i)
#     elif i == 4:
#         print("no")
#     if i == 1:
#         print("yes")
#
# print(not4)

# for i in range(1, colors.count(4)):
#     if 4 in colors:
#         colors.remove(4)
#     print(i)
# print(colors)
#
# colors = [i for i in colors if i != 4]
# print( colors )
# x = len( colors )
#
# for i in range( 0, x ):
#  print( colors.pop( 0 ) )
#  print( 3 in colors )
#  colors = ( colors + colors )
#  x = len( colors )
#  print(x)
#  if x >= 30:
#   break

