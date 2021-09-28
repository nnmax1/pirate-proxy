from flask import Flask,render_template,request, jsonify
from api import rssParse

app = Flask(__name__, template_folder='templates') 
app.secret_key = '931uX0cj0wmQSlsZmZc2w1'




# home page
@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')
# pages 
@app.route('/top/movies')
def movieNew():
    res = rssParse('https://tpb.party/rss/top100/201')
    return render_template("tpb.html", data=res, type="Top Movies", website='TPB')

@app.route('/new/movies')
def movieTop():
    res = rssParse('https://tpb.party/rss/new/201')
    return render_template("tpb.html", data=res, type="New Movies",website='TPB')

@app.route('/top/hd/movies')
def movieTopHD():
    res = rssParse('https://tpb.party/rss/top100/207')
    return render_template("tpb.html", data=res, type="Top HD Movies",website='TPB')

@app.route('/new/hd/movies')
def movieNewHD():
    res = rssParse('https://tpb.party/rss/new/207')
    return render_template("tpb.html", data=res, type="New HD Movies",website='TPB')



@app.route('/top/tv')
def tvTop():
    res = rssParse('https://tpb.party/rss/top100/205')
    return render_template("tpb.html", data=res,type='Top TV Shows',website='TPB')

@app.route('/new/tv')
def tvNew():
    res = rssParse('https://tpb.party/rss/new/205')
    return render_template("tpb.html", data=res,type='New TV Shows',website='TPB')

@app.route('/top/hd/tv')
def tvTopHD():
    res = rssParse('https://tpb.party/rss/top100/208')
    return render_template("tpb.html", data=res,type='Top HD TV Shows',website='TPB')

@app.route('/new/hd/tv')
def tvNewHD():
    res = rssParse('https://tpb.party/rss/new/208')
    return render_template("tpb.html", data=res,type='New HD TV Shows',website='TPB')



@app.route('/top/music')
def musicTop():
    res = rssParse('https://tpb.party/rss/top100/101')
    return render_template("tpb.html", data=res, type="Top Music",website='TPB')

@app.route('/new/music')
def musicNew():
    res = rssParse('https://tpb.party/rss/new/101')
    return render_template("tpb.html", data=res, type="New Music",website='TPB')



@app.route('/top/lossless/music')
def toplosslessmusic():
    res = rssParse('https://tpb.party/rss/top100/104')
    return render_template("tpb.html", data=res,type="Top Lossless",website='TPB')

@app.route('/top/audiobooks')
def audiobooksTop():
    res = rssParse('https://tpb.party/rss/top100/102')
    return render_template("tpb.html", data=res, type='Top Audiobooks',website='TPB')


@app.route('/top/movies/porn')
def topPornMovies():
    res = rssParse('https://tpb.party/rss/top100/501')
    return render_template("tpb.html", data=res,type='Top Porn Movies',website='TPB')

@app.route('/new/movies/porn')
def newPornMovies():
    res = rssParse('https://tpb.party/rss/new/501')
    return render_template("tpb.html", data=res,type='New Porn Movies',website='TPB')

@app.route('/top/hd/movies/porn')
def topHDPornMovies():
    res = rssParse('https://tpb.party/rss/top100/505')
    return render_template("tpb.html", data=res,type='Top HD Porn Movies',website='TPB')

@app.route('/new/hd/movies/porn')
def newHDPornMovies():
    res = rssParse('https://tpb.party/rss/new/505')
    return render_template("tpb.html", data=res,type='New HD Porn Movies',website='TPB')


@app.route('/top/movieclips/porn')
def topPornClipsMovies():
    res = rssParse('https://tpb.party/rss/top100/506')
    return render_template("tpb.html", data=res,type='Top Porn Movie Clips',website='TPB')

@app.route('/new/movieclips/porn')
def newPornClipsMovies():
    res = rssParse('https://tpb.party/rss/new/506')
    return render_template("tpb.html", data=res,type='New Porn Movie Clips',website='TPB')



@app.route('/top/ebooks')
def topEbooks():
    res = rssParse('https://tpb.party/rss//top100/600')
    return render_template("tpb.html", data=res,type='Top E-Books',website='TPB')

@app.route('/new/ebooks')
def newEbooks():
    res = rssParse('https://tpb.party/rss/new/601')
    return render_template("tpb.html", data=res,type='New E-Books',website='TPB')
    

@app.route('/yts/4k')
def yts_4k():
    res = rssParse('https://yts.mx/rss/0/2160p/all/0/all')
    return render_template("tpb.html", data=res,type='YTS 4K',website='YTS')

@app.route('/yts/1080p')
def yts_1080p():
    res = rssParse('https://yts.mx/rss/0/1080p/all/0/all')
    return render_template("tpb.html", data=res,type='YTS 1080p',website='YTS')
@app.route('/yts/720p')
def yts_720p():
    res = rssParse('https://yts.mx/rss/0/720p/all/0/all')
    return render_template("tpb.html", data=res,type='YTS 720p',website='YTS')
    


@app.errorhandler(404)
def page_not_found(e):
    return "No page exists here. :( ", 404


if __name__ == '__main__':
    app.run(port=5000)