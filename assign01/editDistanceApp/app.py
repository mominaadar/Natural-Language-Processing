from flask import Flask, render_template, flash, redirect, url_for, request

app = Flask(__name__)

lst = ['John','Mary','Magdalene','Wick','Nazareth','Smithsonian','Kierra','Henry',
'Brandon','Aiden','Cierra','Mcgonagall','Harry','Filch','Minerva','Dumbledore','Snape','Voldemort']

#######################################################


class Dummy:
    dic = {}

d = Dummy()

def min_editDistance(lst, dic, src):

    for word in lst:

        add = 0
        s_len = len(src)
        w_len = len(word)

        for i in range(min(s_len, w_len)):

            if src[i] == word[i]:
                continue  #same/equal so pass
            else:
                add = add + 2  #substitution

        if len(src) != len(word):

            if s_len < w_len:

                length = w_len - s_len  #insertion if target is longer

                add = add + length
                dic[word] = add

            if s_len > w_len:
                length = s_len - w_len  #deletion if source is longer

                add = add + length
                dic[word] = add

        dic[word] = add


        #first sorting dictionary and then treating is as list and returning first 3 elements

    return list(dict(sorted(dic.items(), key=lambda item: item[1])))[:3]

##########################################################3

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/display', methods=['GET','POST'])
def display():
    if request.method == 'POST':
        source = request.form.get('source')

        top_names = min_editDistance(lst, d.dic, source)

        return render_template('display.html', source=source, top_names=top_names)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
