from flask import Flask,render_template,request, jsonify
from api import TPB_rss

app = Flask(__name__, template_folder='templates') 
app.secret_key = '931uX0cj0wmQSlsZmZc2w1'




# home page
@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')
# pages 
@app.route('/top/movies')
def movieNew():
    res = TPB_rss('https://tpb.party/rss/top100/201')
    return render_template("tpb.html", data=res, type="Top Movies")

@app.route('/new/movies')
def movieTop():
    res = TPB_rss('https://tpb.party/rss/new/201')
    return render_template("tpb.html", data=res, type="New Movies")

@app.route('/top/hd/movies')
def movieTopHD():
    res = TPB_rss('https://tpb.party/rss/top100/207')
    return render_template("tpb.html", data=res, type="Top HD Movies")

@app.route('/new/hd/movies')
def movieNewHD():
    res = TPB_rss('https://tpb.party/rss/new/207')
    return render_template("tpb.html", data=res, type="New HD Movies")



@app.route('/top/tv')
def tvTop():
    res = TPB_rss('https://tpb.party/rss/top100/205')
    return render_template("tpb.html", data=res,type='Top TV Shows')

@app.route('/new/tv')
def tvNew():
    res = TPB_rss('https://tpb.party/rss/new/205')
    return render_template("tpb.html", data=res,type='New TV Shows')

@app.route('/top/hd/tv')
def tvTopHD():
    res = TPB_rss('https://tpb.party/rss/top100/208')
    return render_template("tpb.html", data=res,type='Top HD TV Shows')

@app.route('/new/hd/tv')
def tvNewHD():
    res = TPB_rss('https://tpb.party/rss/new/208')
    return render_template("tpb.html", data=res,type='New HD TV Shows')



@app.route('/top/music')
def musicTop():
    res = TPB_rss('https://tpb.party/rss/top100/101')
    return render_template("tpb.html", data=res, type="Top Music")

@app.route('/new/music')
def musicNew():
    res = TPB_rss('https://tpb.party/rss/new/101')
    return render_template("tpb.html", data=res, type="New Music")



@app.route('/top/lossless/music')
def toplosslessmusic():
    res = TPB_rss('https://tpb.party/rss/top100/104')
    return render_template("tpb.html", data=res,type="Top Lossless")

@app.route('/top/audiobooks')
def audiobooksTop():
    res = TPB_rss('https://tpb.party/rss/top100/102')
    return render_template("tpb.html", data=res, type='Top Audiobooks')


@app.route('/top/movies/porn')
def topPornMovies():
    res = TPB_rss('https://tpb.party/rss/top100/501')
    return render_template("tpb.html", data=res,type='Top Porn Movies')

@app.route('/new/movies/porn')
def newPornMovies():
    res = TPB_rss('https://tpb.party/rss/new/501')
    return render_template("tpb.html", data=res,type='New Porn Movies')

@app.route('/top/hd/movies/porn')
def topHDPornMovies():
    res = TPB_rss('https://tpb.party/rss/top100/505')
    return render_template("tpb.html", data=res,type='Top HD Porn Movies')

@app.route('/new/hd/movies/porn')
def newHDPornMovies():
    res = TPB_rss('https://tpb.party/rss/new/505')
    return render_template("tpb.html", data=res,type='New HD Porn Movies')


@app.route('/top/movieclips/porn')
def topPornClipsMovies():
    res = TPB_rss('https://tpb.party/rss/top100/506')
    return render_template("tpb.html", data=res,type='Top Porn Movie Clips')

@app.route('/new/movieclips/porn')
def newPornClipsMovies():
    res = TPB_rss('https://tpb.party/rss/new/506')
    return render_template("tpb.html", data=res,type='New Porn Movie Clips')





@app.route('/top/ebooks')
def topEbooks():
    res = TPB_rss('https://tpb.party/rss//top100/600')
    return render_template("tpb.html", data=res,type='Top E-Books')

@app.route('/new/ebooks')
def newEbooks():
    res = TPB_rss('https://tpb.party/rss/new/601')
    return render_template("tpb.html", data=res,type='New E-Books')
    


@app.errorhandler(404)
def page_not_found(e):
    return "No page exists here. :( ", 404


if __name__ == '__main__':
    app.run(port=5000)