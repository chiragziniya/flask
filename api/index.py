from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/about')
def about():
  return 'About'


@app.route('/blog')
def blog():
  return render_template('blog.html')


@app.route('/blog-detail')
def blog_detail():
  return render_template('blog-details.html')


@app.route('/portfolio-detail')
def portfolio_details():
  return render_template('portfolio-details.html')


@app.route('/services-detail')
def services_details():
  return render_template('services-details.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
